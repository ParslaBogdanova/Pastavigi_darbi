import math
import matplotlib.pyplot as plt

Vo = [15, 16, 19, 22]
lenkis = math.pi/4
ho = 3
h1 = 3.5
b = 3.5
g = 9.81


# v=len(Vo), nosaka, cik elementu ir sarakstā Vo.
# punkti=[0]*v, vienkārš veidz, kā izveidot srakastu(list)/#
v = len(Vo)
punkti = [0] * v


for i in range(v):
    Vx = Vo[i] * math.cos(lenkis)
    Vy = Vo[i] * math.sin(lenkis)

    T = b/Vx
    yT = Vy * T - ((g*T**2)/2)

    if yT < ho or yT > h1:
        punkti[i] = 0
    elif ho <= yT < 0.5*(h1+ho):
        punkti[i] = 1
    else:  # 0.5*(h1+ho) <= yT <= h1
        punkti[i] = 2

    print("\nVo= %d m/s, \ny(T)= %.2f m, \npunkti= %d" %
          (Vo[i], yT, punkti[i]))

# marker='o' nosaka punktu simbolu(marķieri) uz grafika. o aplis;
# https://www.w3schools.com/python/matplotlib_markers.asp
plt.plot(Vo, punkti, marker='o', color="black")
plt.xlabel("Sākuma ātrums Vo(m/s)")
plt.ylabel("Punkti")
plt.yticks([0, 1, 2])
plt.title("Trāpīt mērķī")
plt.legend()
plt.grid()

plt.savefig("1_patsDarbs/Bogdanova_5uzd.png", dpi=300)

plt.show()
