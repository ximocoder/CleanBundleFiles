#
# 0414. [4000st per låda]
# 71 – 75  [5 lådor]
# 77 – 81  [5 lådor]
# 83 – 87  [5 lådor]
# 89 – 93  [5 lådor]
# 95 – 99  [5 lådor]
# 101 – 125  {25 lådor]
#
#
# 0133. [8000st per låda]
# 126 – 139  [14 lådor]
# 175  - 185  [11 lådor]


# SPE 0414_ACTIVECARTONCONTENT

# file = open("E:/tmp/Games/SPE 0133_ACTIVECARTONCONTENT.txt", 'r')
file = open("E:/tmp/Games/SPE 0414_ACTIVECARTONCONTENT.txt", 'r')

# f = open("E:/tmp/Games/SPE 0133_ACTIVECARTONCONTENT_CLEAN.txt", 'w')
f = open("E:/tmp/Games/SPE 0414_ACTIVECARTONCONTENT_CLEAN.txt", 'w')

newline = ""
splitedline = [""]
parseline = True
num = 0
for line in file:
    splitedline = line.split(' ', -1)

    if "Box:" in line:
        num = splitedline[2].strip()
    inum = int(num)
    if inum in range(71, 75) or inum in range(77, 81) or inum in range(83, 87) or inum in range(89, 93) \
            or inum in range(95, 99) or inum in range(101, 125):
        parseline = True
    else:
        parseline = False

    for item in splitedline:
        if "Box:" in item and parseline:
            newline += line
        if "0414-" in item and parseline:
            newline += item.replace('-', '') + "\n"

    if len(newline.strip()) > 0:
        f.write(newline + '\r\n')
        newline = ""

f.close()
file.close()
