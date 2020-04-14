def print_string(*n):
    for i in n:
        j=tuple(i)
        print(j)
        o=list(j)
        o[2]="r"
        o[3]="u"
        for k in o:
            print(k)
print_string(['hello','how','are','you'])
