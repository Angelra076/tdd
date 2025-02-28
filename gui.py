import tkinter as tk
from water_dispenser import WaterDispenser

def update_status():
    level_label.config(text=f"Nivel de agua: {dispenser.current_level}L")
    cold_temp_label.config(text=f"Temp. Fría: {dispenser.current_cold_temp}°C")
    hot_temp_label.config(text=f"Temp. Caliente: {dispenser.current_hot_temp}°C")

def dispense_water(mode):
    amount = int(amount_entry.get())
    message = dispenser.dispense(mode, amount)
    result_label.config(text=message)
    update_status()

def refill_water():
    message = dispenser.refill()
    result_label.config(text=message)
    update_status()

def cool_down():
    if dispenser.current_cold_temp > dispenser.cold_temp:
        dispenser.current_cold_temp -= 1
        update_status()
    root.after(1000, cool_down)

def heat_up():
    if dispenser.current_hot_temp < dispenser.hot_temp:
        dispenser.current_hot_temp += 1
        update_status()
    root.after(1000, heat_up)

dispenser = WaterDispenser()

root = tk.Tk()
root.title("Bebedero de Agua")

frame = tk.Frame(root)
frame.pack(pady=20)

amount_label = tk.Label(frame, text="Cantidad de agua (L):")
amount_label.grid(row=0, column=0)

amount_entry = tk.Entry(frame)
amount_entry.grid(row=0, column=1)

cold_button = tk.Button(frame, text="Agua Fría", command=lambda: dispense_water("fría"))
cold_button.grid(row=1, column=0)

hot_button = tk.Button(frame, text="Agua Caliente", command=lambda: dispense_water("caliente"))
hot_button.grid(row=1, column=1)

ambient_button = tk.Button(frame, text="Agua Ambiente", command=lambda: dispense_water("ambiente"))
ambient_button.grid(row=1, column=2)

refill_button = tk.Button(frame, text="Reponer Bidón", command=refill_water)
refill_button.grid(row=2, column=1)

level_label = tk.Label(root, text=f"Nivel de agua: {dispenser.current_level}L")
level_label.pack(pady=5)

cold_temp_label = tk.Label(root, text=f"Temp. Fría: {dispenser.current_cold_temp}°C")
cold_temp_label.pack(pady=5)

hot_temp_label = tk.Label(root, text=f"Temp. Caliente: {dispenser.current_hot_temp}°C")
hot_temp_label.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

update_status()
cool_down()
heat_up()

root.mainloop()