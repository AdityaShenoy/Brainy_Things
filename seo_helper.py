import clipboard

seo_elems = dict()

with open('seo_helper_input.txt') as f:
    for key_value in f.read().split('\n\n'):
        split_point = key_value.find('\n')
        key = key_value[:split_point - 1]
        value = key_value[split_point + 1:]
        seo_elems[key] = value

seo_type = 'video' if seo_elems['Type'] == 'V' else 'playlist'

result = seo_elems['Title'] + '\n'*4

result += f'• This {seo_type} contains:\n►'
result += '\n► '.join(seo_elems['Keywords'].split('\n')).title() + '\n'*4

if seo_type == 'video':
    result += '• Timestamps:\n' + seo_elems['Timestamps'] + '\n'*4

result += '• Suggested Videos and Playlists:\n'
for vid_play in seo_elems['Suggested Videos and Playlists'].split('\n'):
    if vid_play[0] == '.':
        result += '►' + '\n'.join(vid_play[1:].split(': ')) + '\n\n'
result += '\n'*2

result += f'''• Social Links
Hi, my name is Aditya Shenoy. I would love to connect with you on other social media platforms as well.
► GitHub
{seo_elems['GitHub Repository']}
All the code that I display in this channel is available in my GitHub profile.

► LinkedIn
https://www.linkedin.com/in/adityashenoy49/
You can connect to me via LinkedIn''' + '\n'*4

result += f'''• Message to Viewers
► If you like the content or the efforts of this {seo_type}, please give {'this' if seo_type == 'video' else 'these'} video{'s' if seo_type == 'playlist' else ''} a like.
► If you have any feedback regarding this {seo_type} or this channel, or you want to suggest topics for future videos (for e.g. data structures, algorithms, coding projects like applications, games, etc) that you want me to do in this channel, please let me know in the comment section.
► Share this {seo_type} with your friends, juniors, or anyone who are interested in programming, competitive programming, preparing for interviews, etc. Your sharing will help this channel grow.
► Subscribe to this channel to see new videos regularly.''' + '\n'*4

result += '''• Fair Use Disclaimer
This video is fair use under U.S. copyright law because it is non-commercial, transformative in nature, uses no more of the original work than necessary for the video's purpose, and does not compete with the original work and could have no negative affect on its market. 

Copyright Disclaimer Under Section 107 of the Copyright Act 1976, allowance is made for 'Fair Use' for purposes such as criticism, comment, news reporting, teaching, scholarship, and research, Fair use is a permitted by copyright statute that might otherwise be infringing, Non-profit, educational or personal use tips the balance in favor of fair use

Thank you to https://www.fesliyanstudios.com for background music.''' + '\n'*4

result += ' '.join(map(lambda x: '#' + x.replace(' ', ''),
                       seo_elems['Hashtags'].split('\n')))

if seo_type == 'video':
    keywords = ','.join(seo_elems['Keywords'].split(
        '\n') + ['aditya shenoy', 'brainy things'])
    result += '\n' + keywords

clipboard.copy(result)
