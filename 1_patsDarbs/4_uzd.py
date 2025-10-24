import math
import matplotlib.pyplot as plt
import numpy as np

# np.arange(0, 25, 1) - 0 sākuma vērtība, 25 veigu vērtība(neieskaitot, tad 24), 1 solis starp vērtībām.
# math.e = 2.71/#
B = 50000
k = 0.2
N0 = 5000

C = B / N0 - 1
print("a) C vērtība %.2f:" % C)

t = 24
N = B / (1 + C * math.e**(-k * t))
print("b)Baktērīju skaits pēc 24h: %.2f" % N)


t_laiks = np.arange(0, 25, 1)
N_populacija = B / (1 + C * np.e**(-k * t_laiks))
plt.plot(t_laiks, N_populacija, color="blue", label="N(t)")
plt.yscale("log")
plt.title("Populācijas pieaugums")
plt.xlabel("Laiks(s)")
plt.ylabel("Populācija(N)")
plt.legend()
plt.grid()

plt.savefig("1_patsDarbs/Bogdanova_4uzd.png", dpi=300)

plt.show()
