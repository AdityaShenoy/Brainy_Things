# Mapping of shorthands used in the input csv file to the actual property
prop_shorthand = {
  'tx': '\t\ttransform: translateX({}px);',
  'ty': '\t\ttransform: translateY({}px);',
  'tz': '\t\ttransform: translateZ({}px);',
  'sx': '\t\ttransform: scaleX({});',
  'sy': '\t\ttransform: scaleY({});',
  'sz': '\t\ttransform: scaleZ({});',
  'rx': '\t\ttransform: rotateX({}deg);',
  'ry': '\t\ttransform: rotateY({}deg);',
  'rz': '\t\ttransform: rotateZ({}deg);',
  'op': '\t\topacity: {};'
}

# Open the input csv file
f = open('input.csv')

# Initialize the output to empty list of strings
output = []

# Iterate through each row except for the first which is header row
for row in f.readlines()[1:]:

  # Extract element ID which is the first column of the row
  elem = row.split(',')[0]

  # CSS output
  output.append(f'#{elem} {{')

  # Remove the element ID from the row
  row_without_elem = row.lstrip(elem)
  
  # Strip the empty rows (commas) from the right of the row
  row_r_striped = row_without_elem.rstrip(',')
  
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
  
  # CSS output
  s = '\tanimation: {}_anim {} ease {} 1 normal forwards running;\n}}\n\n@keyframes {}_anim {{'
  output.append(s.format(elem, anim_durn, anim_delay, elem))

  # Iterate through all frames enumerating its time number
  for time, frame in enumerate(frames):
    
    # Calculate time in percent with respect to the animation duration
    time_in_percent = time / anim_durn * 100

    # Extract the changes in the properties by splitting the current frame by semicolons
    changes = frame.split(';')
    
    # If frame is empty continue with next frame
    if not changes[0]:
      continue

    # CSS output
    output.append(f'\t{time_in_percent}% {{')

    # Iterate through all the property changes
    for change in changes:

      # Extract property and value from change
      # Change will consist of property:value format
      prop, val = change.split(':')

      # CSS output
      output.append(prop_shorthand[prop].format(val))
    
    # CSS output
    output.append('\t}')

  # CSS output
  output.append('}\n')

# Create an output file named animation.css and write the CSS output into it
open('animation.css', 'w').write('\n'.join(output))