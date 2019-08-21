w, h = 1000, 500
a = [10, 22, 9, 33, 21, 50, 41, 60, 80]
lis = [1, 2, 0, 3, 0, 4, 0, 5, 6]
r_w, r_h = 60 * len(a), 50
r_x, r_y = (w - r_w) // 2, (h - r_h) // 2
lis_y = h//2

f = open('longest_increasing_subsequence.svg', 'w')
f.write('<svg width="{}" height="{}">\n'.
  format(w, h))

f.write('<rect class="array" x="{}" y="{}" width="{}" height="{}"/>\n'.
  format(r_x, r_y, r_w, r_h))

for i in range(1, 9):
  temp = r_x + i * (r_w//len(a))
  f.write('<line class="array" x1="{}" y1="{}" x2="{}" y2="{}" />\n'.
    format(temp, r_y, temp, r_y + r_h))

for i, aa in enumerate(a):
  temp = r_x + i * (r_w//len(a)) + (r_w // len(a) // 3)
  f.write('<text class="array" x="{}" y="{}">{}</text>\n'.
    format(temp, r_y + r_h // 2, aa))

f.write('<rect class="lis" x="{}" y="{}" width="{}" height="{}"/>\n'.
  format(r_x, lis_y, r_w, r_h))

for i in range(1, 9):
  temp = r_x + i * (r_w//len(a))
  f.write('<line class="lis" x1="{}" y1="{}" x2="{}" y2="{}" />\n'.
    format(temp, lis_y, temp, lis_y + r_h))

for i, aa in enumerate(lis):
  if aa != 0:
    temp = r_x + i * (r_w//len(a)) + (r_w // len(a) // 3)
    f.write('<text class="lis" x="{}" y="{}">{}</text>\n'.
      format(temp, lis_y + r_h // 2, aa))

for i in range(6):
  f.write('<rect id="green_marker_{}" class="array green_marker" x="{}" y="{}" width="{}" height="{}"/>\n'.
    format(i, r_x, r_y, r_w // len(a), r_h))

f.write('</svg>')
f.close()