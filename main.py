import tkinter
from tkinter import *
import tkinter as tk
import customtkinter
from tkinter import ttk

import pywinstyles
from PIL import Image, ImageTk
import random

from customtkinter import CTkScrollableFrame
from pywinstyles import set_opacity

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

w = 1920
h = 1080
name_list = []
asked = []
score = 0
is_clicked = False


class Menu:
    def __init__(self, parent):
        self.parent = parent
        self.root = root

        background_color = "#cc3628"

   #     self.main_frame = tk.Frame(root)
  #      self.main_frame.pack(fill="both", expand=True)

 #       self.my_canvas = tk.Canvas(self.main_frame)
#        self.my_canvas.pack(side="left", fill="both", expand=True)

   #     self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.my_canvas.yview)
  #      self.scrollbar.pack(side="right", fill="y")

 #       self.scrollable_frame = customtkinter.CTkScrollableFrame(root, width=1800, height=9999)
#        self.scrollable_frame.pack()

       # self.scrollable_frame.bind("<Configure>",
                   #                lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))



        self.original_bg_image = Image.open("Screenshot 2026-05-18 124046.png")
        self.bg_photo = ImageTk.PhotoImage(self.original_bg_image)
        self.bg_label = Label(root, image=self.bg_photo)
        self.bg_label.image = self.bg_photo
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)




        self.bar = Label(root,width=1080, height=4, bg="#153c7d")
        self.bar.place(x=0,y=0)

        #self.image2 = Image.open('Falcon.png')
        #self.phoneix = ImageTk.PhotoImage(self.image2)
        #self.canvas.create_image(150,150,image=self.phoneix)
        #self.image_label = Label(parent, image=self.phoneix, width=420, height = 410, borderwidth=0, border=0)
        #self.image_label.image = self.phoneix
        #self.image_label.place(x=11, y=100)

        self.text = Label(root,text="Mount Roskill Grammar", font=("arial",30,"underline","bold"),bg="#cc3628",)
        self.text.place(x=870, y=500)
        self. text2 = Label(root, font=("arial",20), bg="#cc3628",text="Mount Roskill Grammar was founded 1953 and began with a roll of 363 students, \n that intial started as a part of an auckland rugby union")
        self.text2.place(x=600, y=560)
        # Create button and image
        self.button = PhotoImage(file='button_menu (1).png')
        self.img = Label(root, borderwidth=0, width=200, bg="#cc3628" ,image=self.button,activebackground="#cc3628", activeforeground="white")
        self.img.place(x=60, y=470)

        self.button2 = PhotoImage(file='button_pita.png')
        self.img2 = Button(root, borderwidth=0, command=self.pita, width=200, bg="#cc3628", image=self.button2, activebackground="#cc3628", activeforeground="white")
        self.img2.place(x=60, y=540)

        self.button3 = PhotoImage(file='spec.png')
        self.img3 = Button(root, borderwidth=0, command=self.specials, width=200, bg="#cc3628", image=self.button3,
                           activebackground="#cc3628", activeforeground="white")
        self.img3.place(x=60, y=610)

        self.button4 = PhotoImage(file='button_main.png')
        self.img4 = Button(root, borderwidth=0, command=self.main,width=200, bg="#cc3628", image=self.button4,
                           activebackground="#cc3628", activeforeground="white")
        self.img4.place(x=60, y=680)

        self.button5 = PhotoImage(file='button_sides (1).png')
        self.img5 = Button(root, borderwidth=0, width=200, command=self.sides,bg="#cc3628", image=self.button5,
                           activebackground="#cc3628", activeforeground="white")
        self.img5.place(x=61, y=750)

        self.btn_order = PhotoImage(file='button_order (1).png')
        self.img_order = customtkinter.CTkButton(root, fg_color=("black"), command=self.order,corner_radius=100,height=65,width=10, border_width=3, bg_color="#153c7d")
        self.img_order.place(x=1070, y=0)

        self.parent.bind("<Configure>", self.resize_bg)

        self.quiz_frame = Frame(root, background=background_color)
        self.quiz_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.content_frame = Frame(self.quiz_frame, background=background_color)
        self.content_frame.grid()
        self.bg_label.pack()



        self.info = Label(text="hi")

    def resize_bg(self, event):
        if event.widget == self.parent:
            new_image = self.original_bg_image.resize((event.width, event.height))
            self.bg_photo = ImageTk.PhotoImage(new_image)
            self.bg_label.config(image=self.bg_photo)
            self.bg_label.image = self.bg_photo

    #Chicken
    #Pita - Teriyaki


    #Fresh
    #plain
    #pita
    #with shredded chicken, fresh veggies, cheese, and yummy teriyaki sauce.
    def trueflase(self):
        global is_clicked
        is_clicked = True

    is_clicked = True



    def order(self):
        try:
            self.overlay.destroy()
            self.menu_window.destroy()
        except:
            pass

        # Dark transparent background
        self.overlay = tk.Toplevel(self.parent)
        self.overlay.attributes("-fullscreen", True)
        self.overlay.attributes("-alpha", 0.5)
        self.overlay.configure(bg="black")
        self.overlay.overrideredirect(True)

        # Solid menu
        self.menu_window = tk.Toplevel(self.parent)
        self.menu_window.overrideredirect(True)
        self.menu_window.geometry("300x1080+1620+0")
        self.menu_window.configure(bg="blue")

        self.ko = tkinter.Frame(self.menu_window, borderwidth=100, width=200, bg="black")
        self.ko.place(x=1080, y=0)
        self.ko.lift()


        self.overlay.lift()
        self.menu_window.lift()

        self.overlay.grab_set()

        self.overlay.bind("<Button-1>", self.close_overlay)

    def close_overlay(self, event):
        x = event.x_root
        y = event.y_root

        menu_x = self.menu_window.winfo_rootx()
        menu_y = self.menu_window.winfo_rooty()
        menu_w = self.menu_window.winfo_width()
        menu_h = self.menu_window.winfo_height()

        inside_menu = (
                menu_x <= x <= menu_x + menu_w and
                menu_y <= y <= menu_y + menu_h
        )

        if not inside_menu:
            self.menu_window.destroy()
            self.overlay.destroy()

    def pita(self):



        self.background = Label(width=200, height=200, bg="#cc3628")
        self.background.place(x=600,y=500)

        self.hg1 = customtkinter.CTkButton(root,bg_color="#cc3628", hover_color="#153c7d",height=320,width=250,text="",fg_color="#153c7d",text_color="#ffffff",corner_radius=23)
        self.hg1.place(x=350, y=400)

        self.text = Label(root,
                          text="Fresh plain pita with shredded \nchicken, fresh veggies, cheese,\n and yummy teriyaki sauce.",
                          font=("arial", 10,  "bold"), bg="#153c7d",fg="white" )
        self.text.place(x=375, y=600)

        self.hg = customtkinter.CTkButton(root, hover_color="#416db6",height=120,width=160,text="", bg_color="#153c7d",fg_color="#416db6",text_color="#ffffff",corner_radius=23)
        self.hg.place(x=393, y=440)
        self.hg.lift()

        self.f0ood = Image.open('Untitled Design - 1.png')
        self.f0ood = self.f0ood.resize((200, 300))  # resize to 100x100
        self.f0ood = ImageTk.PhotoImage(self.f0ood)
        self.food = Label(root, borderwidth=0, width=120, height=100, bg="#416db6", image=self.f0ood)
        self.food.place(x=420, y=440)

        self.we = customtkinter.CTkButton(root,bg_color="#cc3628", hover_color="#153c7d",height=320,width=250,text="",fg_color="#153c7d",text_color="#ffffff",corner_radius=23)
        self.we.place(x=650, y=400)

        self.text1 = Label(root,
                          text="Fresh plain pita with shredded \nchicken, fresh veggies, cheese,\n and yummy teriyaki sauce.",
                          font=("arial", 10,  "bold"), bg="#153c7d",fg="white" )
        self.text1.place(x=675, y=600)

        self.qw = customtkinter.CTkButton(root, hover_color="#416db6",height=120,width=160,text="", bg_color="#153c7d",fg_color="#416db6",text_color="#ffffff",corner_radius=23)
        self.qw.place(x=693, y=440)
        self.qw.lift()



    def main(self):
        self.background = Label(root,width=200, height=200, bg="#cc3628")
        self.background.place(x=600,y=500)

        self.image9 = PhotoImage(file='button.png')
        self.img9 = Label(root,borderwidth=100, width=200, bg="#cc3628", image=self.image9)
        self.img9.place(x=400, y=400)

        self.image12 = PhotoImage(file='button.png')
        self.img12 = Label(root,borderwidth=100, width=200, bg="#cc3628", image=self.image12)
        self.img12.place(x=500, y=400)

        self.image42 = PhotoImage(file='button.png')
        self.img42 = Label(root,borderwidth=100, width=200, bg="#cc3628", image=self.image42)
        self.img42.place(x=700, y=400)

    def sides(self):
        self.background = Label(root,width=200, height=200, bg="#cc3628")
        self.background.place(x=600,y=500)


        self.image9 = PhotoImage(file='button.png')
        self.img9 = Label(root,borderwidth=100, width=200, bg="#cc3628", image=self.image9)
        self.img9.place(x=400, y=400)

        self.image12 = PhotoImage(file='button.png')
        self.img12 = Label(root,borderwidth=100, width=200, bg="#cc3628", image=self.image12)
        self.img12.place(x=800, y=800)

        self.image42 = PhotoImage(file='button.png')
        self.img42 = Label(root,borderwidth=100, width=200, bg="#cc3628", image=self.image42)
        self.img42.place(x=1500, y=400)

    def specials(self):
        self.background = Label(root,width=200, height=200, bg="#cc3628")
        self.background.place(x=600,y=500)

        self.image9 = PhotoImage(file='button.png')
        self.img9 = Label(root,borderwidth=100, width=200, bg="#cc3628", image=self.image9)
        self.img9.place(x=400, y=800)

        self.image12 = PhotoImage(file='button.png')
        self.img12 = Label(root,borderwidth=100, width=200, bg="#cc3628", image=self.image12)
        self.img12.place(x=800, y=400)

        self.image42 = PhotoImage(file='button.png')
        self.img42 = Label(root,borderwidth=100, width=200, bg="#cc3628", image=self.image42)
        self.img42.place(x=1500, y=400)


if __name__ == "__main__":
        root = tk.Tk()
        root.geometry("1920x1080")
        root.minsize(10,10)
        root.maxsize(1920,1080)
        root.iconbitmap("Falcon.png")
        root.title("General Knowledge Quiz")
        root.configure(bg="#800517")
        Menu_object = Menu(root)

        root.mainloop()


for x in range(9999):
    customtkinter.CTkScrollableFrame(Menu)