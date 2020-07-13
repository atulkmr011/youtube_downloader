from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
file_size = 0


def startDownload():
    global file_size
    try:
        url = urlField.get()
        print(url)
        dBtn.config(text="Please Wait......")
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return
        ob= YouTube(url)
        strm = ob.streams.first()
        strm.download(path_to_save_video)
        print("done")
        dBtn.config(text="Start Download")
        dBtn.config(state=NORMAL)
        showinfo("Downloaded Finished","Downloaded successfully")
        urlField.delete(0,END)



    except Exception as e:
        print(e)
        print("error!!!!") 


main =Tk()

main.title("My YouTube Downloader")
main.iconbitmap('icon.ico')
main.geometry("600x500")

file = PhotoImage(file = 'youtube.png')
headingIcon= Label(main,image = file)
headingIcon.pack(side=TOP)

urlField=Entry(main,font=("verdana",12),justify= CENTER)
urlField.pack(side = TOP, fill = X ,padx=30)

dBtn=Button(main,text ="Start Download", font=("verdana",12),relief= "ridge", command = startDownload )
dBtn.pack(side=TOP,pady=30)

main.mainloop()

