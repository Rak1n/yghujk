from tkinter import *
import tkinter as tk
import customtkinter


from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

w = 1920
h = 1080


class Menu:
    def __init__(self, parent):
        self.parent = parent
        self.root = root
        self.order_items = []

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
                           text="Mount Roskill Grammar was founded 1953 and began with a roll of 363 students, \n that initially started as a part of an auckland rugby union.")
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

        self.img_order = customtkinter.CTkButton(root, fg_color="black", text="Order", font=("Canva Sans", 16, "bold"),command=self.toggle_sidebar,
                                                 corner_radius=100, height=60, width=30,
                                                 border_width=3, bg_color="#153c7d")
        self.img_order.place(x=10, y=0)

        self.sidebar = Frame(root, bg="#153c7d", width=300)
        self.sidebar_visible = False

        root.bind_all("<Button-1>", self.on_global_click, add="+")

        self.menu_widgets = []

    def clear_items(self):
        for widget in self.menu_widgets:
            widget.destroy()
        self.menu_widgets = []

    def place_order(self):
        if not self.order_items:
            return  # nothing to confirm if the order is empty

        total = sum(price for _, price in self.order_items)

        # Wipe the sidebar and show a confirmation screen in its place
        for widget in self.sidebar.winfo_children():
            widget.destroy()

        Label(self.sidebar, text="✓", font=("arial", 40, "bold"),
              bg="#153c7d", fg="#4CAF50").pack(pady=(40, 0))

        Label(self.sidebar, text="Order Placed!", font=("arial", 18, "bold"),
              bg="#153c7d", fg="white").pack(pady=(0, 10))

        Label(self.sidebar, text=f"Total charged: ${total:.2f}",
              font=("arial", 12), bg="#153c7d", fg="white").pack(pady=5)

        Label(self.sidebar, text="Thanks — your order is being prepared.",
              font=("arial", 11), bg="#153c7d", fg="#cccccc", wraplength=250,
              justify="center").pack(pady=(5, 20))

        customtkinter.CTkButton(
            self.sidebar, text="✕ Close", fg_color="#333333",
            hover_color="#555555", corner_radius=10,
            command=self.toggle_sidebar
        ).pack(pady=5)

        # Clear the cart now that it's "placed"
        self.order_items = []

    def track(self, widget):
        self.menu_widgets.append(widget)
        return widget

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
              bg="#153c7d", fg="white").pack(pady=10)

        total = 0
        for name, price in self.order_items:
            Label(self.sidebar, text=f"{name}  ${price:.2f}",
                  font=("arial", 12), bg="#153c7d", fg="white").pack(pady=2)
            total += price

        Label(self.sidebar, text=f"Total: ${total:.2f}",
              font=("arial", 14, "bold"), bg="#153c7d", fg="white").pack(pady=10)

        customtkinter.CTkButton(
            self.sidebar, text="Place  Order", fg_color="#cc3628",
            hover_color="#a02010", corner_radius=10,
            command=self.place_order
        ).pack(pady=10)

        customtkinter.CTkButton(
            self.sidebar, text="✕ Close", fg_color="#333333",
            hover_color="#555555", corner_radius=10,
            command=self.toggle_sidebar
        ).pack(pady=5)

    def on_global_click(self, event):
        if not self.sidebar_visible:
            return

        w = event.widget
        while w is not None:
            if w == self.img_order:
                return
            w = getattr(w, "master", None)

        sx = self.sidebar.winfo_rootx()
        sy = self.sidebar.winfo_rooty()
        sw = self.sidebar.winfo_width()
        sh = self.sidebar.winfo_height()
        inside_sidebar = (sx <= event.x_root <= sx + sw and
                           sy <= event.y_root <= sy + sh)

        if not inside_sidebar:
            self.toggle_sidebar()

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

    def pita(self):
        self.clear_items()
        parent = root

        self.background = self.track(Label(parent, width=200, height=200, bg="#cc3628"))
        self.background.place(x=600, y=500)

        # --- Card 1 ---
        self.backblue = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23))
        self.backblue.place(x=350, y=500)

        self.lightblue = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23))
        self.lightblue.place(x=393, y=540)
        self.lightblue.lift()

        self.food_image = Image.open('download.png')
        self.food_image = self.food_image.resize((100, 100))
        self.food_image = ImageTk.PhotoImage(self.food_image)
        self.food_load = self.track(Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image))
        self.food_load.place(x=410, y=560)
        self.food_load.lift()

        self.pita_name = self.track(Label(parent, text="Teriyaki Pita", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.pita_name.place(x=425, y=675)

        self.pita_desc = self.track(Label(parent, text="Fresh plain pita with shredded\nchicken, fresh veggies, cheese,\nand yummy teriyaki sauce.",
            font=("arial", 9), bg="#153c7d", fg="white"))
        self.pita_desc.place(x=380, y=698)

        self.price_label = self.track(Label(parent, text="$8.25", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label.place(x=375, y=765)

        self.add_btn = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Teriyaki Pita", 8.25)))
        self.add_btn.place(x=470, y=762)

        # --- Card 2 ---

        self.backblue1 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23))
        self.backblue1.place(x=650, y=500)

        self.lightblue1 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23))
        self.lightblue1.place(x=693, y=540)
        self.lightblue1.lift()

        self.food_image1 = Image.open('download (1).png')
        self.food_image1 = self.food_image1.resize((100, 100))
        self.food_image1 = ImageTk.PhotoImage(self.food_image1)
        self.food_load1 = self.track(Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image1))
        self.food_load1.place(x=715, y=560)
        self.food_load1.lift()

        self.card2_name = self.track(Label(parent, text="Falafel Pita", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card2_name.place(x=735, y=675)

        self.card2_desc = self.track(Label(parent, text="Fresh plain pita with falafel,\n fresh veggies, cheese, \nand sweet chilli sauce.",
            font=("arial", 9), bg="#153c7d", fg="white"))
        self.card2_desc.place(x=700, y=698)

        self.price_label2 = self.track(Label(parent, text="$8.25", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label2.place(x=675, y=765)

        self.add_btn2 = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Falafel Pita", 8.25)))
        self.add_btn2.place(x=770, y=762)

        # --- Card 3 ---
        self.backblue2 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23))
        self.backblue2.place(x=950, y=500)

        self.lightblue2 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23))
        self.lightblue2.place(x=993, y=540)
        self.lightblue2.lift()

        self.food_image2 = Image.open('download (2).png')
        self.food_image2 = self.food_image2.resize((100, 100))
        self.food_image2 = ImageTk.PhotoImage(self.food_image2)
        self.food_load2 = self.track(Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image2))
        self.food_load2.place(x=1010, y=560)
        self.food_load2.lift()

        self.card3_name = self.track(Label(parent, text=" Chicken Pita - Mayonnaise", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card3_name.place(x=975, y=675)

        self.card3_desc = self.track(Label(parent, text="Fresh plain pita with shredded \nchicken,  fresh veggies, \ncheese, and creamy mayo.",
            font=("arial", 9), bg="#153c7d", fg="white"))
        self.card3_desc.place(x=985, y=698)

        self.price_label3 = self.track(Label(parent, text="$8.25", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label3.place(x=975, y=765)

        self.add_btn3 = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order(" Chicken Pita - Mayonnaise", 8.25)))
        self.add_btn3.place(x=1070, y=762)

        # --- Card 4 ---
        self.backblue3 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23))
        self.backblue3.place(x=1250, y=500)

        self.lightblue3 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23))
        self.lightblue3.place(x=1293, y=540)
        self.lightblue3.lift()

        self.food_image3 = Image.open('download (3).png')
        self.food_image3 = self.food_image3.resize((100, 100))
        self.food_image3 = ImageTk.PhotoImage(self.food_image3)
        self.food_load3 = self.track(Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image3))
        self.food_load3.place(x=1310, y=560)
        self.food_load3.lift()

        self.card4_name = self.track(Label(parent, text="Chicken Pita - BBQ - LT", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card4_name.place(x=1295, y=675)

        self.card4_desc = self.track(Label(parent, text="Fresh plain pita with shredded \nchicken, fresh veggies,\n cheese, and classic BBQ sauce.",
            font=("arial", 9), bg="#153c7d", fg="white"))
        self.card4_desc.place(x=1285, y=698)

        self.price_label4 = self.track(Label(parent, text="$8.25", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label4.place(x=1275, y=765)

        self.add_btn4 = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Chicken Pita - BBQ - LT", 8.25)))
        self.add_btn4.place(x=1370, y=762)

        # --- Card 5 ---
        self.backblue4 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23))
        self.backblue4.place(x=1550, y=500)

        self.lightblue4 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23))
        self.lightblue4.place(x=1593, y=540)
        self.lightblue4.lift()

        self.food_image4 = Image.open('download (4).png')
        self.food_image4 = self.food_image4.resize((100, 100))
        self.food_image4 = ImageTk.PhotoImage(self.food_image4)
        self.food_load4 = self.track(Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image4))
        self.food_load4.place(x=1610, y=560)
        self.food_load4.lift()

        self.card5_name = self.track(Label(parent, text="Chicken Pita - Sweet Chilli - LT", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card5_name.place(x=1565, y=675)

        self.card5_desc = self.track(Label(parent, text="Fresh plain pita with\n shredded chicken, fresh veggies, \ncheese, and sweet chilli sauce.",
            font=("arial", 9), bg="#153c7d", fg="white"))
        self.card5_desc.place(x=1585, y=698)

        self.price_label5 = self.track(Label(parent, text="$8.25", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label5.place(x=1575, y=765)

        self.add_btn5 = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order(" Chicken Pita - Sweet Chilli - LT", 8.25)))
        self.add_btn5.place(x=1670, y=762)

    def main(self):
        self.clear_items()
        parent = root

        self.background = self.track(Label(parent, width=200, height=200, bg="#cc3628"))
        self.background.place(x=600, y=500)

        # --- Card 1 ---
        self.backblue = self.track(
            customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d", height=320, width=250, text="",
                                    fg_color="#153c7d", text_color="#ffffff", corner_radius=23))
        self.backblue.place(x=350, y=500)

        self.lightblue = self.track(
            customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160, text="", bg_color="#153c7d",
                                    fg_color="#416db6", text_color="#ffffff", corner_radius=23))
        self.lightblue.place(x=393, y=540)
        self.lightblue.lift()

        self.food_image = Image.open('download (9).png')
        self.food_image = self.food_image.resize((100, 100))
        self.food_image = ImageTk.PhotoImage(self.food_image)
        self.food_load = self.track(
            Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image))
        self.food_load.place(x=410, y=560)
        self.food_load.lift()

        self.pita_name = self.track(
            Label(parent, text="Sloppy Jo", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.pita_name.place(x=434, y=675)

        self.pita_desc = self.track(Label(parent,
                                          text="Savory beef mince in a soft burger\n bun, topped with a melty cheese \nslice and smoky BBQ sauce.",
                                          font=("arial", 9), bg="#153c7d", fg="white"))
        self.pita_desc.place(x=380, y=700)

        self.price_label = self.track(Label(parent, text="$7.70", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label.place(x=375, y=765)

        self.add_btn = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
                                                          hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
                                                          command=lambda: self.add_to_order("Sloppy Jo - LT", 7.70)))
        self.add_btn.place(x=470, y=762)

        # --- Card 2 ---

        self.backblue1 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
                                                            height=320, width=250, text="", fg_color="#153c7d",
                                                            text_color="#ffffff", corner_radius=23))
        self.backblue1.place(x=650, y=500)

        self.lightblue1 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
                                                             text="", bg_color="#153c7d", fg_color="#416db6",
                                                             text_color="#ffffff", corner_radius=23))
        self.lightblue1.place(x=693, y=540)
        self.lightblue1.lift()

        self.food_image1 = Image.open('download (14).png')
        self.food_image1 = self.food_image1.resize((100, 100))
        self.food_image1 = ImageTk.PhotoImage(self.food_image1)
        self.food_load1 = self.track(
            Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image1))
        self.food_load1.place(x=715, y=560)
        self.food_load1.lift()

        self.card2_name = self.track(
            Label(parent, text="Chicken Burger with Works  ", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card2_name.place(x=675, y=675)

        self.card2_desc = self.track(
            Label(parent, text="Golden chicken patty in a soft\n burger bun with melty cheese, fresh\n tomato and lettuce, smoky BBQ\n sauce, and creamy mayo.",
                  font=("arial", 9), bg="#153c7d", fg="white"))
        self.card2_desc.place(x=675, y=698)

        self.price_label2 = self.track(
            Label(parent, text="$7.70", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label2.place(x=675, y=765)

        self.add_btn2 = self.track(
            customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
                                    hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
                                    command=lambda: self.add_to_order("Chicken Burger with Works", 7.70)))
        self.add_btn2.place(x=770, y=762)

        # --- Card 3 ---
        self.backblue2 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
                                                            height=320, width=250, text="", fg_color="#153c7d",
                                                            text_color="#ffffff", corner_radius=23))
        self.backblue2.place(x=950, y=500)

        self.lightblue2 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
                                                             text="", bg_color="#153c7d", fg_color="#416db6",
                                                             text_color="#ffffff", corner_radius=23))
        self.lightblue2.place(x=993, y=540)
        self.lightblue2.lift()

        self.food_image2 = Image.open('download (11).png')
        self.food_image2 = self.food_image2.resize((100, 100))
        self.food_image2 = ImageTk.PhotoImage(self.food_image2)
        self.food_load2 = self.track(
            Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image2))
        self.food_load2.place(x=1010, y=560)
        self.food_load2.lift()

        self.card3_name = self.track(
            Label(parent, text="Spaghetti Meatballs", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card3_name.place(x=1000, y=675)

        self.card3_desc = self.track(
            Label(parent, text="Al dente spaghetti with savoury \nmeatballs, rich Napolitana sauce, and a \nsprinkle of shredded cheese.",
                  font=("arial", 9), bg="#153c7d", fg="white"))
        self.card3_desc.place(x=965, y=698)

        self.price_label3 = self.track(
            Label(parent, text="$9.35", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label3.place(x=975, y=765)

        self.add_btn3 = self.track(
            customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
                                    hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
                                    command=lambda: self.add_to_order("Spaghetti Meatballs - LT", 9.35)))
        self.add_btn3.place(x=1070, y=762)

        # --- Card 4 ---
        self.backblue3 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
                                                            height=320, width=250, text="", fg_color="#153c7d",
                                                            text_color="#ffffff", corner_radius=23))
        self.backblue3.place(x=1250, y=500)

        self.lightblue3 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
                                                             text="", bg_color="#153c7d", fg_color="#416db6",
                                                             text_color="#ffffff", corner_radius=23))
        self.lightblue3.place(x=1293, y=540)
        self.lightblue3.lift()

        self.food_image3 = Image.open('download (12).png')
        self.food_image3 = self.food_image3.resize((100, 100))
        self.food_image3 = ImageTk.PhotoImage(self.food_image3)
        self.food_load3 = self.track(
            Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image3))
        self.food_load3.place(x=1310, y=560)
        self.food_load3.lift()

        self.card4_name = self.track(
            Label(parent, text="Chicken Sub Roll", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card4_name.place(x=1310, y=675)

        self.card4_desc = self.track(Label(parent,
                                           text="Soft split roll filled with \ncrispy chicken bites\n and drizzled with \nspicy chilli mayo.",
                                           font=("arial", 9), bg="#153c7d", fg="white"))
        self.card4_desc.place(x=1310, y=698)

        self.price_label4 = self.track(
            Label(parent, text="$7.15", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label4.place(x=1275, y=765)

        self.add_btn4 = self.track(
            customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
                                    hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
                                    command=lambda: self.add_to_order("Chicken Sub Roll", 7.15)))
        self.add_btn4.place(x=1370, y=762)

        # --- Card 5 ---
        self.backblue4 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
                                                            height=320, width=250, text="", fg_color="#153c7d",
                                                            text_color="#ffffff", corner_radius=23))
        self.backblue4.place(x=1550, y=500)

        self.lightblue4 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
                                                             text="", bg_color="#153c7d", fg_color="#416db6",
                                                             text_color="#ffffff", corner_radius=23))
        self.lightblue4.place(x=1593, y=540)
        self.lightblue4.lift()

        self.food_image4 = Image.open('download (13).png')
        self.food_image4 = self.food_image4.resize((100, 100))
        self.food_image4 = ImageTk.PhotoImage(self.food_image4)
        self.food_load4 = self.track(
            Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image4))
        self.food_load4.place(x=1610, y=560)
        self.food_load4.lift()

        self.card5_name = self.track(
            Label(parent, text="Nachos - Beef ", font=("arial", 11, "bold"), bg="#153c7d",
                  fg="white"))
        self.card5_name.place(x=1615, y=675)

        self.card5_desc = self.track(Label(parent,
                                           text="Crispy corn chips topped \nwith hearty beef chilli\n con carne and melted cheese.",
                                           font=("arial", 9), bg="#153c7d", fg="white"))
        self.card5_desc.place(x=1585, y=698)

        self.price_label5 = self.track(
            Label(parent, text="$9.35", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label5.place(x=1575, y=765)

        self.add_btn5 = self.track(
            customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
                                    hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
                                    command=lambda: self.add_to_order("Nachos - Beef - LT", 9.35)))
        self.add_btn5.place(x=1670, y=762)

    def sides(self):
        self.clear_items()
        parent = root

        self.background = self.track(Label(parent, width=200, height=200, bg="#cc3628"))
        self.background.place(x=600, y=500)

        # --- Card 1 ---
        self.backblue = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23))
        self.backblue.place(x=350, y=500)

        self.lightblue = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23))
        self.lightblue.place(x=393, y=540)
        self.lightblue.lift()

        self.food_image = Image.open('download (15).png')
        self.food_image = self.food_image.resize((100, 100))
        self.food_image = ImageTk.PhotoImage(self.food_image)
        self.food_load = self.track(Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image))
        self.food_load.place(x=410, y=560)
        self.food_load.lift()

        self.pita_name = self.track(Label(parent, text="Pretzel - Sweet", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.pita_name.place(x=415, y=675)

        self.pita_desc = self.track(Label(parent, text="Pretzel coated in sweet\n glaze and dusted with \nwarm cinnamon sugar.",
            font=("arial", 9), bg="#153c7d", fg="white"))
        self.pita_desc.place(x=410, y=698)

        self.price_label = self.track(Label(parent, text="$5.50", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label.place(x=375, y=765)

        self.add_btn = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Pretzel - Sweet - LT", 5.50)))
        self.add_btn.place(x=470, y=762)

        # --- Card 2 ---

        self.backblue1 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23))
        self.backblue1.place(x=650, y=500)

        self.lightblue1 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23))
        self.lightblue1.place(x=693, y=540)
        self.lightblue1.lift()

        self.food_image1 = Image.open('download (16).png')
        self.food_image1 = self.food_image1.resize((100, 100))
        self.food_image1 = ImageTk.PhotoImage(self.food_image1)
        self.food_load1 = self.track(Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image1))
        self.food_load1.place(x=715, y=560)
        self.food_load1.lift()

        self.card2_name = self.track(Label(parent, text="Cheesy Garlic Pita", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card2_name.place(x=710, y=675)

        self.card2_desc = self.track(Label(parent, text="Pita brushed with garlic \nbutter and topped with melted \ngrated cheese.",
            font=("arial", 9), bg="#153c7d", fg="white"))
        self.card2_desc.place(x=685, y=698)

        self.price_label2 = self.track(Label(parent, text="$3.85", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label2.place(x=675, y=765)

        self.add_btn2 = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Cheesy Garlic Pita - LT", 3.85)))
        self.add_btn2.place(x=770, y=762)

        # --- Card 3 ---
        self.backblue2 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23))
        self.backblue2.place(x=950, y=500)

        self.lightblue2 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23))
        self.lightblue2.place(x=993, y=540)
        self.lightblue2.lift()

        self.food_image2 = Image.open('download (17).png')
        self.food_image2 = self.food_image2.resize((100, 100))
        self.food_image2 = ImageTk.PhotoImage(self.food_image2)
        self.food_load2 = self.track(Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image2))
        self.food_load2.place(x=1010, y=560)
        self.food_load2.lift()

        self.card3_name = self.track(Label(parent, text="Garlic Bread Regular", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card3_name.place(x=993, y=675)

        self.card3_desc = self.track(Label(parent, text="Fresh plain pita with shredded \nchicken,  fresh veggies, \ncheese, and creamy mayo.",
            font=("arial", 9), bg="#153c7d", fg="white"))
        self.card3_desc.place(x=990, y=698)

        self.price_label3 = self.track(Label(parent, text="$4.95", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label3.place(x=975, y=765)

        self.add_btn3 = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Garlic Bread Regular - LT", 4.95)))
        self.add_btn3.place(x=1070, y=762)

        # --- Card 4 ---
        self.backblue3 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23))
        self.backblue3.place(x=1250, y=500)

        self.lightblue3 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23))
        self.lightblue3.place(x=1293, y=540)
        self.lightblue3.lift()

        self.food_image3 = Image.open('download (18).png')
        self.food_image3 = self.food_image3.resize((100, 100))
        self.food_image3 = ImageTk.PhotoImage(self.food_image3)
        self.food_load3 = self.track(Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image3))
        self.food_load3.place(x=1310, y=560)
        self.food_load3.lift()

        self.card4_name = self.track(Label(parent, text="Wedges", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card4_name.place(x=1345, y=675)

        self.card4_desc = self.track(Label(parent, text="Warm potato wedges with \na golden, seasoned finish.",
            font=("arial", 9), bg="#153c7d", fg="white"))
        self.card4_desc.place(x=1300, y=698)

        self.price_label4 = self.track(Label(parent, text="$4.95", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label4.place(x=1275, y=765)

        self.add_btn4 = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Wedges - LT", 4.95)))
        self.add_btn4.place(x=1370, y=762)

        # --- Card 5 ---
        self.backblue4 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
            height=320, width=250, text="", fg_color="#153c7d", text_color="#ffffff", corner_radius=23))
        self.backblue4.place(x=1550, y=500)

        self.lightblue4 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
            text="", bg_color="#153c7d", fg_color="#416db6", text_color="#ffffff", corner_radius=23))
        self.lightblue4.place(x=1593, y=540)
        self.lightblue4.lift()

        self.food_image4 = Image.open('download (19).png')
        self.food_image4 = self.food_image4.resize((100, 100))
        self.food_image4 = ImageTk.PhotoImage(self.food_image4)
        self.food_load4 = self.track(Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image4))
        self.food_load4.place(x=1610, y=560)
        self.food_load4.lift()

        self.card5_name = self.track(Label(parent, text="Hashbrown ", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card5_name.place(x=1630, y=675)

        self.card5_desc = self.track(Label(parent, text="Golden hash brown with a\n crisp outside and soft, \nfluffy potato inside.",
            font=("arial", 9), bg="#153c7d", fg="white"))
        self.card5_desc.place(x=1600, y=698)

        self.price_label5 = self.track(Label(parent, text="$2.20", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label5.place(x=1575, y=765)

        self.add_btn5 = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Hashbrown", 2.20)))
        self.add_btn5.place(x=1670, y=762)

    def specials(self):
        self.clear_items()
        parent = root

        self.background = self.track(Label(parent, width=200, height=200, bg="#cc3628"))
        self.background.place(x=600, y=500)

        # --- Card 1 ---
        self.backblue = self.track(
            customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d", height=320, width=250, text="",
                                    fg_color="#153c7d", text_color="#ffffff", corner_radius=23))
        self.backblue.place(x=350, y=500)

        self.lightblue = self.track(
            customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160, text="", bg_color="#153c7d",
                                    fg_color="#416db6", text_color="#ffffff", corner_radius=23))
        self.lightblue.place(x=393, y=540)
        self.lightblue.lift()

        self.food_image = Image.open('download (5).png')
        self.food_image = self.food_image.resize((100, 100))
        self.food_image = ImageTk.PhotoImage(self.food_image)
        self.food_load = self.track(
            Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image))
        self.food_load.place(x=410, y=560)
        self.food_load.lift()

        self.pita_name = self.track(
            Label(parent, text="Premium Pie - Butter Chicken", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.pita_name.place(x=370, y=675)

        self.pita_desc = self.track(Label(parent,
                                          text="Flaky pastry filled \nwith tender chicken in \na creamy, spiced butter sauce.",
                                          font=("arial", 9), bg="#153c7d", fg="white"))
        self.pita_desc.place(x=393, y=698)

        self.price_label = self.track(Label(parent, text="$8.50", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label.place(x=375, y=765)

        self.add_btn = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
                                                          hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
                                                          command=lambda: self.add_to_order("Premium Pie - Butter Chicken", 8.50)))
        self.add_btn.place(x=470, y=762)

        # --- Card 2 ---

        self.backblue1 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
                                                            height=320, width=250, text="", fg_color="#153c7d",
                                                            text_color="#ffffff", corner_radius=23))
        self.backblue1.place(x=650, y=500)

        self.lightblue1 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
                                                             text="", bg_color="#153c7d", fg_color="#416db6",
                                                             text_color="#ffffff", corner_radius=23))
        self.lightblue1.place(x=693, y=540)
        self.lightblue1.lift()

        self.food_image1 = Image.open('download (6).png')
        self.food_image1 = self.food_image1.resize((100, 100))
        self.food_image1 = ImageTk.PhotoImage(self.food_image1)
        self.food_load1 = self.track(
            Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image1))
        self.food_load1.place(x=715, y=560)
        self.food_load1.lift()

        self.card2_name = self.track(
            Label(parent, text="Premium Pie - Mince&Cheese", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card2_name.place(x=670, y=675)

        self.card2_desc = self.track(
            Label(parent, text="Flaky pastry filled \nwith savoury beef mince\n and melted cheese.",
                  font=("arial", 9), bg="#153c7d", fg="white"))
        self.card2_desc.place(x=700, y=698)

        self.price_label2 = self.track(
            Label(parent, text="$8.50", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label2.place(x=675, y=765)

        self.add_btn2 = self.track(
            customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
                                    hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
                                    command=lambda: self.add_to_order("Premium Pie - Mince&Cheese", 8.50)))
        self.add_btn2.place(x=770, y=762)

        # --- Card 3 ---
        self.backblue2 = self.track(customtkinter.CTkButton(parent, bg_color="#cc3628", hover_color="#153c7d",
                                                            height=320, width=250, text="", fg_color="#153c7d",
                                                            text_color="#ffffff", corner_radius=23))
        self.backblue2.place(x=950, y=500)

        self.lightblue2 = self.track(customtkinter.CTkButton(parent, hover_color="#416db6", height=120, width=160,
                                                             text="", bg_color="#153c7d", fg_color="#416db6",
                                                             text_color="#ffffff", corner_radius=23))
        self.lightblue2.place(x=993, y=540)
        self.lightblue2.lift()

        self.food_image2 = Image.open('download (7).png')
        self.food_image2 = self.food_image2.resize((100, 100))
        self.food_image2 = ImageTk.PhotoImage(self.food_image2)
        self.food_load2 = self.track(
            Label(parent, borderwidth=0, border=0, height=80, width=120, bg="#416db6", image=self.food_image2))
        self.food_load2.place(x=1010, y=560)
        self.food_load2.lift()

        self.card3_name = self.track(Label(parent, text="Premium Pie - Steak&Cheese", font=("arial", 11, "bold"), bg="#153c7d", fg="white"))
        self.card3_name.place(x=975, y=675)

        self.card3_desc = self.track(Label(parent, text="Fresh plain pita with shredded \nchicken,  fresh veggies, \ncheese, and creamy mayo.",
            font=("arial", 9), bg="#153c7d", fg="white"))
        self.card3_desc.place(x=985, y=698)

        self.price_label3 = self.track(Label(parent, text="$8.50", font=("arial", 12, "bold"), bg="#153c7d", fg="white"))
        self.price_label3.place(x=975, y=765)

        self.add_btn3 = self.track(customtkinter.CTkButton(parent, text="Add +", width=80, height=28, fg_color="#cc3628",
            hover_color="#a02010", bg_color="#153c7d", corner_radius=10,
            command=lambda: self.add_to_order("Premium Pie - Steak&Cheese", 8.50)))
        self.add_btn3.place(x=1070, y=762)


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