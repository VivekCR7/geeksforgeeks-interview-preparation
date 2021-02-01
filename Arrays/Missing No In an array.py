"""
Question Link: https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1
"""

def Missing_No(arr,n):
  res = (n+1)*n//2

  return res - sum(arr)

for _ in range(int(input())):
  n = int(input())
  arr = [int(i) for i in input().split()]

  print(Missing_No(arr,n))