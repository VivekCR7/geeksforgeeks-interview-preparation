"""
Question Link: https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

"""
import sys
def kadanes_algorithm(arr,n):
  max_so_far = -sys.maxsize
  max_ending_here = 0

  for i in range(n):
    max_ending_here += arr[i]
    if max_so_far < max_ending_here:
      max_so_far = max_ending_here

    if max_ending_here < 0:
      max_ending_here = 0
    
  return max_so_far

for _ in range(int(input())):
  n = int(input())
  arr = [int(i) for i in input().split()]

  print(kadanes_algorithm(arr,n))

