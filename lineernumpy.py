import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = pd.read_csv("linear.csv")  # Verimizi okuyalım

print(data) # Veriyi inceleyelim.

x = data["metrekare"] # Metrekareleri bir axis' e çekelim, panda nın özelliği.
y = data["fiyat"] # Üstteki ile aynı.
x = pd.DataFrame.as_matrix(x) # NumPy matrisine dönüştürelim.
y = pd.DataFrame.as_matrix(y) # NumPy matrisine dönüştürelim.

print(x)
print(y) # Ne oluşturduğumuza bakmak önemli.

plt.scatter(x,y) # Ne oluşturduğumuza 2 boyutlu grafikte bakalım.

#Doğrumuzun denklemi y = m*a+b , Biz ise en uygun m ve b yi arıyoruz. m Eğim, b kesim noktası


m,b = np.polyfit(x,y,1)# NumPy bizim için grafiğe oturtuyor çizgimizi. Bunu matematiksel
# İşlemlerle uzun uzun da yapabilirdik. Fakat NumPy halihazırda sahip. Çok kafa karıştırmamak 
# Adına böylesi daha iyi.
# np.polyfit(x ekseni, y ekseni, kaçıncı dereceden polinom denklemi) ki biz birinci dereceden kullanacağız.


a = np.arange(150) # Denklemimiz hazır. a nın aralığını ayarlayalım.

plt.scatter(x,y) # Scatter ile nokta çizdirimi yapıyoruz.
plt.plot(m*a+b) # 


z = int(input("Kaç metrekare?"))
tahmin = m*z+b
print(tahmin)

plt.scatter(z,tahmin,c="red",marker=">")

plt.show()
print("y=",m,"x+",b)

