# Password Generator

# Import Everything from Tkinter module
from tkinter import *

# Import Messagebox from Tkinter module
import tkinter.messagebox as messagebox

# Import ImageTk from PIL
from PIL import ImageTk, Image

# Import Pyperclip to Copy Text
from pyperclip import copy as pycopy

# Import Random Module
import random

# Define Constant Macros
EASY, MEDIUM, HARD = "easy", "medium", "hard"
diff_l = [EASY, MEDIUM, HARD]

# Define Some Global Parameters for Password Generation
global length, difficulty, chars

length: int = int()
difficulty: str = str()
chars: list = list()

root = Tk()
root.title("Password Generator")
root.iconbitmap("img/icon.ico")
root.resizable(False, False)

# Copy Text
def copy(): pycopy(pass_entry.get())

# Generate Password


def generate():
    # Access global Variables
    global length, difficulty, chars

    # Ask To Confirm the Details
    confirmation = messagebox.askyesno(
        "Confirmation", "Are you sure you want to confirm the details?")

    if (confirmation):
        # Get All Values
        length = int(length_slider.get())
        difficulty = diff_l[diff.get()]
        chars = [u_leters.get(), nos.get(), special_chars.get()]

        lower_case_letters = [chr(i) for i in range(97, 123)]
        upper_case_letters = [chr(i) for i in range(65, 91)]
        numbers = [chr(i) for i in range(48, 57)]
        special_characters = [chr(i) for i in range(33, 43)]

        if (difficulty == EASY):
            # 1. None Selected
            if chars == [0, 0, 0]:
                # 100% Letters -> All Lowercase
                pwd = random.sample(lower_case_letters, length)

            # 2. Only Last
            elif chars == [0, 0, 1]:
                # 80% Letters -> All Lowercase
                # 20% Special Characters
                num_letters = int(0.8 * length)
                num_special_chars = length - num_letters

                x = random.sample(lower_case_letters, num_letters)
                y = random.sample(special_characters, num_special_chars)

                pwd = x + y
                random.shuffle(pwd)
                print("".join(pwd))

            # 3. Only Middle 0
            elif (chars == [0,1,0]):
                # 80% Letters -> All Lower
                # 20% Numbers
                num_letters = int(0.8 * length)
                num_nos = length - num_letters

                x = random.sample(lower_case_letters, num_letters)
                y = random.sample(numbers, num_nos)

                pwd = x + y
                random.shuffle(pwd)
                print("".join(pwd))

            # 4. Only Last 2
            elif (chars == [0,1,1]):
                # 60% Letters -> All Lower
                # 20% Numbers
                # 20% Special Characters
                num_letters = int(0.6 * length)
                num_nos = int(0.2 * length)
                num_special_chars = length - (num_nos + num_letters)

                x = random.sample(lower_case_letters, num_letters)
                y = random.sample(numbers, num_nos)
                z = random.sample(special_characters,num_special_chars)

                pwd = x + y + z
                random.shuffle(pwd)
                print("".join(pwd))

            # 5. Only First
            elif (chars == [1,0,0]):
                # 100% Letters -> 50% Lower and 50% Upper
                num_u_letters = int(0.5 * length)
                num_l_letters = length - num_u_letters

                x = random.sample(lower_case_letters, num_u_letters)
                y = random.sample(upper_case_letters, num_l_letters)

                pwd = x + y
                random.shuffle(pwd)
                print("".join(pwd))
            
            # 6. 1st and Last
            elif (chars == [1,0,1]):
                # 80% Letters -> 40% Upper and 40% Lower
                # 20% Special Characters
                num_u_letters = int(0.4 * length)
                num_l_letters = int(0.4 * length)
                num_sp = length - (num_u_letters + num_l_letters)

                x = random.sample(lower_case_letters, num_u_letters)
                y = random.sample(upper_case_letters, num_l_letters)
                z = random.sample(special_characters, num_sp)

                pwd = x + y + z
                random.shuffle(pwd)
                print("".join(pwd))
            
            # 7. First 2
            elif (chars == [1,1,0]):
                # 80% Letters -> 40% Upper and 40% Lower
                # 20% Numbers
                num_u_letters = int(0.4 * length)
                num_l_letters = int(0.4 * length)
                num_nos = length - (num_u_letters + num_l_letters)

                x = random.sample(lower_case_letters, num_u_letters)
                y = random.sample(upper_case_letters, num_l_letters)
                z = random.sample(numbers, num_nos)

                pwd = x + y + z
                random.shuffle(pwd)
                print("".join(pwd))

            # 8. All Options
            elif (chars == [1,1,1]):
                # 60% Letters -> 30% Upper and 30% Lower
                # 20% Numbers
                # 20% Special Characters
                num_u_letters = int(0.3 * length)
                num_l_letters = int(0.3 * length)
                num_nos = int(0.2 * length)
                num_sp = length - (num_u_letters + num_l_letters + num_nos)

                x = random.sample(lower_case_letters, num_u_letters)
                y = random.sample(upper_case_letters, num_l_letters)
                z = random.sample(numbers, num_nos)
                a = random.sample(special_characters, num_sp)

                pwd = x + y + z + a
                random.shuffle(pwd)
                print("".join(pwd))

        elif (difficulty == MEDIUM):
            # 1. None Selected
            if chars == [0, 0, 0]:
                # 100% Letters -> All Lowercase
                pwd = random.sample(lower_case_letters, length)

            # 2. Only Last
            elif chars == [0, 0, 1]:
                # 60% Letters -> All Lowercase
                # 40% Special Characters
                num_letters = int(0.6 * length)
                num_special_chars = length - num_letters

                x = random.sample(lower_case_letters, num_letters)
                y = random.sample(special_characters, num_special_chars)

                pwd = x + y
                random.shuffle(pwd)
                print("".join(pwd))

            # 3. Only Middle 0
            elif (chars == [0,1,0]):
                # 60% Letters -> All Lower
                # 40% Numbers
                num_letters = int(0.6 * length)
                num_nos = length - num_letters

                x = random.sample(lower_case_letters, num_letters)
                y = random.sample(numbers, num_nos)

                pwd = x + y
                random.shuffle(pwd)
                print("".join(pwd))

            # 4. Only Last 2
            elif (chars == [0,1,1]):
                # 40% Letters -> All Lower
                # 30% Numbers
                # 30% Special Characters
                num_letters = int(0.4 * length)
                num_nos = int(0.3 * length)
                num_special_chars = length - (num_nos + num_letters)

                x = random.sample(lower_case_letters, num_letters)
                y = random.sample(numbers, num_nos)
                z = random.sample(special_characters,num_special_chars)

                pwd = x + y + z
                random.shuffle(pwd)
                print("".join(pwd))

            # 5. Only First
            elif (chars == [1,0,0]):
                # 100% Letters -> 40% Lower and 60% Upper
                num_u_letters = int(0.6 * length)
                num_l_letters = length - num_u_letters

                x = random.sample(lower_case_letters, num_u_letters)
                y = random.sample(upper_case_letters, num_l_letters)

                pwd = x + y
                random.shuffle(pwd)
                print("".join(pwd))
            
            # 6. 1st and Last
            elif (chars == [1,0,1]):
                # 60% Letters -> 40% Upper and 20% Lower
                # 40% Special Characters
                num_u_letters = int(0.4 * length)
                num_l_letters = int(0.2 * length)
                num_sp = length - (num_u_letters + num_l_letters)

                x = random.sample(lower_case_letters, num_u_letters)
                y = random.sample(upper_case_letters, num_l_letters)
                z = random.sample(special_characters, num_sp)

                pwd = x + y + z
                random.shuffle(pwd)
                print("".join(pwd))
            
            # 7. First 2
            elif (chars == [1,1,0]):
                # 60% Letters -> 40% Upper and 20% Lower
                # 40% Numbers
                num_u_letters = int(0.4 * length)
                num_l_letters = int(0.2 * length)
                num_nos = length - (num_u_letters + num_l_letters)

                x = random.sample(lower_case_letters, num_u_letters)
                y = random.sample(upper_case_letters, num_l_letters)
                z = random.sample(numbers, num_nos)

                pwd = x + y + z
                random.shuffle(pwd)
                print("".join(pwd))

            # 8. All Options
            elif (chars == [1,1,1]):
                # 50% Letters -> 30% Upper and 20% Lower
                # 30% Numbers
                # 20% Special Characters
                num_u_letters = int(0.3 * length)
                num_l_letters = int(0.2 * length)
                num_nos = int(0.3 * length)
                num_sp = length - (num_u_letters + num_l_letters + num_nos)

                x = random.sample(lower_case_letters, num_u_letters)
                y = random.sample(upper_case_letters, num_l_letters)
                z = random.sample(numbers, num_nos)
                a = random.sample(special_characters, num_sp)

                pwd = x + y + z + a
                random.shuffle(pwd)
                print("".join(pwd))

        elif (difficulty == HARD):
            # 1. None Selected
            if chars == [0, 0, 0]:
                # 100% Letters -> All Lowercase
                pwd = random.sample(lower_case_letters, length)

            # 2. Only Last
            elif chars == [0, 0, 1]:
                # 50% Letters -> All Lowercase
                # 50% Special Characters
                num_letters = int(0.5 * length)
                num_special_chars = length - num_letters

                x = random.sample(lower_case_letters, num_letters)
                y = random.sample(special_characters, num_special_chars)

                pwd = x + y
                random.shuffle(pwd)
                print("".join(pwd))

            # 3. Only Middle 0
            elif (chars == [0,1,0]):
                # 50% Letters -> All Lower
                # 50% Numbers
                num_letters = int(0.5 * length)
                num_nos = length - num_letters

                x = random.sample(lower_case_letters, num_letters)
                y = random.sample(numbers, num_nos)

                pwd = x + y
                random.shuffle(pwd)
                print("".join(pwd))

            # 4. Only Last 2
            elif (chars == [0,1,1]):
                # 30% Letters -> All Lower
                # 30% Numbers
                # 40% Special Characters
                num_letters = int(0.3 * length)
                num_nos = int(0.3 * length)
                num_special_chars = length - (num_nos + num_letters)

                x = random.sample(lower_case_letters, num_letters)
                y = random.sample(numbers, num_nos)
                z = random.sample(special_characters,num_special_chars)

                pwd = x + y + z
                random.shuffle(pwd)
                print("".join(pwd))

            # 5. Only First
            elif (chars == [1,0,0]):
                # 100% Letters -> 20% Lower and 80% Upper
                num_u_letters = int(0.8 * length)
                num_l_letters = length - num_u_letters

                x = random.sample(lower_case_letters, num_u_letters)
                y = random.sample(upper_case_letters, num_l_letters)

                pwd = x + y
                random.shuffle(pwd)
                print("".join(pwd))
            
            # 6. 1st and Last
            elif (chars == [1,0,1]):
                # 50% Letters -> 30% Upper and 20% Lower
                # 50% Special Characters
                num_u_letters = int(0.3 * length)
                num_l_letters = int(0.2 * length)
                num_sp = length - (num_u_letters + num_l_letters)

                x = random.sample(lower_case_letters, num_u_letters)
                y = random.sample(upper_case_letters, num_l_letters)
                z = random.sample(special_characters, num_sp)

                pwd = x + y + z
                random.shuffle(pwd)
                print("".join(pwd))
            
            # 7. First 2
            elif (chars == [1,1,0]):
                # 50% Letters -> 30% Upper and 20% Lower
                # 40% Numbers
                num_u_letters = int(0.3 * length)
                num_l_letters = int(0.2 * length)
                num_nos = length - (num_u_letters + num_l_letters)

                x = random.sample(lower_case_letters, num_u_letters)
                y = random.sample(upper_case_letters, num_l_letters)
                z = random.sample(numbers, num_nos)

                pwd = x + y + z
                random.shuffle(pwd)
                print("".join(pwd))

            # 8. All Options
            elif (chars == [1,1,1]):
                # 30% Letters -> 20% Upper and 10% Lower
                # 30% Numbers
                # 40% Special Characters
                num_u_letters = int(0.2 * length)
                num_l_letters = int(0.1 * length)
                num_nos = int(0.3 * length)
                num_sp = length - (num_u_letters + num_l_letters + num_nos)

                x = random.sample(lower_case_letters, num_u_letters)
                y = random.sample(upper_case_letters, num_l_letters)
                z = random.sample(numbers, num_nos)
                a = random.sample(special_characters, num_sp)

                pwd = x + y + z + a
                random.shuffle(pwd)
                print("".join(pwd))
        
        else:
            print("Some Error Occured!")

        # Insert The Password in the Entry
        pass_entry["state"] = NORMAL

        pass_entry.delete(0,END)
        pass_entry.insert(0,"".join(pwd))

        pass_entry["state"] = DISABLED

# Center The Window
window_width = 550  # Set the width of the window
window_height = 420  # Set the height of the window

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2) - 50

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a Heading
heading = Label(root,text="Password Generator",font=("Pacifico",20))
heading.pack()

# Create a Form Frame to get neccesary details
form_frame = LabelFrame(root,text="Fill In The Following Details",font=("Calibri",15))
form_frame.pack()

# Add the Feilds in the Form

# 1. Length of the Password

# Create a Length Frame
length_frame = Frame(form_frame)
length_frame.pack()

# Create Label
length_label = Label(length_frame,text="1. Length",font=("Calibri",12))
length_label.grid(row=0,column=0,padx=10)

# Create Slider
length_slider = Scale(length_frame,from_=5,to=25,orient=HORIZONTAL,length=200)
length_slider.grid(row=0,column=1,padx=10)

# 2. Difficulty of the Password

# Create a Difficulty Frame
diff_frame = Frame(form_frame)
diff_frame.pack()

# Create Label
diff_label = Label(diff_frame,text="2. Difficulty",font=("Calibri",12))
diff_label.grid(row=0,column=0,padx=10,pady=20)

# Create 3 Radio Buttons
diff = IntVar(value=1)

diff_radio_1 = Radiobutton(diff_frame,text="Easy",variable=diff,value=0,font=("Calibri",11))
diff_radio_1.grid(row=0,column=1)

diff_radio_2 = Radiobutton(diff_frame,text="Medium",variable=diff,value=1,font=("Calibri",11))
diff_radio_2.grid(row=0,column=2)

diff_radio_3 = Radiobutton(diff_frame,text="Hard",variable=diff,value=2,font=("Calibri",11))
diff_radio_3.grid(row=0,column=3,pady=20)

# 3. Characters to be used In the Password

# Create a Characters Frame
char_frame = Frame(form_frame)
char_frame.pack()

# Create Label
char_label = Label(char_frame,text="3. Characters",font=("Calibri",12))
char_label.grid(row=0,column=0,padx=10)

# Create 3 checkboxes
char_checkbox_1 = Checkbutton(char_frame,text="Lowercase Letters",font=("Calibri",11),state=DISABLED)
char_checkbox_1.toggle()
char_checkbox_1.grid(row=0,column=1)

u_leters = IntVar()
char_checkbox_2 = Checkbutton(char_frame,text="Uppercase Letters",variable=u_leters,font=("Calibri",11))
char_checkbox_2.grid(row=0,column=2)

nos = IntVar()
char_checkbox_3 = Checkbutton(char_frame,text="Numbers",variable=nos,font=("Calibri",11))
char_checkbox_3.grid(row=0,column=3)

special_chars = IntVar()
char_checkbox_4 = Checkbutton(char_frame,text="Special Characters",variable=special_chars,font=("Calibri",11))
char_checkbox_4.grid(row=1,column=1)

# Button Frame
btn_frame = Frame(root)
btn_frame.pack(pady=20)

gen_btn = Button(btn_frame,text="Generate!",font=("Calibri",15),command=generate)
gen_btn.pack()

# Password Result Label Frame
pass_frame = LabelFrame(root,text="Generated Password",font=("Calibri",15))
pass_frame.pack()

# Password Label
pass_label = Label(pass_frame,text="Password: ",font=("Calibri",12))
pass_label.grid(row=0,column=0,padx=5,pady=5)

pass_entry = Entry(pass_frame,font=("Calibri",12),width=20)
pass_entry.insert(0,f"{' ' * 18}N.A")
pass_entry["state"] = DISABLED
pass_entry.grid(row=0,column=1,padx=5,pady=5)

img = ImageTk.PhotoImage(Image.open("img/copy.png"))
pass_copy_icon = Button(pass_frame,image=img,command=copy)
pass_copy_icon.grid(row=0,column=2,padx=5,pady=5)

root.mainloop()