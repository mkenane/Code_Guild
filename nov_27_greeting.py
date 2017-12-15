import datetime

name = input('What is your name?: ')
year = int(input('what year were you born in?(YYYY): '))
age = datetime.datetime.now().year - year

greet = f'Hello {0}, \nI\'m glad to meet you! You are {1} {1} {1}.'.format(name, age)
print(greet)
