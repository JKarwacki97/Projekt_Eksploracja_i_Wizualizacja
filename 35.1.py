import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("licea1.xlsx")

value_over_80 = data[data["Wartość"] >= 80]
values = value_over_80["Wartość"]
provinces = value_over_80["Nazwa"].str.capitalize()

sizes = values
labels = provinces
colors = plt.cm.inferno(np.linspace(0,0.5, len(sizes)))
explode = (0, 0, 0, 0, 0.1)

plt.figure(figsize = (10,8))

for label in labels:
    label.lower()

wedges, texts, autotexts = plt.pie(sizes,
                                   labels = labels,
                                   explode = explode,
                                   colors = colors,
                                   autopct = "%1.0f%%",
                                   shadow = True,
                                   startangle = 30,
                                   counterclock = False
                                   )

for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontsize(10)
    autotext.set_fontweight("bold")

for text in texts:
    autotext.set_fontsize(10)
    autotext.set_fontweight("bold")

plt.title("Liczba liceów ogólnokształcących w Polsce na przykładzie wybranych województw w 2018 roku",
          color = "black",
          fontweight = "bold",
          size = 12,
          loc = "center",
          pad = 25)

plt.axis("equal")

plt.savefig("35.1.pdf", format="pdf")

plt.show(block=True)

