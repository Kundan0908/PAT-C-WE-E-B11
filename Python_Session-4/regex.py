import re
name = 'Ku*dan'
print(re.sub('a','_',name))
print(re.findall('n',name))
print(re.search('n',name))

