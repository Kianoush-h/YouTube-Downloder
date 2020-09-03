
"""
@author: Kianoush 

GitHUb:https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA?view_as=subscriber
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""




import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox 
from tkinter.ttk import Progressbar

import platform
import sys
import time

from datetime import datetime
from time import sleep 
import warnings

from pytube import YouTube
# import os

from tkinter import filedialog


def stop():
    global flgg
    flgg = 0
    # print(flgg)
    
def lol():
    # global flgg
    if flgg != 1:
        text_status = "Stoped"
        statusbar.config(text=text_status) 
        statusbar.update() 
        
        
        return(False)
    
    
    

def submit():
    dt_string = '1'
     
 
    # Progress bar widget 
    progress = Progressbar(window,length = 400, mode = 'determinate') 
    
    
    Sort_print = Sorting_choose.get()
    
    #satus Bar
    text_status = "Status: Please wait ..."
    statusbar.config(text=text_status) 
    statusbar.update()
    
    Intruc.config(text="") 
     # Send to Function

    if "Enter" in URL_string.get():
        URL_string.set("https://www.youtube.com/watch?v=qyHyFsT7Hig")
  
    dt_string = you_tube(statusbar,URL_string.get())
    
    window.title('YouTube Downloader') 
    
    

    
    if dt_string == '0':
        messagebox.showinfo("Status => Done ", "Video is Downloaded.") 
    else:
        messagebox.showwarning("Error ... ", "Check your connection ...") 
   
    status(statusbar,"Status: Ready >> Enter the URL in the text box")





def status(st,tx):
    st.config(text = tx) 
    st.update()


#Grabs the file path for Download
def file_path():
    # home = os.path.expanduser('~')
    # download_path = os.path.join(home, 'Downloads')
    download_path = filedialog.askdirectory()

    return download_path
 
    
 
    
def you_tube(st,link):
    path = file_path()
    status(st,"Your video will be saved to: {}".format(path))
    time.sleep(2)
 
    status(st,"Accessing YouTube URL ...")
    time.sleep(1)
    # Searches for the video and sets up the callback to run the progress indicator. 
    try:
        video = YouTube(link)
    except:
        status(st,"ERROR ... Check your connection")        
        time.sleep(1)
        return '1'
        # redo = you_tube(st,link)
 
    #Get the first video type - usually the best quality.
    video_type = video.streams.filter(progressive = True, file_extension = "mp4").first()
 
    #Gets the title of the video
    title = video.title
    video_title_string.set(title)
    # #Prepares the file for download
    # status(st,"Fetching: {}...".format(title))
    # time.sleep(1)
    
    file_size = video_type.filesize
    #Starts the download process
    video_type.download(path)
    return "0"
 
 





# Creating tkinter window 
window = tk.Tk() 
window.resizable(False, False)
window.title('YouTube Downloader') 
window.geometry('500x300') 
  
# label text for title 
y0=0
x0=0

# tk.Label(window, text = "This app helps you to download any YouTube video",  
#           font = ("Times New Roman", 25)).place(x = x0, y = y0) 

Ins_text= "Instruction: To have a better result, copy and paste the URL of the video"
Intruc = tk.Label(window, text = Ins_text,
         fg="red", font = ("Times New Roman", 12))

Intruc.place(x = 0, y = 15) 

tk.Label(window, text = "By Kianoush H., Ver 1.1",  
          fg="gray",font = ("Times New Roman", 10)).place(x = 360, y = 260) 
                         

                                 
text_status = "Status: Ready >> Enter the URL in the text box"
statusbar = tk.Label(window, text =text_status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)
                                                          


Sorting_lable = tk.Label(window, text = "Select The Format :",   
                        font = ("Times New Roman", 10)).place(x = 5, y = 130) 


  
# Combobox creation 
n = tk.StringVar() 
Sorting_choose = ttk.Combobox(window, width = 21, textvariable = n) 
  
# Adding combobox drop down list 
Sorting_choose['values'] = ('MP4',  
                          'MP3')

Sorting_choose.place(x = 130, y = 130) 
Sorting_choose.current(0) 


URL_string_label = tk.Label(window, width = 12,
                   text = 'Video URL :', 
                   font = ('Times New Roman',10,'normal')).place(x = 0, 
                                           y = 90) 

# Inisitalization and insering initial values
URL_string = tk.StringVar() 
URL_string.set('Enter your URL here ...')


   
# creating a entry for year to 
URL_string_entry = tk.Entry(window, width =65,
                     textvariable = str(URL_string), 
                     font = ('Times New Roman',10,'normal')).place(x = 90, 
                                           y = 93)                   
                                        
                                                                   
video_title_ = tk.Label(window, width = 12,
                    text = 'Video Title :', 
                    font = ('Times New Roman',10,'normal')).place(x = 0, y = 180) 

video_title_string = tk.StringVar() 
video_title_string.set('###########################')

video_title = tk.Entry(window, width = 60,state='disabled',
                     textvariable = str(video_title_string), fg="blue",
                     font = ('Times New Roman',10,'normal')).place(x = 85, y = 180)   
        
        

sub_btn=tk.Button(window,text = 'Search', command =  submit,width = 20) 
sub_btn.place(x = 200, y = 230) 



can_btn = tk.Button(window, text="Stop", command=stop, width = 20)
can_btn.place(x = 50, y = 230) 








window.mainloop() 











