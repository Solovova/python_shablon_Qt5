from file.RecFileInfo import RecFileInfo
import os

class FileWork(object): 
    
    def __init__(self, paths):
        self.paths = paths 

    def printAllFiles(self):
        self.fillAllFiles()
        for frecord in self.allFiles:
            print(frecord.path + "  :" + frecord.name + " size:" + str(frecord.size))

    def fillAllFiles(self):
        self.allFiles = []
        for path in self.paths:
            file_list = os.listdir(path)
            for file_name in file_list:
                self.allFiles.append(RecFileInfo(path, file_name, os.stat(path+"\\"+file_name).st_size))

    def fillPrintDublicates(self):
        self.fillAllFiles()
        file_list = []
        file_list_find_dublicate= []
        for frecord in self.allFiles:
            if frecord.name in file_list_find_dublicate:
                continue
            if frecord.name in file_list:
                file_list_find_dublicate.append(frecord.name)
            else:
                file_list.append(frecord.name)
        
        num = 1
        for duplicate_name in file_list_find_dublicate:
            first = True
            for frecord in self.allFiles:
                if frecord.name != duplicate_name:
                    continue

                if first:
                    first = False
                    print(str(num) + "  " + duplicate_name)

                print(frecord.path + "  :" + str(frecord.size))
            num=num+1