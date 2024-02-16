from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory
        self.app_data = self._command_factory._app_data # Link to the App_data of the system

    def start(self):
        output: list[str] = []
        self.app_data.load_system_data() # Load systam data on start.
        while True:
            input_line = input()
            if input_line.lower() == "exit":
                self.app_data.save_system_data() # Save system data on exit.
                break

            command = self._command_factory.create(input_line)
            print(command.execute())

        print("\n".join(output))
