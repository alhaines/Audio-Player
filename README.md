# Long-Form Audio Player v1.0

A simple and robust Flask and Gunicorn web application for browsing and playing long-form audio files like audiobooks, comedy albums, and instructional series.

This application is designed to be a personal, self-hosted audio library, accessible from any web browser on your local network.

## Features

-   **Database-Driven:** Scans your audio directories and populates a MySQL/MariaDB database for fast browsing.
-   **Folder-Based Navigation:** Browse your library by Category (table), Album/Book (folder), and then Chapter/File.
-   **Resume Playback:** The player automatically saves your listening position every 10 seconds. The main page displays a "Continue Listening" list of your most recently played files.
-   **Continuous Play:** Automatically plays the next track in an album or audiobook. When the last track finishes, it returns you to the main menu.
-   **Clean & Simple UI:** A straightforward web interface designed for ease of use.

## Requirements

1.  A Linux system with Python 3, `pip`, and a running MySQL/MariaDB server.
2.  An `audio` database. The necessary tables will be created by the import script.
3.  `Gunicorn` for running the application as a service.

## Installation

This project is designed for manual installation by a system administrator.

/home/$USER/projects/audio-player
├── app.py
├── audio-player.1
├── audio-player.sql
├── audio.service
├── config_audio.py
├── MySql.py
├── OV.py
├── read_audio_to_mysql.py
├── README.md
├── static
│   └── styles.css
├── templates
│   ├── browser.html
│   ├── index.html
│   └── player.html
└── wsgi.py


1.  **Place Project Files:**
    Copy the entire `audio-player` project directory to your desired location (e.g., `/home/al/projects/audio-player`).

2.  **Install Python Dependencies:**
    Install the required libraries using `pip`.
    ```bash
    pip install Flask PyMySQL gunicorn
    ```

3.  **Configure Database:**
    Edit the `config_audio.py` file with your `audio` database credentials.

4.  **Populate the Database:**
    *   First, run the included `add_resume_columns.sql` and `add_track_number_column.sql` scripts on your `audio` database using a tool like phpMyAdmin.
    *   Then, run the importer script to scan your media files and populate the tables:
    ```bash
    python3 /path/to/your/read_audio_to_mysql.py
    ```

5.  **Install the Service File:**
    Copy the included `audio.service` file to your system's `systemd` directory.
    ```bash
    sudo cp /path/to/your/audio.service /etc/systemd/system/audio.service
    ```

6.  **Enable and Start the Service:**
    ```bash
    sudo systemctl enable audio.service
    sudo systemctl start audio.service
    ```

## Verify the Service

You can check the status of the running application at any time with:
```bash
sudo systemctl status audio.service

