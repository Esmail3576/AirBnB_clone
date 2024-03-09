import cmd
class hbnb(cmd.Cmd):
    prompt = '(hbnb) '
    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)
    def do_EOF(self, arg: str) -> bool | None:
        return True
    def do_quit(self, arg: str) -> bool | None:
        return True
if __name__ == '__main__':
    hbnb().cmdloop()