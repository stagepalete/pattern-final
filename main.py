from cli.CLI import CLI
from library.Library import Library
from user.User import User

library = Library()


def main():
    cli = CLI()
    cli.run()
if __name__ == '__main__':
    main()