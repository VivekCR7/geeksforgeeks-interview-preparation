"""
Question Link: https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

"""

def subarraysum(arr,n,s):
  start = 0
  i = 1
  curr_sum = arr[0]
  while i<=n:
    while curr_sum > s and start < i-1:
      curr_sum -= arr[start]
      start+=1
    
    if curr_sum == s:
      print(start+1,i)
      return 
    
    if i < n:
      curr_sum += arr[i]
    i+=1

  print("-1")
  return 

for _ in range(int(input())):
  n, s = map(int,input().split())
  arr = [int(i) for i in input().split()]

  subarraysum(arr,n,s)
