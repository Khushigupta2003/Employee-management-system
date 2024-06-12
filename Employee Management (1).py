#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import Tk, Label, Frame
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


# In[ ]:


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Employee Management System')
        
        #variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        
        
        lb1_title = Label(self.root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman', 37, 'bold'), fg='darkblue', bg='white')
        lb1_title.place(x=0, y=0, width=1530, height=50)
        
        # logo
        img_logo = Image.open('sin1.png')
        img_logo = img_logo.resize((50, 50))  
        self.photo_logo = ImageTk.PhotoImage(img_logo)
        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.image = self.photo_logo  # Keep a reference to the image
        self.logo.place(x=270, y=0, width=50, height=50)
        
        # image frame
        img_frame = Frame(self.root, bd=2, relief='ridge', bg='white')
        img_frame.place(x=0, y=50, width=1530, height=170)
        
        # first image
        img1 = Image.open('new1.png')
        img1 = img1.resize((540, 160))  
        self.photo1 = ImageTk.PhotoImage(img1)
        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.image = self.photo1  # Keep a reference to the image
        self.img_1.place(x=0, y=0, width=540, height=160)
        
        # 2nd image
        img2 = Image.open('new3.png')
        img2 = img2.resize((540, 160))  
        self.photo2 = ImageTk.PhotoImage(img2)
        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.image = self.photo2  # Keep a reference to the image
        self.img_2.place(x=540, y=0, width=540, height=160)
        
        # 3rd image
        img3 = Image.open('new4.png')
        img3 = img3.resize((540, 160))  
        self.photo3 = ImageTk.PhotoImage(img3)
        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.image = self.photo3  # Keep a reference to the image
        self.img_3.place(x=1008, y=0, width=540, height=160)
        
        
        # Main Frame
        main_frame = Frame(self.root, bd=2, relief='ridge', bg='white')
        main_frame.place(x=10, y=230, width=1500, height=560)

        # Upper frame
        upper_frame = LabelFrame(main_frame, bd=2, relief='ridge', bg='white', text='Employee Information', font=('times new roman', 11, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1480, height=400)
        
        # Labels and Entry Fields
        # department
        lbl_dep = Label(upper_frame, text='Department:', font=('arial', 12, 'bold'), bg='white')
        lbl_dep.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        combo_dep = ttk.Combobox(upper_frame, font=('arial', 12, 'bold'), width=17, state='readonly', textvariable=self.var_dep)
        combo_dep['values'] = ('Select Department', 'HR', 'Software Engg', 'Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        
        
        #name
        # name
        lbl_name = Label(upper_frame, font=('arial', 12, 'bold'), text='Name:', bg='white')
        lbl_name.grid(row=0, column=2, padx=10, pady=10, sticky='e')
        txt_name = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'), textvariable=self.var_name)
        txt_name.grid(row=0, column=3, padx=10, pady=10, sticky='w')

        # designation
        lbl_designation = Label(upper_frame, font=('arial', 12, 'bold'), text='Designation:', bg='white')
        lbl_designation.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txt_designation = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'), textvariable=self.var_designation)
        txt_designation.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        # email
        lbl_email = Label(upper_frame, font=('arial', 12, 'bold'), text='Email:', bg='white')
        lbl_email.grid(row=1, column=2, padx=10, pady=10, sticky='e')
        txt_email = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'), textvariable=self.var_email)
        txt_email.grid(row=1, column=3, padx=10, pady=10, sticky='w')

        # address
        lbl_address = Label(upper_frame, font=('arial', 12, 'bold'), text='Address:', bg='white')
        lbl_address.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txt_address = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'), textvariable=self.var_address)
        txt_address.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        # married status
        lbl_married_status = Label(upper_frame, font=('arial', 12, 'bold'), text='Married Status:', bg='white')
        lbl_married_status.grid(row=2, column=2, padx=10, pady=10, sticky='e')
        com_married_status = ttk.Combobox(upper_frame, state='readonly', width=18, font=('arial', 12, 'bold'), textvariable=self.var_married)
        com_married_status['values'] = ('Married', 'Unmarried')
        com_married_status.current(0)
        com_married_status.grid(row=2, column=3, padx=10, pady=10, sticky='w')

        # dob
        lbl_dob = Label(upper_frame, font=('arial', 12, 'bold'), text='DOB:', bg='white')
        lbl_dob.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txt_dob = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'), textvariable=self.var_dob)
        txt_dob.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        # doj
        lbl_doj = Label(upper_frame, font=('arial', 12, 'bold'), text='DOJ:', bg='white')
        lbl_doj.grid(row=4, column=2, padx=10, pady=10, sticky='e')
        txt_doj = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'), textvariable=self.var_doj)
        txt_doj.grid(row=4, column=3, padx=10, pady=10, sticky='w')

        # id proof
        com_txt_proof = ttk.Combobox(upper_frame, state='readonly', font=('arial', 12, 'bold'), width=22, textvariable=self.var_idproofcomb)
        com_txt_proof['values'] = ('Select ID Proof', 'PAN Card', 'ADHAR Card', 'DRIVING LICENCE', 'OTHER')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4, column=0, sticky='w', padx=10, pady=7)
        txt_proof = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'), textvariable=self.var_idproof)
        txt_proof.grid(row=4, column=1, padx=10, pady=10)

        
        
        
        
        # gender
        lbl_gender = Label(upper_frame, font=('arial', 12, 'bold'), text='Gender:', bg='white')
        lbl_gender.grid(row=3, column=2, padx=10, pady=10, sticky='e')  # Aligning with DOJ

        combo_gender = ttk.Combobox(upper_frame, state='readonly', width=20, font=('arial', 11, 'bold'), textvariable=self.var_gender)
        combo_gender['values'] = ('Male', 'Female', 'Other')
        combo_gender.current(0)
        combo_gender.grid(row=3, column=3, padx=10, pady=10, sticky='w')  # Aligning with DOJ

        #$phone number
        lbl_phone = Label(upper_frame, font=('arial', 12, 'bold'), text='Phone No:', bg='white')
        lbl_phone.grid(row=0, column=4, padx=10, pady=10, sticky='w')
        txt_phone = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'), textvariable=self.var_phone)
        txt_phone.grid(row=0, column=5, padx=10, pady=10, sticky='w')

        # country
        lbl_country = Label(upper_frame, font=('arial', 12, 'bold'), text='Country:', bg='white')
        lbl_country.grid(row=1, column=4, padx=10, pady=10, sticky='w')
        txt_country = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'), textvariable=self.var_country)
        txt_country.grid(row=1, column=5, padx=10, pady=10, sticky='w')
        
        # salary
        lbl_salary = Label(upper_frame, font=('arial', 12, 'bold'), text='Salary (CTC):', bg='white')
        lbl_salary.grid(row=2, column=4, padx=10, pady=10, sticky='w')
        txt_salary = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'), textvariable=self.var_salary)
        txt_salary.grid(row=2, column=5, padx=10, pady=10, sticky='w')

        
        
        # Mask image
        img2_mask = Image.open('dualper.jpeg')
        img2_mask = img2_mask.resize((220, 220))
        self.photo2mask = ImageTk.PhotoImage(img2_mask)
        
        self.img2_mask = Label(upper_frame, image=self.photo2mask, bg='white')
        self.img2_mask.place(x=1080, y=0, width=220, height=220)
        
        
        
        # Button Frame
        button_frame = Frame(upper_frame, bd=2, relief='ridge', bg='white')
        button_frame.place(x=1290, y=10, width=170, height=210)
        
        
        
        # Add button
        btn_add = Button(button_frame, text='SAVE', command=self.add_data, font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=1, pady=5)
        
        btn_update = Button(button_frame, text='DELETE',command=self.delete_data,font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_update.grid(row=1, column=0, padx=1, pady=5)
        
        btn_delete = Button(button_frame, text='UPDATE',command=self.update_data ,font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_delete.grid(row=2, column=0, padx=1, pady=5)
        
        
        
        # Clear Button
        btn_clear = Button(button_frame, text='CLEAR',command=self.reset_data , font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_clear.grid(row=3, column=0, padx=1, pady=5)
        
        
        
        # Down Frame
        down_frame = LabelFrame(main_frame, bd=2, relief='ridge', bg='white', text='Employee Information Table', font=('times new roman', 11, 'bold'), fg='red')
        down_frame.place(x=10, y=280, width=1480, height=270)
        
        
        
        
        # Search_frame
        search_frame = LabelFrame(down_frame, bd=2, relief='ridge', bg='white', text='Search Employee Information', font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1470, height=65)
        
        search_by = Label(search_frame, font=('arial', 11, 'bold'), text='Search By:', fg='white', bg='red')
        search_by.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
        
        
        # Search
        self.var_com_search=StringVar()
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(search_frame, textvariable=self.var_com_search,state='readonly', width=22, font=('Arial', 11, 'bold'))
        com_txt_search['values'] = ('Search Option', 'Phone', 'ID Proof')
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, padx=2, pady=5, sticky='w')
        
        
        self.var_search = StringVar()
        txt_search = ttk.Entry(search_frame, textvariable=self.var_search, width=22, font=('Arial', 11, 'bold'))
        txt_search.grid(row=0, column=2, padx=5, pady=5, sticky='w')
        
        btn_search = Button(search_frame, text='Search',command=self.search_data, font=('Arial', 11, 'bold'), width=14, bg='blue', fg='white')
        btn_search.grid(row=0, column=3, padx=5, pady=5, sticky='w')
        
        btn_showall = Button(search_frame, text='Show all',command=self.fetch_data, font=('Arial', 11, 'bold'), width=14, bg='blue', fg='white')
        btn_showall.grid(row=0, column=4, padx=5, pady=5, sticky='w')
        
        
        
        # Text add
        mgmt = Label(search_frame, text='PEOPLE WORK IN SYSTEM, MANAGEMENT CREATE THE SYSTEM', font=('times new roman', 12, 'bold'), fg='darkblue', bg='white')
        mgmt.grid(row=0, column=5, padx=5, pady=5)
        
        
        
        # Adding image
        img_logo_mask = Image.open('em.png')
        img_logo_resized = img_logo_mask.resize((55,55))
        self.photoimg_logo_mask = ImageTk.PhotoImage(img_logo_resized)
        
        self.logo = Label(search_frame, image=self.photoimg_logo_mask)
        self.logo.grid(row=0, column=6, padx=5, pady=2)

        
        #===============EMPLOYEE TABLE================
        
                
        # Table Frame
        table_frame = Frame(down_frame, bd=4, relief='ridge')
        table_frame.place(x=0, y=66, width=1470, height=170)
        
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.empp_table=ttk.Treeview(table_frame,column=('dep','name','degi','email','address','married','dob','doj','idproofcombo','idproof','gender','phone','country','salary'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.empp_table.xview)
        scroll_y.config(command=self.empp_table.yview)
        
        self.empp_table.heading('dep',text='Department')
        self.empp_table.heading('name',text='Name')
        self.empp_table.heading('degi',text='Designation')
        self.empp_table.heading('email',text='Email')
        self.empp_table.heading('address',text='Address')
        self.empp_table.heading('married',text='Married Status')
        self.empp_table.heading('dob',text='DOB')
        self.empp_table.heading('doj',text='DOJ')
        self.empp_table.heading('idproofcombo',text='ID Proof Type')
        self.empp_table.heading('idproof',text='ID Proof')
        self.empp_table.heading('gender',text='Gender')
        self.empp_table.heading('phone',text='Phone')
        self.empp_table.heading('country',text='Country')
        self.empp_table.heading('salary',text='Salary')
        
        self.empp_table['show']='headings'
        
        self.empp_table.column('dep',width=100)
        self.empp_table.column('name',width=100)
        self.empp_table.column('degi',width=100)
        self.empp_table.column('email',width=100)
        self.empp_table.column('address',width=100)
        self.empp_table.column('married',width=100)
        self.empp_table.column('dob',width=100)
        self.empp_table.column('doj',width=100)
        self.empp_table.column('idproofcombo',width=100)
        self.empp_table.column('idproof',width=100)
        self.empp_table.column('gender',width=100)
        self.empp_table.column('phone',width=100)
        self.empp_table.column('country',width=100)
        self.empp_table.column('salary',width=100)
        
        self.empp_table.pack(fill=BOTH,expand=1)
        
        self.empp_table.bind('<ButtonRelease>',self.get_cursor)
        
        self.fetch_data()
        
        #========================FUNCTION DECLARATION===============================
    def add_data(self):
        if (self.var_dep.get() == "" or self.var_name.get() == "" or self.var_designation.get() == "" or
        self.var_email.get() == "" or self.var_address.get() == "" or self.var_married.get() == "" or
        self.var_dob.get() == "" or self.var_doj.get() == "" or self.var_idproofcomb.get() == "" or
        self.var_idproof.get() == "" or self.var_gender.get() == "" or self.var_phone.get() == "" or
        self.var_country.get() == "" or self.var_salary.get() == ""):
            messagebox.showerror('ERROR', 'All Fields are required!')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Khushijee@123', database='dbms')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into empp values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_designation.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_married.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_idproofcomb.get(),
                    self.var_idproof.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_country.get(),
                    self.var_salary.get()))

                conn.commit() 
                conn.close()
                messagebox.showinfo('Success', 'Employee has been added!', parent=self.root)
                self.fetch_data()
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)
        
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='Khushijee@123', database='dbms')
            my_cursor = conn.cursor()
            my_cursor.execute('SELECT * FROM empp')
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.empp_table.delete(*self.empp_table.get_children())  # Corrected the attribute name
                for i in data:
                    self.empp_table.insert('', END, values=i)  # Corrected the attribute name
                conn.commit()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
        finally:
            conn.close()


    #Get cursor
    def get_cursor(self,event=''):
        cursor_row=self.empp_table.focus()
        content=self.empp_table.item(cursor_row)
        data=content['values']
        
        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10]) # Corrected the variable name
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])
    
    def update_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
            messagebox.showerror('ERROR', 'All Fields are required!')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure to update this employee data?')
                if update:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Khushijee@123', database='dbms')
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE empp SET Departmet=%s, Name=%s, Designation=%s, Email=%s, Address=%s, `Married Status`=%s, DOB=%s, DOJ=%s, `ID Proof Type`=%s, Gender=%s, Phone=%s, Country=%s, Salary=%s WHERE `ID Proof`=%s",
                                      (
                                        self.var_dep.get(),
                                        self.var_name.get(),
                                        self.var_designation.get(),
                                        self.var_email.get(),
                                        self.var_address.get(),
                                        self.var_married.get(),
                                        self.var_dob.get(),
                                        self.var_doj.get(),
                                        self.var_idproofcomb.get(),
                                        self.var_gender.get(),
                                        self.var_phone.get(),
                                        self.var_country.get(),
                                        self.var_salary.get(),
                                        self.var_idproof.get()
                                    )
                                )

                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo('Success', 'Employee successfully updated', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)
    

                
                    
    #delete
    def delete_data(self):
        if self.var_idproof.get() == "":
            messagebox.showerror('Error', 'ID Proof is required')
        else:
            try:
                delete = messagebox.askyesno('Delete', 'Are you sure you want to delete this employee record?', parent=self.root)
                if delete:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Khushijee@123', database='dbms')
                    my_cursor = conn.cursor()
                    sql = 'DELETE FROM empp WHERE `ID Proof` = %s'  # Assuming 'id_proof' is the correct column name
                    value = (self.var_idproof.get(),)
                    print("SQL Query:", sql % value)  # Print the SQL query for debugging
                    my_cursor.execute(sql, value)
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    self.reset_data()
                    messagebox.showinfo('Delete', 'Employee record has been successfully deleted')
            except Exception as es:
                print(f"Error deleting data: {str(es)}")
                messagebox.showerror('Error', f'Due to {str(es)}')


                
    #reset
    def reset_data(self):
        self.var_dep.set('Select Department')
        self.var_name.set('')
        self.var_designation.set('')
        self.var_email.set('')
        self.var_address.set('')
        self.var_married.set('Married')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_idproofcomb.set('Select ID Proof')
        self.var_idproof.set('')
        self.var_gender.set('')  # Corrected the variable name
        self.var_phone.set('')
        self.var_country.set('')
        self.var_salary.set('')
                
    def search_data(self):
        if self.var_com_search.get() == '' or self.var_search.get() == '':
            messagebox.showerror('Error', 'ALL FIELDS ARE REQUIRED')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Khushijee@123', database='dbms')
                my_cursor = conn.cursor()
                if self.var_com_search.get() == 'Phone':
                    my_cursor.execute('SELECT * FROM empp WHERE Phone LIKE %s', (f'%{self.var_search.get()}%',))
                elif self.var_com_search.get() == 'ID Proof':
                    my_cursor.execute('SELECT * FROM empp WHERE `ID Proof` LIKE %s', (f'%{self.var_search.get()}%',))

                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.empp_table.delete(*self.empp_table.get_children())
                    for i in rows:
                        self.empp_table.insert('',END,values=i)
                    conn.commit()
                    conn.close()
            except Exception as es:
                messagebox.showerror('ERROR', f'Due to {str(es)}')
                

    
                    
                
                
                    

root = Tk()
obj = Employee(root)
root.mainloop()

        


# In[ ]:




