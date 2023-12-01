import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk

# Product List
product_list = [
    {"id": 1, "name": "CoffeeS", "price": 2.00, "quantity": 2},
    {"id": 2, "name": "CoffeeM", "price": 4.00, "quantity": 100},
    {"id": 3, "name": "CoffeeL", "price": 6.00, "quantity": 100},
    {"id": 4, "name": "Tea", "price": 3.00, "quantity": 50},
    {"id": 5, "name": "Muffin", "price": 4.00, "quantity": 15},
    {"id": 6, "name": "Water", "price": 1.00, "quantity": 45},
    {"id": 7, "name": "Toast", "price": 2.00, "quantity": 50},
    {"id": 8, "name": "Breakfast Sandwich", "price": 7.00, "quantity": 25},
    {"id": 9, "name": "Oatmeal", "price": 3.00, "quantity": 10},
    {"id": 10, "name": "1lb Coffee beans", "price": 20.00, "quantity": 36},
    {"id": 11, "name": "Donut", "price": 1.00, "quantity": 50},
    {"id": 12, "name": "Bagel", "price": 2.00, "quantity": 50}
]
userList = ['John']
passList = ['123']
order = []
user = "0"

class MainGUI():
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.title('POS System')
        self.show_login()

    def show_login(self):
        # Login Frame
        self.loginFrame = tk.Frame(self.mainWindow)
        self.loginFrame.pack()

        # Username UI
        username_label = ttk.Label(self.loginFrame, text="User:")
        username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = ttk.Entry(self.loginFrame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password UI
        password_label = ttk.Label(self.loginFrame, text="Password:")
        password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = ttk.Entry(self.loginFrame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login Button
        login_button = ttk.Button(self.loginFrame, text="Login", command=self.login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        # Get input from user fields
        username = str(self.username_entry.get())
        password = str(self.password_entry.get())
        
        # Check if boxes contain any information before proceeding
        if len(username) < 1:
            messagebox.showinfo(title="Error", message="A username must be entered")
            return
        if len(password) < 1:
            messagebox.showinfo(title="Error", message="A password must be entered")
            return
        if username in userList:
            passIndex = userList.index(username)
            if passList[passIndex] == password:
                # messagebox.showinfo(title="Login Success", message="You logged in.") Removed for convenience
                self.loginFrame.pack_forget()
                #self.loginFrame.destroy()
                self.initialize_POS()
            else:
                messagebox.showinfo(title="Error", message="Invalid password")
        else:
            messagebox.showinfo(title="Error", message="User does not exist")
        

    def initialize_POS(self):
        self.orderID = 1
        
        # Frames
        self.frameLeft = tk.Frame(self.mainWindow).pack(side='left')
        self.frameRight = tk.Frame(self.mainWindow).pack(side='right')
        
        self.frameHeader = tk.Frame(self.frameLeft)
        self.frameRow1 = tk.Frame(self.frameLeft)
        self.frameRow2 = tk.Frame(self.frameLeft)
        self.frameSide = tk.Frame(self.frameRight, width=400)
        self.frameHeader.pack()
        self.frameRow1.pack()
        self.frameRow2.pack()
        self.frameSide.pack()
        
        # Import images
        self.imageCoffee = PhotoImage(file = r"imagesPOS\coffee.png")
        self.imageCoffeeS = PhotoImage(file = r"imagesPOS\coffeeS.png")
        self.imageCoffeeM = PhotoImage(file = r"imagesPOS\coffeeM.png")
        self.imageCoffeeL = PhotoImage(file = r"imagesPOS\coffeeL.png")
        self.imageToast = PhotoImage(file = r"imagesPOS\toast.png")
        self.imageMuffin = PhotoImage(file = r"imagesPOS\muffin.png")
        self.imageDonut = PhotoImage(file = r"imagesPOS\donut.png")
        self.imageTea = PhotoImage(file = r"imagesPOS\tea.png")
        self.imageSandwich = PhotoImage(file = r"imagesPOS\sandwich.png")
        self.imageOatmeal = PhotoImage(file = r"imagesPOS\oatmeal.png")
        self.imageBeans = PhotoImage(file = r"imagesPOS\bean.png")
        self.imageBagel = PhotoImage(file = r"imagesPOS\bagel.png")
        self.imageWater = PhotoImage(file = r"imagesPOS\water.png")
        
        self.labelTitle = tk.Label(self.frameHeader, text='New order entry').pack()
        
        # First row buttons
        self.buttonCoffeeS = tk.Button(self.frameRow1, text = 'Small Coffee', image = self.imageCoffeeS, command=lambda: self.itemAdd(1)).pack(side = 'left')
        self.buttonCoffeeM = tk.Button(self.frameRow1, text = 'Medium Coffee', image = self.imageCoffeeM, command=lambda: self.itemAdd(2)).pack(side = 'left')
        self.buttonCoffeeL = tk.Button(self.frameRow1, text = 'Large Coffee', image = self.imageCoffeeL, command=lambda: self.itemAdd(3), height=100).pack(side = 'left')
        self.buttonTea = tk.Button(self.frameRow1, text = 'Tea', image = self.imageTea, command=lambda: self.itemAdd(4)).pack(side = 'left')
        self.buttonWater = tk.Button(self.frameRow1, text = 'Water Bottle', image = self.imageWater, command=lambda: self.itemAdd(6)).pack(side = 'left')
        # Second row buttons
        self.buttonToast = tk.Button(self.frameRow2, text = 'Toast', image = self.imageToast, command=lambda: self.itemAdd(7)).pack(side = 'left')
        self.buttonMuffin = tk.Button(self.frameRow2, text = 'Muffin', image = self.imageMuffin, command=lambda: self.itemAdd(5)).pack(side = 'left')
        self.buttonDonut = tk.Button(self.frameRow2, text = 'Donut', image = self.imageDonut, command=lambda: self.itemAdd(11)).pack(side = 'left')
        self.buttonSandwich = tk.Button(self.frameRow2, text = 'Breakfast Sandwich', image = self.imageSandwich, command=lambda: self.itemAdd(8)).pack(side = 'left')
        self.buttonOatmeal = tk.Button(self.frameRow2, text = 'Oatmeal', image = self.imageOatmeal, command=lambda: self.itemAdd(9)).pack(side = 'left')
        self.buttonBeans = tk.Button(self.frameRow2, text = '1lb Coffee Beans', image = self.imageBeans, command=lambda: self.itemAdd(10)).pack(side = 'left')
        self.buttonBagel = tk.Button(self.frameRow2, text='Bagel', image=self.imageBagel, command=lambda: self.itemAdd(12)).pack(side='left')

        # List order items
        self.listBox = tk.Listbox(self.frameSide, width = 100)
        self.listBox.pack(side='right',fill='both')
        self.scrollBar = tk.Scrollbar(self.frameSide)
        self.scrollBar.pack(side='right',fill='both')
        self.listBox.config(yscrollcommand = self.scrollBar.set)
        self.scrollBar.config(command = self.listBox.yview)
        
        # Order management buttons
        self.itemRemoveButton = tk.Button(self.frameSide, text='Remove Item', command=lambda: self.itemRemove()).pack()
        self.orderSubmitButton = tk.Button(self.frameSide, text = 'Submit Order', command=lambda: self.orderSubmit()).pack()
        
        # Start loop
        tk.mainloop()
    
    def itemAdd(self, ITEM):
        # First check if item exists in inventory
        if product_list[ITEM-1]['quantity'] > 0:
            # Add item to the order and UI list
            order.append(ITEM)
            self.listBox.insert(tk.END, product_list[ITEM-1]["name"])
            
            # Remove item from inventory
            product_list[ITEM-1]['quantity'] -= 1
        else:
            tk.messagebox.showinfo('Error','That item is out of stock')
            print('Out of stock')
        
    def itemRemove(self): 
        selectionIndex = 0
        existingSelection = self.listBox.curselection()
        if existingSelection:
            selectionIndex = existingSelection[0]
            
            # Weird function to match selection index to the dictionary index of the item
            productIndex = next((index for index, product in enumerate(product_list) if product["name"] == str(self.listBox.get(selectionIndex))), None)
            
            # Remove item from UI list and order using selection index
            order.pop(selectionIndex)
            self.listBox.delete(selectionIndex)
            
            # Add item back to inventory using the product index
            product_list[productIndex]['quantity'] += 1
            
    def orderSubmit(self):
        orderTotal = 0
        if len(order) > 0:
            # Calculate the order total
            for item in order:
                # Weird function to match selection index to the dictionary index of the item
                productIndex = next((index for index, product in enumerate(product_list) if product["id"] == item), None)
                orderTotal += product_list[productIndex]['price']
            tk.messagebox.showinfo('Success',f'The total for order {self.orderID} is {orderTotal}')
            print(f'The total for order {self.orderID} is {orderTotal}')
            
            # Assign new order ID (why is there an error marker here)
            self.orderID += 1
            
            # Clear entire (previous) order
            self.listBox.delete(0, tk.END)
            order.clear()
            
        else:
            tk.messagebox.showinfo('Error','There are no items to submit!')
            print('There is nothing to submit!')

if __name__ == '__main__':
    gui = MainGUI()
    gui.mainWindow.mainloop()
