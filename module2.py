import math

data = []
result = []
memory_dic = {}

file = open('/Users/gunyong-bok/Desktop/code1.pl', 'r')
line = file.readlines()

# 파일을 읽고 데이터 값 보관소에 한줄씩 저장하기
for i in line:
    row = i.strip().split(",")  # split the line into values ®using comma as delimiter
    data.append(row)

def isNaN(value):
    try:
        float_value = float(value)
        return False
    except ValueError:
        return True

# 오피코드에 따라 저장되는 기계어
for i in data:
    newline = " ".join(i).split()
    if len(newline) == 0:
        continue  # Skip empty lines
    opcode = newline[0]
    memory_name = (i[0].split(' '))[1]

    if opcode == "WRITE":
        memory_dic[memory_name] = i[1]
        result.append(f'0011 {i[2]}\n1000 {i[1]}\n0101')

    if opcode == 'ADD':
        if isNaN(newline[1]) is False:
            result.append(f'0000 {bin(int(newline[1]))[2:].zfill(4)}')
            result.append(f'0001 {memory_dic[i[1]]}\n0100')
            result.append('0110\n0101')
        if isNaN(newline[2]) is False:
            result.append(f'0001 {memory_dic[memory_name]}\n0100')
            result.append(f'0000 {bin(int(newline[2]))[2:].zfill(4)}')
            result.append('0110\n0101')
        if isNaN(newline[1]) is True and isNaN(newline[2]) is True:
            result.append(f'0001 {memory_dic[memory_name]}\n0100')
            result.append(f'0001 {memory_dic[i[1]]}')
            result.append('0110\n0101')

    if opcode == 'SUB':
        if isNaN(newline[1]) is False:
            result.append(f'0000 {bin(int(newline[1]))[2:].zfill(4)}')
            result.append(f'0001 {memory_dic[i[1]]}\n0100')
            result.append('0111\n0101')
        if isNaN(newline[2]) is False:
            result.append(f'0001 {memory_dic[memory_name]}\n0100')
            result.append(f'0000 {bin(int(newline[2]))[2:].zfill(4)}')
            result.append('0111\n0101')
        if isNaN(newline[1]) is True and isNaN(newline[2]) is True:
            result.append(f'0001 {memory_dic[memory_name]}\n0100')
            result.append(f'0001 {memory_dic[i[1]]}')
            result.append('0111\n0101')

    if opcode == 'STORE':
        result.append(f'0010 {memory_dic[memory_name]}')

    if opcode == 'PRINT':
        result.append(f'1001 {memory_dic[memory_name]}')

file.close()


machine_language = '\n'.join(result)
print(data)
# print(machine_language)
#
# f = open('/Users/gunyong-bok/Desktop/code2.pl', 'w')
#
# f.write(f'{machine_language}')