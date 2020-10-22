

def RecursionSolve(encoding,result,count):
    if isinstance(encoding,list):
        for i in encoding:
            if i>90:
                global t
                t=(i-90)+64
                if t <= 90:
                    result.append("A"+chr(t))
                else:
                    RecursionSolve(t,result,count)
            else:result.append(chr(t))
    else:
        if encoding > 90:
            count+=1
            encoding=(encoding-90)+64
            if encoding <= 90:
                result.append(chr(65+count)+chr(encoding))
            else:
                RecursionSolve(encoding,result,count)
        else:
            result.append
            return result
