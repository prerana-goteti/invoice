import sqlite3
import tkinter as tk
from tkinter import messagebox

def create_database():
    conn = sqlite3.connect('invoice.db')
    crsr = conn.cursor()

    crsr.execute('''
    CREATE TABLE IF NOT EXISTS customers (
                    cust_id INTEGER PRIMARY KEY,
                    name VARCHAR(50),
                    email VARCHAR(20)
    )
    ''')

    crsr.execute('''
    CREATE TABLE IF NOT EXISTS products (
                    prod_id INTEGER PRIMARY KEY,
                    name VARCHAR(50),
                    price REAL
    )
    ''')

    crsr.execute('''
    CREATE TABLE IF NOT EXISTS invoices (
                    inv_id INTEGER PRIMARY KEY,
                    cust_id INTEGER,
                    date DATE,
                    FOREIGN KEY (cust_id) REFERENCES customers (cust_id)
    )
    ''')

    crsr.execute('''
    CREATE TABLE IF NOT EXISTS invoice_items (
                    item_id INTEGER PRIMARY KEY,
                    inv_id INTEGER,
                    prod_id INTEGER,
                    quantity INTEGER,
                    FOREIGN KEY (inv_id) REFERENCES invoices (inv_id),
                    FOREIGN KEY (prod_id) REFERENCES products (prod_id)
    )
    ''')

    conn.commit()
    conn.close()

def add_customer(name, email):
    conn = sqlite3.connect('invoice.db')
    crsr = conn.cursor()

    crsr.execute('''
    INSERT INTO customers (name, email)
    VALUES (?, ?)'    
    ''', (name, email) )

    conn.commit()
    conn.close()

def add_product(name, price):
    conn = sqlite3.connect('invoice.db')
    crsr = conn.cursor()

    crsr.execute('''
    INSERT INTO products (name, price)
    VALUES (?, ?)'    
    ''', (name, price) )

    conn.commit()
    conn.close()

def create_invoice(customer_id, date, items):
    conn = sqlite3.connect('invoice.db')
    crsr = conn.cursor()

    crsr.execute('''
    INSERT INTO invoice_items (inv_id, prod_id, quantity)
    VALUES (?, ?, ?)
    ''', (inv_id, item['prod_id'], item['quantity']))

    conn.commit()
    conn.close()

class InvoiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Invoice App')

        create_database()

        tk.Label(root, text="Customer Name : ").grid(row=0, column=0, padx=10, pady=10)
        self.customer_name_entry = tk.Entry(root)
        self.customer_name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Customer Email : ").grid(row=1, column=0, padx=10, pady=10)
        self.customer_email_entry = tk.Entry(root)
        self.customer_email_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(root, text="Add Customer", command=None).grid(row=2, column=0, columnspan=2, pady=10)

        tk.Label(root, text="Product Name : ").grid(row=3, column=0, padx=10, pady=10)
        self.product_name_entry = tk.Entry(root)
        self.product_name_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(root, text="Product Price : ").grid(row=4, column=0, padx=10, pady=10)
        self.product_price_entry = tk.Entry(root)
        self.product_price_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(root, text="Add Product", command=self.add_product).grid(row=5, column=0, columnspan=2, pady=10)

        tk.Label(root, text="Invoice Date : ").grid(row=6, column=0, padx=10, pady=10)
        self.inv_date_entry = tk.Entry(root)
        self.inv_date_entry.grid(row=6, column=1, padx=10, pady=10)

        tk.Label(root, text="Select Products and Quantities : ").grid(row=7, column=0, padx=10, pady=10)
        self.inv_items_entry = tk.Entry(root)
        self.inv_items_entry.grid(row=8, column=1, padx=10, pady=10)

        tk.Button(root, text="Create Invoice", command=None).grid(row=9, column=0, columnspan=2, pady=10)

        def add_product(self):
            name = self.product_name_entry.get()
            price = self.product_price_entry.get()

            if name and price:
                add_product(name, float(price))
                messagebox.showinfo("Success", "Product Added Successfully.")
            else:
                messagebox.showerror("Error", "Please Enter Both Product and it's Price.")

if __name__ == '__main__':
    root = tk.Tk()
    app = InvoiceApp(root)
    root.mainloop()