import math

# %d - vesels skaitlis (integer), piem., 50;
# %.2f - decimālskaitlis(float)ar 2 zīmēm aiz komata, piem., 4,26, ja rezutāts 5,138, tad terminālī rādīs 5,14;
# % v[i] - v[i] vērtība, bet % v[i] tiek izmantots %d formātu, lai ievietotu vērtību "šajā vietā"/#

g = 9.81
r = [2.7, 3.43, 5.62, 7.1]
num_loops = len(r)
v = [0] * num_loops

for i in range(num_loops):
    print("\nLoop %d:" % (i+1))
    print("r= %.2f m " % r[i])
    v[i] = math.sqrt(r[i] * g)
    print("sqrt(r*g)= %.2f m/s" % v[i])
    v[i] = v[i] * 3600 / 1000
    print("Convert to km/h: %.2f" % v[i])

print("\nResults:")
for i in range(num_loops):
    print("Loop %d: %.2f km/h" % (i+1, v[i]))
