import json

dic = {"name": "hanshuai", "age": 23}

f = open('text.txt', 'w')

# text = json.dumps(dic)

# f.write(text)

text = json.dump(dic, f)

f.close()
