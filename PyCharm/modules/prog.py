from modules import help
from modules import display_man
from modules import select_man
from modules import list_man
from modules import add_man



def main():
    people = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == "add":
           people.append(add_man.add_man())
           if len(people) > 1:
               people.sort(key=lambda item: item.get('tel', ''))

        elif command == 'list':
           display_man.display_man(people)

        elif command.startswith('select'):
            parts = command.split(' ', maxsplit=1)
            period = parts[1]
            select = select_man.select_man(people, period)
            display_man.display_man(select)

        elif command == 'help':
           help.help_man()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)