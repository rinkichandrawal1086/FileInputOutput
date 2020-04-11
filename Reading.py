# jabber=open("/Users/Dinesh/Desktop/test.txt",'r')
# for line in jabber:
#     if "TOR" in line.upper():
#         print(line, end='')
# jabber.close()

# jabber=open("test.txt",'r')
# for line in jabber:
#     if "TOR" in line.upper():
#         print(line, end='')
# jabber.close()

# with open("test.txt",'r') as richie:
#     for line in richie:
#         if "TOR" in line.upper():
#             print(line, end='')


# with open("test.txt",'r') as richie:
#     line= richie.readline()
#     while line:
#             print(line, end='')
#             line = richie.readline()

# with open("test.txt",'r') as richie:
#     lines= richie.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

# with open("test.txt",'r') as richie:
#     lines= richie.readlines()
# print(lines)
#
# for line in lines[10:5:-1]:
#     print(line, end='')

with open("test.txt",'r') as richie:
    l = richie.read()                            #read is function who print output line by line

for line in l[::-1]:
    print(line, end='')
