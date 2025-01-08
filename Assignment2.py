y = [x**2 for x in range (5)]
print(y)

x = 1
def my_function():
    x = 2
    print(x)
print(x)
my_function()
print(x)

x = 'String'
y = 10
z = 5.0
print(x + x) # print command 1
print(y + y) # print command 2
#print(y + x) # print command 3
print(y + z) # print command 4

s = (1,2,3)
print(s[-0:0])

x = (1,2,3)
print(sum(x))

print("0"+"1")
print(str(range(10)))
x = "125000"
print(x.isnumeric())

x = {1,2,3}
y = {1,2,3,4}
print(x.issubset(y))

import copy
x = [1,[2]]
y = copy.copy(x)
z = copy.deepcopy(x)
print(y is z)

if False:
    print("False!")
elif True:
    print("Now True!")
else:
    print("Finally True!")

bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}   
for bear in bears:
    if (bears[bear] == "friendly"):
        print("Hello, "+bear+" bear!")
else:
    print("odd")

n=100
number_of_times = 0
while n >= 1:
    n //= 2
    number_of_times += 1
print(number_of_times)

F = open("input.txt", "w")
F.write("Hello\nWorld")
F.close()
lines = []
for line in open("input.txt"):
    lines.append(line.strip())
print(lines)

def modify(mylist):
    mylist[0] *= 10
    return(mylist)
L = [1, 3, 5, 7, 9]
M = modify(L)
print(L)
print(M is L)

def increment(n):
    n += 1
    return n

n = 1
while n < 10:
    n = increment(n)
print(n)

class NewList(list):
    def remove_max(self):
        self.remove(max(self))
    def append_sum(self):
        self.append(sum(self))

x = NewList([1,2,3])
while max(x) < 10:
    x.remove_max()
    x.append_sum()

print(x)

from matplotlib import pyplot as plt
plt.plot([0,1,2],[0,1,4],"rd-")
plt.show()

import random
print(random.choice([0,1]))

import pandas as pd
data = pd.Series([1,2,3,4])
data = data.ix[[3,0,1,2]]
print(data)