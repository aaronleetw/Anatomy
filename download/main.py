# get all markdown files in ./data/ and rename them
# to the first word of the file name, all lowercase

import os
import re
import datetime

onlyfiles = [f for f in os.listdir('data') if os.path.isfile(os.path.join('data', f))]
for i in onlyfiles:
    if i.startswith('Template'):
        os.remove('data/' + i)
        continue
    with open('data/' + i, "r") as f:
        lines = f.readlines()
    featureImage = lines[2]
    # get string insde ()
    featureImage = re.search(r'\((.*?)\)', featureImage).group(1)
    featureImage = featureImage.strip()
    featureImage = '/images/' + featureImage
    del lines[0]
    del lines[1]
    with open('data/' + i, "w") as f:
        for line in lines:
            if (line.startswith('![')):
                line = line.replace('(', '(/images/')
            f.write(line)
    first_word = re.search(r'^[a-zA-Z]+', i).group(0)
    with open('data/' + i, 'r') as f:
        lines = f.readlines()
        # get string inside () on the third line
        # inesrt the below lines into the start of the file
        with open('data/' + i, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('+++\nauthor = "Aaron and Kate"\n' + 'title = "' + first_word + ' System"\n' + 'date = "' + datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + '+08:00' +
            '"\ndescription = "' + lines[4].replace('\n', '') + '"\ntags = [\n\t"' + first_word.lower() + '",\n]\nfeature_image = "'
             + featureImage + '"\n+++\n' + content)
        new_name = first_word.lower()
        os.rename('data/' + i, 'data/' + new_name + '.md')
    print('hugo new content/post/' + new_name + '.md\n')