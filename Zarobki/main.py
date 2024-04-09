import pandas
import math
from tkinter import *

BOLD_FONT = ("Ariel", 15, "bold")
NORMAL_FONT = ("Ariel", 15, "normal")
data = pandas.read_csv("data.csv")

napiwki = [int(n) for n in data["Napiwek"] if int(n) != 0]
anulowania = [int(n) for n in data["Opłata za anulowanie"] if int(n) != 0]
kwota = [int(n) for n in data["Cena"]]
ilosc_przejazdow = [1 for n in data["Stan"] if n == "Zakończony"]
km = [float(n) for n in data["Odległość"]]

window = Tk()
window.title("Bolt")
window.config(pady=50, padx=150)

bolt = Label(text="Przejazdy Bolt", font=("Ariel", 35, "bold"))
bolt.grid(row=0, column=0, columnspan=2, pady=40)

ilosc_przejazdow_text = Label(text="Przejazdy:", font=BOLD_FONT)
ilosc_przejazdow = Label(text=sum(ilosc_przejazdow), font=NORMAL_FONT)
ilosc_przejazdow_text.grid(row=1, column=0, pady=20, padx=20, sticky="w")
ilosc_przejazdow.grid(row=1, column=1)

km_text = Label(text="Kilometry:", font=BOLD_FONT)
km = Label(text=f"{math.ceil(sum(km))}km", font=NORMAL_FONT)
km_text.grid(row=2, column=0, pady=20, padx=20, sticky="w")
km.grid(row=2, column=1)

kwota_text = Label(text="Kwota całkowita:", font=BOLD_FONT)
kwota = Label(text=f"{sum(kwota)}zł", font=NORMAL_FONT)
kwota_text.grid(row=3, column=0, pady=20, padx=20, sticky="w")
kwota.grid(row=3, column=1)

napiwki_text = Label(text="Napiwki:", font=BOLD_FONT)
napiwki = Label(text=f"{(sum(napiwki))}zł", font=NORMAL_FONT)
napiwki_text.grid(row=4, column=0, pady=20, padx=20, sticky="w")
napiwki.grid(row=4, column=1)

anulowania_text = Label(text="Opłaty za anulowanie:", font=BOLD_FONT)
anulowania = Label(text=f"{sum(anulowania)}zł", font=NORMAL_FONT)
anulowania_text.grid(row=5, column=0, pady=20, padx=20, sticky="w")
anulowania.grid(row=5, column=1)

window.mainloop()
