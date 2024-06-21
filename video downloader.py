from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def downloader(save_path,url):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_quality = streams.get_highest_resolution()
        highest_quality.download(output_path=save_path)
        print("Download Complete")

    except Exception as e:
        print(e)

def open_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__=="__main__":
    root = tk.Tk()
    root.withdraw

video_url = input("Enter video url: ")
save_dir = open_dialog()
if save_dir:
    print("Download started")
    downloader(save_dir,video_url)
else:
    print("invalid directory")