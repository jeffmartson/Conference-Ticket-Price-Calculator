import tkinter as tk
from tkinter import messagebox

def calculate_ticket_price(age):
    if age < 18:
        return 0
    elif 18 <= age < 25:
        return 990
    else:
        return 1390

def calculate_total_price():
    num_tickets = int(num_tickets_entry.get())
    total_price = 0

    for _ in range(num_tickets):
        age = int(age_entries[_].get())
        ticket_price = calculate_ticket_price(age)
        total_price += ticket_price

    if num_tickets > 3:
        total_price *= 0.9  # Apply 10% discount for more than 3 tickets

    messagebox.showinfo("Total Cost", f"Сумма к оплате: {total_price:.2f} руб.")

root = tk.Tk()
root.title("Conference Ticket Price Calculator")

num_tickets_label = tk.Label(root, text="Количество билетов:")
num_tickets_label.pack()

num_tickets_entry = tk.Entry(root)
num_tickets_entry.pack()

age_labels = []
age_entries = []

def add_age_fields():
    num_tickets = int(num_tickets_entry.get())

    for i in range(num_tickets):
        age_labels.append(tk.Label(root, text=f"Возраст посетителя {i + 1}:"))
        age_labels[i].pack()

        age_entries.append(tk.Entry(root))
        age_entries[i].pack()

    calculate_button.pack()

add_button = tk.Button(root, text="Добавить", command=add_age_fields)
add_button.pack()

calculate_button = tk.Button(root, text="Рассчитать стоимость", command=calculate_total_price)

root.mainloop()