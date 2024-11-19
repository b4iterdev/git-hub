def cal_mean(*args): 
    inpList = list(args)
    sum = float()
    for i in inpList:
        sum += i
    return (sum/len(inpList))

print(cal_mean(8,2,5,123))
