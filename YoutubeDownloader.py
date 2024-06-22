import pytube
from tqdm import tqdm

def progress_bar(stream, chunk, bytes_remaining):
    global pbar
    bytes_downloaded = stream.filesize - bytes_remaining
    pbar.update(len(chunk))

url = input("Enter Video URL: ")


path = ""  


yt = pytube.YouTube(url, on_progress_callback=progress_bar)

stream = yt.streams.get_highest_resolution()

total_size = stream.filesize

with tqdm(total=total_size, unit='B', unit_scale=True, desc=yt.title) as pbar:

    stream.download(path)

print("Download complete!")
