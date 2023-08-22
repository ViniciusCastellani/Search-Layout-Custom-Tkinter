import customtkinter
from tkinter import *
from tkinter import font
import json
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.geometry("800x600")
window.title("Search Data")
window.resizable(False, False) #not manipulate the window

#FONTS
font= customtkinter.CTkFont(family="Consolas", size=20, weight="bold", slant="roman") 
fontwo= customtkinter.CTkFont(family="Consolas", size=25, weight="bold", slant="roman")   
font2= customtkinter.CTkFont(family="Ivy", size=12, weight="bold", slant="roman")
font3= customtkinter.CTkFont(family="Bodoni", size=9, weight="bold", slant="roman")     
font4= customtkinter.CTkFont(family="Times", size=25, weight="bold", slant="italic") 


#STRING VARS / STORE THE ENTRYS
cpf_var = customtkinter.StringVar()

#FRAME 1
frame = customtkinter.CTkFrame(master=window, width=700, height=550)
frame.pack()

#FRAME WD 
label = customtkinter.CTkLabel(master=frame, text="Search account", font = font)
label.place(x=265, y=40)


#CPF LABEL ENTRY
labelCpf = customtkinter.CTkLabel(master=frame, text="CPF", font = font2)
labelCpf.place(x=30, y=100)
Firstentry = customtkinter.CTkEntry(master=frame, width=300, textvariable=cpf_var)
Firstentry.place(x=30, y=130)


###BUTTON
button = customtkinter.CTkButton(master=frame, text="SEARCH", font=font2, width=130).place(x=370, y= 130)
button2 = customtkinter.CTkButton(master = frame, text = "SEARCH ALL", font = font2, width= 130).place(x =530, y = 130 )

###DATA LAYOUT

canvas = customtkinter.CTkCanvas(master=frame, width=780, height=430)
canvas.place(x=40, y=230)

canvas_scrollbar = customtkinter.CTkScrollbar(master=frame, command=canvas.yview, height=355)
canvas_scrollbar.place(x=660, y=180)
canvas.configure(yscrollcommand=canvas_scrollbar.set)

###INFOS

label2 = customtkinter.CTkLabel(master=window, text="Mugiwara's corp.", font=font4)
label2.place(x=10, y=560)

label3 = customtkinter.CTkLabel(master=window, text="All Rights reserved ©", font = font3)
label3.place(x=210, y=565)


#FAJ LOGO
# logo = PhotoImage(file="images/faj (1).png")
# logo = logo.subsample(5,5)
# logoLabel = Label(image=logo, bg= "#141414")

#MUGI
#MugiLogo = PhotoImage(file="images/mugi.png")
#MugiLogo = MugiLogo.subsample(3,3)
#MugiLogoLabel= Label(image=MugiLogo, bg="#141414")


#MugiLogoLabel.place(x=55, y=140)
#logoLabel.place(x=20, y=10)

window.mainloop()