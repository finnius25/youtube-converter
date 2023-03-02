import tkinter
import customtkinter
from pytube import YouTube


def downloadVideo():
    print("video download")
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()

        video.download()
        finishLabel.configure(text="Download Complete", text_color="green")
    except:
        finishLabel.configure(text="Download Failed", text_color="red")


def downloadAudio():
    print("audio download")
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        audio = ytObject.streams.get_audio_only()

        audio.download()
        finishLabel.configure(text="Download Complete", text_color="green")
    except:
        finishLabel.configure(text="Download Failed", text_color="red")


#Systems Settings
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#Create Window
app = customtkinter.CTk() 
app.geometry("720x480")
app.title("Youtube Converter")


title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)


url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

downloadAudio = customtkinter.CTkButton(app, text='Download Audio', command=downloadAudio)
downloadAudio.pack(padx=10, pady=10)


downloadVideo = customtkinter.CTkButton(app, text='Download Video', command=downloadVideo)
downloadVideo.pack(padx=10, pady=10)

app.mainloop()
