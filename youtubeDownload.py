from pytube import YouTube

from sys import argv

link = argv[111]
yt = YouTube([link])

print("title;",yt.title)

print("view:",yt.views)

yd = yt.streams.get_gighest_resolution()

yd.download('https://www.youtube.com/watch?v=vEQ8CXFWLZU/desktop')

