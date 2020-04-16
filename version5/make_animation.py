# Open the input keyframes.csv file
with open('keyframes.csv') as f:

  for line in map(str.strip, f.readlines()[1:]):

    row = line.split(',')
    print(row)

    elem = row[0]
    print(elem)

    row_r_striped = line[len(elem)+1:].rstrip(',').split(',')
    print(row_r_striped)

    row_lr_striped = row_r_striped.strip(',').split(',')
    print(row_lr_striped)

    