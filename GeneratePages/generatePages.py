import csv
import os
from datetime import datetime
import dateutil.parser as parser

# directory
os.chdir(r'F:\Projects\Temp')
chars = '#%&*+-<>=@^~|!?{}/\\\'\"'

with open('converted.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # if visibility is not public, skip
        if row['Visibility'] != 'Public':
            continue

        # print(row['Video Id'], row['Title'])
        path = row['Title'] + '.kr.md'
        # remove spaces from path
        path = path.replace(' ', '_')
        # remove characters in chars from path
        for char in chars:
            path = path.replace(char, '_')

        # path = 'F:/Projects/Website3/testpages/' + path
        # path = path.replace('/', '\\')

        # remove consecutive underscores
        path = path.replace('__', '_')
        path = path.replace('__', '_')

        # remove leading and trailing underscores
        path = path.strip('_')

        print(path)
        f = open(path, 'w', encoding='utf-8')
        f.write('---\n')
        f.write('title: "' + row['Title'] + '"\n')
        
        time = row['Time Published']
        # format time as iso8601
        time = parser.parse(time)
        time = time.isoformat()

        f.write('date: ' + time + '\n')
        f.write('draft: false\n')
        f.write('tags: ["' + row['Category'] + '", "Videos"]\n')
        f.write('categories: ["' + row['Category'] + '"]\n')
        f.write('---\n')
        str = "{{< youtube id=\"" + row['Video Id'] + '" title="' + row['Title'] + "\">}}\n"
        f.write(str)
        f.close()