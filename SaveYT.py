from pytube import YouTube
import os
import tkinter as tk
from tkinter.ttk import Label
from tkinter import Text, ttk, filedialog
import pyperclip

def beillesztes():
    global url
    url.delete('1.0', tk.END)
    url.insert('1.0', pyperclip.paste())
    yt = YouTube(str(url.get("1.0", tk.END)))
    cim = tk.Label(ablak, text=yt.title, font=("Arial", 8))
    cim.place(x=20)
def utvonalselect():
    utvonalURL = filedialog.askdirectory()
    utvonaltext = tk.Label(ablak, text=utvonalURL ,fg="blue")
    utvonaltext.place(x=10, y=100)
def letoltes():
    yt = YouTube(str(url.get("1.0", tk.END)))
    video = yt.streams.filter(only_audio=True).first()
    kimenet = video.download(output_path=utvonalURL)
    filename, ext = os.path.splitext(kimenet)
    if(formatum.get() == ".MP3"):
        ujfile = filename + '.mp3'
        os.rename(kimenet, ujfile)
    elif(formatum.get() == ".WAV"):
        ujfile = filename + '.wav'
        os.rename(kimenet, ujfile)
    elif(formatum.get() == ".OGG"):
        ujfile = filename + '.ogg'
        os.rename(kimenet, ujfile)
    else:
        ujfile = filename + '.mp3'
        os.rename(kimenet, ujfile)
    print(yt.title + " sikeresen letöltve!")
    letoltve = tk.Label(ablak, text="Letöltve!")
    letoltve.place(x = 190, y=190)
### 
utvonalURL = os.path.dirname(os.path.realpath(__file__))
ablak = tk.Tk()
ablak.title('SaveYT')
szelesseg = 270
magassag = 250
kepernyoszelesseg = ablak.winfo_screenwidth()
kepernyomagassag = ablak.winfo_screenheight()
x = int(kepernyoszelesseg/2 - szelesseg / 2)
y = int(kepernyomagassag/2 - magassag / 2)
ablak.geometry(f'{szelesseg}x{magassag}+{x}+{y}')
ablak.resizable(False, False)

urllbl = Label(ablak, text='URL:')
urllbl.pack(ipadx=100, ipady=20)

pathlbl = Label(ablak, text='Útvonal:')
pathlbl.pack(ipadx=100, ipady=20)

url = Text(width=23, height=1)
url.place(relx=0.56, rely=0.08, anchor='n')

beilleszt=ttk.Button(ablak, text="Beillesztés", command=beillesztes)
beilleszt.place(x=170, y=45)

utvonal=ttk.Button(ablak, text="...", command=utvonalselect, width=2)
utvonal.place(x=60, y=75)
utvonaltext = tk.Label(ablak, text=utvonalURL ,fg="blue")
utvonaltext.place(x=10, y=100)

formatumok = [".MP3", ".WAV", ".OGG"]
formatum = ttk.Combobox(ablak, state="readonly", values = formatumok, width = 7)
formatum.set(".MP3")
formatum.place(x=10, y = 215)
formatumlbl = tk.Label(ablak, text="Formátum:")
formatumlbl.place(x=10, y=194)

letolt =ttk.Button(ablak, text="Letöltés", command=letoltes)
letolt.place(x=180, y=213)
ablak.mainloop()

