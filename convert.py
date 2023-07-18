import pytube
from moviepy.editor import VideoFileClip
import time

# Configure the download and conversion paths
download_path = r"file\directory\here"
conversion_path = r"convert-file\directory\here"
video_url = input("Paste your video url here: ")

# Function to download the YouTube video
def download_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video_filename = video.default_filename
    video.download(download_path)
    return video_filename
    time.sleep(6)

filename = download_video(video_url)

# Function to convert the downloaded video to MP3
def convert_to_mp3(filename):
    video = VideoFileClip(download_path + "\\" + filename)
    mp3_filename = filename.split(".")[0] + ".mp3"
    video.audio.write_audiofile(conversion_path + "\\" +mp3_filename)
    return mp3_filename

mp3_filename = convert_to_mp3(filename)



print("Downloaded video:", filename)
print("Converted MP3:", mp3_filename)
