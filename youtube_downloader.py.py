import yt_dlp
import os
import asyncio


async def download_youtube_playlist_audio(playlist_url, output_path="."):
    """
    Downloads the audio from a YouTube playlist as fast as possible.

    Args:
        playlist_url (str): The URL of the YouTube playlist.
        output_path (str): The root folder where the playlist folder will be created.
                        Defaults to the current directory (".")
    """

    ydl_opts = {
        'format': 'bestaudio/best',  # Select the best available audio format
        'extractaudio': True,  # Only extract audio
        'audioformat': 'mp3',  # Convert to MP3 (you can change this)
        'outtmpl': '%(playlist)s/%(title)s.%(ext)s',  # Output path with playlist name
        'noplaylist': False,  # Ensure it processes the whole playlist
        'nocheckcertificate': True, # Avoid SSL errors
        'ignoreerrors': True, # Continue if a video fails
        'quiet': True, # Suppress output messages, remove for debugging
        'concurrent_fragment_downloads': 10,  # Download multiple audio fragments concurrently, adjust as needed
    }

    # Resolve playlist name before downloading.  This prevents a weird folder name if it fails later.
    try:
        with yt_dlp.YoutubeDL({'quiet': True, 'extract_flat': True}) as ydl:  # extract_flat gets playlist info fast
            playlist_info = ydl.extract_info(playlist_url, download=False)
            playlist_name = playlist_info['title']
    except Exception as e:
        print(f"Error getting playlist name: {e}")
        return # Stop if we can't even get the name

    playlist_folder = os.path.join(output_path, playlist_name)  # Construct the full path
    os.makedirs(playlist_folder, exist_ok=True)  # Create the directory if it doesn't exist

    ydl_opts['outtmpl'] = os.path.join(playlist_folder, '%(title)s.%(ext)s') # Update output template with full path

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])

    except Exception as e:
        print(f"An error occurred during download: {e}")



async def main():
    """
    Main function to handle user input and start the download.
    """

    playlist_url = input("Enter the YouTube playlist URL: ")
    output_path = input("Enter the output folder (leave blank for current directory): ") or "."  # Use current dir if blank

    print(f"Downloading audio from playlist: {playlist_url}")
    print(f"Saving to folder: {output_path}")

    await download_youtube_playlist_audio(playlist_url, output_path)
    print("Download complete!")

if __name__ == "__main__":
    asyncio.run(main())