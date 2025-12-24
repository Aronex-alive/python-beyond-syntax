#Creating a Do while in python
i=0
while True:
    print(i)
    i+=1
    if i>=5:
        break
# We can use break and continue functions in boyh for as well as while loops
# Example of continue in for loop
for i in range(10):
    if i%2==0:
        continue
    print(i)
# Example of break in while loop
j=0
while j<10:
    if j==5:
        break
    print(j)
    j+=1