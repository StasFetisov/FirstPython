my_file = open("task1.txt", "w+")

for i in range(1,7):
    my_file.write(str(i))
    if i < 7:
        my_file.write('\n')
my_file.close()

tekst = open('task1.txt').readlines()
for i1 in range(0,6):
    tekst[i1] = tekst[i1].rstrip("\n")

import json
json_str = json.dumps(tekst, ensure_ascii=False, indent=2)

file_descriptor = open(r'task2.json','w+',encoding='utf-16')
file_descriptor.write (json_str)
file_descriptor.close ()