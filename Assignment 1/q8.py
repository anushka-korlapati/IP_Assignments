pop=[50, 1450, 1400, 1700, 1500, 600, 1200]
l=[2.5, 2.1, 1.7, 1.3, 0.9, 0.5, 0.1]

def CalcTotal(x):
    currentPopulation=0
    for i in x:
        currentPopulation+=i
    return currentPopulation

initialPopulation=CalcTotal(pop)

j=0
k=0

years=0
calculate = 0
h=0
sum = 0
while True:
    for i in range(7):
        pop[i] += ((l[i]/100)+h)*pop[i]
    h -= 0.001
    calculate = CalcTotal(pop)
    a = initialPopulation
    initialPopulation = calculate
    calculate = a
    
    if calculate > initialPopulation:
        break
    years += 1


print(years)
print(int(calculate),"millions")