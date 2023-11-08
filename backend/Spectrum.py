import datetime
import ctypes
import os

os.dont_write_bytecode = True

class Spectrum():
    def __init__(self):
        self.colors = {
            'black':"\x1b[30m",
            'red':"\x1b[31m",
            'green':"\x1b[32m",
            'yellow':"\x1b[33m",
            'blue':"\x1b[34m",
            'purple':"\x1b[35m",
            'magneta':"\x1b[35m",
            'pink':"\x1b[38;5;201m",
            'cyan':"\x1b[36m",
            'white':"\x1b[37m",
            'reset':"\x1b[0m"            
            # Colors are from https://talyian.github.io/ansicolors/
        }
    
        self.title = ctypes.windll.kernel32.SetConsoleTitleW
                
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def logging(self, color=None, mode='notDefined', fg=None, text=None):
        
        modes = {
            "notDefined":"Mode hasn't been defined.",
            "notFound":"Mound was not found.",
            "Success":"Success!",
            "Failed":"Failed!",
            "Error":"Error!"
        }
        
        color = self.colors.get(color, self.colors['white'])
        mode = modes.get(mode, modes['notDefined'])
        fg = self.colors.get(fg, self.colors['white'])
        text = text or ''
        
        message = f"{color}{mode}   {fg}{text}"
        
        print(message + self.colors['reset'])
    
    
    def time(self, color=None, fg=None, text=None):
        
        time = datetime.datetime.now().strftime('[%H:%M:%S %p]')
        
        color = self.colors.get(color, self.colors['white'])
        fg = self.colors.get(fg, self.colors['white'])
        text = text or ''
        
        message = f"{color}{time}   {fg}{text}{self.colors['reset']}"

        print(message)
        
    def print(self, text, color=None):
        color = self.colors.get(color, self.colors['white'])
        message = f"{color}{text}{self.colors['reset']}"
        
        print(message)
        
    def input(self, text=None, color=None, fg=None):
        color = self.colors.get(color, self.colors['white'])
        fg = self.colors.get(fg, self.colors['white'])
        user_input = input(f"{color}{text}{self.colors['reset']}{fg}{self.colors['reset']}")
        return user_input

    
# Inspired / Helped by @User319183