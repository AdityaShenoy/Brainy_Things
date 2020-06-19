def interpolation_search(a, key):
  l, r = 0, len(a) - 1
  while l <= r:
    mid = l + ((key - a[l]) * (r - l) // (a[r] - a[l]))
    if key == a[mid]:
      return mid
    if key < a[mid]:
      r = mid - 1
    else:
      l = mid + 1
  return -1

a = [1, 3, 4, 7, 8, 12, 15, 17, 19]
# a = [1]
# a = [6]
# a = []
key = 4
# key = 0
# key = 5
# key = 20
print(interpolation_search(a, key))