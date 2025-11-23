# Day 16: YouTube Video Downloader
# Author: Janani

from pytube import YouTube

print("🎬 YouTube Video Downloader")

url = input("📌 Enter YouTube video URL: ")

try:
    yt = YouTube(url)
    print(f"🎥 Title: {yt.title}")

    print("📥 Downloading...")
    stream = yt.streams.get_highest_resolution()
    stream.download()

    print("✅ Download completed successfully!")

except Exception as e:
    print(f"❌ Error: {e}")
