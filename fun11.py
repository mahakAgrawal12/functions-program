def stars(n):
##n=5
    for i in range(1,n+1):
        for j in range(1,i):
            print("*",end="  ")
        print()
stars(5)
