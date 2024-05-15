#!/usr/bin/python3
"""The cmd Module.
for building line-oriented command interpreters
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "  # Set the prompt for the command line

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_EOF(self, line):
        """Exit the console on EOF (Ctrl+D) command."""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program\n")


    def default(self, line):
        """Handle unrecognized commands."""
        parts = line.split('.')
        if len(parts) == 2:
            class_name, action = parts
            self.handle_custom_command(class_name, action)
        else:
            print(f"Unrecognized command: {line}.\
                  Type 'help' for assistance.\n")
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()  # Start the command loop if the script is executed directly
