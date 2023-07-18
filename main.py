import pytube
from moviepy.editor import VideoFileClip

download_path = r"C:\Users\Billy.davison\Downloads\YoutubeDownloads"
conversion_path = r"C:\Users\Billy.davison\Downloads\YoutubeDownloads\Converted"


# Function to download the YouTube video
def download_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download(download_path)
    return video.default_filename

# Function to convert the downloaded video to MP3
def convert_to_mp3(filename):
    video = VideoFileClip(download_path + filename)
    mp3_filename = filename.split(".")[0] + ".mp3"
    video.audio.write_audiofile(conversion_path + mp3_filename)
    return mp3_filename



# Example usage
video_url = "https://www.youtube.com/watch?v=r-GSGH2RxJs"
filename = download_video(video_url)
mp3_filename = convert_to_mp3(filename)
print("Downloaded video:", filename)
print("Converted MP3:", mp3_filename)