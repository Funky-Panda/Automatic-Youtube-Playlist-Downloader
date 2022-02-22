#from __future__ import unicode_literals 
import subprocess
from cgitb import reset
from sys import api_version
from urllib import request, response
from googleapiclient.discovery import build
#import pandas as pd
import seaborn as sns
import yt_dlp
import os 
from youtube_dl import YoutubeDL
import pyudev
import shutil 
from pushbullet import Pushbullet
import time


pushbullet_key = 'o.9r4kfPlL31WmffeqNOmH6wsCLFwLsB08'
pb = Pushbullet(pushbullet_key)
api_key = "AIzaSyAzFd8E4KCdYYESa_zgBBGjUE8q7ktQrxk"
playlist_id = "PLdZNFVCDo_1dPYrlJkQIWlwjRZXQ-r9YN"

youtube = build("youtube","v3",developerKey=api_key)

api_service_name = 'youtube'
api_version = 'v3'

request = youtube.playlistItems().list(part=['snippet'], playlistId=playlist_id)
response = request.execute()

for (k, v) in response.items():
    if(k == 'items'):
        video_ids = [pli['snippet']['resourceId']['videoId'] for pli in v if pli['snippet']['resourceId']['kind']=='youtube#video']
        
youtube_link = "https://www.youtube.com/watch?v="+video_ids[0]
YDL_OPTIONS={}

with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(youtube_link , download=False)

title = (info["title"])

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')
pushes = pb.get_pushes()
#pb.push_note("DOWNLOADED:", "IT IS SAFE TO REMOVE NOW")

import os.path

file_exists = os.path.exists('/media/pi/MOVIES/'+(title)+".mp4")

#print(file_exists)
print ("Insert USB:")

for device in iter(monitor.poll, None):
    if device.action == 'add':
        pb.push_note("BUG REPORT","Transfering...")
        print ("Loading...")
        time.sleep(10)
        #subprocess.run(["mount","/dev/sda1","/media/usb/"])
        #time.sleep(2)
        subprocess.run(["mv","*.mp4","/media/pi/MOVIES"])
        #subprocess.run(["umount","/media/usb/"])
        #subprocess.run(["eject","sda1"])        
        pb.push_note("BUG REPORT","The file has Successfully transferd to usb")
        print(file_exists)
        #subprocess.run(["python3", "test.py"])




      		
        

        #pb.push_note("DOWNLOADED:", "IT IS SAFE TO REMOVE NOW")
        #print(title)
        
#subprocess.run(["mv",title+".mp4","/media/pi/2275-474D/Muma"])
