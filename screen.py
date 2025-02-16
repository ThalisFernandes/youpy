from tkinter import *
from tkinter import ttk
import random
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from youpy import download_youtube_as_mp3

class Interface:
    def __init__(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title("Youpy downloader")
        self.style = Style(theme='cyborg')
        self.root.resizable(False, False)

    def url_field(self):
        self.url = StringVar()
        self.url_entry = ttk.Entry(self.root, textvariable=self.url)
        self.url_entry.place(x=10, y=10, width=300, height=30)

    def download_button(self):
        self.download = ttk.Button(self.root, text="Download", command=self.download)
        self.download.place(x=10, y=50, width=300, height=30)
    
    def download(self):
        video_url = self.url.get()
        download_youtube_as_mp3(video_url)
        
    def youpy_run(self):
        self.url_field()
        self.download_button()
        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    interface = Interface(root, 320, 120)
    interface.youpy_run()