s = set()

cost=0

def waterjug(three, four, p1, p2, level):
    global cost
    if level == 3:
        print("\n\nCOST=:", cost)
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
            waterjug(three, 0, three, four, level+1)
    # fill 4l from source
    if four < 4:
        if (three, 4) not in s:
            print("Fill 4 Gallon Container")
            cost+=1
            waterjug(three, 4, three, four, level+1)

    # sending water to 4l
    if three > 0:
        # empty 3l onto floor
        if (0, four) not in s:
            print("Empty 3 Gallon Container")
            cost+=1
            waterjug(0, four, three, four, level+1)
        # pour 3l into 4l
        else:
            if four < 4:
                fillable = 4 - four
                # empty 3l fully into 4l
                if fillable > three:
                    if (0, four+three) not in s:
                        print("Transfer Contents of 3 Gallon to 4 Gallon - non overflow")
                        cost+=1
                        waterjug(0, four+three, three, four, level+1)
                # 3l still has remaining
                else:
                    if (three-fillable, 4) not in s:
                        print("Transfer Contents of 3 Gallon to 4 Gallon- overflow")
                        cost+=1
                        waterjug(three-fillable, 4, three, four, level+1)
    # empty 4l onto floor
    if three < 3:
        # filling 3l from 4l
        if four > 0:
            fillable = 3 - three
            # emptying 4l into 3l fully
            if fillable > four:
                if (three+four, 0) not in s:
                    print("Transfer Contents of 4 Gallon to 3 Gallon - non overflow")
                    cost+=1
                    waterjug(three+four, 0, three, four, level+1)
            # 4l still has remaining water
            else:
                if (3, four-fillable) not in s:
                    print("Transfer Contents of 4 Gallon to 3 Gallon -  overflow")
                    cost+=1
                    waterjug(3, four - fillable, three, four, level+1)
        # filling 3l from source
        else:
            if (3, four) not in s:
                print("Fill 3 Gallon Container")
                cost+=1
                waterjug(3, four, three, four, level+1)



waterjug(0, 0, -1, -1, 0)

