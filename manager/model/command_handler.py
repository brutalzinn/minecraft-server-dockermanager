class CommandHandler:
    def __init__(self):
        self.command = ''
    def checkCommand(self, command, getCommands):
        for obj in getCommands():
            if obj.command == command[0].strip():
                print('search here', obj.command)
                if len(command) >= obj.min_arg and len(command) <= obj.max_arg:
                    print('tring to execute..')
                    return obj.execute(command)
                else:
                    print('argumntos inválidos.')
                        #return False
