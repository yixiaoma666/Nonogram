class Solve:
    def __init__(self, _file) -> None:
        self.file_name = _file
        
    def _read_txt(self):
        with open(self.file_name) as f:
            s = f.read()
        print(s)
        
if __name__ == "__main__":
    myx = Solve("input.txt")
    myx._read_txt()