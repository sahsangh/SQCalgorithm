import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot

df = pd.read_csv("AAPL.csv")
df.head(5)
plt.figure()
lag_plot(df['Open'], lag=3)
plt.title('APPLE Stock - Autocorrelation plot with lag = 3')
plt.show()

df = pd.read_csv("TSLA.csv")
df.head(5)
plt.figure()
lag_plot(df['Open'], lag=3)
plt.title('TESLA Stock - Autocorrelation plot with lag = 3')
plt.show()

df = pd.read_csv("AMZN.csv")
df.head(5)
plt.figure()
lag_plot(df['Open'], lag=3)
plt.title('AMAZON Stock - Autocorrelation plot with lag = 3')
plt.show()

df = pd.read_csv("GOOGL.csv")
df.head(5)
plt.figure()
lag_plot(df['Open'], lag=3)
plt.title('GOOGLE Stock - Autocorrelation plot with lag = 3')
plt.show()