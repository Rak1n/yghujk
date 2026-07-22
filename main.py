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
        self.original_bg_image = self.original_bg_image.resize((1920, 1080), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.original_bg_image)
        self.bg_label = Label(root, image=self.bg_photo, borderwidth=0, highlightthickness=0)
        self.bg_label.image = self.bg_photo
        self.bg_label.place(x=0, y=0, width=1920, height=1080)
        self.bg_label.lower()

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

        self.img_order = customtkinter.CTkButton(root, fg_color="black", command=self.toggle_sidebar,
                                                 corner_radius=100, height=65, width=10,
                                                 border_width=3, bg_color="#153c7d")
        self.img_order.place(x=1070, y=0)

        # Sidebar frame — placed off-screen to the right initially
        self.sidebar = Frame(root, bg="#153c7d", width=300)
        self.sidebar_visible = False

        self.overlay = None
        self.menu_window = None
        self.quiz_frame = Frame(root, background=background_color)
        self.quiz_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.content_frame = Frame(self.quiz_frame, background=background_color)
        self.content_frame.grid()

        self.overlay = None
        self.menu_window = None

        # --- NEW: a single container frame that holds whichever section's ---
        # --- cards are currently on screen. Every section-building method ---
        # --- (pita/main/sides/specials) builds its widgets inside this frame ---
        # --- instead of directly on `root`. To clear a section we just ---
        # --- destroy this one frame and recreate it — no need to track ---
        # --- dozens of individual widget references.
        self.items_frame = Frame(root, bg="#cc3628", bd=0, highlightthickness=0)
        self.items_frame.place(x=0, y=0, width=1920, height=1080)
        self.items_frame.lower(self.bg_label)  # keep it above bg but we'll raise cards as needed
        self.items_frame.lift(self.bg_label)

    def resize_bg(self, event):
        if event.widget == self.parent:
            new_image = self.original_bg_image.resize((event.width, event.height), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(new_image)
            self.bg_label.config(image=self.bg_photo)
            self.bg_label.image = self.bg_photo
            self.bg_label.lower()

    # ------------------------------------------------------------------
    # NEW: call this at the top of every method that draws a section's
    # cards (pita, main, sides, specials). It destroys the ENTIRE old
    # frame (and therefore every widget inside it, all at once) and
    # replaces it with a fresh empty frame ready to be filled in.
    # ------------------------------------------------------------------
    def clear_items(self):
        self.items_frame.destroy()
        self.items_frame = Frame(root, bg="#cc3628", bd=0, highlightthickness=0)
        self.items_frame.place(x=0, y=0, width=1920, height=1080)
        self.items_frame.lift(self.bg_label)

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
            self.sidebar.place(x=root.winfo_width() - 300, y=0, width=300, height=root.winfo_height())
            self.sidebar.lift()
            self.sidebar_visible = True
            self.update_order_display()

    def clear_order(self):
        self.order_items = []
        self.update_order_display()

    def order(self):
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

    # ------------------------------------------------------------------
    # Every card below is now built with `self.items_frame` as the parent
    # (instead of `root`), and `clear_items()` is called first. That's the
    # entire fix — nothing else about the layout/logic changes.
    # ------------------------------------------------------------------
    def pita(self):
        self.clear_items()
        parent = self.items_frame

        self.background = Label(parent, width=200, height=200, bg="#cc3628")
        self.background.place(x=600, y=500)

        # --- Card 1: Teriyaki Pita ---
        self.backblue = customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23)
        self.backblue.place(x=350, y=400)

        self.lightblue = customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23)
        self.lightblue.place(x=393, y=440)
        self.lightblue.lift()

        self.food_image = Image.open('Untitled Design - 1.png')
        self.food_image = self.food_image.resize((200, 200))
        self.food_image = ImageTk.PhotoImage(self.food_image)
        self.food_load = Label(parent, borderwidth=0, border=0, height=75, width=120, bg="#416db6", image=self.food_image)
        self.food_load.place(x=420, y=450)
        self.food_load.lift()

        self.pita_name = Label(parent, text="Teriyaki Pita", font=("arial", 11, "bold"), bg="#153c7d", fg="white")
        self.pita_name.place(x=425, y=575)

        self.pita_desc = Label(parent, text="Fresh plain pita with shredded\nchicken, fresh veggies, cheese,\nand yummy teriyaki sauce.",
            font=("arial", 9), bg="#153c7d", fg="white")
        self.pita_desc.place(x=380, y=598)

        self.price_label = Label(parent, text="$8.25", font=("arial", 12, "bold"), bg="#153c7d", fg="white")
        self.price_label.place(x=375, y=665)

        self.add_btn = customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Teriyaki Pita", 8.25))
        self.add_btn.place(x=470, y=662)

        # --- Card 2 ---
        self.backblue1 = customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23)
        self.backblue1.place(x=650, y=400)

        self.lightblue1 = customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23)
        self.lightblue1.place(x=693, y=440)
        self.lightblue1.lift()

        self.card2_name = Label(parent, text="Falafel Pita", font=("arial", 11, "bold"), bg="#153c7d", fg="white")
        self.card2_name.place(x=735, y=575)

        self.card2_desc = Label(parent, text="Fresh plain pita with falafel,\n fresh veggies, cheese, \nand sweet chilli sauce.",
            font=("arial", 9), bg="#153c7d", fg="white")
        self.card2_desc.place(x=700, y=598)

        self.price_label2 = Label(parent, text="$8.25", font=("arial", 12, "bold"), bg="#153c7d", fg="white")
        self.price_label2.place(x=675, y=665)

        self.add_btn2 = customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Falafel Pita", 8.25))
        self.add_btn2.place(x=770, y=662)

        # --- Card 3 ---
        self.backblue2 = customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23)
        self.backblue2.place(x=950, y=400)

        self.lightblue2 = customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23)
        self.lightblue2.place(x=993, y=440)
        self.lightblue2.lift()

        self.card3_name = Label(parent, text=" Chicken Pita - Mayonnaise", font=("arial", 11, "bold"), bg="#153c7d", fg="white")
        self.card3_name.place(x=975, y=575)

        self.card3_desc = Label(parent, text="Fresh plain pita with shredded \nchicken,  fresh veggies, \ncheese, and creamy mayo.",
            font=("arial", 9), bg="#153c7d", fg="white")
        self.card3_desc.place(x=985, y=598)

        self.price_label3 = Label(parent, text="$8.25", font=("arial", 12, "bold"), bg="#153c7d", fg="white")
        self.price_label3.place(x=975, y=665)

        self.add_btn3 = customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order(" Chicken Pita - Mayonnaise", 8.25))
        self.add_btn3.place(x=1070, y=662)

        # --- Card 4 ---
        self.backblue3 = customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23)
        self.backblue3.place(x=1250, y=400)

        self.lightblue3 = customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23)
        self.lightblue3.place(x=1293, y=440)
        self.lightblue3.lift()

        self.card4_name = Label(parent, text="Chicken Pita - BBQ - LT", font=("arial", 11, "bold"), bg="#153c7d", fg="white")
        self.card4_name.place(x=1275, y=575)

        self.card4_desc = Label(parent, text="Fresh plain pita with shredded \nchicken, fresh veggies,\n cheese, and classic BBQ sauce.",
            font=("arial", 9), bg="#153c7d", fg="white")
        self.card4_desc.place(x=1285, y=598)

        self.price_label4 = Label(parent, text="$8.25", font=("arial", 12, "bold"), bg="#153c7d", fg="white")
        self.price_label4.place(x=1275, y=665)

        self.add_btn4 = customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Chicken Pita - BBQ - LT", 8.25))
        self.add_btn4.place(x=1370, y=662)

        # --- Card 5 ---
        self.backblue4 = customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23)
        self.backblue4.place(x=1550, y=400)

        self.lightblue4 = customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23)
        self.lightblue4.place(x=1593, y=440)
        self.lightblue4.lift()

        self.card5_name = Label(parent, text="Chicken Pita - Sweet Chilli - LT", font=("arial", 11, "bold"), bg="#153c7d", fg="white")
        self.card5_name.place(x=1565, y=575)

        self.card5_desc = Label(parent, text="Fresh plain pita with\n shredded chicken, fresh veggies, \ncheese, and sweet chilli sauce.",
            font=("arial", 9), bg="#153c7d", fg="white")
        self.card5_desc.place(x=1585, y=598)

        self.price_label5 = Label(parent, text="$8.25", font=("arial", 12, "bold"), bg="#153c7d", fg="white")
        self.price_label5.place(x=1575, y=665)

        self.add_btn5 = customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order(" Chicken Pita - Sweet Chilli - LT", 8.25))
        self.add_btn5.place(x=1670, y=662)

        # NOTE: the old broken line `self.sides.destroy()` has been removed.
        # It was trying to destroy a method reference, not a widget — it
        # would have raised an AttributeError and never actually ran.

    def main(self):
        self.clear_items()
        parent = self.items_frame

        self.background = Label(parent, width=200, height=200, bg="#cc3628")
        self.background.place(x=600, y=500)

        self.image9 = PhotoImage(file='button.png')
        self.img9 = Label(parent, borderwidth=100, width=200, bg="#cc3628", image=self.image9)
        self.img9.place(x=400, y=400)

        self.image12 = PhotoImage(file='button.png')
        self.img12 = Label(parent, borderwidth=100, width=200, bg="#cc3628", image=self.image12)
        self.img12.place(x=500, y=400)

        self.image42 = PhotoImage(file='button.png')
        self.img42 = Label(parent, borderwidth=100, width=200, bg="#cc3628", image=self.image42)
        self.img42.place(x=700, y=400)

    def sides(self):
        self.clear_items()
        parent = self.items_frame

        self.background = Label(parent, width=200, height=200, bg="#cc3628")
        self.background.place(x=600, y=500)

        self.image9 = PhotoImage(file='button.png')
        self.img9 = Label(parent, borderwidth=100, width=200, bg="#cc3628", image=self.image9)
        self.img9.place(x=400, y=400)

        self.image12 = PhotoImage(file='button.png')
        self.img12 = Label(parent, borderwidth=100, width=200, bg="#cc3628", image=self.image12)
        self.img12.place(x=800, y=800)

        self.image42 = PhotoImage(file='button.png')
        self.img42 = Label(parent, borderwidth=100, width=200, bg="#cc3628", image=self.image42)
        self.img42.place(x=1500, y=400)

    def specials(self):
        self.clear_items()
        parent = self.items_frame

        self.background = Label(parent, width=200, height=200, bg="#cc3628")
        self.background.place(x=600, y=500)

        self.image9 = PhotoImage(file='button.png')
        self.img9 = Label(parent, borderwidth=100, width=200, bg="#cc3628", image=self.image9)
        self.img9.place(x=400, y=800)

        self.image12 = PhotoImage(file='button.png')
        self.img12 = Label(parent, borderwidth=100, width=200, bg="#cc3628", image=self.image12)
        self.img12.place(x=800, y=400)

        self.image42 = PhotoImage(file='button.png')
        self.img42 = Label(parent, borderwidth=100, width=200, bg="#cc3628", image=self.image42)
        self.img42.place(x=1500, y=400)


if __name__ == "__main__":
    root = tk.Tk()
    app_icon = tk.PhotoImage(file="Falcon.png")
    root.iconphoto(False, app_icon)
    root.geometry("1920x1080")
    root.minsize(10, 10)
    root.maxsize(1920, 1080)
    root.title("General Knowledge Quiz")
    root.configure(bg="#800517")
    Menu_object = Menu(root)

    root.mainloop()