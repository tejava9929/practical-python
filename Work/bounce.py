# bounce.py
#
# Exercise 1.5
InitialHeight = 100

Height = InitialHeight
for i in range(10):
    Height = Height*3/5
    print(i+1, end=' ')
    print(round(Height,4))

