from pytube import YouTube

link = input("Enter a YouTube video URL: ")
DEST_PATH = input("Enter a file destination path: ")

try:
    video = YouTube(link).streams[0].download(DEST_PATH)
    print("Video downloaded successfully")
except:
    print("An error occurred while trying to download the video")

