with open("tables.txt",'a') as tables:
    for i in range(2,12):
        for j in range(1,12):
            print("{1:>2} times {0} is {2}".format(i,j,i*j),file=tables)
        print("-"*20,file=tables)