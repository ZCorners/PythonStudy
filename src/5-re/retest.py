import re

text = 'imooc python'
pa = re.compile(r'imooc')
ma = pa.match(text)
print ma.group()

ma = re.match(r'\[[\w]\]', '[a]')
print ma.group()

ma = re.match(r'(<book>)\w+\1', '<book>python<book>')
print ma.group()


def add(match):
    val = match.group()
    num = int(val) + 1
    return str(num)


text = 'num = 9999'
result = re.sub(r'\d+', add, text)
print result

text = 'imooc:C C++ python Java,PHP'
result = re.split(r':| |,', text)
print result

