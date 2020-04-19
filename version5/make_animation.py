transforms = {
  'sx': 'scaleX({})',
  'sy': 'scaleY({})',
  'tx': 'translateX({})',
  'ty': 'translateY({})',
  'r': 'rotateZ({}deg)'
}

non_transforms = {
  'op': 'opacity: {}'
}

with open('keyframes.csv') as inp:

  with open('animation.css', 'w') as out:

    for line in inp.readlines()[1:]:

      line = line.strip().rstrip(',')

      elem = line[:line.find(',')]

      line = line.lstrip(elem)

      frames = line.lstrip(',')

      anim_delay = len(line) - len(frames) - 1

      frames = frames.split(',')

      anim_durn = len(frames) - 1

      out.write(f'#{elem} {{\n')
      out.write(f'  animation-name: {elem}_animation;\n')
      out.write(f'  animation-duration: {anim_durn}s;\n')
      out.write(f'  animation-delay: {anim_delay}s;\n')
      out.write('}\n\n')
      out.write(f'@keyframes {elem}_animation {{\n')

      for frame_num, frame in enumerate(frames):
        
        if not frame:
          continue
      
        out.write(f'  {frame_num / anim_durn * 100:.2f}% {{\n')

        t_ops = []

        for op in frame.split(';'):

          prop, val = op.split(':')

          if prop in transforms:

            t_ops.append((prop, val))

          else:

            out.write(f'    {non_transforms[prop].format(val)};\n')

        if t_ops:

          out.write('    transform: ')
          out.write(" ".join(
              [transforms[prop].format(val) for prop, val in t_ops[::-1]]
            ) + ';\n'
          )

        out.write('  }\n')
      
      out.write('}\n\n')