import ffmpeg
import requests
from tqdm import tqdm

# download random png image from unsplash
r = requests.get("https://source.unsplash.com/random/1920x1080", stream=True)

# save the extension to a variable
filename = str.format("input.{0}", r.headers["content-type"].split("/")[-1])

# get the total file size
total = int(r.headers.get("content-length", 0))
block_size = 1024
t = tqdm(total=total, unit="iB", unit_scale=True)

# save image to file
with open(filename, "wb") as f:
    for data in r.iter_content(block_size):
        t.update(len(data))
        f.write(data)

t.close()

# read png image
stream = ffmpeg.input(filename)

# convert png to webp (lossy, qulity 0, compression_level 0)
stream = ffmpeg.output(stream, "output.webp", compression_level=0, qscale=0)

# run ffmpeg. if file exists, overwrite it
ffmpeg.run(stream, overwrite_output=True)

# download random wav audio from internet
r = requests.get("https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav", stream=True)

total = int(r.headers.get("content-length", 0))
block_size = 1024
t = tqdm(total=total, unit="iB", unit_scale=True)

# save audio to file
with open("input.wav", "wb") as f:
    for data in r.iter_content(block_size):
        t.update(len(data))
        f.write(data)

t.close()

# read wav audio
stream = ffmpeg.input("input.wav")

# convert wav to mp3 (lossy, 16kbps)
stream = ffmpeg.output(stream, "output.mp3", audio_bitrate="16k")

# run ffmpeg. if file exists, overwrite it
tqdm(ffmpeg.run(stream, overwrite_output=True))

# print output.webp and output.mp3 file size in MB
import os

print("Done!")

print(
    str.format(
        "output.webp size: {0:.2f} MB", os.path.getsize("output.webp") / (1024 * 1024)
    )
)
print(
    str.format(
        "output.mp3 size: {0:.2f} MB", os.path.getsize("output.mp3") / (1024 * 1024)
    )
)
