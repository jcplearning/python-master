import pandas as pd
import matplotlib.pyplot as plt


# reading the database
data = pd.read_csv("inbound/tips.csv")

total_tip = pd.DataFrame(data.groupby('day')['tip'].sum()).reset_index()
total_tip.columns = ['Days','Total Tip']

print(total_tip)

# Bar chart with day against tip
plt.bar(total_tip.Days, total_tip['Total Tip'])

plt.title("Bar Chart")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# Adding the legends
plt.show()


