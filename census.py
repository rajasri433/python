import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C://Users/Devi/Desktop/censes.csv")
martial_income = data.groupby('Household Type')['Income'].mean().reset_index()
print("Average Income by Household Type:\n", martial_income)
fig,axs = plt.subplots(3, 2, figsize=(15,10))
axs[0,0].bar(martial_income['Household Type'], martial_income['Income'])
axs[0,0].set_title("Average Income by Household Type")
axs[0,0].set_xlabel("Household Type")
axs[0,0].set_ylabel("Average Income")
plt.tight_layout()
plt.show()
