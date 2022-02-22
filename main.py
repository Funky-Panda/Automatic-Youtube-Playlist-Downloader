from __future__ import unicode_literals 
from urllib import request, response
from googleapiclient.discovery import build
from os import link
from pytube import YouTube
import time
import datetime
from datetime import timedelta
import time
import os
from pushbullet import Pushbullet

pushbullet_key = "YOUR-KEY"
pb = Pushbullet(pushbullet_key)
api_key = "youtube api key"
playlist_id = "playlist Id"

youtube = build("youtube","v3",developerKey=api_key)

api_service_name = 'youtube'
api_version = 'v3'

request = youtube.playlistItems().list(part=['snippet'], playlistId=playlist_id)
response = request.execute()

# scrape out the actual video ids (probably could be safer)
for (k, v) in response.items():
    if(k == 'items'):
        video_ids = [pli['snippet']['resourceId']['videoId'] for pli in v if pli['snippet']['resourceId']['kind']=='youtube#video']

youtube_link = "https://www.youtube.com/watch?v="+video_ids[0]
print(youtube_link)

start = time.time()




pb.delete_pushes()
video = YouTube(youtube_link)
stream = video.streams.get_by_itag(22)
#print(stream)
title = stream.title
print(title)
stream.download()
end = time.time()
end_time = round(end - start)
mins = end_time/60
string_end_time = str(mins)
pb.push_note("DOWNLOADED:", "Download video in: "+string_end_time)
print(round(end_time,2))
