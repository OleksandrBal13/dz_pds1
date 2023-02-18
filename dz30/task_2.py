import hashlib

def write_info(file_name : str, dictionary):
    with open(file_name, 'w') as f:
        for k, v in dictionary.items():
           f.write(f'{k} {v}\n')
    f.close()

def read_info(file_name : str):
    my_dict = {}
    with open(file_name, mode='r', encoding='utf-8') as f:
       for line in f:
           ls = line.split()
           my_dict[ls[0]] = ls[1]

    return my_dict

def registration():
    while True:
        login = input('Введіть логін: ')
        if login in hash_pass_table:
            print('Логіни не мають повторюватись, введіть інший.')
        else:
            while True:
                pass1 = input('Введіть пароль: ')
                pass2 = input('Повторіть пароль: ')
                if pass2 == pass1:
                    pass_hash = hashlib.md5(pass2.encode())
                    hash_pass_table[login] = pass_hash.hexdigest()
                    print("Вас зареєстровано")
                    write_info('info.txt', hash_pass_table)
                    break
                else:
                    print('Ви ввели різні паролі, спробуйте знову')
            break

def login():
    while True:
        login = input('Введіть логін: ')
        if login in hash_pass_table:
            count = 0
            while True and count < 3:
                count += 1
                password = input('Введіть пароль: ')
                pass_hash = hashlib.md5(password.encode())
                if hash_pass_table[login] != pass_hash.hexdigest():
                    if count != 3:
                        print(f"Щось пішло не так. Спробуйте ще раз. {3 - count} спроб залишилось.")
                    else:
                        print("Підбір паролів недопустимий, користувач заблокований. ")
                else:
                    print("Доступ дозволено.")
                    break
            break

        else:
            print("Невідомий логін.")
            choice = input("Якщо хочете спробувати ще раз - натисніть ( 0 ), якщо хочете зареєструватись - натіснить ( 1 ): ")
            if choice.lower() == '1':
                registration()
                break
            elif choice.lower() == '0':
                continue
            else:
                print("Помилка.")
            break

choice = input("Для входу натисніть ( 0 ), якщо хочете зареєструватись - натіснить ( 1 ): ")
hash_pass_table = read_info('info.txt')
if choice == "1":
    registration()
elif choice == "0":
    login()
else:
    print("Ви ввели невірний символ!")
