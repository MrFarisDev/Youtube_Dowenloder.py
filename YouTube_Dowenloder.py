from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube
import pytube





def Dowenlod():

    url = text.get()

    youtube_video = YouTube(url)

    option = selected_option.get()

    if option == 1:
        
        quality = "1080p"
        
        video = youtube_video.streams.filter(res=quality).first()
        
        video.download()

        messagebox.showinfo("Alert" , "Video download complete !")

        print("1080p")


    elif option == 2:

        quality = "720p"
        
        video = youtube_video.streams.filter(res=quality).first()
        
        video.download()

        messagebox.showinfo("Alert" , "Video download complete !")

        print("720p")


    elif option == 3:

        quality = "480p"
        
        video = youtube_video.streams.filter(res=quality).first()
        
        video.download()

        messagebox.showinfo("Alert" , "Video download complete !")
        
        print("480p")


    elif option == 4:

        quality = "144p"
        
        video = youtube_video.streams.filter(res=quality).first()
        
        video.download()

        messagebox.showinfo("Alert" , "Video download complete !")

        print("144p")


    elif option == 5:
        
        video = youtube_video.streams.filter(only_audio=True).first()
        
        video.download()

        messagebox.showinfo("Alert" , "Sound download complete !")

        print("Sound")


    else:
        messagebox.showerror("Error" , "The url not True")
        

tk = Tk()


tk.title("YouTube Dowenloder")

tk.geometry("400x460")

tk.maxsize(400 , 460)
tk.minsize(380 , 440)

tk.config(background="#332e2f")

fr = Frame(tk , bg="#332e2f")
fr.pack(expand=YES)


label = Label(fr , text="YouTube Dowenloder" , font=("Tahoma" , 20 ) , background="#332e2f" , border=5)
label.pack(pady=5)


text = Entry(fr , font=("Arial" , 16) , relief="sunken" , border=5)
text.pack(pady=10)



selected_option = IntVar()


option1 = ttk.Radiobutton(fr , text="1080p" , variable=selected_option , value=1 )
option1.pack(pady=10 , padx=5)


option2 = ttk.Radiobutton(fr , text="720p" , variable=selected_option , value=2)
option2.pack(pady=10 , padx= 5)


option3 = ttk.Radiobutton(fr , text="480p" , variable=selected_option , value=3)
option3.pack(pady=10 , padx= 5)


option4 = ttk.Radiobutton(fr , text="144p" , variable=selected_option , value=4)
option4.pack(pady=10 , padx= 5)


optionSound = ttk.Radiobutton(fr , text="Sound" , variable=selected_option , value=5)
optionSound.pack(pady=10 , padx= 5)



button = Button(tk , text="Enter" , font=("Tahoma" , 15) , foreground="Black" , background="#7c0315" , command=Dowenlod)
button.pack(pady=10)




tk.mainloop()