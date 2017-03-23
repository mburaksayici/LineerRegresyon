import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as plt

data = pd.read_csv("linear.csv")

x = data["metrekare"]
y = data["fiyat"]

x = x.reshape(99,1)
y = y.reshape(99,1)

lineerregresyon = lr() # Lineer Regresyonu çağırdık.

lineerregresyon.fit(x,y) # Verilerimizi x ve y eksenine oturttuk.

lineerregresyon.predict(x) #x'e göre, yani metrekareye göre ev fiyatlarını tahmin edeceğiz.

m = lineerregresyon.coef_ # Coefficient - yani katsayı, bu komutla eğimimizi
                          # Yani m i buluyoruz.
b= lineerregresyon.intercept_ # Intercept - b dir. yani y = mx+b 'de x'e sıfır 
                              # verdiğimizde kalan değer.

a = np.arange(150)

plt.scatter(x,y) # Gerçek verilerimizi nokta nokta, scatter ile cizdiriyoruz.
plt.scatter(a,m*a+b, c="red",marker=">")
plt.show()

















print('Eğim: ', lineerregresyon.coef_)
print('Y de kesiştiği yer: ', lineerregresyon.intercept_)


print("Denklem")
print("y=",m,"x+",b)



