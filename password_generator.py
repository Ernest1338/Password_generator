from tkinter import *
import random
characters=""
passwo=""
def gen():
    global characters
    global passwo
    characters=int(many.get())
    if characters<1 or characters>100:
        password.delete('1.0', END)
        password.insert(END, "ERROR - Invalid number of characters.")
    elif characters>0 and characters<101:
        password.delete('1.0', END)
        charact = ["q","Q","w","W","e","E","r","R","t","T","y","Y","u","U","i","I","o","O","p","P","a","A","s","S","d","D","f","F","g","G","h","H","j","J","k","K","l","L","z","Z","x","X","c","C","v","V","b","B","n","N","m","M","1","2","3","4","5","6","7","8","9","0"]
        i=int(characters)
        while i>=1:
            i=i-1
            passw = charact[random.randint(0,61)]
            passwo = passwo + str(passw)
        password.insert(END, passwo)
        passwo=""

# Main Window
root=Tk()
root.title("Random Password Generator")
root.minsize(500,300)
root.maxsize(500,300)

# Layout
how_many=Label(root, text="how many characters you want your password to have (1-100): ")
how_many.grid(row=0, column=0)
how_many.config(font=("courier", 10))
many=Entry(root)
many.grid(row=1, column=0, padx=10)
space=Label(root)
space.grid(row=2)
generate=Button(root, text="Generate", width=15, height=3, bg="lightgrey", command=gen)
generate.grid(row=3, column=0, padx=10)
password=Text(root, width=40, height=10)
password.grid(row=4)
root.mainloop()