class CommandHandler:
    def __init__(self):
        self.command = ''
    def checkCommand(self, command,getCommands):
        for obj in getCommands():
            if obj.command == command[0]:
                if len(command) > obj.min_arg:
                    return obj.execute()
                else:
                    print('argumntos inválidos.')
                    return False