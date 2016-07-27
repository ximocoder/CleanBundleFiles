
# SSGame0601Ship01Packs-
#for bundles (49, 67, 80, 162, 173, 180, 184, 198, 199, 212):



file = open("E:/tmp\SSGame0601Ship01Packs-v1.txt", 'r')
# file = open("E:/tmp/Games/SPE 0414_ACTIVECARTONCONTENT.txt", 'r')

f = open("E:/tmp\SSGame0601Ship01Packs-v1_CLEAN.txt", 'w')
#f = open("E:/tmp/Games/SPE 0414_ACTIVECARTONCONTENT_CLEAN_FIX.txt", 'w')

gamecode = "0601"
newline = ""
splitedline = [""]

num = 0
for line in file:
    splitedline = line.split("\t", -1)
    firstitem = splitedline[0].strip()
    if firstitem in '2':
        num = int(splitedline[3])
        if num in (49, 67, 80, 162, 173, 180, 184, 198, 199, 212):
            newline += splitedline[1]

    if len(newline.strip()) > 0:
        f.write(newline + '\r\n')
        newline = ""

f.close()
file.close()
