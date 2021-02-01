"""
Question Link: https://practice.geeksforgeeks.org/problems/count-the-triplets4615/1

"""
def count_the_triplets(arr,n):
  
  count = 0
  
  for i in range(n):
    for j in range(i+1,n):
      if arr[i]+arr[j] in arr:
        count+=1
    
  print(count)
  return


for _ in range(int(input())):
  n = int(input())
  arr = [int(i) for i in input().split()]
  
  count_the_triplets(arr,n)
