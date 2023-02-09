import json
import time

path_json = r"autoIssueGoods.json"  # Путь до джсона
with open(path_json, 'rb') as file:  # Открываем его в режиме чтения
    data = json.load(file)
# print(json.dumps(data, indent=4)) # Это для просмотра джисона
all_names = [data[section]['name'] for section in range(len(data))]
num_and_names = []
for i, name in enumerate(all_names):
    num_and_names.append(f'{i + 1}. ' + name)
main_menu_switcher = True

def main_menu():
    print(*[str(i) for i in num_and_names], sep='\n')
    user_num = int(input('Выберите раздел для ключа:\n'))
    selecting_user_section = data[user_num - 1]["name"]
    print(f'В этом разделе {len(data[user_num - 1]["nodes"])} ключей')
    print(f'Ваши текущие ключи в разделе "{selecting_user_section}":')
    keys_list = data[user_num - 1]['nodes']
    l = []
    for i, key in enumerate(keys_list):
        l.append(f"{i + 1}. " + key.split("\n")[0])
    print(*l, sep='\n')
    user_choice = input(f'Хотите добавить (1) или удалить (2) ключи? Или можете вернуться в гл. меню (3). Чтобы сохранить изменения и выйти напишите любое другое.\n')
    stopper = True
    count_keys = 0
    if user_choice == '1':
        while stopper:
            new_user_key = input('Введите новый ключ\nЧтобы остановить добавление ключей напишите "stop"\n')
            if new_user_key == 'stop':
                stopper = False
            else:
                keys_list.append(
                    f'{new_user_key}\nЧтобы получить инструкцию по активации напиши мне "!инструкция"\nTo receive activation instructions write me "!instruction"\nИнформация по горячим главишам: "!горячие_клавиши"\nHotkeys information: "!hotkeys"')
                print(f'Ключ {new_user_key} добавлен в раздел "{selecting_user_section}"')
                count_keys += 1
        return f'Вы успешно добавили {count_keys} ключей'
    elif user_choice == '2':
        while stopper:
            user_del_choice = input('Введите номер ключа для удаления или напишите "stop"\n')
            if user_del_choice == 'stop':
                stopper = False
            else:
                keys_list.remove(keys_list[int(user_del_choice) - 1])
                print(f'Вы успешно удалили {user_del_choice} ключ')
    elif user_choice == '3':
        return
    else:
        global main_menu_switcher
        main_menu_switcher = False
        return


while main_menu_switcher:
    main_menu()
with open(path_json, 'w', encoding="utf-8") as saver:
    json.dump(data, saver, indent=4, ensure_ascii=False)
print('Все изменения успешно сохранены!')
time.sleep(2)