import re
import sys
import glob
from urllib import request

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

    post_content = open(post_url).read()
    for url in images:
        new_url = '../../images/' + images[url]
        try:
            request.urlretrieve(url, new_url)
        except:
            print('*** This file is not found; %s' % url)

        post_content = post_content.replace(url, '{{ site.baseurl }}/images/' + images[url])

    open(post_url, 'w').write(post_content)
