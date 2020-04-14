def humpty_dumpty(n):
    if(n%3==0):
        print("humpty")
    elif(n%5==0):
        print("dumpty")
    elif((n%3==0)and(n%5==0)):
        print("humpty and dumpty")
    else:
        print("same number")
n=int(input("Enter the number:")
humpty_dumpty(n)
