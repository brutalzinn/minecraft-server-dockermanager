class Command:
    def __init__(self, command, limit, register = False):
        self.command = command
        self.limit = limit
        register(self)
    def execute(self):
        print('executando...' + self.command)