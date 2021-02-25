
import os
import re
import pyshorteners # pip install pyshorteners


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
os.system(f"""ffmpeg -ss {time1} -i "{links[0]}" -ss {time1} -i "{links[1]}" -map 0:v -map 1:a -t {int(time2)-int(time1)} -c:v libx264 -c:a aac NoizeOx.mp4""")

print("done")

