from pytube import YouTube

DEST_PATH = "/Users/chi-mingyip/Documents/Youtube"
link = "https://www.youtube.com/watch?v=Kg-HHXuOBlw"

try:
    video = YouTube(link).streams[0].download(DEST_PATH)
except:
    print("An error occurred while trying to download the video")

print("Video downloaded successfully")
