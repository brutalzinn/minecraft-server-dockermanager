class Command:
    def __init__(self, command,  max_arg=1, min_arg=0, method=False, register=False):
        self.command = command
        self.method = method
        self.max_arg = max_arg
        self.min_arg = min_arg
        register(self)
    def execute(self, command):
        if self.method is not False:
            return self.method(command)