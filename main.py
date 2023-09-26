import os
import moviepy
from moviepy.editor import *
from moviepy.video.fx import loop

audioList = os.listdir("audio")
videoList = os.listdir("videos")

videoClipO = VideoFileClip('videos/' + videoList[0])
videoClipT = VideoFileClip('videos/' + videoList[1])

final = concatenate_videoclips([videoClipO, videoClipT]);
final.write_videofile("merged.mp4")

