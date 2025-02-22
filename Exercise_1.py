#Time complexity is O(logn)
#Space complexity is O(1)


# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  l=0
  r=len(arr)-1
  middle=0
  while l<=r:
    middle=(l+r)//2
    if arr[middle]>x:
      r=middle-1
    elif arr[middle]<x:
      l=middle+1 
    else:
      return middle
  return -1
  
  



  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
