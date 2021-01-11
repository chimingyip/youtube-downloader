from pytube import YouTube
import tkinter as tk

HEIGHT = 300
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

button = tk.Button(root, text="Test button")
button.pack()
root.mainloop()

link = input("Enter a YouTube video URL: ")
DEST_PATH = input("Enter a file destination path: ")

try:
    video = YouTube(link).streams[0].download(DEST_PATH)
    print("Video downloaded successfully")
except:
    print("An error occurred while trying to download the video")

