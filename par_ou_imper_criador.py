f = open("batota.txt","w+")

for i in range(10001):
    if i % 2 == 0:
        oddeven = "par"
    else:
        oddeven = "impar"

    f.write("if num == {}:\n    print('Seu número é {}')\n".format(str(i),oddeven))
    f.write("if num > 10000:\n    print('Não sei esse número, desculpa :)!!!'")
