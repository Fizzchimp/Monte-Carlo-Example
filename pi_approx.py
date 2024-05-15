import matplotlib.pyplot as plt
import random
from math import sqrt

line = {"x": [], "y": []}

iters = 100000
for i in range(iters + 1):
    x = i / iters
    line["x"].append(x)
    line["y"].append(sqrt(1 - x ** 2))
    

bPoints = [[], []]
aPoints = [[], []]
for i in range(iters):
    x, y = random.randint(0, iters), random.randint(0, iters) / iters
    
    if line["y"][x] > y:
        bPoints[0].append(x / iters)
        bPoints[1].append(y)
        
    if line["y"][x] < y:
        aPoints[0].append(x / iters)
        aPoints[1].append(y)
        
        
plt.plot(line["x"], line["y"], color = "r", label = "f(x) = √(1 - x²)")
plt.scatter(bPoints[0], bPoints[1], color = "y", s = iters / 10000000, label = "Below f(x)")
plt.scatter(aPoints[0], aPoints[1], color = "b", s = iters / 10000000, label = "Above f(x)")

pi = 4 * len(bPoints[0]) / iters
plt.title(f"Pi ≈ {pi}")
plt.legend(shadow = True, markerscale = 50)
plt.show()