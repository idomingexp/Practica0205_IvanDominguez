n = int(input("Dime un Nº entero:"))
f = 1
for x in range(n):
    if (n-x) != 0:
        f = f * (n-x)
print(f)
input()