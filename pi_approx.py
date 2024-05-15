import matplotlib.pyplot as plt
import random
from math import sqrt

def main():
    line = [[], []]

    iters = 100000
    for i in range(iters + 1):
        num = i / iters
        line[0].append(num)
        line[1].append(sqrt(1 - num ** 2))
    

    bPoints = [[], []]
    aPoints = [[], []]
    for i in range(iters):
        x, y = random.randint(0, iters), random.randint(0, iters) / iters
    
        if line[1][x] > y:
            bPoints[0].append(x / iters)
            bPoints[1].append(y)
        
        if line[1][x] < y:
            aPoints[0].append(x / iters)
            aPoints[1].append(y)
        
        
    plt.plot(line[0], line[1], color = "r", label = "f(x) = √(1 - x²)")
    plt.scatter(bPoints[0], bPoints[1], color = "y", s = 400 / iters, label = "b: Below f(x)")
    plt.scatter(aPoints[0], aPoints[1], color = "b", s = 400 / iters, label = "a: Above f(x)")


    pi = 4 * len(bPoints[0]) / iters
    plt.title(f"Pi ≈ {pi}")
    plt.legend(shadow = True, markerscale = 50, loc = "upper right")
    plt.show()
    
def approx():
    n = 0
    b = 0
    while True:
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if y < sqrt(1 - x ** 2):
            b += 1   
        n += 1
        if n % 1000000 == 0:
            print(f"Pi ≈ {4 * b / n}")
            
main()
#approx()