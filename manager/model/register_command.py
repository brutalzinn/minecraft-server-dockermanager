class RegisterCommand:
    def __init__(self):
        self.allCommands = []

    def addCommand(self, command_model):
        self.allCommands.append(command_model)

    def getCommands(self):
        return self.allCommands