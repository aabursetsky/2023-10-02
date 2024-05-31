input_number = int(input('Введите число (3-20) :'))
pass_word = ''

for i in range(1, input_number):
    for j in range(i + 1, input_number):
        if (input_number %  (i + j) == 0):
#            print(i, j)
            pass_word = pass_word + str(i) + str(j)
    continue

print('Пароль :', pass_word)
