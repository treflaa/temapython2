import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

print(df)
df.plot(title="Toate Valorile")
plt.show()

X = 5 
Y = 12

print(df.head(X))
df.head(X).plot(title=f"Primele {X} Valori")
plt.show()

print(df.tail(Y)[['Durata', 'Puls']])
df.tail(Y)[['Durata', 'Puls']].plot(title=f"Ultimele {Y} Valori pentru Durata și Puls", color = ["red","black"])
plt.show()
