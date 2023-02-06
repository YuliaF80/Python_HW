"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

with open('doubl_text3.txt', 'w', encoding='utf-8') as test_file2, \
        open('text3.txt', 'r', encoding='utf-8') as test_file:
    # задаю списки слов, которые надо заменить
    old_list = ['One', 'Two', 'Three', 'Four']
    new_list = ['Один', 'Два', 'Три', 'Четыре']
    lines = test_file.readlines()
    for line in lines:
        for i in range(len(old_list)):
            line = line.replace(old_list[i], new_list[i])
        test_file2.write(line)
        print(line.strip())



