import os
import pygame
from mutagen.easyid3 import EasyID3
from tkinter.filedialog import *
from tkinter import *
import tkinter.messagebox as tmsg



pygame.mixer.init()


class MP3_Player(Tk):

    listofsongs =[]
    index = 0
    temp = 1
    firstdir = True

    def __init__(self):
        super().__init__()

        self.geometry("900x650")
        # self.resizable(0,0)
        self.minsize(900,650)
        self.title("MP3 MUSIC PLAYER")
        self.iconbitmap("Tk_mp3_Player_icon.py.ico")

        self.label = Label(self, text="RSP - MP3 MUSIC PLAYER", font="arial 15 bold", bg="skyblue", fg="red")
        self.label.pack(pady= 5, fill=X)

        self.current_song_label = Label(self, fg='Black', font="Helvetica 12 bold", borderwidth = 5, relief=SUNKEN)
        self.current_song_label.pack(pady=15, fill = X, padx=10)

        self.listbox = Listbox(self, width=100, height=23)
        self.listbox.pack()

        self.frame = Frame(self)
        self.frame.pack(side = BOTTOM, pady=10)

        self.prevbutton = Button(self.frame, text="Prevous Song", font="arial 15 bold", bg="silver",fg="blue", command=self.Prev_Button)
        self.prevbutton.pack(side=LEFT, padx=20, pady=50)

        self.playbutton = Button(self.frame, text="Play", font="arial 15 bold", bg="silver",fg="blue", command=self.Play_Button)
        self.playbutton.pack(side=LEFT, padx=20, pady=50)

        self.nextbutton = Button(self.frame, text="Next Song", font="arial 15 bold", bg="silver",fg="blue", command=self.Next_Button)
        self.nextbutton.pack(side=LEFT, padx=20, pady=50)

        self.pause_unpausebutton = Button(self.frame, text="Pause/Unpause", font="arial 15 bold", bg="silver",fg="blue", command=self.Pause_Unpause_Button)
        self.pause_unpausebutton.pack(side=LEFT, padx=20, pady=50)

        self.frame1 = Frame(self.frame)
        self.frame1.pack(pady=10)

        self.volume = Scale(self.frame1, from_ = 0, to = 100, bg="silver", length=150, orient=HORIZONTAL, command=self.Volume_fun)
        self.volume.set(25)
        self.volume.pack()

        self.label = Label(self.frame1, text="Volume", font="arial 10 ", bg="skyblue", fg="red")
        self.label.pack()

        
    def Volume_fun(self, vol):
        self.New_Volume = int(vol)/100
        pygame.mixer.music.set_volume(self.New_Volume)

    def Prev_Button(self):
        if(MP3_Player.index==-(len(MP3_Player.listofsongs)-1)):
            MP3_Player.index=0
        else:
            MP3_Player.index-=1
        self.Play_Button()
    
    def Play_Button(self):
        pygame.mixer.music.load(MP3_Player.listofsongs[MP3_Player.index])
        pygame.mixer.music.play()
        self.current_song_label['text'] = self.Current_Song()
    
    def Next_Button(self):
        if(MP3_Player.index==(len(MP3_Player.listofsongs)-1)):
            MP3_Player.index=0
        else:
            MP3_Player.index+=1
        self.Play_Button()
    
    def Pause_Unpause_Button(self):
        if(MP3_Player.temp%2==0):
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        MP3_Player.temp+=1
    
    def my_music(self):
        os.chdir(self.First_directory)
        self.DirectoryChooser()
    
    def open_file(self):
        directory = askdirectory()
        os.chdir(directory)
        self.DirectoryChooser()
    
    def save_as_playlist(self):
        tmsg.showinfo("Add to...", "The given command is empty.")
    
    def settings(self):
        tmsg.showinfo("Settings", "The GUI Settings appear here. GUI settings are in development phase.")
    
    def welcome_fun(self):
        tmsg.showinfo("Welcome", 
        '''        Welcome to RSP - MP3 Music Player.
        Here You Can Enjoy Your Favorite Sogs.
        Thank You For Choosing us.''')
    
    def rate_us_fun(self):
        que = tmsg.askquestion("Rate us", "You used this GUI.. Was your experience Good?")
        if que == "yes":
            msg = "Great. Thank you for your valuable response."
        else:
            msg = "Sorry for your inconvenience. You can tell us what went wrong. We will call you soon."
        tmsg.showinfo("Experience", msg)
    
    def about_fun(self):
        tmsg.showinfo("About",
        '''        Version: 1.1.1 (user setup)
        Commit: -------------------
        Date: 2021-1-16 T 06:32:46
        OS: Windows_NT x64 10.0.19042
        ..
        .''')

    def Current_Song(self):

        self.temp_index = MP3_Player.index
        if (self.temp_index<0):
            self.temp_index = len(MP3_Player.listofsongs) + self.temp_index
        
        self.song = EasyID3(MP3_Player.listofsongs[MP3_Player.index])
        self.song_data = "  Now playing: Nr: " + str(self.temp_index + 1) + "  " + str(self.song['title']) + "  -  " + str(self.song['artist'])
        return self.song_data


    def Menubar(self):
        
        mainmenu = Menu(self)

        m1 = Menu(mainmenu, tearoff=0)
        m1.add_command(label="My Music", command=self.my_music)
        m1.add_command(label="Open File...", command=self.open_file)
        m1.add_command(label="Save As a Playlist...", command=self.save_as_playlist)
        m1.add_separator()
        m1.add_command(label="Settings", command=self.settings)
        m1.add_separator()
        m1.add_command(label="Exit", command=quit)
        self.config(menu=mainmenu)
        mainmenu.add_cascade(label="File", menu=m1)

        m2 = Menu(mainmenu, tearoff=0)
        m2.add_command(label="Welcome", command=self.welcome_fun)
        m2.add_command(label="Rate us", command=self.rate_us_fun)
        m2.add_separator()
        m2.add_command(label="About", command=self.about_fun)
        self.config(menu=mainmenu)
        mainmenu.add_cascade(label="Help", menu=m2)

    def DirectoryChooser(self):
        MP3_Player.listofsongs.clear()
        MP3_Player.index = 0
        self.listbox.delete(0, END)
        self.listbox.insert(END, "                                                                                   NOW PLAYING LIST")
        self.listbox.insert(END, " ")
        pygame.mixer.music.stop()
        try:
            for files in os.listdir():
                if files.endswith(".mp3"):
                    MP3_Player.listofsongs.append(files)
            # print("Firest for loop")
            if len(MP3_Player.listofsongs)==0:
                print(9+"9")
            # print("Firest if statement")

            for self.key, self.item in enumerate(MP3_Player.listofsongs):
                self.song = EasyID3(self.item)
                self.song_data = (" " + str(self.key + 1) + '  :  ' + self.song['title'][0] + '  -  '+ self.song['artist'][0])
                self.listbox.insert(END, self.song_data)
                # print("Inside second for loop")
            # print("Second for loop")

            if MP3_Player.firstdir == True:
                self.First_directory = os.getcwd()
                MP3_Player.firstdir = False
            # print("Second if statement")

            self.current_song_label['text'] = self.Current_Song()
            # print("song label")

        except TypeError:
            tmsg.showinfo("Message", "Current directory has no songs. Please Select the files or folder where list of songs are present.")
            directory = askdirectory()
            os.chdir(directory)
            self.DirectoryChooser()








if __name__ == "__main__":

    window = MP3_Player()
    window.Menubar()
    window.DirectoryChooser()
    window.mainloop()



