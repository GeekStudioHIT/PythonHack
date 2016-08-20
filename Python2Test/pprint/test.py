import sys
import pprint

# print sys.path

# pprint.pprint(sys.path)

str = pprint.pformat(sys.path)
print str

print '\n'.join(['  ' + i for i in pprint.pformat(sys.path).split('\n')])
