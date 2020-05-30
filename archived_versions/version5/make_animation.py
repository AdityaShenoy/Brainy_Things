import pyautogui as pag

# CSS transform animations
transforms = {
  'sx': 'scaleX({})',
  'sy': 'scaleY({})',
  'tx': 'translateX({})',
  'ty': 'translateY({})',
  'r': 'rotateZ({}deg)'
}

# CSS non transform animations
non_transforms = {
  'op': 'opacity: {}'
}

# Open the input CSV file
with open('keyframes.csv') as inp:

  # Open the output CSS file
  with open('animation.css', 'w') as out:

    # For all lines in the input file except for first (header)
    for line in inp.readlines()[1:]:

      # Remove leading whitespaces and commas to the right
      line = line.strip().rstrip(',')

      # The id of the element being animated
      elem = line[:line.find(',')]

      # Remove the element from the line
      line = line.lstrip(elem)

      # Remove trailing commas to the left
      frames = line.lstrip(',')

      # Calculate animation delay
      anim_delay = len(line) - len(frames) - 1

      # Split the remaining line for extracting frame info
      frames = frames.split(',')

      # Calculate animation duration
      anim_durn = len(frames) - 1

      # Write CSS output
      out.write(f'#{elem} {{\n')
      out.write(f'  animation-name: {elem}_animation;\n')
      out.write(f'  animation-duration: {anim_durn}s;\n')
      out.write(f'  animation-delay: {anim_delay}s;\n')
      out.write(f'  animation-fill-mode: forwards;\n')
      out.write('}\n\n')
      out.write(f'@keyframes {elem}_animation {{\n')

      # For all frames
      for frame_num, frame in enumerate(frames):
        
        # If frame is empty continue
        if not frame:
          continue
      
        # Write CSS output
        out.write(f'  {frame_num / anim_durn * 100:.2f}% {{\n')

        # List to store CSS transforms
        t_ops = []

        # For all operations in the frame
        for op in frame.split(';'):

          # Extract property and value of the operation
          prop, val = op.split(':')

          # If the property is a CSS transform operation
          if prop in transforms:

            # Append it to transform operation list
            t_ops.append((prop, val))

          # If the property is not a CSS transform operation
          else:

            # Write CSS output
            out.write(f'    {non_transforms[prop].format(val)};\n')

        # If the transform operation is not empty
        if t_ops:

          # Write CSS output
          out.write('    transform: ')
          out.write(" ".join(
              [transforms[prop].format(val) for prop, val in t_ops[::-1]]
            ) + ';\n'
          )
        out.write('  }\n')
      out.write('}\n\n')

# Open browser and refresh animation
pag.hotkey('win', '3')
pag.press('f5')