# lst = [1, 2, 3, 4, 5]
# lst2 = []
#
# for num in lst:
#     lst2.append(num + 33)
#
# print(lst2)
#
# num = 87
# while num < 1000:
#     num += 1
#     print(num)


while True:
    try:
        num = int(input('please enter a number: '))
    except ValueError:
        print('That is not an int. try again')
