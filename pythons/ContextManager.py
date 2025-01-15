# simplfy resources management(files,database connections)
# using with function for handling files 

# with open('data.txt','r') as file:
#     content = file.read()
#     print(content)
# usages - managing database connections locking resources 

class FileManager:
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager('example.txt', 'w') as f:
    f.write("Hello, World!")