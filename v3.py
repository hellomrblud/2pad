#Joshua Code.

import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import random
import re

# Code for the item hire details.
class HireItem:
    # Start of the hire item.
    
    def __init__(self, firstname, lastname, receipt, item, quantity):
        # Set the first name of the customer for the hire item. 

        self.firstname = firstname

        # Set the last name of the customer for the hire item. 
        self.lastname = lastname

        # The unique receipt number for the hire item. 

        self.receipt = receipt

        # The name of the item that was hired. 

        self.item = item

        # The quantity of the item that was hired. 

        self.quantity = quantity

# Class for Julie's Party Hire Store
class PartyHireStore:
    # Start the party hire store with the main root window. 
    def __init__(self, root):

        # Store the main root window. 

        self.root = root

        # The title for the main window. 

        self.root.title("Julie's Party Hire Store")

        # Make the background colour of the main window light blue. 

        self.root.configure(bg="light blue")

        # Start an empty list to store the item details.

        self.HIRE_ITEMS = []

        # Custom font for the program, font = verdana, size = 10, in bold. 

        self.CUSTOM_FONT = Font(family="Verdana", size=10, weight="bold")

        # Options that a user can pick from for what item they have hired. 

        self.ITEM_OPTIONS = ["Chairs", "Candles", "Balloons"]

        # Search bar to search for hire entries
        search_frame = tk.Frame(root, bg="light blue")

        # Display the search frame, northwest. 
        search_frame.pack(pady=10, padx=10, anchor="nw")

        # Create a label for the search bar 

        self.LABEL_SEARCH = tk.Label(search_frame, text="Search For An Entry:", font=self.CUSTOM_FONT)

        # Position of the search label. 

        self.LABEL_SEARCH.grid(row=0, column=0, padx=5, pady=5)

        self.ENTRY_SEARCH = tk.Entry(search_frame, font=self.CUSTOM_FONT)
        self.ENTRY_SEARCH.grid(row=0, column=1, padx=5, pady=5)

        # Create a button that is for finding the hire entries, also in orange. 
        self.SEARCH_BUTTON = tk.Button(search_frame, bg="orange", text="Search", command=self.search, font=self.CUSTOM_FONT)
        self.SEARCH_BUTTON.grid(row=0, column=2, padx=5, pady=5)

        # Button for showing all entries.
        self.SHOW_ALL_BUTTON = tk.Button(search_frame, text="Show All Entries", command=self.show_all_entries, font=self.CUSTOM_FONT)
        self.SHOW_ALL_BUTTON.grid(row=1, column=0, padx=5, pady=5)

        # Frame for the customer details.
        customer_frame = tk.Frame(root, bg="light blue")
        customer_frame.pack(pady=10)

        # Label for the first name.
        self.LABEL_FIRSTNAME = tk.Label(customer_frame, text="First Name:", font=self.CUSTOM_FONT)
        self.LABEL_FIRSTNAME.grid(row=0, column=0, padx=5, pady=5)

        # Create an entry for the fist name. 
        self.ENTRY_FIRSTNAME = tk.Entry(customer_frame, font=self.CUSTOM_FONT)
        self.ENTRY_FIRSTNAME.grid(row=0, column=1, padx=5, pady=5)

        # Label for the last name.
        self.LABEL_LASTNAME = tk.Label(customer_frame, text="Last Name:", font=self.CUSTOM_FONT)
        self.LABEL_LASTNAME.grid(row=1, column=0, padx=5, pady=5)

        # Create an entry for the last name. 
        self.ENTRY_LASTNAME = tk.Entry(customer_frame, font=self.CUSTOM_FONT)
        self.ENTRY_LASTNAME.grid(row=1, column=1, padx=5, pady=5)

        # Frame for the receipt number
        self.LABEL_RECEIPT = tk.Label(customer_frame, text="Receipt Number:", font=self.CUSTOM_FONT)
        self.LABEL_RECEIPT.grid(row=2, column=0, padx=5, pady=5)

        # Create an entry that cannot be used for showing the receipt number. 
        self.ENTRY_RECEIPT = tk.Entry(customer_frame, font=self.CUSTOM_FONT, state=tk.DISABLED)
        self.ENTRY_RECEIPT.grid(row=2, column=1, padx=5, pady=5)

        # Frame for item details
        item_frame = tk.Frame(root, bg="light blue")
        item_frame.pack(pady=10)

        # Label for item that was hired
        self.LABEL_ITEM = tk.Label(item_frame, text="Item That Was Hired:", font=self.CUSTOM_FONT)
        self.LABEL_ITEM.grid(row=0, column=0, padx=5, pady=5)

        # Dropdown menu for pre-selected items
        self.ITEM_VAR = tk.StringVar()
        self.ITEM_VAR.set(self.ITEM_OPTIONS[0])

        # Dropdown menu for picking a item to hire. 
        self.ITEM_DROPDOWN = tk.OptionMenu(item_frame, self.ITEM_VAR, *self.ITEM_OPTIONS)

        # The font for dropdown menu. 
        self.ITEM_DROPDOWN.config(font=self.CUSTOM_FONT)
        self.ITEM_DROPDOWN.grid(row=0, column=1, padx=5, pady=5)

        # Label for a custom item a user wants to enter.
        self.LABEL_CUSTOM_ITEM = tk.Label(item_frame, text="Enter A Custom Item:", font=self.CUSTOM_FONT)
        self.LABEL_CUSTOM_ITEM.grid(row=1, column=0, padx=5, pady=5)

        # Entry for a custom item to hire. 
        self.ENTRY_CUSTOM_ITEM = tk.Entry(item_frame, font=self.CUSTOM_FONT)
        self.ENTRY_CUSTOM_ITEM.grid(row=1, column=1, padx=5, pady=5)

        # Label for the quantity. 
        self.LABEL_QUANTITY = tk.Label(item_frame, text="Quantity:", font=self.CUSTOM_FONT)
        self.LABEL_QUANTITY.grid(row=2, column=0, padx=5, pady=5)

        # Entry for putting the number of an item hired. 
        self.ENTRY_QUANTITY = tk.Entry(item_frame, font=self.CUSTOM_FONT)
        self.ENTRY_QUANTITY.grid(row=2, column=1, padx=5, pady=5)

        # Button for adding an item / entry.
        self.SUBMIT_BUTTON = tk.Button(root, bg="light green", text="Add An Item", command=self.submit, font=self.CUSTOM_FONT)
        self.SUBMIT_BUTTON.pack(pady=10)

        # Listbox to display the hire details.
        self.LISTBOX = tk.Listbox(root, font=self.CUSTOM_FONT, height=10, width=100)
        self.LISTBOX.pack(pady=10)

        # Button for deleting selected item.
        self.DELETE_BUTTON = tk.Button(root, bg="red", text="Delete", command=self.delete_item, font=self.CUSTOM_FONT)
        self.DELETE_BUTTON.pack(pady=10)

    # Makes a unique receipt number for each entry. 
    def generate_unique_receipt(self):

        # Random number between 1000 and 10000 for the receipt number. 
        receipt = str(random.randint(1000, 10000))

        # Check is a receipt number has already been used for a entry that was made before. 
        while any(item.receipt == receipt for item in self.HIRE_ITEMS):

            # Random number between 1000 and 10000 for the receipt number.
            receipt = str(random.randint(1000, 10000))

        # Return the receipt number that was made. 
        return receipt

    # Process the entry and add the hire item to the list. 
    def submit(self):

        # Get what was entered in the first name entry. 
        firstname = self.ENTRY_FIRSTNAME.get()

        # Get what was entered in the last name entry. 
        lastname = self.ENTRY_LASTNAME.get()

        receipt = self.generate_unique_receipt()
        quantity = self.ENTRY_QUANTITY.get()

        # Get the item hired from the dropdown menu. 
        item = self.ITEM_VAR.get()

        # Get the custom item the user wanted, if it was entered. 
        custom_item = self.ENTRY_CUSTOM_ITEM.get()

        # Check is the entries are filled in before adding an item. 
        if not (firstname and lastname and quantity):
            messagebox.showerror("Error!", "Make sure everything is filled in")

        # Make sure the first and last name only have letters entered in. 
        elif not firstname.isalpha() or not lastname.isalpha():
            messagebox.showerror("Error!", "First and Last Name should only contain letters")

        # Make sure the number entered in quantity is between 1 and 500. 
        elif not quantity.isdigit() or not 1 <= int(quantity) <= 500:
            messagebox.showerror("Error!", "The quantity must be a number between 1 and 500")

        # Code for item that is selected or a custom item has been written. 
        elif not item and not custom_item:
            messagebox.showerror("Error!", "Select an item or enter a custom item")

        # Custom item should only have letters entered and not numbers. 
        elif custom_item and not custom_item.isalpha():
            messagebox.showerror("Error!", "Custom item should only contain letters")

        else:
            if custom_item:
                item = custom_item

            # Create a hire entry, show it in the listbox and add it to HIRE_ITEM list. 
            hire_item = HireItem(firstname, lastname, receipt, item, quantity)
            hire_details = f"Full Name: {firstname} {lastname}, Receipt Number: {receipt}, Hired Item: {item}, Quantity: {quantity}"
            self.LISTBOX.insert(tk.END, hire_details)
            self.HIRE_ITEMS.append(hire_item)

            # Code that clears all of the entry fields also resets the receipt number and the item dropdown menu. 
            self.ENTRY_FIRSTNAME.delete(0, tk.END)
            self.ENTRY_LASTNAME.delete(0, tk.END)
            self.ENTRY_RECEIPT.config(state=tk.NORMAL)
            self.ENTRY_RECEIPT.delete(0, tk.END)
            self.ENTRY_RECEIPT.insert(tk.END, receipt)
            self.ENTRY_RECEIPT.config(state=tk.DISABLED)
            self.ENTRY_QUANTITY.delete(0, tk.END)
            self.ITEM_VAR.set(self.ITEM_OPTIONS[0])
            self.ENTRY_CUSTOM_ITEM.delete(0, tk.END)

    # Deletes the selected item hire from HIRE_ITEM list. 
    def delete_item(self):
        selected_index = self.LISTBOX.curselection()
        if selected_index:
            del self.HIRE_ITEMS[selected_index[0]]

            # Clear and reload the LISTBOX to show the updated entries.

            self.LISTBOX.delete(0, tk.END)
            for item in self.HIRE_ITEMS:
                hire_details = f"Full Name: {item.firstname} {item.lastname}, Receipt Number: {item.receipt}, Hired Item: {item.item}, Quantity: {item.quantity}"
                self.LISTBOX.insert(tk.END, hire_details)
        else:
            messagebox.showerror("Error!", "Select an item to delete.")


    # Make a search based on what text was entered and make the listbox display that entry.
    def search(self):
        search_text = self.ENTRY_SEARCH.get().lower()
        first_name, last_name = re.split(r'\s+', search_text.strip()) if ' ' in search_text else (search_text, search_text)
        self.LISTBOX.delete(0, tk.END)

        # Sort out the hire item details on what was searched and show it in the listbox. 
        for item in self.HIRE_ITEMS:
            if (first_name in item.firstname.lower() and last_name in item.lastname.lower() or
                first_name in item.lastname.lower() and last_name in item.firstname.lower() or
                first_name in item.firstname.lower() or last_name in item.lastname.lower() or
                search_text in item.receipt.lower() or search_text in item.item.lower() or
                search_text in item.quantity.lower()):
                hire_details = f"Full Name: {item.firstname} {item.lastname}, Receipt Number: {item.receipt}, Hired Item: {item.item}, Quantity: {item.quantity}"
                self.LISTBOX.insert(tk.END, hire_details)

        # Clear the search bar after search
        self.ENTRY_SEARCH.delete(0, tk.END)

    # Show all entries that are stored in the HIRE_ITEM list and show it in the listbox.
    def show_all_entries(self):
        self.LISTBOX.delete(0, tk.END)
        for item in self.HIRE_ITEMS:
            hire_details = f"Full Name: {item.firstname} {item.lastname}, Receipt Number: {item.receipt}, Hired Item: {item.item}, Quantity: {item.quantity}"
            self.LISTBOX.insert(tk.END, hire_details)

# Create the main window and run the GUI. 
def main():
    root = tk.Tk()
    app = PartyHireStore(root)
    root.mainloop()

if __name__ == "__main__":
    main()



