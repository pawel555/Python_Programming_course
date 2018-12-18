import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import math
import numpy as np

df = pd.read_csv('L06_Ecommerce_Customers.csv')

# df.info()
# print('\nDescribe:\n')
# print(df.describe(include='all'))
# print(df.describe())


# jpl = sb.jointplot(data=df, x='Time on Website', y='Yearly Amount Spent')

# jpl2 = sb.jointplot(data=df, x='Time on App', y='Yearly Amount Spent')

# jpl3 = sb.jointplot(data=df, x='Time on App', y='Length of Membership', kind="hex", color="#4CB391")

# pr = sb.pairplot(data=df)

# im = sb.lmplot(data=df, x='Yearly Amount Spent', y='Length of Membership')

# plt.show()

x = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']].values
y = df['Yearly Amount Spent'].values

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=101)

lr = LinearRegression()

lr.fit(X_train, Y_train)

print(lr.coef_)

predicted = lr.predict(X_test)

fig2, ax2 = plt.subplots()
ax2.scatter(Y_test, predicted)
fig2.show()

MAE = mean_absolute_error(Y_test, predicted)
MSE = mean_squared_error(Y_test, predicted)
RMSE = math.sqrt(MSE)

print(f'MAE: {MAE}')
print(f'MSE: {MSE}')
print(f'RMSE: {RMSE}')

sb.distplot(predicted, bins=30, axlabel='Yearly Amount Spent', hist_kws=dict(edgecolor="k", linewidth=2))
plt.show()

coefs = np.asmatrix(lr.coef_)

print(coefs)


df2 = pd.DataFrame(coefs,  columns=['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership'])

df2.info()
print(df2.describe(include='all'))

# jasne za na apce, no kurde popacz na koefy
