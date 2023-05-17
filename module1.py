file = open('/Users/gunyong-bok/Desktop/code2.pl', 'r')
line = file.readlines()

data = ''.join(line)
arr = [line.split() for line in data.strip().split("\n")]

data_register = []
stack = []
memeory_dic = {}

for i in arr:
    # PUSH
    if i[0] == '0011':
        stack.append(i[1])
    # WRITE
    if i[0] == '1000':
        memeory_dic[i[1]] = stack[0]
        stack = []
    # LOAD
    if i[0] == '0001':
        data_register.append(memeory_dic[i[1]])
    # SUB
    if i[0] == '0111':
        stack.append(int(data_register[0],2) - int(data_register[1],2))
        data_register = []
    # ADD
    if i[0] == '0110':
        stack.append(int(data_register[0], 2) + int(data_register[1], 2))
        data_register = []
    # STORE
    if i[0] == '0010':
        memeory_dic[i[1]] = f"{stack[0]:04b}"
        stack = []
    # LOAD NUM
    if i[0] == '0000':
        data_register.append(i[1])
    # PRINT
    if i[0] == '1001':
        print(memeory_dic[i[1]])


