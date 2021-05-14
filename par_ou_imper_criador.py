f = open("batota.txt","w+")

for i in range(10001):
    if i % 2 == 0:
        oddeven = "even"
    else:
        oddeven = "odd"

    f.write("if num == {}:\n    print('Your number is {}')\n".format(str(i),oddeven))