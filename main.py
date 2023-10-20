from random import*
from tkinter import*
from PIL import ImageTk , Image


# lists
letterList = [chr(s) for s in range(97 , 123)]
symbolList = ["!" , "'" , "+" , "#" , "$" , "%" , "&" , "/" , "{" , "}" , "}", "=" , "?" , "-" , " "]
numList = [1,2,3,4,5,6,7,8,9,0]
Pasword = list()
# values
globalLetterİnt = int()
globalSymbolİnt = int()
globalNumİnt = int()

# screen
root = Tk()
root.title("Welcome to pasword generator ")
root.minsize(width=500,height=700)
root.config(background="black")
# bg picture
image = Image.open("C:\download.png")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.place(x=120,y=350)

# information letter
letterLabel = Label(root)
letterLabel.config(text="How many letter would you like in your pasword?")
letterLabel.place(y=5, x=120)



# letter entry
letterEntry = Entry(root)
letterEntry.place(x=180 , y=40)

# symobol label
symbolLabel = Label(root)
symbolLabel.config(text="How many symbol would you like?")
symbolLabel.place(x=150 , y=70)

# symbol entry
symbolEntry = Entry(root)
symbolEntry.place(x=180 , y=100)

# number label
numLabel = Label(root)
numLabel.config(text="How many numbers would you like?")
numLabel.place(x=140 , y=135)

# number entry
numEntry = Entry(root)
numEntry.place(x=180 , y=170)

# error llabel
errorLabel = Label(root)
errorLabel.config(width=50 , height=3)

# functions
def letterFun():

    try:
        letterİnt = int(letterEntry.get())
        global globalLetterİnt
        globalLetterİnt += letterİnt
    except ValueError:
        errorLabel.config(tetx="ERROR please enter number")
        errorLabel.pack()


def symbolFun():
    try:
        symbolİnt = int(symbolEntry.get())
        global globalSymbolİnt
        globalSymbolİnt += symbolİnt
    except:

        errorLabel.config(tetx="ERROR please enter number")
        errorLabel.pack()
def numFun():
    try:
        numİnt = int(numEntry.get())
        global globalNumİnt
        globalNumİnt += numİnt

    except:
        errorLabel.config(tetx="ERROR please enter number")
        errorLabel.pack()


# generate pasword
def generatePasword():
    global Pasword
    for char in range(1 , globalLetterİnt +1):
        Pasword.append(choice(letterList))
    for char in range(1 , globalNumİnt +1):
        Pasword.append(choice(numList))
    for char in range(1 , globalSymbolİnt +1):
        Pasword.append(choice(symbolList))
    shuffle(Pasword)

# wiew the pasword user
resaults = Label(root)
def Resault():
    resaults.config(text="your pasword is generated!")
    resaults.place(x=160, y=200)

# wiew user the pasword
wiewUser = Label(root)
def wiewUserPasword():
    wiewUser.config(text=f"{Pasword}")
    wiewUser.place(y=230)

# button functions
def callEntryFunctions():
    letterFun()
    symbolFun()
    numFun()
    generatePasword()
    Resault()
    wiewUserPasword()

# apyly button
applyButton = Button(root , text="Submit" ,command= callEntryFunctions)
applyButton.place(x=170 , y=600)
applyButton.config(width=20 , height=2,bg="green")

root.mainloop()



