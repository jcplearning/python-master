import pandas as pd
import matplotlib.pyplot as plt

tips = pd.read_csv('inbound/tips.csv')

print(tips.head())

plt.plot(tips['total_bill'], tips['tip'], 'go', scalex=True, scaley=True)
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

