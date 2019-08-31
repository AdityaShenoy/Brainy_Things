# Mapping of csv shortcuts to actual css properties
# The curly braces in the property will be filled as per the input
csv_to_css = {
  'tx' : '    transform: translate3d({}px, 0, 0);\n',
  'ty' : '    transform: translate3d(0, {}px, 0);\n',
  'op' : '    opacity: {};\n'
}

# Input csv file
f_in = open('../csv/lis.csv')

# Output css file
f_out = open('../animation/lis.css', 'w')

# Read the input file
lines = f_in.readlines()[1:];

# Iterate over all the lines in the csv file
for line in lines:
  
  # Strip emply columns to the right and split data delimited by ','
  row = line.rstrip(',\n').split(',')
  
  # The first col is the tag id for which the animation is defined
  tag_id = row[0]

  # The following while loop calculates animation delay
  # by counting empty cols to the left of the first entry 
  anim_delay = 0
  while (row[anim_delay + 1] == ''):
    anim_delay += 1
  
  # Animation duration can be calculated now
  anim_dur = len(row) - anim_delay - 1

  # This writes the css code for associating animation keyframes to the id
  f_out.write('#{} {{\n'.format(tag_id))
  f_out.write(('  animation: {}Animate {}s ease {}s 1 normal forwards running;\n') \
    .format(tag_id, anim_dur, anim_delay))
  f_out.write('}\n\n')

  # This writes the keyframes accoring to the input csv file
  f_out.write('@keyframes {}Animate {{\n'.format(tag_id))

  # This stores the information of the previous and
  # current frames of the animation
  prev_frame = 0
  cur_frame = 0

  # This has the information about the relative time
  # animation key frames
  frames = list(enumerate(row[anim_delay+1:]))

  # This loop will print all the keyframe information
  while cur_frame < len(frames):
    # This will store the animation properties specified
    cur_frame_prop = frames[cur_frame][1].split(';')

    # This will 
    # Exception raised when no frame remains
    try:
      while frames[prev_frame][1] != '':
        prev_frame += 1
    except:
      f_out.write('  to {\n')
      for cur_prop in cur_frame_prop:
        cur_prop_name, cur_prop_val = cur_prop.split(':')
        f_out.write(csv_to_css[cur_prop_name].format(cur_prop_val))
      f_out.write('  }\n')
      break

    # This will increment till there is no animation instruction
    cur_frame = prev_frame
    while frames[cur_frame][1] == '':
      cur_frame += 1
    f_out.write('  {:.2f}%, {:.2f}% {{\n'
      .format(prev_frame / anim_dur * 100, cur_frame / anim_dur * 100))
    for cur_prop in cur_frame_prop:
      cur_prop_name, cur_prop_val = cur_prop.split(':')
      f_out.write(csv_to_css[cur_prop_name].format(cur_prop_val))
    f_out.write('  }\n')
    prev_frame = cur_frame

  f_out.write('}\n')

# Closing the input and output files
f_out.close()
f_in.close()