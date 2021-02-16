# import tkinter.font as font 
from tkinter import *
from PIL import ImageTk,Image
import random
from moviepy.editor import *
from tkinter import filedialog
from tkinter import messagebox as msg


root = Tk()
root.title("Convert Video To Audio")
root.geometry("680x300")
root.iconbitmap("icon_convert.ico")
root.configure(bg = "#6C6C6C")
root.resizable(False, False)


# deklarasi Fungsi command untuk membuka file mp4
def open_file_mp4():
    global isi_mp4
    global entry_file_mp4
    openfile = filedialog.askopenfilename(
        initialdir="C:/Users/RADEARSR/Videos",
        title='Open File',
        filetypes=(('MP4', '*.*'), ('All Files', '*.*'))
        )
    entry_file_mp4.insert(0, openfile)
    isi_mp4 = entry_file_mp4.get()

# deklarasi Fungsi command untuk menempatkan hasil convert mp4 -> mp3
def open_dir_mp3():
    global isi_mp3
    global entry_file_mp3
    opendir = filedialog.askdirectory(initialdir = "C:/Users/RADEARSR/Music")
    entry_file_mp3.insert(0, opendir)
    isi_mp3 = entry_file_mp3.get()


# deklarasi Fungsi command untuk menamai nama file hasil convert mp4 -> mp3
def convert():
    global isi_mp4
    global isi_mp3
    isi_mp3 = entry_file_mp3.get()
    isi_mp4 = entry_file_mp4.get()
    file_name = entry_name_file.get()
    if isi_mp3 != '' and isi_mp4 != '' and file_name != '':
        name_mp3 = isi_mp3 + "/" + file_name + ".mp3"
        video_clip = VideoFileClip(isi_mp4)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(name_mp3)
        msg.showinfo(title= "Konfirmasi", message="Convert Suscess")
    else:
        msg.showwarning(title="Error", message="Isi semua kolom yang ada")

# deklarasi Change Theme
def theme():
    global entry_file_mp3
    global entry_file_mp4
    global entry_name_file
    global label_open_file_mp4
    global label_open_dir_mp3
    global label_enter_name
    
    color = ["#56C4C5", "#6C6C6C", "#FF9935"]
    random_color = random.randint(0, 2)
    theme = color[random_color]
    print(theme)
    if random_color == 0:
        root.configure(bg = theme)
        # deklarasi button untuk default Theme
        button_open_file_mp4 = Button(
            # root,
            # command = open_file_mp4,
            # image = ico_file_mp4,
            # padx = 30,
            # pady = 7,
            # border = 0,
            bg = theme,
            activebackground = theme
            )
            
        button_open_dir_mp3 = Button(
            root,
            command = open_dir_mp3,
            image = ico_file_mp3,
            padx = 30,
            pady = 7,
            border = 0,
            bg = theme,
            activebackground = theme
            )

        button_convert = Button(
            root,
            command = convert,
            image = ico_convert,
            padx = 255,
            pady = 7,
            border = 0,
            bg = theme,
            activebackground = theme
            )
        # deklarasi Varibel Entry default Theme
        color_entry = "#006E6F"
        font_color = "#FFFFFF"
        entry_file_mp4 = Entry(
            root,
            width = 54,
            borderwidth = 3,
            bg = color_entry,
            fg = font_color,
            font=("Times", "12", "bold")
            )
        entry_file_mp3 = Entry(
            root,
            width = 54,
            borderwidth = 3,
            bg = color_entry,
            fg = font_color,
            font = ("Times", "12", "bold")
            )
        entry_name_file = Entry(
            root,
            width = 68,
            borderwidth = 3,
            bg = color_entry,
            fg = font_color,
            font = ("Times", "12", "bold")
            )
        # deklarasi Variabel Label Theme Mode 2
        bg_label = "#d5bb3a"
        label_open_file_mp4 = Label(
            root,
            text = "Select File Mp4:",
            bg = bg_label,
            font = ("Times", "12", "bold")
            )
        label_open_dir_mp3 = Label(
            root,
            text = "Destination       :",
            bg = bg_label,
            font = ("Times", "12", "bold")
            )
        label_enter_name = Label(
            root,
            text = "Name Mp3       :",
            bg = bg_label,
            font = ("Times", "12", "bold")
            )

    elif random_color == 1:
        root.configure(bg = theme)
        # deklarasi button untuk Theme Mode 1
        button_open_file_mp4 = Button(
            root,
            command = open_file_mp4,
            image = ico_file_mp4,
            padx = 30,
            pady = 7,
            border = 0,
            bg = theme,
            activebackground = theme
            )
            
        button_open_dir_mp3 = Button(
            root,
            command = open_dir_mp3,
            image = ico_file_mp3,
            padx = 30,
            pady = 7,
            border = 0,
            bg = theme,
            activebackground = theme
            )

        button_convert = Button(
            root,
            command = convert,
            image = ico_convert,
            padx = 255,
            pady = 7,
            border = 0,
            bg = theme,
            activebackground = theme
            )
        # deklarasi Variabel Entry Theme Mode 1
        color_entry = "#121212"
        font_color = "#FFFFFF"
        entry_file_mp4 = Entry(
            root,
            width = 54,
            borderwidth = 3,
            bg = color_entry,
            fg = font_color,
            font = ("Times", "12", "bold")
            )
        entry_file_mp3 = Entry(
            root,
            width = 54,
            borderwidth = 3,
            bg = color_entry,
            fg = font_color,
            font = ("Times", "12", "bold")
            )
        entry_name_file = Entry(
            root,
            width = 68,
            borderwidth = 3,
            bg = color_entry,
            fg = font_color,
            font = ("Times", "12", "bold")
            )

    elif random_color == 2:
        root.configure(bg = theme)
        # deklarasi button untuk Theme Mode 2
        button_open_file_mp4 = Button(
            root,
            command = open_file_mp4,
            image = ico_file_mp4,
            padx = 30,
            pady = 7,
            border = 0,
            bg = theme,
            activebackground = theme
            )
            
        button_open_dir_mp3 = Button(
            root,
            command = open_dir_mp3,
            image = ico_file_mp3,
            padx = 30,
            pady = 7,
            border = 0,
            bg = theme,
            activebackground = theme
            )

        button_convert = Button(
            root,
            command = convert,
            image = ico_convert,
            padx = 255,
            pady = 7,
            border = 0,
            bg = theme,
            activebackground = theme
            )
        # deklarasi Variabel Entry Theme Mode 2
        color_entry = "#FE3813"
        font_color = "#FFFFFF"
        entry_file_mp4 = Entry(
            root,
            width = 54,
            borderwidth = 3,
            bg = color_entry,
            fg = font_color,
            font = ("Times", "12", "bold")
            )
        entry_file_mp3 = Entry(
            root,
            width = 54,
            borderwidth = 3,
            bg = color_entry,
            fg = font_color,
            font = ("Times", "12", "bold")
            )
        entry_name_file = Entry(
            root,
            width = 68,
            borderwidth = 3,
            bg = color_entry,
            fg = font_color,
            font = ("Times", "12", "bold")
            )
        # deklarasi Variabel Label Theme Mode 2
        bg_label = "#93CADE"
        label_open_file_mp4 = Label(
            root,
            text = "Select File Mp4:",
            bg = bg_label,
            font = ("Times", "12", "bold")
            )
        label_open_dir_mp3 = Label(
            root,
            text = "Destination       :",
            bg = bg_label,
            font = ("Times", "12", "bold")
            )
        label_enter_name = Label(
            root,
            text = "Name Mp3       :",
            bg = bg_label,
            font = ("Times", "12", "bold")
            )

    # Theme Button Position
    button_open_file_mp4.place(x = 565 , y = 10)
    button_open_dir_mp3.place(x = 565, y = 57)
    button_convert.place(x = 180, y = 180)

    # Theme Entry Position
    entry_file_mp4.place(x = 120, y = 20)
    entry_file_mp3.place(x = 120, y = 65)
    entry_name_file.place(x = 120, y = 110)

    # Label Position
    # label_open_file_mp4.place(x = 0, y = 20)
    # label_open_dir_mp3.place(x = 0, y = 65)
    # label_enter_name.place(x = 0,  y = 110)

# deklarasi icon untuk Button
ico_file_mp4 = PhotoImage(file = "browse1.png")
ico_file_mp3 = PhotoImage(file = "browse2.png")
ico_convert = PhotoImage(file = "convert.png")
ico_theme = PhotoImage(file = "change.png")
ico_quit = PhotoImage(file = "exit.png") 

# deklarasi background button dan activebackground
color_theme = str("#6C6C6C")

# deklarasi Variabel Button
button_open_file_mp4 = Button(
    root,
    command = open_file_mp4,
    image = ico_file_mp4,
    padx = 30,
    pady = 7,
    border = 0,
    bg = color_theme,
    activebackground = color_theme
    )
    
button_open_dir_mp3 = Button(
    root,
    command = open_dir_mp3,
    image = ico_file_mp3,
    padx = 30,
    pady = 7,
    border = 0,
    bg = color_theme,
    activebackground = color_theme
    )

button_convert = Button(
    root,
    command = convert,
    image = ico_convert,
    padx = 255,
    pady = 7,
    border = 0,
    bg = color_theme,
    activebackground = color_theme
    )

button_quit = Button(
    root,
    command=quit,
    image=ico_quit,
    padx=30,
    pady=8,
    border=0,
    bg="#cd0d0d",
    activebackground="#cd0d0d"
    )

button_theme=Button(
    root,
    command=theme,
    image=ico_theme,
    padx=30,
    pady=8,
    border=0,
    bg="#9ce224",
    activebackground="#9ce224"
    )

# deklarasi Variabel Label
bg_label = "#d5bb3a"
label_open_file_mp4 = Label(
    root,
    text = "Select File Mp4:",
    bg = bg_label,
    font = ("Times", "12", "bold")
    )
label_open_dir_mp3 = Label(
    root,
    text = "Destination       :",
    bg = bg_label,
    font = ("Times", "12", "bold")
    )
label_enter_name = Label(
    root,
    text = "Name Mp3       :",
    bg = bg_label,
    font = ("Times", "12", "bold")
    )

# deklarasi Variabel Entry
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
    width = 54,
    borderwidth = 3,
    bg = color_entry,
    fg = font_color,
    font = ("Times", "12", "bold")
    )
entry_name_file = Entry(
    root,
    width = 68,
    borderwidth = 3,
    bg = color_entry,
    fg = font_color,
    font = ("Times", "12", "bold")
    )


# Button Position
button_open_file_mp4.place(x = 565 , y = 10)
button_open_dir_mp3.place(x = 565, y = 57)
button_convert.place(x = 180, y = 180)
button_quit.place(x = 554 , y = 257)
button_theme.place(x  = 5, y = 257)


# Entry Position
entry_file_mp4.place(x = 120, y = 20)
entry_file_mp3.place(x = 120, y = 65)
entry_name_file.place(x = 120, y = 110)

# Label Position
label_open_file_mp4.place(x = 0, y = 20)
label_open_dir_mp3.place(x = 0, y = 65)
label_enter_name.place(x = 0,  y = 110)

root.mainloop()