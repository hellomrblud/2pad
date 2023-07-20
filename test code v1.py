import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

class HireItem:
    def __init__(self, firstname, lastname, receipt, item, quantity):
        self.firstname = firstname
        self.lastname = lastname
        self.receipt = receipt
        self.item = item
        self.quantity = quantity

class PartyHireStore:
    def __init__(self, root):
        self.root = root
        self.root.title("Julie's Party Hire Store")

        self.hire_items = []

        #code to make the background color light blue

        self.root.configure(bg="light blue")

        #verdana font for all the text in the program

        self.custom_font = Font(family="Verdana", size=10, weight="bold")

        #entry box with the verdana font

        self.label_firstname = tk.Label(root, text="First Name:", font=self.custom_font)
        self.label_firstname.pack()
        self.entry_firstname = tk.Entry(root, font=self.custom_font)
        self.entry_firstname.pack(pady=5)


        self.label_lastname = tk.Label(root, text="Last Name:", font=self.custom_font)
        self.label_lastname.pack()
        self.entry_lastname = tk.Entry(root, font=self.custom_font)
        self.entry_lastname.pack(pady=5)

        self.label_receipt = tk.Label(root, text="Receipt Number:", font=self.custom_font)
        self.label_receipt.pack()
        self.entry_receipt = tk.Entry(root, font=self.custom_font)
        self.entry_receipt.pack(pady=5)

        self.label_item = tk.Label(root, text="Item That Was Hired:", font=self.custom_font)
        self.label_item.pack()

        #create the dropdown box for the item that was hired 


        self.item_options = ["Chairs", "Candles", "Balloons"]
        self.item_var = tk.StringVar()
        self.item_var.set("Chairs")
        self.item_dropdown = tk.OptionMenu(root, self.item_var, *self.item_options)
        self.item_dropdown.config(font=self.custom_font)
        self.item_dropdown.pack(pady=5)

        self.label_custom_item = tk.Label(root, text="Or enter a custom item:", font=self.custom_font)
        self.label_custom_item.pack()

        #entry box for custom item if the user wants to

        self.entry_custom_item = tk.Entry(root, font=self.custom_font)
        self.entry_custom_item.pack(pady=5)

        self.label_quantity = tk.Label(root, text="Quantity:", font=self.custom_font)
        self.label_quantity.pack()
        self.entry_quantity = tk.Entry(root, font=self.custom_font)
        self.entry_quantity.pack(pady=5)

        #the submit button for the entry

        self.submit_button = tk.Button(root, text="Add Item", command=self.submit, font=self.custom_font)
        self.submit_button.pack(pady=10)

        #listbox for all of the previous entries

        self.listbox = tk.Listbox(root, font=self.custom_font, height=10, width=70)  # Adjusted height and width
        self.listbox.pack(pady=10)

        #code for the delete button to remove an existing entry

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_item, font=self.custom_font)
        self.delete_button.pack(pady=10)


    def submit(self):
        firstname = self.entry_firstname.get()
        lastname = self.entry_lastname.get()
        receipt = self.entry_receipt.get()
        quantity = self.entry_quantity.get()
        item = self.item_var.get()
        custom_item = self.entry_custom_item.get()

        if not (firstname and lastname and receipt and quantity):
            messagebox.showerror("Error", "Please make sure everything is answered.")
        elif not firstname.isalpha() or not lastname.isalpha():
            messagebox.showerror("Error", "First Name and Last Name should only contain letters.")
        elif not receipt.isdigit():
            messagebox.showerror("Error", "Receipt Number can only be numbers.")
        elif not quantity.isdigit() or not 1 <= int(quantity) <= 500:
            messagebox.showerror("Error", "Quantity must be a number between 1 and 500.")
        elif not item and not custom_item:
            messagebox.showerror("Error", "Please select an item or enter a custom item.")
        else:
            if custom_item:
                item = custom_item

            hire_item = HireItem(firstname, lastname, receipt, item, quantity)
            hire_details = f"Full Name: {firstname} {lastname}, Receipt Number: {receipt}, Hired Item: {item}, Quantity: {quantity}"
            self.listbox.insert(tk.END, hire_details)
            self.hire_items.append(hire_item)

            self.entry_firstname.delete(0, tk.END)
            self.entry_lastname.delete(0, tk.END)
            self.entry_receipt.delete(0, tk.END)
            self.entry_quantity.delete(0, tk.END)
            self.item_var.set("Chairs")
            self.entry_custom_item.delete(0, tk.END)

    def delete_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
            del self.hire_items[selected_index[0]]
        else:
            messagebox.showerror("Error", "Please select an item to delete.")


root = tk.Tk()
app = PartyHireStore(root)

root.mainloop()


