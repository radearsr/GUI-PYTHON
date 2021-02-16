from tkinter import *
from moviepy.editor import *
from tkinter import filedialog
from tkinter import messagebox as msg


root = Tk()
root.title("Convert Video To Audio")
root.geometry("680x300")
root.iconbitmap("icon_convert.ico")
root.configure(bg="#6C6C6C")
root.resizable(False, False)


# Fungsi command untuk membuka file mp4
def open_file_mp4():
    openfile = filedialog.askopenfilename(
        initialdir="C:/Users/RADEARSR/Videos",
        title='Open File',
        filetypes=(('MP4', '*.*'), ('All Files', '*.*'))
        )
    entry_file_mp4.insert(0, openfile)


# deklarasi Fungsi command untuk menempatkan hasil convert mp4 -> mp3
def open_dir_mp3():
    opendir = filedialog.askdirectory(initialdir="C:/Users/RADEARSR/Music")
    entry_file_mp3.insert(0, opendir)


# deklarasi Fungsi command untuk menamai nama file hasil convert mp4 -> mp3
def convert():
    isi_mp3 = entry_file_mp3.get()
    isi_mp4 = entry_file_mp4.get()
    file_name = entry_name_file.get()
    if isi_mp3 != '' and isi_mp4 != '' and file_name != '':
        name_mp3 = isi_mp3 + "/" + file_name + ".mp3"
        video_clip = VideoFileClip(isi_mp4)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(name_mp3)
        msg.showinfo(title="Konfirmasi", message="Convert Suscess")
    else:
        msg.showwarning(title="Error", message="Isi semua kolom yang ada")


# Button Untuk Open File Video
button_open_file_mp4 = Button(
    root,
    text="Browse",
    command=open_file_mp4,
    padx=30,
    pady=7,
    border=2,
    )
button_open_file_mp4.place(x=565, y=10)

# Button Memilih Folder/Direktori Untuk Menyimpan Hasil File Mp3
button_open_dir_mp3 = Button(
    root,
    text="Browse",
    command=open_dir_mp3,
    padx=30,
    pady=7,
    border=2,
    )
button_open_dir_mp3.place(x=565, y=57)

# Button Untuk Menjalankan Convert Video Ke Audio
button_convert = Button(
    root,
    text="CONVERT NOW",
    command=convert,
    padx=190,
    pady=7,
    border=5,
    )
button_convert.place(x=105, y=180)

# Button Untuk Mengganti Tema
button_theme = Button(
    root,
    text="Change Theme",
    padx=8,
    pady=8,
    border=3,
    )
button_theme.place(x=5, y=257)

# Button Keluar Atau Close Program
button_quit = Button(
    root,
    text="Exit",
    command=quit,
    padx=35,
    pady=8,
    border=2,
    )
button_quit.place(x=580, y=257)

# Variabel Label
bg_label = "#d5bb3a"
label_open_file_mp4 = Label(
    root,
    text="Select File Mp4:",
    bg=bg_label,
    font=("Times", "12", "bold")
    )
label_open_dir_mp3 = Label(
    root,
    text="Destination       :",
    bg=bg_label,
    font=("Times", "12", "bold")
    )
label_enter_name = Label(
    root,
    text="Name Mp3       :",
    bg=bg_label,
    font=("Times", "12", "bold")
    )

# Variabel Entry
color_entry = "#121212"
font_color = "#FFFFFF"

entry_file_mp4 = Entry(
    root,
    width=54,
    borderwidth=3,
    bg=color_entry,
    fg=font_color,
    font=("Times", "12", "bold")
    )
entry_file_mp3 = Entry(
    root,
    width=54,
    borderwidth=3,
    bg=color_entry,
    fg=font_color,
    font=("Times", "12", "bold")
    )
entry_name_file = Entry(
    root,
    width=68,
    borderwidth=3,
    bg=color_entry,
    fg=font_color,
    font=("Times", "12", "bold")
    )

# Entry Position
entry_file_mp4.place(x=120, y=20)
entry_file_mp3.place(x=120, y=65)
entry_name_file.place(x=120, y=110)

# Label Position
label_open_file_mp4.place(x=0, y=20)
label_open_dir_mp3.place(x=0, y=65)
label_enter_name.place(x=0,  y=110)

root.mainloop()
