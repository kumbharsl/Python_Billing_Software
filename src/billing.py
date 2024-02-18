import tkinter as tk
from tkinter import*
import random
import os
from tkinter import messagebox

class Bill_App:
    def __init__(self):
        self.root = tk.Tk()
        self.select_screen_width=self.root.winfo_screenwidth()
        self.select_screen_height=self.root.winfo_screenheight()
        self.root.geometry(f"{ self.select_screen_width}x{self.select_screen_height}")
        self.root.title("Billing Software")
        bg_color = "#213C0D"
        fg_colr="White"
        title = Label(self.root, text="Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#213C0D", fg="White")
        title.pack(fill=X)
    # ================variables=======================
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.syrup = IntVar()
        self.cream = IntVar()
        self.thermal_gun = IntVar()
    # ============grocery==============================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.spices = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        #=============coldDrinks=============================
        self.sprite = IntVar()
        self.mineral = IntVar()
        self.juice = IntVar()
        self.coke = IntVar()
        self.lassi = IntVar()
        self.mountain_duo = IntVar()
    # ==============Total product price================
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
    
        self.search_bill = IntVar()
    # ===============Tax================================
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('Rockwell', 15, 'bold'), fg="White", bg="#213C0D")
        F1.place(x=0, y=100, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('Rockwell', 15, 'bold'), fg="White")
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='Rockwell')
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg=bg_color, fg="White",font=('Rockwell', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='Rockwell 15')
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg=bg_color, font=('Rockwell', 15, 'bold'), fg="White")
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='Rockwell 15')
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10,  font=('Rockwell', 12, 'bold'))
        bil_btn.grid(row=0, column=10, pady=5, padx=10)

      
        # ===================Medical====================================
        F2 = LabelFrame(self.root, text="Medical Purpose", font=('Rockwell', 15, 'bold'),  fg=fg_colr, bg=bg_color)
        F2.place(x=10, y=210, width=325, height=380)

        sanitizer_lbl = Label(F2, text="Sanitizer", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font=('Rockwell', 16, 'bold'))
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F2, text="Mask", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mask_txt = Entry(F2, width=10, textvariable=self.mask, font=('Rockwell', 16, 'bold'))
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('Rockwell', 16, 'bold'), bg=bg_color, fg="White")
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font=('Rockwell', 16, 'bold'))
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

        syrup_lbl = Label(F2, text="Syrup", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        syrup_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        syrup_txt = Entry(F2, width=10, textvariable=self.syrup, font=('Rockwell', 16, 'bold'))
        syrup_txt.grid(row=3, column=1, padx=10, pady=10)

        cream_lbl = Label(F2, text="Cream", font=('Rockwell', 16, 'bold'), bg = bg_color, fg = fg_colr)
        cream_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        cream_txt = Entry(F2, width=10, textvariable=self.cream, font=('Rockwell', 16, 'bold'))
        cream_txt.grid(row=4, column=1, padx=10, pady=10)

        thermal_gun_lbl = Label(F2, text="Thermal Gun", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        thermal_gun_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        thermal_gun_txt = Entry(F2, width=10, textvariable=self.thermal_gun, font=('Rockwell', 16, 'bold'))
        thermal_gun_txt.grid(row=5, column=1, padx=10, pady=10)
        
          # ==========GroceryItems=========================
        F3 = LabelFrame(self.root, text="Grocery Items", font=('Rockwell', 15, 'bold'),  fg=fg_colr, bg=bg_color)
        F3.place(x=360, y=210, width=325, height=380)

        rice_lbl = Label(F3, text="Rice", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('Rockwell', 16, 'bold'))
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        food_oil_txt = Entry(F3, width=10, textvariable=self.food_oil, font=('Rockwell', 16, 'bold'))
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=('Rockwell', 16, 'bold'))
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        spices_lbl = Label(F3, text="Spices", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        spices_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        spices_txt = Entry(F3, width=10, textvariable=self.spices, font=('Rockwell', 16, 'bold'))
        spices_txt.grid(row=3, column=1, padx=10, pady=10)

        flour_lbl = Label(F3, text="Flour", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        flour_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        flour_txt = Entry(F3, width=10, textvariable=self.flour, font=('Rockwell', 16, 'bold'),relief=GROOVE)
        flour_txt.grid(row=4, column=1, padx=10, pady=10)

        maggi_lbl = Label(F3, text="Maggi", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        maggi_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        maggi_txt = Entry(F3, width=10, textvariable=self.maggi, font=('Rockwell', 16, 'bold'))
        maggi_txt.grid(row=5, column=1, padx=10, pady=10)

    # ===========ColdDrinks================================
        F4 = LabelFrame(self.root, text="Cold Drinks", font=('Rockwell', 15, 'bold'), fg=fg_colr, bg=bg_color)
        F4.place(x=710, y=210, width=325, height=380)

        sprite_lbl = Label(F4, text="Sprite", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sprite_txt = Entry(F4, width=10, textvariable=self.sprite, font=('Rockwell', 16, 'bold'))
        sprite_txt.grid(row=0, column=1, padx=10, pady=10)

        mineral_lbl = Label(F4, text="Mineral Water", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        mineral_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mineral_txt = Entry(F4, width=10, textvariable=self.mineral, font=('Rockwell', 16, 'bold'))
        mineral_txt.grid(row=1, column=1, padx=10, pady=10)

        juice_lbl = Label(F4, text="Juice", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        juice_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        juice_txt = Entry(F4, width=10, textvariable=self.juice, font=('Rockwell', 16, 'bold'))
        juice_txt.grid(row=2, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        coke_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        coke_txt = Entry(F4, width=10, textvariable=self.coke, font=('Rockwell', 16, 'bold'))
        coke_txt.grid(row=3, column=1, padx=10, pady=10)

        lassi_lbl = Label(F4, text="Lassi", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        lassi_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        lassi_txt = Entry(F4, width=10, textvariable=self.lassi, font=('Rockwell', 16, 'bold'))
        lassi_txt.grid(row=4, column=1, padx=10, pady=10)

        mountain_duo_lbl = Label(F4, text="Mountain Duo", font=('Rockwell', 16, 'bold'), bg=bg_color, fg=fg_colr)
        mountain_duo_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        mountain_duo_txt = Entry(F4, width=10, textvariable=self.mountain_duo, font=('Rockwell', 16, 'bold'))
        mountain_duo_txt.grid(row=5, column=1, padx=10, pady=10)

    # =================BillArea======================
        F5 = Frame(self.root)
        F5.place(x=1110, y=170, width=350, height=440)

        bill_title = Label(F5, text="Bill Area", font='Rockwell 20 bold')
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
        F6 = LabelFrame(self.root, text="Bill Area", font=('Rockwell', 14, 'bold'),  fg=fg_colr, bg=bg_color)
        F6.place(x=0, y=650, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Medical Price", font=('Rockwell', 14, 'bold'), bg=bg_color, fg=fg_colr)
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.medical_price, font='arial 10 bold')
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", font=('Rockwell', 14, 'bold'), bg=bg_color, fg=fg_colr)
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold')
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=('Rockwell', 14, 'bold'), bg=bg_color, fg=fg_colr)
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price, font='arial 10 bold')
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="Medical Tax", font=('Rockwell', 14, 'bold'), bg=bg_color, fg=fg_colr)
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.medical_tax, font='arial 10 bold')
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Grocery Tax", font=('Rockwell', 14, 'bold'), bg=bg_color, fg=fg_colr)
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold')
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Cold Drinks Tax", font=('Rockwell', 14, 'bold'), bg=bg_color, fg=fg_colr)
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='arial 10 bold')
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

    # =======Buttons-======================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=900, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg=bg_color,  fg=fg_colr, pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill",bg=bg_color, fg=fg_colr, pady=15, bd=5,width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg=bg_color, fg=fg_colr, pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bg=bg_color, fg=fg_colr, pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

        #==============execute mainloop===========
        self.root.mainloop()


    def total(self):
        self.m_h_g_p = self.hand_gloves.get()*20    
        self.m_s_p = self.sanitizer.get()*50        
        self.m_m_p = self.mask.get()*10
        self.m_s = self.syrup.get()*100
        self.m_c_p = self.cream.get()*150
        self.m_t_g_p = self.thermal_gun.get()*300
        self.total_medical_price = float(self.m_m_p+self.m_h_g_p+self.m_s+self.m_c_p+self.m_t_g_p+self.m_s_p)

        self.medical_price.set("Rs. "+str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price*0.018), 2)
        self.medical_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p = self.rice.get()*50
        self.g_f_o_p = self.food_oil.get()*100
        self.g_w_p = self.wheat.get()*40
        self.g_s_p = self.spices.get()*15
        self.g_f_p = self.flour.get()*50
        self.g_m_p = self.maggi.get()*14
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_s_p+self.g_f_p+self.g_m_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.018), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.sprite.get()*20
        self.c_d_w_p = self.mineral.get()*20
        self.c_d_j_p = self.juice.get()*10
        self.c_d_c_p = self.coke.get()*25
        self.c_d_l_p = self.lassi.get()*35
        self.c_m_d = self.mountain_duo.get()*20
        self.total_cold_drinks_price = float(self.c_d_s_p+self.c_d_w_p+self.c_d_j_p+self.c_d_c_p+self.c_d_l_p+self.c_m_d)

        self.cold_drinks_price.set("Rs. "+str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.018), 2)
        self.cold_drinks_tax.set("Rs. "+str(self.c_d_tax))

        self.total_bill = float(self.total_medical_price+self.total_grocery_price+self.total_cold_drinks_price+self.c_tax+self.g_tax+self.c_d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome Grocery Retail")
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number:{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
    # ============medical===========================
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}")
        if self.mask.get() != 0:
            self.txtarea.insert(END, f"\n Mask\t\t{self.mask.get()}\t\t{self.m_m_p}")
        if self.hand_gloves.get() != 0:
            self.txtarea.insert(END, f"\n Hand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
        if self.syrup.get() != 0:
            self.txtarea.insert(END, f"\n Syrup\t\t{self.syrup.get()}\t\t{self.m_s}")
        if self.cream.get() != 0:
            self.txtarea.insert(END, f"\n Cream\t\t{self.cream.get()}\t\t{self.m_c_p}")
        if self.thermal_gun.get() != 0:
            self.txtarea.insert(END, f"\n Thermal Gun\t\t{self.sanitizer.get()}\t\t{self.m_t_g_p}")
    # ==============Grocery============================
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
        if self.spices.get() != 0:
            self.txtarea.insert(END, f"\n Spices\t\t{self.spices.get()}\t\t{self.g_s_p}")
        if self.flour.get() != 0:
            self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
        if self.maggi.get() != 0:
            self.txtarea.insert(END, f"\n Maggi\t\t{self.maggi.get()}\t\t{self.g_m_p}")
        #================ColdDrinks==========================
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
        if self.mineral.get() != 0:
            self.txtarea.insert(END, f"\n Mineral\t\t{self.mineral.get()}\t\t{self.c_d_w_p}")
        if self.juice.get() != 0:
            self.txtarea.insert(END, f"\n Juice\t\t{self.juice.get()}\t\t{self.c_d_j_p}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
        if self.lassi.get() != 0:
            self.txtarea.insert(END, f"\n Lassi\t\t{self.cream.get()}\t\t{self.c_d_l_p}")
        if self.mountain_duo.get() != 0:
            self.txtarea.insert(END, f"\n Mountain Duo\t\t{self.sanitizer.get()}\t\t{self.c_m_d}")
            self.txtarea.insert(END, f"\n--------------------------------")
    # ===============taxes==============================
        if self.medical_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Medical Tax\t\t\t{self.medical_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bill:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)

            try:
                f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
                f1.write(self.bill_data)
            #     print("hel")
            except FileNotFoundError:
                print("file not found")
            
            # f1=open("G:/Python/Project/my_projects/bills/bills.txt", "a+")
            # f1.write(self.bill_data)
                
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    def find_bill(self):
        present = "no"

        for i in os.listdir("bills/"):
            f1=open(f"bills/{i}", "r+")


        # for i in os.listdir("bills/"):
        #     if i.split('.')[0] == self.search_bill.get():
        #         f1 = open(f"bills/{i}", "r+")
        #         self.txtarea.delete("1.0", END)
        #         for d in f1:
        #             self.txtarea.insert(END, d)
        #             f1.close()
        #         present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.sanitizer.set(50)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.syrup.set(0)
            self.cream.set(0)
            self.thermal_gun.set(0)
    # ============grocery==============================
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.spices.set(0)
            self.flour.set(0)
            self.maggi.set(0)
    # =============coldDrinks=============================
            self.sprite.set(0)
            self.mineral.set(0)
            self.juice.set(0)
            self.coke.set(0)
            self.lassi.set(0)
            self.mountain_duo.set(0)
    # ====================taxes================================
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")

            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            #  self.bill_no.set("")

            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


# root = Tk()
# obj = Bill_App()
# root.mainloop()


