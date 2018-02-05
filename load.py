import json

f = open('text.txt', 'r')
# data = f.read()

# text = json.loads(data)

text = json.load(f)
print('text: {}'.format(text))

f.close()
