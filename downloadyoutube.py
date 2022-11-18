from pytube import Playlist
import yt_dlp
from colorama import Fore
from colorama import Style




def mulvid():
    downloadDirectory = "C:\\Desktop\\Music\\"

    playlist = Playlist(input("Your playlist URL: "))

    finished = 0
    total = 0
    for video in playlist.videos:
        print(total, video.title, video.watch_url)
        total += 1
    print(f"DOWNLOADING {total} VIDEOS")
    for video in playlist.videos:
        try:
            video_url = video.watch_url
            video_info = yt_dlp.YoutubeDL().extract_info(
                url=video_url, download=False
            )
            filename = f"{downloadDirectory}{video_info['title']}.mp3"
            options = {
                'format': 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': filename,
            }

            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])

            print("Download complete... {}".format(filename))
            print(f"{Fore.CYAN}FINISHED TOTAL OF {finished + 1} / {total} VIDEOS{Style.RESET_ALL}")
            finished += 1
        except yt_dlp.DownloadError:
            print(f"{Fore.RED}Warning download error!{Style.RESET_ALL}")
            pass
    print(f"{Fore.YELLOW}FINISHED DOWNLOADING ALL {total} VIDEOS{Style.RESET_ALL}")


def mulvid4():
    downloadDirectory = "C:\\Desktop\\Video\\"

    playlist = Playlist(input("Your playlist URL: "))

    finished = 0
    total = 0
    for video in playlist.videos:
        print(total, video.title, video.watch_url)
        total += 1
    print(f"DOWNLOADING {total} VIDEOS")
    for video in playlist.videos:
        try:
            video_url = video.watch_url
            video_info = yt_dlp.YoutubeDL().extract_info(
                url=video_url, download=False
            )
            filename = f"{downloadDirectory}{video_info['title']}.mp4"
            options = {
                'format': 'bestaudio/best',
                'keepvideo': True,
                'outtmpl': filename,
            }

            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])

            print("Download complete... {}".format(filename))
            print(f"{Fore.CYAN}FINISHED TOTAL OF {finished + 1} / {total} VIDEOS{Style.RESET_ALL}")
            finished += 1
        except yt_dlp.DownloadError:
            print(f"{Fore.RED}Warning download error!{Style.RESET_ALL}")
            pass
    print(f"{Fore.YELLOW}FINISHED DOWNLOADING ALL {total} VIDEOS{Style.RESET_ALL}")


def singvid():
    video_url = input("Your video URL: ")
    video_info = yt_dlp.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f"{downloadDirectory}{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))


print("YOUTUBE VIDEO/PLAYLIST DOWNLOADER (MP3)")
choice = int(input("Single video - 1\nPlaylist - 2\nPlaylist but mp4 - 3\nEnter option: "))
if choice == 1:
    singvid()
elif choice == 3:
    mulvid4()
else:
    mulvid()
