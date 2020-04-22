This was made to be run on a Windows machine. That being said there are certain dependencies required.
This was an old project that I wanted to publish in case anyone was interested in such a program.

Dependencies:
- Python 3 or higher
- pip install gtts
- pip install praw
- pip install pillow

- ffmpeg - please install this using this guide: https://video.stackexchange.com/questions/20495/how-do-i-set-up-and-use-ffmpeg-in-windows

Usage:
- Run using the main.py file.
- The program generates video based upon the generationFile.py where you can select the desired subreddit and such.
- The fileNum.txt file is used for keeping track of how many videos have been created.
- The files.txt is a concatenation of all the files that are going to be pieced together.
Do NOT delete these files as they are necessary for the generation of your video.