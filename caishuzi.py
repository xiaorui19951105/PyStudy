"""
��������Ϸ
�������һ��1~100֮����������������
����������˲µ����ֱַ������ʾ��һ��/Сһ��/�¶���



"""

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('������: '))
    if number < answer:
        print('��һ��')
    elif number > answer:
        print('Сһ��')
    else:
        print('��ϲ��¶���!')
        break
print('���ܹ�����%d��' % counter)
if counter > 7:
    print('�������������Բ���')