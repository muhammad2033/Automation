from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

print(yt.title)
print(yt.thumbnail_url)
