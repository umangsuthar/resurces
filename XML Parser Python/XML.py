import xml.etree.ElementTree as ET
tree = ET.parse('testdata.xml').getroot()

findx = raw_input("What You Have To Search!!??")

data = []

for aname in tree.findall('book'):
	data.append(aname.find(findx).text)

for d in data:
	print(d)

print("We Found This Data As Per Your Selection Now What You Have To Search From This Data?")

findy = raw_input("What You Have To Find In %s? "%findx)

flag=0
for d in data:
	if findy == d:
		print("Data Found "+d)
		flag = 0
		break;
	else:
		flag = 1

if flag == 1:
	print("Data Not Found")

