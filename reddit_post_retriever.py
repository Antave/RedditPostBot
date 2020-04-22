import praw
import urllib.request
import textwrap
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
from generationFile import subreddit
from generationFile import generateNum

fileNum = open('fileNum.txt', 'r')

#accesses reddit api with credentials
reddit = praw.Reddit(client_id = 'CLIENTID',
	client_secret = '_CLIENTSECRET', 
	user_agent = 'USERAGENT')
	
page_num = 0
textLine = 0
numOfFiles = int(fileNum.readline())

file_name = 'reddit'
message = ""
id_num = numOfFiles

def img_create():
	#create Image object with the input image
	image = Image.open('background.png')

	#initialise the drawing context with
	#the image object as background
	draw = ImageDraw.Draw(image)

	#create font object with the font file and specify
	#desired size
	font = ImageFont.truetype('Roboto-Bold.ttf', size=40)

	#starting position of the message
	(x, y) = (50, 480)
	
	#change color of text
	color = 'rgb(0, 0, 0)'

	#draw the message on the background
	draw.text((x, y), message, fill=color, font=font)
	(x, y) = (150, 150)
	name = 'Vinay'
	color = 'rgb(255, 255, 255)' # white color
	draw.text((x, y), name, fill=color, font=font)

	#save the edited image
	image.save("reddit_" + str(id_num) + "_" + str(page_num).zfill(2) + ".png")

#targets each post as specified
for submission in reddit.subreddit(subreddit).new(limit = generateNum):
	print(submission.title)
	print(submission.url)
	id_num += 1
	print('id_num: ' + str(id_num))
	
	#starts encoding script into .txt file
	message += submission.title + "\n \n"
	message += "credit to u/" + str(submission.author) + "\n"
	img_create()
	print(message)
	tts = gTTS(text = message, lang = 'en', slow=False)
	tts.save("reddit_" + str(id_num) + "_" + str(page_num).zfill(2) + ".mp3")
	message = ""
	page_num += 1
	
	
	#formats and wraps text correctly
	w = textwrap.wrap(submission.selftext, 100, break_long_words=False)
	for line in w:
		#formats each message for 2 lines
		submission.selftext = line + "\n" + "\n"
		message += submission.selftext
		
        
        #Experimental swearing filter (completely optional)
        
        #goes through text filtering to remove profanity and errors
		message = message.replace("&#x200B;", "")
		message = message.replace("fuck", "frick")
		message = message.replace("bitch", "batch")
		message = message.replace("shit", "crap")
		message = message.replace("dick", "jerk")
		#i cant figure out how to replace ignoring case so, oh well
		message = message.replace("FUCK", "FRICK")
		message = message.replace("BITCH", "BATCH")
		message = message.replace("SHIT", "CRAP")
		message = message.replace("DICK", "JERK")
		
		#creates a google text to speech mp3 of each line
		tts = gTTS(text = message, lang = 'en')
		tts.save("reddit_" + str(id_num) + "_" + str(page_num).zfill(2) + ".mp3")
			
		img_create()
		print(message)
		
		if textLine == 2:
			message = ""
			page_num += 1
			textLine = 0
			
		textLine += 1

	page_num = 1
	print("------------------")
	
	#saves progress of each file in text document
	fileNumber = open('fileNum.txt', 'w')
	fileNumber.write(str(id_num))
	
	#closes each document
	fileNumber.close()
	fileNum.close()