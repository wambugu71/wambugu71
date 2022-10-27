"""MUSIC PLAYER PROJECT @ken
"""
from tkinter import *
from tkinter import Tk
from tkinter import ttk, filedialog
from pygame import mixer
from pygame import *
import os
from tkinter import messagebox


root=Tk()
root.title('MUSIC PLAYER PROJECT @ken')
root.geometry("800x700")
root.configure(bg= "grey")
root.resizable(True, True)
my_label=Label(root, text="MUSIC PLAYER MADE BY\n @KEN",font=("Copperplate Gothic Bold", 12, 'bold')).pack()

mixer.init()

def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
            elif song.endswith(".flac"):
                Playlist.insert(END, song)
            else:
                pass
def Play_Music():
    Music_Name= Playlist.get(ACTIVE)
   # print(Music_Name[0:-4])
    Label(root, text=Music_Name[0:-4], height=10, width=60, font=("Bernard MT Condensed", 12, "bold")).place(x=500, y=50)
    mixer.music.load(Music_Name)
    mixer.music.play()


def new_func():
    return mixer.music.rewind(Playlist.get(ACTIVE))


def volumedown():
    mixer.music.set_volume(0.5)


def volumeup():
    mixer.music.set_volume(1)

def destroy():
    shut = messagebox.askquestion( "QUIT","Quit the player?")
    if shut == "yes":
        exit()
    else:
        root.mainloop()
#next music
def Next():
    next_one= Playlist.curselection()
    next_one=next_one[0]+1
    #to get the selected song index
   # next_one=songs_list.curselection()
    #to get the next song index

    #to get the next song
    music_Name= Playlist.get(next_one)
    mixer.music.load(music_Name)
    mixer.music.play()
    Playlist.selection_clear(0,END)
    #activate newsong
    Playlist.activate(next_one)
     #set the next song
    Playlist.selection_set(next_one)

#Previous music
def Prev():
    next_one= Playlist.curselection()
    next_one=next_one[0]-1
    #to get the selected song index
   # next_one=songs_list.curselection()
    #to get the next song index

    #to get the next song
    music_Name= Playlist.get(next_one)
    mixer.music.load(music_Name)
    mixer.music.play()
    Playlist.selection_clear(0,END)
    #activate newsong
    Playlist.activate(next_one)
     #set the next song
    Playlist.selection_set(next_one)

#icon
#root.iconphoto(False,image_icon)

#Top = PhotoImage(file="top1.png")
#Label(root, image=Top, bg="#0f1a2b").pack()

#logo
#logo = PhotoImage(file="logo1.png")
#def songinfo():
#Music_Name= song.get(ACTIVE)
#Label(root,text=music_Name[0:-4],height=90, width=60).place(x=500, y=50)


#Label(root, text=songinfo, bg="grey").place(x=500, y=30)
# Button
#rewind_button=Button(root, text="rewind", command=rewindsong, font=("times new roman",12,"bold"), height=4, width=10)
#rewind_button.place(x=700, y=5)
play_=Button(root, text="play", command=Play_Music, bg="white", fg="black", font=("times new roman",12,"bold"), height=2, width=7)
play_.place(y=500, x=10)
stop=Button(root, text="stop", command=mixer.music.stop, font=("times new roman",12,"bold"), height=2, width=7)
stop.place(x=200, y=500)
pause=Button(root, text="pause", command=mixer.music.pause, font=("times new roman",12,"bold"),  height=2, width=7)
pause.place(x=100, y=500)
unpause=Button(root, text="Unpause", font=("times new roman",12,"bold"), command=mixer.music.unpause, height=2, width=7)
unpause.place(x=300, y=500)
Next_ =Button(root, text="Next", command=Next, height=2, width=7,font=("times new roman",12,"bold") ).place(x=400, y=500)
Prev_=Button(root, text="Prev", command=Prev,height=2, width=7,font=("times new roman",12,"bold") ).place(x=500, y=500)
#ken_volup=Button(root, text="vol up", command=volumeup, height=2, width=7, font=("times new roman", 12, "bold"))
#ken_volup.grid(row=1,column=4)
#ken_voldown=Button(root, text="vol down", command=volumedown, height=2, width=7, font=("times new roman", 12, "bold"))
#ken_voldown.grid(row=1,column=5)
#ken_quit=Button(root, text="quit", command=destroy, width=7, height=2, font=("times new roman", 12, "bold") )
#ken_quit.place(x=600, y=5)
#sken_rewind=Button(root, text="Rewind", command=new_func).pack()
#ke=Label(root, text="player @ken", font=("times new roman", 12, "bold"), width)

#Button_Play = PhotoImage(file="play1.png")
#ken=Button(root, image=Button_Play, bd=0, bg="lightblue", command=Play_Music, height=120, width=180).place(x=550, y=130)

#Button_Stop = PhotoImage(file="stop1.png")
#Button(root, image=Button_Stop, bg="#0f1a2b", bd=0, command=mixer.music.stop,  height=120, width=180).place(x=550, y=250)

#Button_Resume = PhotoImage(file="resume1.png")
#Button(root, image=Button_Resume, bg="#0f1a2b", bd=0, command=mixer.music.unpause,  height=120, width=180).place(x=550, y=300)

#Button_Pause = PhotoImage(file="pause1.png")
#Button(root, image=Button_Pause, bg="#0f1a2b", bd=0, command=mixer.music.pause,  height=120, width=180).place(x=550, y=380)
#music
#Menu = PhotoImage(file="menu1.png")
#Label(root, text="white", bg="white").pack(padx=10, pady=80, side=RIGHT)


#Adding the menu to my music player
my_menu=Menu(root, font=("times new roman", 12, "bold"))
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=Add_Music)
add_song_menu.add_command(label="Quit",command=destroy)
add_Music_menu.add_command(label="About", command=About)

Frame_Music = Frame(root, bd=2, relief = RIDGE)
Frame_Music.place(x=60, y=100, width=400, height=350)

#Button(root, text="Add Music", width=15, height=2, font=("times new roman",12,"bold"),fg="Black", bg="#21b3de", command= Add_Music).place(x=30, y=100)
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman",10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()