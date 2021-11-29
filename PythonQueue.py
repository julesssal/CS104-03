names =[]
for x in range(10):
    name = str(input("Enter name: "))
    names.append(name)

for i in range(len(names)):
    print(names.pop(0))

