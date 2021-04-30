import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii
"+91 1234567890"'''

# function used in re module
# 1.findall   2.search   3.split   4.sub   5.finditer

# patt = re.compile(r'fass')
# patt = re.compile(r'.')
# patt = re.compile(r'.adm')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iin$')
# patt = re.compile(r'ai*')
# patt = re.compile(r'ai{2}')
# patt = re.compile(r'(ai){2}')
# patt = re.compile(r'ai{1}|Fax')

# special sequence
# patt = re.compile(r'\ATata')
# patt = re.compile(r'\bTata')
# patt = re.compile(r'27\b')
# patt = re.compile(r'\BTata')
# patt = re.compile(r'\d{5}-\d{4}')
patt = re.compile(r'\b91 \d{10}')

matches = patt.finditer(mystr)

for match in matches:
    print(match)

# print(mystr[448:452])
# print(mystr[0:4])