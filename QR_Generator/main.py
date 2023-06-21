from tkinter import *
from tkinter import Tk

import qrcode
from PIL import ImageTk
from resizeimage import resizeimage


class QR_Generator:


    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR_GENERATOR | Developed by Prabhleen")
        self.root.resizable(False, False)

        Label(self.root, text="  QR_Generator", font=("Times", 40), bg='#8a582d', fg='white', anchor='w').place(x=0,
                                                                                                                y=0,
                                                                                                                relwidth=1)

        # ===Employee details window====
        # ==variables==
        self.var_emp_code = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_dept = StringVar()
        self.var_emp_post = StringVar()

        emp_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        emp_Frame.place(x=50, y=100, width=500, height=380)

        emp_title = Label(emp_Frame, text="Employee Details", font=("goudy old style", 20), bg='#e6b86e',fg='white').place(x=0, y=0, relwidth=1)

        lbl_emp = Label(emp_Frame, text="Employee ID", font=("times new roman", 15, 'bold'), bg='#fff').place(x=20, y=60)
        lbl_name = Label(emp_Frame, text="Name", font=("times new roman", 15, 'bold'), bg='#fff').place(
            x=20, y=100)
        lbl_dept = Label(emp_Frame, text="Department", font=("times new roman", 15, 'bold'), bg='#fff').place(
            x=20, y=140)
        lbl_post = Label(emp_Frame, text="Designation", font=("times new roman", 15, 'bold'), bg='#fff').place(
            x=20, y=180)

        txt_emp = Entry(emp_Frame, font=("times new roman", 15), textvariable=self.var_emp_code, bg='#faf9dc').place(
            x=200, y=60)
        txt_name = Entry(emp_Frame, font=("times new roman", 15), textvariable=self.var_emp_name, bg='#faf9dc').place(
            x=200, y=100)
        txt_dept = Entry(emp_Frame, font=("times new roman", 15), textvariable=self.var_emp_dept, bg='#faf9dc').place(
            x=200, y=140)
        txt_post = Entry(emp_Frame, font=("times new roman", 15), textvariable=self.var_emp_post, bg='#faf9dc').place(
            x=200, y=180)

        btn_generate = Button(emp_Frame, text='Generate QR', command=self.generate,
                              font=("times new roman", 18, 'bold'), bg='#e35c30', fg='white').place(x=90, y=250,
                                                                                                    width=180,
                                                                                                    height=30)

        btn_clear = Button(emp_Frame, text='Clear', command=self.clear, font=("times new roman", 18, 'bold'),
                           bg='#f26f44', fg='white').place(x=280, y=250, width=120, height=30)

        self.msg = ''
        self.lbl_msg = Label(emp_Frame, text=self.msg, font=("times new roman", 20), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=320, relwidth=1)

        # ===Employee QR code window====

        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=600, y=100, width=250, height=380)

        emp_title = Label(qr_Frame, text="Employee QR Code", font=("goudy old style", 20), bg='#e6b86e',
                          fg='white').place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_Frame, text='No QR \nAvailable', font=("times new roman", 15), bg='#d16a47', fg='white',
                             bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):
        self.var_emp_code.set('')
        self.var_emp_name.set('')
        self.var_emp_dept.set('')
        self.var_emp_post.set('')

        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_emp_post.get() == '' or self.var_emp_code.get() == '' or self.var_emp_dept.get() == '' or self.var_emp_name.get() == '':
            self.msg = 'All Fields are required! :('
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            qr_data = (f"Employee ID: {self.var_emp_code.get()}\nName:{self.var_emp_name.get()}\nDepartment:{self.var_emp_dept.get()}\nDesignation:{self.var_emp_post.get()}")
            qr_code = qrcode.make(qr_data)
            print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save('Employee_QR' + str(self.var_emp_code.get()) + '.png')

            # ===QR Code image update===
            self.im=ImageTk.PhotoImage(file="Employee_QR" + str(self.var_emp_code.get()) + '.png')
            self.qr_code.config(image=self.im)

            # ====updating notifications====
            self.msg = 'Qr Generator Successfully! :)'
            self.lbl_msg.config(text=self.msg, fg='green')


root: Tk = Tk()
obj = QR_Generator(root)
root.mainloop()
