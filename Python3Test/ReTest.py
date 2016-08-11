import re

# m = re.match('foo', 'foo')
# m = re.match('foo', 'seafood')
m = re.search('foo', 'seafood')
if m is not None:
    print(m.group())

