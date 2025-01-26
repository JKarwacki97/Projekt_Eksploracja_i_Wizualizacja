import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("jezykiobce2.xlsx")

data_provinces = data[data["Nazwa"].isin(["LUBELSKIE", "LUBUSKIE"])]
data_provinces_limited = data_provinces[["Nazwa", "Języki obce", "Wartość"]]

data_provinces_limited_pivot = data_provinces_limited.pivot(index = "Języki obce", columns = "Nazwa", values = "Wartość")
data_provinces_limited_pivot.columns = data_provinces_limited_pivot.columns.astype(str).str.capitalize()

colors = ["gold", "green"]

ax = data_provinces_limited_pivot.plot(kind = "bar",
                                       width = 0.8,
                                       color = colors,
                                       figsize = (10,8))

for container in ax.containers:
    ax.bar_label(container, fmt = "%.0f", label_type = "edge")

ax.set_ylabel("Ilość osób", fontweight = "bold", fontsize = 10)
ax.set_title("Popularność języków obcych na przykładzie wybranych województw", fontweight = "bold", fontsize = 11)
ax.set_xlabel("Języki obce", fontweight = "bold", fontsize = 10)
ax.set_xticklabels(data_provinces_limited_pivot.index, rotation = 0)
ax.legend(title = "Województwa")
ax.grid(axis = "y", color = "gray", linewidth = 0.5, linestyle = "--")

plt.tight_layout()

plt.savefig("35.2.jpeg", format = "webp")
plt.show(block = True)

