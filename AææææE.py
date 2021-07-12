import os
import re
import pyshorteners # pip install pyshorteners
import clipboard # pip install clipboard



def srt2mkv():
	videofile = input("Videofile name:")
	srtfile = input("SRTfile name:")
	result = f"ffmpeg -i {videofile} -f srt -i {srtfile} -map 0:0 -map 0:1 -map 1:0 -c:v copy -c:a copy -c:s srt out.mkv"
	clipboard.copy(result)
	print("\n===> Check your clipboard. <===\n")


def partdown():
	while True:
		name = input("Name of output file:")
		put = input("Link:")
		time1 = input("time1:")
		time2 = input("time2:")

		cmd = f"youtube-dl -g {put} > aeef.txt"
		os.system(cmd)
		file1 = open("aeef.txt", "r")
		for line in file1:
			print(line+"\n\n")
		file1.close()

		file1 = open("aeef.txt", "r")
		links = []
		s = pyshorteners.Shortener()
		for line in file1:
			links.append(s.isgd.short(line.rstrip()))
		file1.close()

		print(links)


		#FINAL STEP
		os.system(f"""ffmpeg -ss {time1} -i "{links[0]}" -ss {time1} -i "{links[1]}" -map 0:v -map 1:a -t {int(time2)-int(time1)} -c:v libx264 -c:a aac {name}.mp4""")

		print("done")
		retry = input("\n\nRetry?[No\\Yes]:")
		if retry=="No":
			break

while True:
	choice = input("1 - partdown\n2 - SRTtoMKV\n:__-->")
	if choice == "1":
		partdown()
	elif choice == "2":
		srt2mkv()
	elif choice == "exit":
		break
	else:
		print("===> There is no such command. <===\n")
