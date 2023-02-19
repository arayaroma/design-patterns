from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def display(self):
        pass

class File(FileSystemComponent):
    def __init__(self, name, size, content):
        super().__init__(name)
        self.size = size
        self.content = content

    def get_size(self):
        return self.size
    
    def display(self, indentation=''):
       print(f'{indentation}└── {self.name}') 

class Folder(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def get_size(self):
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

    def display(self, indentation=''):
        print(f'{indentation}└── Folder \'{self.name}\'')
        for child in self.children[:-1]:
            child.display(indentation + '│   ')
        if self.children:
            self.children[-1].display(indentation + '    ') 

def main():
    file_one = File("fileOne.txt", 100, "Hello World!")
    folder_one = Folder("folderOne")
    folder_one.add_child(file_one)

    file_two = File("fileTwo.txt", 100, "Bye World!")
    folder_two = Folder("FolderTwo")

    folder_two.add_child(folder_one)
    folder_two.add_child(file_two)

    folder_two.display() 

if __name__ == "__main__":
    main()