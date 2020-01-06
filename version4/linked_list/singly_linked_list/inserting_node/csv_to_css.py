import numpy as np
from math import cos, sin, pi

# Open the input csv file
f = open('input.csv')

# Initialize the output to empty list of strings
animation = []

# Iterate through each row except for the first which is header row
for row in f.readlines()[1:]:

  # Extract element ID which is the first column of the row
  elem = row.split(',')[0]

  # Output contents
  animation.append(f'#{elem} {{')

  # Remove the element ID from the row
  row_without_elem = row.lstrip(elem)
  
  # Strip the new line character and empty rows (commas) from the right of the row
  row_r_striped = row_without_elem.rstrip().rstrip(',')
  
  # Strip the empty rows (commas) from the left of the row
  row_lr_striped = row_r_striped.lstrip(',')
  
  # Animation delay is the difference in the lengths of
  # the above two strings and a correcting factor of -1
  anim_delay = len(row_r_striped) - len(row_lr_striped) - 1
  
  # Split the striped row by commas to extract the frames
  frames = row_lr_striped.split(',')
  
  # Aniation duration is the count of the frames
  # Subtracting 1 as the last frame does not consume time
  anim_durn = len(frames) - 1
  
  # Output contents
  s = '\tanimation: {}_anim {}s ease {}s 1 normal forwards running;\n}}\n\n@keyframes {}_anim {{'
  animation.append(s.format(elem, anim_durn, anim_delay, elem))

  # Iterate through all frames enumerating its time number
  for time, frame in enumerate(frames):
    
    # Extract the changes in the properties by splitting the current frame by semicolons
    changes = frame.split(';')

    # If frame is empty continue with next frame
    if not changes[0]:
      continue

    # Calculate time in percent with respect to the animation duration
    time_in_percent = time / anim_durn * 100

    # Output contents
    animation.append(f'\t{time_in_percent:.2f}% {{')

    # Initialize transformation matrix to an identity matrix
    mat = np.identity(3)

    # Iterate through all the property changes
    for change in changes:

      # Extract property and value from change
      # Change will consist of property:value format
      prop, val = change.split(':')
      
      # Multiply the transformation matrix with appropriate matrix
      if prop == 'tx':
        mat = np.dot(np.array(([1, 0, float(val)], [0, 1, 0], [0, 0, 1])), mat)
      elif prop == 'ty':
        mat = np.dot(np.array(([1, 0, 0], [0, 1, float(val)], [0, 0, 1])), mat)
      elif prop == 'sx':
        mat = np.dot(np.array(([float(val), 0, 0], [0, 1, 0], [0, 0, 1])), mat)
      elif prop == 'sy':
        mat = np.dot(np.array(([1, 0, 0], [0, float(val), 0], [0, 0, 1])), mat)
      elif prop == 'r':
        c = cos(float(val) * pi / 180)
        s = sin(float(val) * pi / 180)
        mat = np.dot(np.array(([c, -s, 0], [s, c, 0], [0, 0, 1])), mat)
      elif prop == 'op':
        animation.append(f'\t\topacity: {val};')
    
    # If the frame does not contain only opacity change
    if not (len(changes) == 1 and changes[0].startswith('op')):

      # Output contentsR
      animation.append(
        f'\t\ttransform: matrix({mat[0][0]}, {mat[1][0]}, {mat[0][1]}, {mat[1][1]}, {mat[0][2]}, {mat[1][2]});')

    # Output contents
    animation.append('\t}')

  # Output contents
  animation.append('}\n')

# Create animation.css file and write the contents into it
open('animation.css', 'w').write('\n'.join(animation))