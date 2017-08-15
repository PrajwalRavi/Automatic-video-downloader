import requests
import tkinter
import os
from bs4 import BeautifulSoup
import sys

class GetInput:

    def __init__(self):

        file_list=None

    def files(self):

        path=input().strip()
        all_files=os.listdir(path)
        file_list=[]
        for f in all_files:
            if(f[-3:] is not "mp4"):
                file_list.append(f)

class Download:

        def geturl(self, vid):


        def yt_download(self):

            for vid in self.file_list:
                url=self.geturl(vid)


class youtube:

    def __init__(self):



obj=GetInput()
obj.files()
