print("Full Pyramid Pattern of Stars (*): ")
for i in range(5):
    for s in range(-6, -i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()
print("Inverted Full Pyramid of Stars (*): ")
for i in range(5):
    for s in range(i):
        print(" ", end="")
    for j in range(i, 5):
        print("* ", end="")
    print()