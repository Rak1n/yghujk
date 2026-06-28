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
        self.order_items = []

        background_color = "#cc3628"


        self.original_bg_image = Image.open("Screenshot 2026-05-18 124046.png")
        self.bg_label= self.original_bg_image.resize((9999, 9999))
        self.bg_photo = ImageTk.PhotoImage(self.original_bg_image)
        self.bg_label = Label(root, image=self.bg_photo)
        self.bg_label.image = self.bg_photo

        self.bg_label.place(x=0, y=0)

        self.bar = Label(root, bg="#153c7d")
        self.bar.place(x=0, y=0, relwidth=1, height=60)

        self.text = Label(root, text="Mount Roskill Grammar", font=("arial", 30, "underline", "bold"), bg="#cc3628")
        self.text.place(x=870, y=500)

        self.text2 = Label(root, font=("arial", 20), bg="#cc3628",
                           text="Mount Roskill Grammar was founded 1953 and began with a roll of 363 students, \n that intial started as a part of an auckland rugby union")
        self.text2.place(x=600, y=560)

        self.button = PhotoImage(file='button_menu (1).png')
        self.img = Label(root, borderwidth=0, width=200, bg="#cc3628", image=self.button,
                         activebackground="#cc3628", activeforeground="white")
        self.img.place(x=60, y=470)

        self.button2 = PhotoImage(file='button_pita.png')
        self.img2 = Button(root, borderwidth=0, command=self.pita, width=200, bg="#cc3628",
                           image=self.button2, activebackground="#cc3628", activeforeground="white")
        self.img2.place(x=60, y=540)

        self.button3 = PhotoImage(file='spec.png')
        self.img3 = Button(root, borderwidth=0, command=self.specials, width=200, bg="#cc3628",
                           image=self.button3, activebackground="#cc3628", activeforeground="white")
        self.img3.place(x=60, y=610)

        self.button4 = PhotoImage(file='button_main.png')
        self.img4 = Button(root, borderwidth=0, command=self.main, width=200, bg="#cc3628",
                           image=self.button4, activebackground="#cc3628", activeforeground="white")
        self.img4.place(x=60, y=680)

        self.button5 = PhotoImage(file='button_sides (1).png')
        self.img5 = Button(root, borderwidth=0, width=200, command=self.sides, bg="#cc3628",
                           image=self.button5, activebackground="#cc3628", activeforeground="white")
        self.img5.place(x=61, y=750)

        # In __init__, replace the img_order button and remove overlay/menu_window lines, add these:

        self.img_order = customtkinter.CTkButton(root, fg_color="black", command=self.toggle_sidebar,
                                                 corner_radius=100, height=65, width=10,
                                                 border_width=3, bg_color="#153c7d")
        self.img_order.place(x=1070, y=0)

        # Sidebar frame — placed off-screen to the right initially
        self.sidebar = Frame(root, bg="blue", width=300)
        self.sidebar_visible = False
        # Don't place it yet; we'll use place() to show/hide it

        self.overlay = None
        self.menu_window = None  # keep for compatibility but won't be used
        self.quiz_frame = Frame(root, background=background_color)
        self.quiz_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.content_frame = Frame(self.quiz_frame, background=background_color)
        self.content_frame.grid()

        self.overlay = None
        self.menu_window = None

    def resize_bg(self, event):
        if event.widget == self.parent:
            new_image = self.original_bg_image.resize((event.width, event.height))
            self.bg_photo = ImageTk.PhotoImage(new_image)
            self.bg_label.config(image=self.bg_photo)
            self.bg_label.image = self.bg_photo

    def add_to_order(self, item_name, price):
        self.order_items.append((item_name, price))
        try:
            self.update_order_display()
        except Exception:
            pass

    def update_order_display(self):
        if not self.sidebar_visible:
            return

        for widget in self.sidebar.winfo_children():
            widget.destroy()

        Label(self.sidebar, text="Your Order", font=("arial", 16, "bold"),
              bg="blue", fg="white").pack(pady=10)

        total = 0
        for name, price in self.order_items:
            Label(self.sidebar, text=f"{name}  ${price:.2f}",
                  font=("arial", 12), bg="blue", fg="white").pack(pady=2)
            total += price

        Label(self.sidebar, text=f"Total: ${total:.2f}",
              font=("arial", 14, "bold"), bg="blue", fg="white").pack(pady=10)

        customtkinter.CTkButton(
            self.sidebar, text="Clear Order", fg_color="#cc3628",
            hover_color="#a02010", corner_radius=10,
            command=self.clear_order
        ).pack(pady=10)

        # Close button at the top
        customtkinter.CTkButton(
            self.sidebar, text="✕ Close", fg_color="#333333",
            hover_color="#555555", corner_radius=10,
            command=self.toggle_sidebar
        ).pack(pady=5)
    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar.place_forget()
            self.sidebar_visible = False
        else:
            # Place sidebar on the right edge, full height
            self.sidebar.place(x=root.winfo_width() - 300, y=0, width=300, height=root.winfo_height())
            self.sidebar.lift()
            self.sidebar_visible = True
            self.update_order_display()

    def clear_order(self):
        self.order_items = []
        self.update_order_display()

    def order(self):
        # Kept for compatibility; now just calls toggle
        self.toggle_sidebar()

        self.overlay = tk.Toplevel(self.parent)
        self.overlay.attributes("-fullscreen", True)
        self.overlay.attributes("-alpha", 0.5)
        self.overlay.configure(bg="black")
        self.overlay.overrideredirect(True)

        self.menu_window = tk.Toplevel(self.parent)
        self.menu_window.overrideredirect(True)
        self.menu_window.geometry("300x1080+1620+0")
        self.menu_window.configure(bg="blue")

        self.overlay.lift()
        self.menu_window.lift()
        self.overlay.grab_set()
        self.overlay.bind("<Button-1>", self.close_overlay)

        self.update_order_display()

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
            self.overlay = None
            self.menu_window = None

    def pita(self):
        self.background = Label(width=200, height=200, bg="#cc3628")
        self.background.place(x=600, y=500)

        # --- Card 1: Teriyaki Pita ---
        self.hg1 = customtkinter.CTkButton(root, bg_color="#cc3628", hover_color="#153c7d",
                                            height=320, width=250, text="",
                                            fg_color="#153c7d", text_color="#ffffff", corner_radius=23)
        self.hg1.place(x=350, y=400)

        self.hg = customtkinter.CTkButton(root, hover_color="#416db6", height=120, width=160,
                                           text="", bg_color="#153c7d", fg_color="#416db6",
                                           text_color="#ffffff", corner_radius=23)
        self.hg.place(x=393, y=440)
        self.hg.lift()

        self.f0ood = Image.open('Untitled Design - 1.png')
        self.f0ood = self.f0ood.resize((150, 110))
        self.f0ood = ImageTk.PhotoImage(self.f0ood)
        self.food = Label(root, borderwidth=0, bg="#416db6", image=self.f0ood)
        self.food.place(x=393, y=440)
        self.food.lift()

        self.pita_name = Label(root, text="Teriyaki Pita", font=("arial", 11, "bold"),
                               bg="#153c7d", fg="white")
        self.pita_name.place(x=425, y=575)

        self.pita_desc = Label(root, text="Fresh plain pita with shredded\nchicken, fresh veggies, cheese,\nand yummy teriyaki sauce.",
                               font=("arial", 9), bg="#153c7d", fg="white")
        self.pita_desc.place(x=375, y=598)

        self.price_label = Label(root, text="$7.50", font=("arial", 12, "bold"),
                                 bg="#153c7d", fg="white")
        self.price_label.place(x=375, y=665)

        self.add_btn = customtkinter.CTkButton(
            root, text="Add +", width=80, height=28,
            fg_color="#cc3628", hover_color="#a02010",
            bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Teriyaki Pita", 7.50)
        )
        self.add_btn.place(x=450, y=662)

        # --- Card 2 ---
        self.we = customtkinter.CTkButton(root, bg_color="#cc3628", hover_color="#153c7d",
                                           height=320, width=250, text="",
                                           fg_color="#153c7d", text_color="#ffffff", corner_radius=23)
        self.we.place(x=650, y=400)

        self.qw = customtkinter.CTkButton(root, hover_color="#416db6", height=120, width=160,
                                           text="", bg_color="#153c7d", fg_color="#416db6",
                                           text_color="#ffffff", corner_radius=23)
        self.qw.place(x=693, y=440)
        self.qw.lift()

        self.card2_name = Label(root, text="Plain Pita", font=("arial", 11, "bold"),
                                bg="#153c7d", fg="white")
        self.card2_name.place(x=675, y=575)

        self.card2_desc = Label(root, text="Fresh plain pita with shredded\nchicken, fresh veggies, cheese,\nand yummy teriyaki sauce.",
                                font=("arial", 9), bg="#153c7d", fg="white")
        self.card2_desc.place(x=660, y=598)

        self.price_label2 = Label(root, text="$6.50", font=("arial", 12, "bold"),
                                  bg="#153c7d", fg="white")
        self.price_label2.place(x=675, y=665)

        self.add_btn2 = customtkinter.CTkButton(
            root, text="Add +", width=80, height=28,
            fg_color="#cc3628", hover_color="#a02010",
            bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Plain Pita", 6.50)
        )
        self.add_btn2.place(x=750, y=662)

    def main(self):
        self.background = Label(root, width=200, height=200, bg="#cc3628")
        self.background.place(x=600, y=500)

        self.image9 = PhotoImage(file='button.png')
        self.img9 = Label(root, borderwidth=100, width=200, bg="#cc3628", image=self.image9)
        self.img9.place(x=400, y=400)

        self.image12 = PhotoImage(file='button.png')
        self.img12 = Label(root, borderwidth=100, width=200, bg="#cc3628", image=self.image12)
        self.img12.place(x=500, y=400)

        self.image42 = PhotoImage(file='button.png')
        self.img42 = Label(root, borderwidth=100, width=200, bg="#cc3628", image=self.image42)
        self.img42.place(x=700, y=400)

    def sides(self):
        self.background = Label(root, width=200, height=200, bg="#cc3628")
        self.background.place(x=600, y=500)

        self.image9 = PhotoImage(file='button.png')
        self.img9 = Label(root, borderwidth=100, width=200, bg="#cc3628", image=self.image9)
        self.img9.place(x=400, y=400)

        self.image12 = PhotoImage(file='button.png')
        self.img12 = Label(root, borderwidth=100, width=200, bg="#cc3628", image=self.image12)
        self.img12.place(x=800, y=800)

        self.image42 = PhotoImage(file='button.png')
        self.img42 = Label(root, borderwidth=100, width=200, bg="#cc3628", image=self.image42)
        self.img42.place(x=1500, y=400)

    def specials(self):
        self.background = Label(root, width=200, height=200, bg="#cc3628")
        self.background.place(x=600, y=500)

        self.image9 = PhotoImage(file='button.png')
        self.img9 = Label(root, borderwidth=100, width=200, bg="#cc3628", image=self.image9)
        self.img9.place(x=400, y=800)

        self.image12 = PhotoImage(file='button.png')
        self.img12 = Label(root, borderwidth=100, width=200, bg="#cc3628", image=self.image12)
        self.img12.place(x=800, y=400)

        self.image42 = PhotoImage(file='button.png')
        self.img42 = Label(root, borderwidth=100, width=200, bg="#cc3628", image=self.image42)
        self.img42.place(x=1500, y=400)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1920x1080")
    root.minsize(10, 10)
    root.maxsize(1920, 1080)
    root.iconbitmap("Falcon.png")
    root.title("General Knowledge Quiz")
    root.configure(bg="#800517")
    Menu_object = Menu(root)
    root.mainloop()