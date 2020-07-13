from pytube import *
from tkinter import *
from tkinter.filedialog import *
file_size = 0


def startDownload(url):
    global file_size
    try:
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return
        ob= YouTube(url)
        strm = ob.streams.first()
        strm.download(path_to_save_video)
        print("done")



    except Exception as e:
        print(e)
        print("error!!!!") 


main =Tk()

main.title("My YouTube Downloader")
main.iconbitmap('C:\\Users\\Atul\\Desktop\\progs\\youtube_downloader\\icon.ico')
main.geometry("500x600")

