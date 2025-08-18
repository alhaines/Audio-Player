SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE TABLE `audio_audiobooks` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `file_path` text NOT NULL,
  `category` varchar(255) DEFAULT NULL,
  `artist` varchar(255) DEFAULT NULL,
  `album` varchar(255) DEFAULT NULL,
  `track_number` int(11) DEFAULT NULL,
  `resume_position` float DEFAULT 0,
  `last_played` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `audio_collections` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `file_path` text NOT NULL,
  `category` varchar(255) DEFAULT NULL,
  `artist` varchar(255) DEFAULT NULL,
  `album` varchar(255) DEFAULT NULL,
  `track_number` int(11) DEFAULT NULL,
  `resume_position` float DEFAULT 0,
  `last_played` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `audio_comedy` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `file_path` text NOT NULL,
  `category` varchar(255) DEFAULT NULL,
  `artist` varchar(255) DEFAULT NULL,
  `album` varchar(255) DEFAULT NULL,
  `track_number` int(11) DEFAULT NULL,
  `resume_position` float DEFAULT 0,
  `last_played` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `audio_instructional` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `file_path` text NOT NULL,
  `category` varchar(255) DEFAULT NULL,
  `artist` varchar(255) DEFAULT NULL,
  `album` varchar(255) DEFAULT NULL,
  `track_number` int(11) DEFAULT NULL,
  `resume_position` float DEFAULT 0,
  `last_played` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `audio_singles` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `file_path` text NOT NULL,
  `category` varchar(255) DEFAULT NULL,
  `artist` varchar(255) DEFAULT NULL,
  `album` varchar(255) DEFAULT NULL,
  `track_number` int(11) DEFAULT NULL,
  `resume_position` float DEFAULT 0,
  `last_played` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


ALTER TABLE `audio_audiobooks`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `audio_collections`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `audio_comedy`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `audio_instructional`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `audio_singles`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `audio_audiobooks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `audio_collections`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `audio_comedy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `audio_instructional`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `audio_singles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
