from os import *
from sys import *
from collections import *
from math import *


def knapSackMemo(weights,values,index,capacity,dp):
    #base case
    if index==0:
        if weights[0]<=capacity:
            return values[0]
        else:
            return 0 
    if dp[index][capacity]!=-1:
       return dp[index][capacity]
    include=0 
    if weights[index]<=capacity:
        include=values[index]+knapSackMemo(weights,values,index-1,capacity-weights[index],dp)
    exclude=0+knapSackMemo(weights,values,index-1,capacity,dp)
    dp[index][capacity]=max(include,exclude)
    return dp[index][capacity]


def knapSack(W, wt, val, n):

	# Base Case
	if n == 0 or W == 0:
		return 0
	if (wt[n-1] > W):
		return knapSack(W, wt, val, n-1)
	else:
		return max(
			val[n-1] + knapSack(
				W-wt[n-1], wt, val, n-1),
			knapSack(W, wt, val, n-1))


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
dp=[]
for i in range(n):
	t=[]
	for j in range(W+1):
		t.append(-1)
	dp.append(t)
print(knapSackMemo(wt,val,n-1,W,dp))


