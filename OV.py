#!/home/al/miniconda3/envs/py/bin/python3
# -*- coding: utf-8 -*-
#
#  filename:   /home/al/projects/audio-player/OV.py
#
#  Copyright 2025 AL Haines
#
#  Definitive Version: Correctly implements track number sorting
#                      AND the resume playback functionality.

from flask import render_template, jsonify, request, Response, send_file, stream_with_context
import os
import re
from MySql import MySQL
import config_audio

def _get_db_connection():
    return MySQL(**config_audio.mysql_config)

def _get_item_details(table_name, item_id):
    db = _get_db_connection()
    query = f"SELECT * FROM `{table_name}` WHERE id = %s"
    results = db.get_data(query, (item_id,))
    return results[0] if results else None

def get_resume_items():
    db = _get_db_connection()
    all_tables_raw = db.get_data("SHOW TABLES")
    if not all_tables_raw: return []

    audio_tables = [list(t.values())[0] for t in all_tables_raw if list(t.values())[0].startswith('audio_')]
    union_queries = []

    for table in audio_tables:
        columns = db.get_field_names(table)
        if 'resume_position' in columns and 'last_played' in columns:
            union_queries.append(f"(SELECT id, title, album, '{table}' as category, last_played, resume_position FROM `{table}` WHERE resume_position > 0.1)")

    if not union_queries: return []

    full_query = " UNION ALL ".join(union_queries) + " ORDER BY last_played DESC LIMIT 20"
    return db.get_data(full_query)

def render_index_page():
    db = _get_db_connection()
    all_tables_raw = db.get_data("SHOW TABLES")
    longform_tables = [list(t.values())[0] for t in all_tables_raw if list(t.values())[0] in ['audio_audiobooks', 'audio_instructional', 'audio_comedy']]
    resume_items = get_resume_items()
    return render_template('index.html', categories=longform_tables, resume_items=resume_items)

def get_albums(category_name):
    db = _get_db_connection()
    query = f"SELECT DISTINCT album FROM `{category_name}` WHERE album IS NOT NULL ORDER BY album ASC"
    results = db.get_data(query)
    albums = [row['album'] for row in results] if results else []
    return jsonify(albums)

def get_tracks(category_name, album_name):
    db = _get_db_connection()
    query = f"SELECT id, title FROM `{category_name}` WHERE album = %s ORDER BY track_number, title ASC"
    tracks = db.get_data(query, (album_name,))
    return jsonify(tracks if tracks else [])

def render_player_page(table_name, item_id):
    current_item = _get_item_details(table_name, item_id)
    if not current_item: return "Audio item not found", 404

    playlist, current_track_index = [], -1
    album_name = current_item.get('album')
    if album_name:
        db = _get_db_connection()
        query = f"SELECT id, title FROM `{table_name}` WHERE album = %s ORDER BY track_number, title ASC"
        playlist = db.get_data(query, (album_name,))
        for i, track in enumerate(playlist):
            if track['id'] == item_id:
                current_track_index = i
                break

    return render_template('player.html', item=current_item, category=table_name, playlist=playlist, current_track_index=current_track_index)

def update_resume_position(table_name, item_id, position, duration):
    db = _get_db_connection()
    position_to_save = float(position)
    # Clear resume position if less than 15 seconds remain
    if (float(duration) - position_to_save) < 15:
        position_to_save = 0
    query = f"UPDATE `{table_name}` SET resume_position = %s, last_played = NOW() WHERE id = %s"
    db.put_data(query, (position_to_save, item_id))
    return jsonify(status='success')

def clear_resume_position(table_name, item_id):
    db = _get_db_connection()
    query = f"UPDATE `{table_name}` SET resume_position = 0, last_played = NOW() WHERE id = %s"
    db.put_data(query, (item_id,))
    return jsonify(status='success')

def stream_audio_file(table_name, item_id):
    # This is a robust streaming implementation
    item = _get_item_details(table_name, item_id)
    if not (item and item.get('file_path')):
        return "File path not found", 404
    path = item['file_path']
    if not os.path.exists(path):
        return "File on disk not found", 404
    file_size = os.path.getsize(path)
    range_header = request.headers.get('Range', None)

    def generate_chunks(file, start, length):
        with file:
            file.seek(start)
            remaining = length
            while remaining > 0:
                chunk_size = min(remaining, 1024 * 1024) # 1MB chunks
                data = file.read(chunk_size)
                if not data: break
                yield data
                remaining -= len(data)

    if range_header:
        byte1, byte2 = 0, None
        m = re.search(r'(\d+)-(\d*)', range_header)
        g = m.groups()
        if g[0]: byte1 = int(g[0])
        if g[1]: byte2 = int(g[1])
        if byte2 is None: byte2 = file_size - 1
        length = byte2 - byte1 + 1
        resp = Response(stream_with_context(generate_chunks(open(path, 'rb'), byte1, length)), 206, mimetype='audio/mpeg', direct_passthrough=True)
        resp.headers.add('Content-Range', f'bytes {byte1}-{byte2}/{file_size}')
        resp.headers.add('Accept-Ranges', 'bytes')
        return resp

    return Response(stream_with_context(generate_chunks(open(path, 'rb'), 0, file_size)), mimetype='audio/mpeg', headers={'Content-Length': str(file_size)})
