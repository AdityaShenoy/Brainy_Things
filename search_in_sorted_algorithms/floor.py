def floor(a, key):
  if key < a[0]:
    return
  l, r = 0, len(a) - 1
  while (l + 1) < r:
    mid = (l + r) // 2
    if key == a[mid]:
      return key
    if key > a[mid]:
      l = mid
    else:
      r = mid - 1
  return a[r] if a[r] <= key else min(a[l], a[r])

a = [1, 3, 4, 7, 8, 12, 15, 17, 19]
# a = [1]
# a = [6]
# a = []
key = 4
# key = 0
# key = 5
# key = 20
for i in range(21):
  print(i, floor(a, i), a)