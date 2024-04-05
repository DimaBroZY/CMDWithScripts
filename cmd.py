import json
import os
import subprocess
import sys

def load_commands(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        commands = json.load(file)
    return commands

def execute_command(command, commands_list):
    if command.lower() == 'help':
        print("Доступные команды:")
        for cmd in commands_list:
            print("- {}: {}".format(cmd["command"], cmd["description"]))
        return

    for cmd in commands_list:
        if cmd["command"] == command:
            script_path = cmd["script_path"]
            if os.path.exists(script_path):
                os.system('python {}'.format(script_path))
            else:
                print("Скрипт '{}' не найден.".format(script_path))
            return
    print("Команда '{}' не найдена. Введите 'Help' для просмотра доступных команд.".format(command))

def check_dependencies():
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("Не удалось установить зависимости. Пожалуйста, убедитесь, что файл requirements.txt существует и содержит правильные зависимости.")
        exit(1)

def clear_console():
    # Для Windows
    if sys.platform.startswith('win'):
        os.system('cls')
    # Для Linux и MacOS
    else:
        os.system('clear')

def main():
    commands_file = 'commands.json'
    check_dependencies()  # Проверка зависимостей
    commands_list = load_commands(commands_file)
    if not commands_list:
        print("Команды не найдены в файле {}.".format(commands_file))
        return

    clear_console()  # Очистка консоли
    while True:
        user_input = input("Введите команду ('Help' для списка команд) ").strip()
        if user_input.lower() == 'exit':
            break

        execute_command(user_input, commands_list)

if __name__ == "__main__":
    main()
