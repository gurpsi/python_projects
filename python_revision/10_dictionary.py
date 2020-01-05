'''
Dictionary holds a key:value pair.
Uses curly braces {}
Dictionary is not a ordered data (like list)
'''

post = {
    "user_id":209,
    "message": "D5 E5 C5 C5 G5",
    "language": "English",
    "location": (44.509,-104.5)
    }

print(type(post))

# In constructor we dont need to add double quotes like below:

post2 = dict(message='Foo bar', language='English', text_type='Italic')
print(post2)

try:
    print(post2['location'])
except KeyError:
    print('The post does not have a location')

for key in post.keys():
    value = post[key]
    print(key,"=", value)

print(post['user_id'])

post2.pop('text_type')
print(post2)

post2.clear()
print(post2)