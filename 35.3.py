import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("koleje3.csv", sep="\\s+", on_bad_lines="skip")

eurostar = data[data["Marka"] == "Eurostar"]
amtrak = data[data["Marka"] == "Amtrak"]

df_eurostar_melted = eurostar.melt(id_vars =  ["Marka"], var_name = "Rok", value_name = "Wartość")
df_amtrak_melted = amtrak.melt(id_vars = ["Marka"], var_name = "Rok", value_name = "Wartość")

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

fig.suptitle("Porównanie liczby pasażerów Eurostar i Amtrak (2010-2019)", fontweight = "bold", fontsize = 16)

axes[0].bar(df_eurostar_melted["Rok"], df_eurostar_melted["Wartość"], color = "darkgray")
axes[0].set_title("Eurostar", fontweight = "bold", fontsize = 13)
axes[0].set_ylabel("Wartość", fontweight = "bold", fontsize = 13)
axes[0].set_xticks(df_eurostar_melted["Rok"])
axes[0].set_xticklabels(df_eurostar_melted["Rok"], rotation = 45)
axes[0].set_yticks(range(0, 13000, 2000))
axes[0].grid(True, linestyle = "--", alpha = 0.5, color = "black")

axes[1].bar(df_amtrak_melted["Rok"], df_amtrak_melted["Wartość"], color = "silver")
axes[1].set_title("Amtrak", fontweight = "bold", fontsize = 13)
axes[1].set_ylabel("Wartość", fontweight = "bold", fontsize=13)
axes[1].set_xlabel("Rok", fontweight = "bold", fontsize=13)
axes[1].set_xticks(df_amtrak_melted["Rok"])
axes[1].set_xticklabels(df_amtrak_melted["Rok"], rotation=45)
axes[1].set_yticks(range(0, 13000, 2000))
axes[1].grid(True, linestyle = "--", alpha = 0.5, color = "black")

fig.legend(["Eurostar", "Amtrak"], loc = 1, fontsize = 10)

plt.tight_layout()

plt.savefig("35.3.eps", format="eps")
plt.show()


