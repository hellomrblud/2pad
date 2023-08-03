# v4 code. 

import tkinter as tk

# Import the messagebox and also the file dialog.
from tkinter import messagebox, filedialog

# Import the font for having custom text fonts in the program.
from tkinter.font import Font

# Import the function of generating random numbers. 
import random

# Import csv module.
import csv
 
import re

# Code for the line for showinfo function.
from tkinter.messagebox import showinfo  

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

        # Search bar to search for hire entries, in light blue.
        search_frame = tk.Frame(root, bg="light blue")

        # Display the search frame, northwest.
        search_frame.pack(pady=10, padx=10, anchor="nw")

        # Create a label for the search bar.
        self.LABEL_SEARCH = tk.Label(search_frame, text="Search For An Entry:", font=self.CUSTOM_FONT)

        # Position and style the search label.
        self.LABEL_SEARCH.grid(row=0, column=0, padx=5, pady=5)

        # Create an entry field for the user to input search text.
        self.ENTRY_SEARCH = tk.Entry(search_frame, font=self.CUSTOM_FONT)

        # Display the search entry field with padding on the X and Y axes. 
        self.ENTRY_SEARCH.grid(row=0, column=1, padx=5, pady=5)

        # Create a button that is for finding the hire entries, also in orange.
        self.SEARCH_BUTTON = tk.Button(search_frame, bg="orange", text="Search", command=self.search, font=self.CUSTOM_FONT)

        # Position the search button. 
        self.SEARCH_BUTTON.grid(row=0, column=2, padx=5, pady=5)

        # Button for showing all entries, in a yellow colour.
        self.SHOW_ALL_BUTTON = tk.Button(search_frame, bg="yellow", text="Show All Entries", command=self.show_all_entries, font=self.CUSTOM_FONT)

        # Position the Show All Entries button. 
        self.SHOW_ALL_BUTTON.grid(row=1, column=0, padx=5, pady=5)

        # Frame for the customer details.
        customer_frame = tk.Frame(root, bg="light blue")

        # Position the customer frame with padding.
        customer_frame.pack(pady=10)

        # Label for the first name.
        self.LABEL_FIRSTNAME = tk.Label(customer_frame, text="First Name:", font=self.CUSTOM_FONT)

        # Position the first name label within the customer frame with padding.
        self.LABEL_FIRSTNAME.grid(row=0, column=0, padx=5, pady=5)

        # Create an entry for the first name.
        self.ENTRY_FIRSTNAME = tk.Entry(customer_frame, font=self.CUSTOM_FONT)

        # Entry field for first name, in row 0 and column 1 with padding. 
        self.ENTRY_FIRSTNAME.grid(row=0, column=1, padx=5, pady=5)

        # Label for the last name.
        self.LABEL_LASTNAME = tk.Label(customer_frame, text="Last Name:", font=self.CUSTOM_FONT)

        # Last Name label placement. 
        self.LABEL_LASTNAME.grid(row=1, column=0, padx=5, pady=5)

        # Create an entry for the last name.
        self.ENTRY_LASTNAME = tk.Entry(customer_frame, font=self.CUSTOM_FONT)

        # Last Name entry placement.
        self.ENTRY_LASTNAME.grid(row=1, column=1, padx=5, pady=5)

        # Frame for the receipt number.
        self.LABEL_RECEIPT = tk.Label(customer_frame, text="Receipt Number:", font=self.CUSTOM_FONT)

        # Receipt label placement. 
        self.LABEL_RECEIPT.grid(row=2, column=0, padx=5, pady=5)

        # Create an entry that cannot be used for showing the receipt number.
        self.ENTRY_RECEIPT = tk.Entry(customer_frame, font=self.CUSTOM_FONT, state=tk.DISABLED)

        # Receipt entry placement. 
        self.ENTRY_RECEIPT.grid(row=2, column=1, padx=5, pady=5)

        # Frame for item details, with the colour light blue.
        item_frame = tk.Frame(root, bg="light blue")

        # Item frame placement. 
        item_frame.pack(pady=10)

        # Label for item that was hired.
        self.LABEL_ITEM = tk.Label(item_frame, text="Item That Was Hired:", font=self.CUSTOM_FONT)

        # Item label placement. 
        self.LABEL_ITEM.grid(row=0, column=0, padx=5, pady=5)

        # Dropdown menu for pre-selected items.
        self.ITEM_VAR = tk.StringVar()

        # Set default dropdown option. 
        self.ITEM_VAR.set(self.ITEM_OPTIONS[0])

        # Dropdown menu for picking an item to hire.
        self.ITEM_DROPDOWN = tk.OptionMenu(item_frame, self.ITEM_VAR, *self.ITEM_OPTIONS)

        # The font for the dropdown menu.
        self.ITEM_DROPDOWN.config(font=self.CUSTOM_FONT)

        # Display the dropdown menu. 
        self.ITEM_DROPDOWN.grid(row=0, column=1, padx=5, pady=5)

        # Label for a custom item a user wants to enter.
        self.LABEL_CUSTOM_ITEM = tk.Label(item_frame, text="Enter A Custom Item:", font=self.CUSTOM_FONT)

        # Display custom item label.
        self.LABEL_CUSTOM_ITEM.grid(row=1, column=0, padx=5, pady=5)

        # Entry for a custom item to hire.
        self.ENTRY_CUSTOM_ITEM = tk.Entry(item_frame, font=self.CUSTOM_FONT)

        # Create an entry for the custom item.
        self.ENTRY_CUSTOM_ITEM.grid(row=1, column=1, padx=5, pady=5)

        # Label for the quantity.
        self.LABEL_QUANTITY = tk.Label(item_frame, text="Quantity:", font=self.CUSTOM_FONT)
        
        # Create label for the quantity.  
        self.LABEL_QUANTITY.grid(row=2, column=0, padx=5, pady=5)

        # Entry for putting the number of an item hired.
        self.ENTRY_QUANTITY = tk.Entry(item_frame, font=self.CUSTOM_FONT)

        # Create an entry for the quantity.  
        self.ENTRY_QUANTITY.grid(row=2, column=1, padx=5, pady=5)

        # Button for adding an item / entry, in a light green colour.
        self.SUBMIT_BUTTON = tk.Button(root, bg="light green", text="Add An Item", command=self.submit, font=self.CUSTOM_FONT)

        # Create the submit button. 
        self.SUBMIT_BUTTON.pack(pady=10)

        # Button for uploading data from a CSV file, in a pink colour.
        self.UPLOAD_BUTTON = tk.Button(search_frame, bg="pink", text="Upload Data From CSV File",

                                       # Browse and upload CSV file with the custom font.
                                       command=self.browse_file, font=self.CUSTOM_FONT)

        # Position of the upload button widget on row 1, column 1.
        self.UPLOAD_BUTTON.grid(row=1, column=1, padx=5, pady=5)

        # Listbox to display the hire details.
        self.LISTBOX = tk.Listbox(root, font=self.CUSTOM_FONT, height=10, width=100)
        self.LISTBOX.pack(pady=10)

        # Button for deleting the selected item, in red colour.
        self.DELETE_BUTTON = tk.Button(root, bg="red", text="Delete", command=self.delete_item, font=self.CUSTOM_FONT)
        self.DELETE_BUTTON.pack(pady=10)

        # List to store the original indices of displayed items during search.
        self.filtered_indices = []

    # Makes a unique receipt number for each entry.
    def generate_unique_receipt(self):

        # Random number between 1000 and 10000 for the receipt number.
        receipt = str(random.randint(1000, 10000))

        # Check if a receipt number has already been used for an entry that was made before.
        while any(item.receipt == receipt for item in self.HIRE_ITEMS):

            # Random number between 1000 and 10000 for the receipt number.
            receipt = str(random.randint(1000, 10000))

        # Return the receipt number that was generated.
        return receipt

    # Process the entry and add the hire item to the list.
    def submit(self):

        # Get what was entered in the first name entry.
        firstname = self.ENTRY_FIRSTNAME.get()

        # Get what was entered in the last name entry.
        lastname = self.ENTRY_LASTNAME.get()

        # Generate a receipt number and get the quantity value.
        receipt = self.generate_unique_receipt()
        quantity = self.ENTRY_QUANTITY.get()

        # Get the item hired from the dropdown menu.
        item = self.ITEM_VAR.get()

        # Get the custom item the user wanted, if it was entered.
        custom_item = self.ENTRY_CUSTOM_ITEM.get()

        # Check if the entries are filled in before adding an item, or this error message will pop up.
        if not (firstname and lastname and quantity):
            messagebox.showerror("Error!", "Make sure everything is filled in")
            return

        # Make sure the first and last name only have letters entered in.
        elif not firstname.isalpha() or not lastname.isalpha():

            # Otherwise this error message will pop up to inform the user . 
            messagebox.showerror("Error!", "First and Last Name should only contain letters")
            return

        # Make sure the number entered in quantity is between 1 and 500.
        elif not quantity.isdigit() or not 1 <= int(quantity) <= 500:

            # This error message will pop up to inform the user the quantity they have set is invaild. 
            messagebox.showerror("Error!", "The quantity must be a number between 1 and 500")
            return

        # Code for the item that is selected or a custom item has been written.
        elif not item and not custom_item:

            # Otherwise this error message will pop up for an invaild entry. 
            messagebox.showerror("Error!", "Select an item or enter a custom item")
            return

        # Custom item should only have letters entered and not numbers.
        elif custom_item and not custom_item.replace(" ", "").isalpha():

            # This error message will pop up, if the user makes an invaild input.
            messagebox.showerror("Error!", "Custom item should only contain letters")
            return

        # Set item to custom_item if it there is an entry made by the user.
        if custom_item:
            item = custom_item

        # Create a hire entry, show it in the listbox, and add it to HIRE_ITEM list.
        hire_item = HireItem(firstname, lastname, receipt, item, quantity)
        hire_details = f"Full Name: {firstname} {lastname}, Receipt Number: {receipt}, Hired Item: {item}, Quantity: {quantity}"

        # Display hire details and store the hire item.
        self.LISTBOX.insert(tk.END, hire_details)
        self.HIRE_ITEMS.append(hire_item)

        # Show success message, to show the user the entry has been added. 
        showinfo("Success!", "Entry successfully added")

        # Code that clears all of the entry fields also resets the receipt number and the item dropdown menu.
        self.ENTRY_FIRSTNAME.delete(0, tk.END)
        self.ENTRY_LASTNAME.delete(0, tk.END)

        # Clear and also enable the receipt number entry.
        self.ENTRY_RECEIPT.config(state=tk.NORMAL)
        self.ENTRY_RECEIPT.delete(0, tk.END)

        # Display the receipt number that was generated and block the entry.
        self.ENTRY_RECEIPT.insert(tk.END, receipt)
        self.ENTRY_RECEIPT.config(state=tk.DISABLED)

        # Reset the inputs after adding a hire entry / item.
        self.ENTRY_QUANTITY.delete(0, tk.END)
        self.ITEM_VAR.set(self.ITEM_OPTIONS[0])
        self.ENTRY_CUSTOM_ITEM.delete(0, tk.END)

        # Update filtered indices to include the new hire item.
        self.filtered_indices.append(len(self.HIRE_ITEMS) - 1)

    # Deletes the selected item hire from HIRE_ITEM list.
    def delete_item(self):
        selected_index = self.LISTBOX.curselection()

        # Delete selected hire item if an item is selected in the listbox.
        if selected_index:

             # Get the original index.
            original_index = self.filtered_indices[selected_index[0]]  
            del self.HIRE_ITEMS[original_index]

            # Clear and reload the LISTBOX to show the updated entries.
            self.LISTBOX.delete(0, tk.END)

            # Clear filtered indices after deleting an entry.
            self.filtered_indices = []  

            # Loop through hire items.
            for index, item in enumerate(self.HIRE_ITEMS):

                # Format hire details for displaying customer information.
                hire_details = f"Full Name: {item.firstname} {item.lastname}, Receipt Number: {item.receipt}, Hired Item: {item.item}, Quantity: {item.quantity}"

                # Add hire details to the listbox.
                self.LISTBOX.insert(tk.END, hire_details)

                # Save the original index of the displayed item during search.
                self.filtered_indices.append(index)


                
        # This error message will pop up to inform the user to select an item to delete.
        else:
            messagebox.showerror("Error!", "Select an item to delete.")

    # Make a search based on what text was entered and make the listbox display that entry.
    def search(self):
        search_text = self.ENTRY_SEARCH.get().lower()

        # Check if the search text is empty.
        if not search_text.strip():

            # Otherwise, this error message will pop up.
            messagebox.showerror("Error!", "Enter something to search first")
            return

        # Split search text into first and last names and then clear the listbox.
        first_name, last_name = re.split(r'\s+', search_text.strip()) if ' ' in search_text else (search_text, search_text)
        self.LISTBOX.delete(0, tk.END)

        # Clear filtered indices during search.
        self.filtered_indices = []  

        # Search for matching hire items by first and last names.
        for index, item in enumerate(self.HIRE_ITEMS):
            if (first_name in item.firstname.lower() and last_name in item.lastname.lower() or

                # Check for matches in first and last names.
                first_name in item.lastname.lower() and last_name in item.firstname.lower() or
                first_name in item.firstname.lower() or last_name in item.lastname.lower() or

                # Check for matches in receipt, item, or quantity.
                search_text in item.receipt.lower() or search_text in item.item.lower() or
                search_text in item.quantity.lower()):

                # Create hire details string and put it into the listbox.
                hire_details = f"Full Name: {item.firstname} {item.lastname}, Receipt Number: {item.receipt}, Hired Item: {item.item}, Quantity: {item.quantity}"
                self.LISTBOX.insert(tk.END, hire_details)

                # Save the original index of the displayed item during search.
                self.filtered_indices.append(index)

                # Clear the search bar after performing the search.
                self.ENTRY_SEARCH.delete(0, tk.END)

        # Show success message if search was successful.
        if self.filtered_indices:
            messagebox.showinfo("Success!", "Entry successfully searched")

    # Display all entries in the listbox.
    def show_all_entries(self):
        self.LISTBOX.delete(0, tk.END)

        # Clear filtered indices when showing all entries.
        self.filtered_indices = []  

        # Loop through hire items with its index and item.
        for index, item in enumerate(self.HIRE_ITEMS):

            # Create hire details string for display.
            hire_details = f"Full Name: {item.firstname} {item.lastname}, Receipt Number: {item.receipt}, Hired Item: {item.item}, Quantity: {item.quantity}"
        
            # Add hire details to the listbox.
            self.LISTBOX.insert(tk.END, hire_details)

            # Save the original index of the displayed item during search.
            self.filtered_indices.append(index) 

    # Upload data from a CSV file.
    def browse_file(self):

        # Ask the user to choose a csv file and get the selected file path.
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

        # Check if a valid file path was selected.
        if file_path:

            #  Read and display data from the selected csv file.
            self.read_csv_file(file_path)

    # Read data from the CSV file and display it in the listbox.
    def read_csv_file(self, file_path):

        # Open the selected csv file and read its information.
        try:
            with open(file_path, newline='') as csvfile:

                # Read the csv file as a dictionary. 
                reader = csv.DictReader(csvfile)

                # Loop through csv rows.
                for row in reader:

                    # Get the First Name from csv row.
                    firstname = row['First Name']

                    # Get the Last Name from csv row.
                    lastname = row['Last Name']

                    # Get the Receipt Number from csv row.
                    receipt = row['Receipt Number']

                    # Get the Hired Item from csv row.
                    item = row['Hired Item']

                    # Get the Quantity from csv row.
                    quantity = row['Quantity']

                    # Create HireItem object and add to hire items.
                    hire_item = HireItem(firstname, lastname, receipt, item, quantity)
                    self.HIRE_ITEMS.append(hire_item)

                    # Display hire details in the listbox.
                    hire_details = f"Full Name: {firstname} {lastname}, Receipt Number: {receipt}, Hired Item: {item}, Quantity: {quantity}"
                    self.LISTBOX.insert(tk.END, hire_details)

        # File not found error handling.
        except FileNotFoundError:

            # Show error message for file not found or invalid cvs file.
            messagebox.showerror("Error!", "File not found or the CSV file is invalid.")

        # Get any unexpected exception and store it in e.
        except Exception as e:

            # Show error message with the exception details for csv file reading.
            messagebox.showerror("Error!", f"Error while reading the information in the CSV file: {str(e)}")

# Create main window, start the app, and run the main loop.
def main():
    root = tk.Tk()
    app = PartyHireStore(root)
    root.mainloop()

# Run the main function.  
if __name__ == "__main__":
    main()





