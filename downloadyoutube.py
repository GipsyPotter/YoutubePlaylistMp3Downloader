from pytube import Playlist
import yt_dlp
from colorama import Fore
from colorama import Style

import os
from pynput import keyboard
from pynput.keyboard import Key


def clear():
    os.system("cls")


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
    downloadDirectory = "C:\\Desktop\\Music\\"
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


def update_cur(math):
    global cur
    global maxi
    if math == "+":
        if cur < maxi - 1:
            cur += 1
        else:
            cur = 0
    elif math == "-":
        if cur > 0:
            cur -= 1
        else:
            cur = maxi - 1


def chose(index):
    global chosen
    if index == 0:
        mulvid()
    elif index == 1:
        mulvid4()
    elif index == 2:
        singvid()
    chosen = True


def on_key_release(key):
    if key == Key.up:
        update_cur("-")
    elif key == Key.down:
        update_cur("+")
    elif key == Key.left or key == Key.right:
        chose(cur)
    return False


def export_menu(opt: list, cur: int):
    for i in range(len(opt)):
        if i == cur:
            print(f"{Fore.CYAN}>> {opt[i]}{Style.RESET_ALL}")
        else:
            print("  ", opt[i])


if __name__ == '__main__':
    opt = ["Playlist as MP3", "Playlist as MP4", "Single video as MP3"]  # Create a list of options
    maxi = len(opt)  # Get the max index
    cur = 0  # Set the cursor to 0
    chosen = False  # Set the chosen to False
    while chosen is False:
        clear()
        print("""
YOUTUBE VIDEO/PLAYLIST DOWNLOADER
Made by: ThePotterio
        """)
        export_menu(opt, cur)
        print("Press up/down to navigate, left/right to select")
        with keyboard.Listener(on_release=on_key_release) as listener:
            listener.join()
