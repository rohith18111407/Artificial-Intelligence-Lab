cost=0
def waterjug(three, four, p1, p2, level, x):
    global cost
    #cost=0
    if level == x:
        print("\n\nCOST in this level=",cost)
        return
    if (three, four) not in s:
        print(three, four, "Parents :: ", p1, p2, "Level :: ", level, end="\n")
        s.add((three, four))
    if four == 2:
        print("Goal State")

    if four > 0:
        if (three, 0) not in s:
            print("Empty 4 Gallon Container")
            cost+=1
            waterjug(three, 0, three, four, level + 1, x)

    if four < 4:
        if (three, 4) not in s:
            print("Fill 4 Gallon Container")
            cost+=1
            waterjug(three, 4, three, four, level + 1, x)
    
    if three > 0:
        if (0, four) not in s:
            print("Empty 3 Gallon Container")
            cost+=1
            waterjug(0, four, three, four, level + 1, x)
        else:
            if four < 4:
                fillable = 4 - four
                if fillable > three:
                    if (0, four + three) not in s:
                        print("Transfer Contents of 3 Gallon to 4 Gallon - non overflow")
                        cost+=1
                        waterjug(0, four + three, three, four, level + 1, x)
                else:
                    if (three - fillable, 4) not in s:
                        print("Transfer Contents of 3 Gallon to 4 Gallon- overflow")
                        cost+=1
                        waterjug(three - fillable, 4, three, four, level + 1, x)

    if three < 3:
        if four > 0:
            fillable = 3 - three
            if fillable > four:
                if (three + four, 0) not in s:
                    print("Transfer Contents of 4 Gallon to 3 Gallon - non overflow")
                    cost+=1
                    waterjug(three + four, 0, three, four, level + 1, x)
            else:
                if (3, four - fillable) not in s:
                    print("Transfer Contents of 4 Gallon to 3 Gallon -  overflow")
                    cost+=1
                    waterjug(3, four - fillable, three, four, level + 1, x)
        else:
            if (3, four) not in s:
                print("Fill 3 Gallon Container")
                cost+=1
                waterjug(3, four, three, four, level + 1, x)


for i in range(1, 8):
    s = set()
    print()
    print("--" * 40)
    print("\nLevel = ", i - 1)
    waterjug(0, 0, -1, -1, 0, i)
    
