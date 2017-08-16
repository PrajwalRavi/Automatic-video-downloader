import requests
import tkinter
import os
from bs4 import BeautifulSoup
import sys
import re
from pytube import YouTube

class GetInput:

    def __init__(self):

        self.file_list=None
        self.path=None

    def files(self):

        self.path=input().strip()
        all_files=os.listdir(self.path)
        self.file_list=[]
        for f in all_files:
            if(f[-3:] is not "mp4"):
                self.file_list.append(f[:-4])

class Download:

        def __init__(self, files, path):

            self.path=path
            self.file_list=files

        def getid(self, vid):

            url = "https://www.youtube.com/results?search_query=" + vid
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "lxml")
            a = soup.find("a",
                          class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link ")
            vid_id = a["href"]
            return vid_id


        def yt_download(self):

            print(self.file_list)
            finished = []

            for vid in self.file_list:
                if vid in finished:
                    finished[vid]+=1
                else:
                    finished[vid]=0

            for vid in self.file_list:
                if(finished[vid]==0):
                    print("Downloading ",vid)
                    id=self.getid(vid)
                    url="https://www.youtube.com"+id
                    yt=YouTube(url)
                    yt.set_filename(vid)
                    video=yt.get("mp4", "360p")
                    video.download(self.path)

            print("\nDONE!!!\n")

obj=GetInput()
obj.files()
download_obj=Download(obj.file_list, obj.path)
download_obj.yt_download()
