# Input
# arr = [60, 34, 78, 89, 23, 2, 4, 76, 3]
# target = 23

arr.sort()
low = 0
high = len(arr)-1
mid = 0

found = False
while low <= high:
  mid = (high + low )//2
  if arr[mid] < target:
    low = mid + 1
  elif arr[mid] > target:
    high = mid-1
  else:
    found = True
    break
    
print(found)
