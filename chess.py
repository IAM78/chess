n= int(input("n::"))

m=int(input("m::"))


for q in range(n):

    if q%2!=0:

        for i in range(m):

            print("*#",end="")

    else:

        for i in range(m):

            print("#*",end="")

    print()