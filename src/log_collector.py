class LogCollector:
    def __init__(self):
        self.sources = []
        
    def collect_logs(self):
        pass

    try:
        with open('file.txt', "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")

        # 'r' - meaning for read only 
        # 'w' - meaning for write only 
        # 'a' - meaning for append only 
        # 'r+' - meaning for read and write 
        # 'w+' - meaning for read and write 
        # 'a+' - meaning for read and write 
        # 'x' - meaning for create and write only 
    