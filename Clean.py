# File for cleaning bundle files
# ximo.coder@gmail.com
#
# 0414.
# 71 – 75  [5 lådor]
# 77 – 81  [5 lådor]
# 83 – 87  [5 lådor]
# 89 – 93  [5 lådor]
# 95 – 99  [5 lådor]
# 101 – 125  {25 lådor]
#
#
# 0133.
# 126 – 139  [14 lådor]
# 175  - 185  [11 lådor]


# file = open("E:/tmp/Games/SPE 0133_ACTIVECARTONCONTENT.txt", 'r')
file = open("E:/tmp/Games/SPE 0414_ACTIVECARTONCONTENT.txt", 'r')

# f = open("E:/tmp/Games/SPE 0133_ACTIVECARTONCONTENT_CLEAN.txt", 'w')
f = open("E:/tmp/Games/SPE 0414_ACTIVECARTONCONTENT_CLEAN.txt", 'w')

boxstr = "Box:"
gamecode = "0414-"
newline = ""
splitedline = [""]
parseline = True
num = 0
for line in file:
    splitedline = line.split(' ', -1)

    if boxstr in line:
        num = splitedline[2].strip()
    inum = int(num)
    if inum in range(71, 75) or inum in range(77, 81) or inum in range(83, 87) or inum in range(89, 93) \
            or inum in range(95, 99) or inum in range(101, 125):
        parseline = True
    else:
        parseline = False

    for item in splitedline:
        if boxstr in item and parseline:
            newline += line
        if gamecode in item and parseline:
            newline += item.replace('-', '') + "\n"

    if len(newline.strip()) > 0:
        f.write(newline + '\r\n')
        newline = ""

f.close()
file.close()
