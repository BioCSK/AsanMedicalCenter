

def RecursionSolve(encoding):
    count=0
    temp=[]
    for i in encoding:
        if i <=90:
            temp.append(chr(i))
        else:
            while (i > 90):
            
                count+=1
                i=i-90+64
                if i <= 90:
                    temp.append(chr(64+count)+chr(i))
                    count=0
    return temp


