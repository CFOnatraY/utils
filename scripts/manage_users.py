import string
import random


def create_users_file():
    file = open('users.txt', 'w+')

    for i in range(10):
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        last_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        ssn = generate_ssn()
        file.write('{0},{1},{2}\n'.format(name, last_name, ssn))

    file.close()


def generate_ssn():
    ssn = ''
    for i in range(10):
        digit = random.randrange(0, 10)
        ssn = ssn + str(digit)
    return ssn


def show_users_file_content():
    with open('users.txt') as file:
        for line in file:
            line = line.replace('\n', '')
            line_content = line.split(',')
            name = line_content[0]
            last_name = line_content[1]
            ssn = line_content[2]
            print('Name: {0}, Last name: {1}, SSN: {2}'.format(name, last_name, ssn))


def create_new_file():
    users_file = open('new_user.txt', 'w+')

    with open('users.txt') as file:
        for line in file:
            line = line.replace(',', ';')
            users_file.write(line)
    users_file.close()


create_new_file()
# show_users_file_content()
# create_users_file()
