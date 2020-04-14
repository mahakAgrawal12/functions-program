def speed(s):
    if(s<=70):
        print("ok")
    else:
        sp=(s-70)//5
        if(sp<=12):
            print(sp)
        else:
            print("license suspended")
sp=int(input("Enter the speed:"))
sol=speed(sp)
print(sol)

