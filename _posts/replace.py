import re
import sys
import glob

regex = r"(?:(?:https?|ftp|file):\/\/|www\.|ftp\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z0-9+&@#\/%=~_|$])"

for post_url in glob.glob('*.md'):
    images = {}

    img_prefix = post_url[11:-3] + '-'

    matches = re.finditer(regex, open(post_url).read(), re.IGNORECASE | re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        url = match.group()
        if url.endswith('.jpg') or url.endswith('.png') or url.endswith('.JPG'):
            images[url] = img_prefix + url.split('/')[-1]

    print('post: %s' % post_url)
    print(images)
    print()
    print()
    print()
    sys.exit()
