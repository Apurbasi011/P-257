from tkinter import *
from web3 import Web3
from PIL import ImageTk, Image

root = Tk()
root.title("Account Details")

ganache_url = 'http://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

img = ImageTk.PhotoImage(Image.open("image.png"))
panel = Label(root, image=img, bg='white')
panel.pack(side="top")

frame = Frame(
    root,
    bg='white',
    padx=5,
    pady=5
)
# create the labels to hold the account numbers
Label(frame, text =  "Account Number 1 : ", fg = "purple", bg = "pink").grid(row = 0, column = 0, sticky = W, pady = 10)

Label(frame, text =  "Account Number 2 : ", fg = "purple", bg = "pink").grid(row = 1, column = 0, sticky = W, pady = 10)

Label(frame, text =  "Account Number 3 : ", fg = "purple", bg = "pink").grid(row = 2, column = 0, sticky = W, pady = 10)

Label(frame, text =  "Account Number 4 : ", fg = "purple", bg = "pink").grid(row = 3, column = 0, sticky = W, pady = 10)

Label(frame, text =  "Account Number 5 : ", fg = "purple", bg = "pink").grid(row = 4, column = 0, sticky = W, pady = 10)



#Create entry elements to get the use input for account addresses 

account1 = Entry(frame).grid(row = 0, column = 1, padx = 20, pady = 20)
account2 = Entry(frame).grid(row = 1, column = 1, padx = 20, pady = 20)
account3 = Entry(frame).grid(row = 2, column = 1, padx = 20, pady = 20 )
account4 = Entry(frame).grid(row = 3, column = 1, padx = 20, pady = 20)
account5 = Entry(frame).grid(row = 4, column = 1, padx = 20, pady = 20)

result = Text(root, height = 10, width = 45, bg = "white")
#place the entry elements on the root window






#create the text box


#define a function CHECK_BALANCE() and add the code inside it.

def CHECK_BALANCE():
    account_no = []
    account_no.append(account1.get())
    account_no.append(account2.get())
    account_no.append(account3.get())
    account_no.append(account4.get())
    account_no.append(account5.get())
    
    count = 1

    for i in account_no : 
        balance = web3.eth.get_balance(i)
        balance = balance * 0.000000000000000001
        result.insert(END, f'Account{count} balance is {balance}\n ')
        count = count + 1


frame.pack()

#Create a button element to call the CHECK_BALANCE()
btn = Button(root, width = 15, text = "Check Balance", command = CHECK_BALANCE, highlightbackground = "white")
btn.pack(fill = 'both')
    

result.pack(pady=5)
root.mainloop()

