from commands import COMMANDS, good_bye, no_command


def command_handler(text: str):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, '').strip()
    return no_command, None


def main():
    print("Type 'hello' for help.\n")
    while True:
        user_input = input('Enter your command: ').lower()
        command, data = command_handler(user_input)
        print(command(data))
        if command == good_bye:
            break


if __name__ == '__main__':
    main()
