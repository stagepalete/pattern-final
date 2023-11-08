from commands.basic import Command
from cli.CLI import CLI

class CommandDecorator():
    def __init__(self, command):
        self._command = command

    def execute(self, args):
        self._command.execute(args)


class WarnCommandDecorator(CommandDecorator):
    def execute(self, args):
        self._command.execute(args)
        print(f"Warning: {CLI.instance.user} - executed {self._command.name}")
