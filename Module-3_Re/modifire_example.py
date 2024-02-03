import re


mystr="This is Python!6584644"

#x=re.findall('[A-Z]',mystr)
#x=re.findall('[a-z]',mystr)
#x=re.findall('[A-Za-z]',mystr)
#x=re.findall('[0-9]',mystr)
#x=re.findall('[A-Za-z0-9]',mystr)
#x=re.findall('Py..on',mystr)
#x=re.findall('This|That',mystr)
#x=re.findall('[A-Z]|[a-z]',mystr)
#x=re.findall('^This',mystr)
#x=re.findall('^[A-Z]',mystr)
#x=re.findall('44$',mystr)
#x=re.findall('\w',mystr)
#x=re.findall('\W',mystr)
#x=re.findall('\d',mystr)
#x=re.findall('\D',mystr)
#x=re.findall('\s',mystr)
#x=re.findall('\S',mystr)
#x=re.findall(r'\bThis',mystr)
#x=re.findall('\B44',mystr)
#x=re.findall('\AThis',mystr)
x=re.findall('44\Z',mystr)
print(x)