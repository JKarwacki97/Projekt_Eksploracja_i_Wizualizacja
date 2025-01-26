import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("ceny5.xlsx").set_index("Rok")

trout = data[data["Rodzaje produktów"] == "pstrąg świeży niepatroszony - za 1 kg"]["Wartosc"]
hake = data[data["Rodzaje produktów"] == "filety z morszczuka mrożone - za 1kg"]["Wartosc"]
herring = data[data["Rodzaje produktów"] == "śledź solony, niepatroszony - za 1kg"]["Wartosc"]

x = trout.index
y = trout.values
y2 = hake.values
y3 = herring.values

plt.figure(figsize = (10,8))

plt.plot(x, y2, "green", linestyle = "-", label = "Morszczuk", lw = 2)
plt.plot(x, y, "orange", linestyle = "--", label = "Pstrąg", lw = 2)
plt.plot(x, y3, "black", linestyle = "-.", label = "Śledź", lw = 2)
plt.grid(True, which = "both", color = "gray", linewidth = 0.1, linestyle = "--")
plt.title("Cena wybranych ryb [PLN] 2010/2016", fontweight = "bold", fontsize = 16)
plt.xlabel("Rok", fontweight = "bold", fontsize = 12)
plt.ylabel("Cena [PLN]", fontweight = "bold", fontsize = 12)
plt.legend(loc = 2)

plt.savefig("35.5.webp", format = "webp")
plt.show(block = True)
