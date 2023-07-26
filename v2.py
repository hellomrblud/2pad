import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import random

# The code for the item hire details. 

class HireItem:
    def __init__(self, firstname, lastname, receipt, item, quantity):
        self.firstname = firstname
        self.lastname = lastname
        self.receipt = receipt
        self.item = item
        self.quantity = quantity

# Class for Julia's Party Hire Store.

class PartyHireStore:
    def __init__(self, root):
        self.root = root
        self.root.title("Julie's Party Hire Store")

        # Code for the background colour to be light blue.
        self.root.configure(bg="light blue")  

        self.hire_items = []

        # Verdana font for all the text in the program.
        # The text is in size 10.
        # All text shown in the program is bold.
        # This will be used in the rest of the text in the program.
        
        self.custom_font = Font(family="Verdana", size=10, weight="bold")

        # Frame for the customer details.
        # With the colour light blue.

        customer_frame = tk.Frame(root, bg="light blue")
        customer_frame.pack(pady=10)

        # Label for the first name.

        self.label_firstname = tk.Label(customer_frame, text="First Name:", font=self.custom_font)
        
        # Label position for first name.
        
        self.label_firstname.grid(row=0, column=0, padx=5, pady=5)
        self.entry_firstname = tk.Entry(customer_frame, font=self.custom_font)
        
        # Entry box position for first name.
        
        self.entry_firstname.grid(row=0, column=1, padx=5, pady=5)

        # Label for the last name.

        self.label_lastname = tk.Label(customer_frame, text="Last Name:", font=self.custom_font)
        
        # Label position for lastname.
        
        self.label_lastname.grid(row=1, column=0, padx=5, pady=5)
        self.entry_lastname = tk.Entry(customer_frame, font=self.custom_font)

        # Entry box position.
        
        self.entry_lastname.grid(row=1, column=1, padx=5, pady=5)

        # Frame for the receipt number.

        self.label_receipt = tk.Label(customer_frame, text="Receipt Number:", font=self.custom_font)
        
        # Label position for the receipt box.
        
        self.label_receipt.grid(row=2, column=0, padx=5, pady=5)
        self.entry_receipt = tk.Entry(customer_frame, font=self.custom_font, state=tk.DISABLED)
        
        # Entry box for the receipt.
        
        self.entry_receipt.grid(row=2, column=1, padx=5, pady=5)

        # Frame for item details.
        # With the baxkground colour light blue.
        
        item_frame = tk.Frame(root, bg="light blue")
        item_frame.pack(pady=10)
        
        # Label for item that was hired.
        
        self.label_item = tk.Label(item_frame, text="Item That Was Hired:", font=self.custom_font)
        
        # Position for the item that was hired. 
        
        self.label_item.grid(row=0, column=0, padx=5, pady=5)

        # Dropdown menu for pre selected items, makes it easier for the user to enter an item.  

        self.item_options = ["Chairs", "Candles", "Balloons"]
        self.item_var = tk.StringVar()
        self.item_var.set("Chairs")
        self.item_dropdown = tk.OptionMenu(item_frame, self.item_var, *self.item_options)
        self.item_dropdown.config(font=self.custom_font)
        
        # This is the position for the dropdown grid.
        
        self.item_dropdown.grid(row=0, column=1, padx=5, pady=5)

        # Label for a custom item a user wants to enter. 

        self.label_custom_item = tk.Label(item_frame, text="Enter A Custom Item:", font=self.custom_font)
        
        # The position for the label.
        
        self.label_custom_item.grid(row=1, column=0, padx=5, pady=5)

        self.entry_custom_item = tk.Entry(item_frame, font=self.custom_font)
                
        # The position for the entry for custom item.
        
        self.entry_custom_item.grid(row=1, column=1, padx=5, pady=5)

        # Label for the quantity of an amount that was hired.

        self.label_quantity = tk.Label(item_frame, text="Quantity:", font=self.custom_font)
        
        # The postion for the quantity label.
        
        self.label_quantity.grid(row=2, column=0, padx=5, pady=5)
        self.entry_quantity = tk.Entry(item_frame, font=self.custom_font)
        
        # The position for the entry.
        
        self.entry_quantity.grid(row=2, column=1, padx=5, pady=5)


        # Buttom for adding an item or making an entry.

        self.submit_button = tk.Button(root, text="Add An Item", command=self.submit, font=self.custom_font)
        self.submit_button.pack(pady=10)
        
        # Listbox to show all entries with the custom font.

        self.listbox = tk.Listbox(root, font=self.custom_font, height=10, width=70)
        self.listbox.pack(pady=10)

        # The button to allow the user to delete an entry.

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_item, font=self.custom_font)
        self.delete_button.pack(pady=10)

    # Making a random receipt number for each entry that has been made.

    def generate_unique_receipt(self):

        # Random receipt number that is generated between 1000 and 100000.

        receipt = str(random.randint(1000, 10000))
        while any(item.receipt == receipt for item in self.hire_items):
            receipt = str(random.randint(1000, 10000))
        return receipt

    # Code to record the users input for a new hire item.

    def submit(self):
        firstname = self.entry_firstname.get()
        lastname = self.entry_lastname.get()
        receipt = self.generate_unique_receipt()
        quantity = self.entry_quantity.get()
        item = self.item_var.get()
        custom_item = self.entry_custom_item.get()

        # Make sure all user entries are valid before adding a new hire item.
        
        if not (firstname and lastname and quantity):

            # If the user tries to add an item without filling in all the details. 

            messagebox.showerror("Error!", "Make sure everything is filled in")

        # Uses isalpha to make sure the string only has letters and not numbers.

        elif not firstname.isalpha() or not lastname.isalpha():

            # Error message if first and last name was filled in with numbers not letters.

            messagebox.showerror("Error!", "First and Last Name should only contain letters")

        # Making sure the quantity is set between 1 and 500.
        
        elif not quantity.isdigit() or not 1 <= int(quantity) <= 500:

            # Error message for the quantity if it was below 1 or above 500.

            messagebox.showerror("Error!", "The quantity must be a number between 1 and 500")
        elif not item and not custom_item:

            messagebox.showerror("Error!", "Select an item or enter a custom item")
        else:
            if custom_item:
                item = custom_item

            hire_item = HireItem(firstname, lastname, receipt, item, quantity)
            hire_details = f"Full Name: {firstname} {lastname}, Receipt Number: {receipt}, Hired Item: {item}, Quantity: {quantity}"
            self.listbox.insert(tk.END, hire_details)
            self.hire_items.append(hire_item)

            # Resetting the input after adding a hire item.

            self.entry_firstname.delete(0, tk.END)
            self.entry_lastname.delete(0, tk.END)
            self.entry_receipt.config(state=tk.NORMAL)
            self.entry_receipt.delete(0, tk.END)
            self.entry_receipt.insert(tk.END, receipt)
            self.entry_receipt.config(state=tk.DISABLED)
            self.entry_quantity.delete(0, tk.END)
            self.item_var.set("Chairs")
            self.entry_custom_item.delete(0, tk.END)

    # Code to delete selcted item hired from the list.

    def delete_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
            del self.hire_items[selected_index[0]]
        else:

            # If the user tries to click the button delete without actually selecting an entry.
            
            messagebox.showerror("Error!", "Select an item to delete.")

# Code that runs the program.
 
root = tk.Tk()
app = PartyHireStore(root)

root.mainloop()




