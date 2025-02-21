# 🔴 YouTube Playlist Audio Downloader ⬇️

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Trinitysudo/Youtube-Playlist-Downloader/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Download audio tracks from YouTube playlists quickly and easily as MP3 files. This script utilizes `yt-dlp` for fast, reliable, and efficient downloads. It automatically creates a folder named after the playlist and saves all audio files within.

## ✨ Features

*   **⚡️ Fast Downloads:** Employs concurrent fragment downloads for optimized speed.
*   **📂 Automatic Folder Creation:** Organizes your downloads by creating a folder for each playlist, named accordingly.
*   **🛠️ Error Handling:** Gracefully handles potential errors during the download process.
*   **🎼 MP3 Conversion:** Converts downloaded audio to widely compatible MP3 format.
*   **💻 Simple Usage:** User-friendly interface with clear prompts for playlist URL and output directory.

## ⚙️ Installation

1.  **Prerequisites:** Make sure you have Python 3.7 or higher installed on your system.
2.  **Install Dependencies:**
    ```bash
    pip install yt-dlp asyncio
    ```

## 🚀 Usage

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Trinitysudo/Youtube-Playlist-Downloader.git
    cd Youtube-Playlist-Downloader
    ```
2.  **Run the Script:**
    ```bash
    python youtube_downloader.py
    ```
3.  **Follow Prompts:** The script will ask you to:
    *   Enter the YouTube playlist URL.
    *   Enter the desired output folder (leave blank for the current directory).

4.  **Sit Back and Relax:** The script will download all audio from the playlist and save it in the specified folder. 🎧

## 📂 Output

The downloaded audio files will be saved in a folder created in the specified output directory (or the current directory if none is specified). The folder name will match the name of the YouTube playlist.
