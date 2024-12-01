import tkinter as tk
from tkinter import ttk

def main():
    # Main Window
    root = tk.Tk()
    root.title("Inventory Management System")
    root.geometry("800x600")  # Width x Height

    # Notebook for Tabs
    notebook = ttk.Notebook(root)

    # Items Management Tab
    items_tab = ttk.Frame(notebook)
    notebook.add(items_tab, text="Items Management")

    # Category Management Tab
    category_tab = ttk.Frame(notebook)
    notebook.add(category_tab, text="Category Management")

    # Transactions Tab
    transactions_tab = ttk.Frame(notebook)
    notebook.add(transactions_tab, text="Transactions")

    # Add notebook to main window
    notebook.pack(expand=1, fill="both")

    # --- Items Management Section ---
    tk.Label(items_tab, text="Item Management", font=("Arial", 16)).pack(pady=10)
    tk.Label(items_tab, text="Item Name:").pack()
    item_name_entry = tk.Entry(items_tab, width=30)
    item_name_entry.pack()

    tk.Label(items_tab, text="SKU:").pack()
    sku_entry = tk.Entry(items_tab, width=30)
    sku_entry.pack()

    tk.Label(items_tab, text="Category:").pack()
    category_entry = tk.Entry(items_tab, width=30)
    category_entry.pack()

    tk.Label(items_tab, text="Price:").pack()
    price_entry = tk.Entry(items_tab, width=30)
    price_entry.pack()

    tk.Label(items_tab, text="Quantity:").pack()
    quantity_entry = tk.Entry(items_tab, width=30)
    quantity_entry.pack()

    tk.Button(items_tab, text="Add Item", command=lambda: print("Add Item clicked")).pack(pady=5)
    tk.Button(items_tab, text="Update Stock", command=lambda: print("Update Stock clicked")).pack(pady=5)
    tk.Button(items_tab, text="View Items", command=lambda: print("View Items clicked")).pack(pady=5)

    # --- Category Management Section ---
    tk.Label(category_tab, text="Category Management", font=("Arial", 16)).pack(pady=10)
    tk.Label(category_tab, text="Category Name:").pack()
    category_name_entry = tk.Entry(category_tab, width=30)
    category_name_entry.pack()

    tk.Button(category_tab, text="Add Category", command=lambda: print("Add Category clicked")).pack(pady=5)
    tk.Button(category_tab, text="View Categories", command=lambda: print("View Categories clicked")).pack(pady=5)

    # --- Transactions Section ---
    tk.Label(transactions_tab, text="Transactions", font=("Arial", 16)).pack(pady=10)
    tk.Label(transactions_tab, text="SKU:").pack()
    transaction_sku_entry = tk.Entry(transactions_tab, width=30)
    transaction_sku_entry.pack()

    tk.Label(transactions_tab, text="Quantity:").pack()
    transaction_quantity_entry = tk.Entry(transactions_tab, width=30)
    transaction_quantity_entry.pack()

    tk.Label(transactions_tab, text="Transaction Type:").pack()
    transaction_type_combo = ttk.Combobox(transactions_tab, values=["Sale", "Restock"])
    transaction_type_combo.pack()

    tk.Button(transactions_tab, text="Record Transaction", command=lambda: print("Record Transaction clicked")).pack(pady=5)
    tk.Button(transactions_tab, text="View Transactions", command=lambda: print("View Transactions clicked")).pack(pady=5)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
