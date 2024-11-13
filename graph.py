import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C://Users/Devi/Documents/matches.csv")
matches_per_season = data.groupby('Winner').size().reset_index(name='Match_Count')
print(matches_per_season)

plt.bar(matches_per_season['Winner'],
matches_per_season['Match_Count'])
plt.xlabel('Winner')
plt.ylabel('Number of Matches')
plt.title('Number of Matches in Each Winner')
plt.show()