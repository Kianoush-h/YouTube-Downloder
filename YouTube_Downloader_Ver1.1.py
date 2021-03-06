
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


default_link = 'https://www.youtube.com/watch?v=tu4RHUPK1Mg&t=7s'


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
        URL_string.set(default_link)
  
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
    
    try:
        video_type = video.streams.filter(subtype='mp4', progressive=True, res=Sorting_quality.get())[0]
        name = video.title + '_' + Sorting_quality.get()
    except:
        video_type = video.streams.filter(progressive = True, file_extension = "mp4").first()
        messagebox.showinfo("Warning", 'The prefered quality is not available')
        name = video.title

 
    #Gets the title of the video
    title = video.title
    video_title_string.set(title)
    
    
    if sb_1.get():
        try:
            a = video.captions['en']
            a.download(title= title + '_sub',output_path=path)
        except:
            messagebox.showinfo("Warning", 'The prefered subtitle is not available')
            
    
    file_size = video_type.filesize
    #Starts the download process
    video_type.download(output_path= path, filename=name)
    return "0"
 
 



def description():
    
    if "Enter" in URL_string.get():
        URL_string.set(default_link)
        
    status(statusbar,"Accessing YouTube URL ... Description")
    time.sleep(1)
    
    try:
        video = YouTube(URL_string.get())
    except:
        status(statusbar,"ERROR ... Check your connection")        
        time.sleep(1)
        return '1'
        
        
    title = video.title
    video_title_string.set(title)
    
    des = video.description
    des = des.encode('utf-8')
    
    messagebox.showinfo("Video Description", des)
    






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
          fg="gray",font = ("Times New Roman", 10)).place(x = x0+360,
                                                          y = y0+260) 
                         

                                 
text_status = "Status: Ready >> Enter the URL in the text box"
statusbar = tk.Label(window, text =text_status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)
                                                          


Sorting_lable = tk.Label(window, text = "Select the Format :",   
                        font = ("Times New Roman", 10)).place(x = x0+5,
                                                              y = y0+100) 


  
# Combobox creation 
n = tk.StringVar() 
Sorting_choose = ttk.Combobox(window, width = 7, textvariable = n) 
  
# Adding combobox drop down list 
Sorting_choose['values'] = ('MP4','MP3')
Sorting_choose.place(x = x0+130, y = y0+100) 
Sorting_choose.current(0) 





quality_label = tk.Label(window, text = "Select the Quality :",   
                        font = ("Times New Roman", 10)).place(x = x0+230,
                                                              y = y0+100) 
                                                              
m = tk.StringVar() 
Sorting_quality = ttk.Combobox(window, width = 7, textvariable = m) 
  
# Adding combobox drop down list 
Sorting_quality['values'] = ('720p', '480p','360p')
Sorting_quality.place(x = x0+350, y = y0+100) 
Sorting_quality.current(0) 






URL_string_label = tk.Label(window, width = 12,
                   text = 'Video URL :', 
                   font = ('Times New Roman',10,'normal')).place(x = x0+0,
                                                                 y = y0+50) 

# Inisitalization and insering initial values
URL_string = tk.StringVar() 
URL_string.set('Enter your URL here ...')


   
# creating a entry for year to 
URL_string_entry = tk.Entry(window, width =65,
                     textvariable = str(URL_string), 
                     font = ('Times New Roman',10,'normal')).place(x = x0+90, 
                                           y = y0+53)                   
             
                                                                   
                                                                   
                                                                   
                                                                   
video_title_ = tk.Label(window, width = 12,
                    text = 'Video Title :', 
                    font = ('Times New Roman',10,'normal')).place(x = x0+0,
                                                                  y = y0+185) 

video_title_string = tk.StringVar() 
video_title_string.set('###########################')

video_title = tk.Entry(window, width = 40 ,state='disabled',
                     textvariable = str(video_title_string), fg="blue",
                     font = ('Times New Roman',9,'normal')).place(x = x0+85,
                                                                   y = y0+185)   
   
                                                                  
   
                                                                   
Sub_label = tk.Label(window, 
                    text = 'Subtitle :', 
                    font = ('Times New Roman',10,'normal')).place(x = x0+5,
                                                                  y = y0+140) 
                                                                  
sb_1 = tk.IntVar()      
sb_1.set(0)
subtitle_btn1 = tk.Checkbutton(window, text = "English", variable=sb_1, onvalue=1, offvalue=0)                                                         
subtitle_btn1.place(x = x0+80, y = y0+140)                                                       
                                                                  
sb_2 = tk.IntVar()                                                                     
sb_2.set(0)
subtitle_btn2 = tk.Checkbutton(window, text = "Russia", variable=sb_2, onvalue=1, offvalue=0)                                                         
subtitle_btn2.place(x = x0+170, y = y0+140)   
                                                        
                             
                                                        
                             
                                
des_btn=tk.Button(window,text = 'Description', command =  description,width = 10) 
des_btn.place(x = x0+380, y = y0+180) 
                                                                  
        

sub_btn=tk.Button(window,text = 'Search', command =  submit,width = 20) 
sub_btn.place(x = x0+200, y = y0+230) 



can_btn = tk.Button(window, text="Stop", command=stop, width = 20)
can_btn.place(x = x0+50, y = y0+230) 








window.mainloop() 











