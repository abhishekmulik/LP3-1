def fracKnapsack(wt,val,W):
    n = len(wt)
    if n == 0:
        return 0
    else:
        maxRatioIndex = -1
        maxRatio = -1
        for i in range(n):
            if val[i]/wt[i] > maxRatio:
                maxRatioIndex = i
                maxRatio = val[i]/wt[i]
    maxVal = maxRatio*W
    return maxVal

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print("The answer is :",fracKnapsack(wt, val, W))
