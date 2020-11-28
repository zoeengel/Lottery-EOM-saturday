# ZOE ENGEL, CLASS 1

from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Ithuba Lottery")
window.geometry("330x200")
window.config(bg="orange")

# HEADING LABEL
head_lbl = Label(window, text="Age verification", font=30,width=20)
head_lbl.pack(side=TOP, pady=10)

# AGE LABEL AND ENTRY
age_lbl = Label(window, text="Enter your age:" )
age_entry = Entry(window, width=10, justify="center")
age_lbl.place(x=10, y=80)
age_entry.place(x=130,y=80)

# AGE CHECKING FUNCTION
def ageCheck():
    try:
        age = int(age_entry.get())
        if age < 18:
             raise ValueError(messagebox.showinfo("ERROR","You need to be 18 years or older to play the lottery!"))
        elif type(age) != int:
            raise ValueError(messagebox.showerror("Enter a valid input"))

    # except ValueError as e:
    #     print(e)
    #     age_entry.delete(0, END)
    except ValueError:
        messagebox.showinfo("ERROR","Enter a valid input")
        window.destroy()
    else:
            messagebox.showinfo('Message',"Get ready to play the Lotto!")
            age_entry.delete(0, END)
            window.withdraw()
            import real
            real.real()
    return age

# SUBMIT BUTTON
HEIGHT = 1
WIDTH = 10
submit_btn = Button(window, text="Submit", width=WIDTH, height=HEIGHT, command=ageCheck)
submit_btn.config(bg="lime")
submit_btn.place(x=110,y=140)

window.mainloop()
