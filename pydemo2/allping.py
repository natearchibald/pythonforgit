import re
ms_200_500 = re.compile(r'=[2-4]\d{2}\.?\d*?\s')
re1 = re.compile(r'(?P<sign>abc){2}')
m = re.match(r'(\w+) (\w+)(?P<sign>.?)', 'hello world!?')
re2 = re.compile(r'^(abc)')
print re.findall(ms_200_500,"=229.855555 ")
print m.groupdict()
print m.groups()
print re.findall(re2,"bvc")
