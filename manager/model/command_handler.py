class CommandHandler:
    def __init__(self):
        self.command = ''
    def checkCommand(self, command, getCommands):
        for obj in getCommands():
            if obj.command == command[0].strip():
                return obj.execute(command)
