import re
import json
file = open('websiteData.txt', 'r', encoding='utf-8')
s = file.read()
contents= re.findall('[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*', s)
emails = {}
for i in contents:
    emails[i] = {}
    emails[i]['Occurance'] = contents.count(i)
    a = i.split('@')
    if re.findall('\S+\.\S+@\S+', i) or (len(a[0]) >= 8):
        emails[i]['EmailType'] = 'Human'
    else:
        emails[i]['EmailType'] = 'Non-Human'
print(emails)
email_json=json.dumps(emails)
email_json = open('result.json', 'w')
email_json = json.dump(emails, email_json)