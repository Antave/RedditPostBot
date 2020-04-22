import os
import glob
import subprocess
frameNum = 0
from oauth2client import file
from generationFile import title
from generationFile import numOfFiles
from generationFile import generateNum
idNum = numOfFiles + 1

#runs the post retriever to fetch all of the information about each post
print('running retriever: ')
os.system('python reddit_post_retriever.py')
print('finished encoding mp3 and png')

#targets each post and creates videos out of each collection
for i in range(0, generateNum):
	for name in glob.glob('reddit_' + str(idNum) + '_??.png'):
		os.system("ffmpeg -i " + name + " -i reddit_" + str(idNum) + "_" + str(frameNum).zfill(2)
		+".mp3 reddit_" + str(idNum) + "_" + str(frameNum).zfill(2) + ".avi")
		
		#adds all video clips to the files doc to prepare for concatenation
		os.system("@echo file reddit_" + str(idNum) + "_" + str(frameNum).zfill(2) + ".avi >>files.txt")
		
		#adds one number after each video clip
		frameNum += 1
	print("------------------")
	print("finished video " + str(idNum))
	idNum += 1
	frameNum = 1
		
#concatenates all of the video clips together
os.system("ffmpeg -f concat -i files.txt -c copy final_video.avi")

#fixes encoding issues as well as speed up the video
os.system("ffmpeg -i final_video.avi" + " -filter_complex \"[0:v]setpts=0.625*PTS[v];[0:a]atempo=1.6[a]\" -map \"[v]\" -map \"[a]\" -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192k -pix_fmt yuv420p -max_muxing_queue_size 40000 fixed_final_video.mp4")

#posts the video to youtube via the youtube api (experimental, read documentation)
#os.system("python -m youtube_upload --title=" + title + str(idNum) + " fixed_final_video.mp4")