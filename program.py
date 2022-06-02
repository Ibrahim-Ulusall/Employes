from io import UnsupportedOperation
import os
import sys
import time


class Employes:
    header_list = ["ID","IDENTITY NO","NAME","SURNAME","AGE","GENDER","WAGE","TELEPHONE NO","DATE OF START"]
    file_name = "worker.txt"
    def __init__(self) -> None:
        self.dateOfStart = time.strftime("%d:%m:%Y")
        self.id = 1
        self.clearTerminal()
        self.fileLocationControl()
    def addWorker(self):
        try:
            identity_number = str(input("Identity Number : "))
            while len(identity_number) < 11 or len(identity_number) > 11:
                identity_number = str(input("Identity Number : "))
            name = str(input("Name : "))
            surname = str(input("Surname : "))
            age = int(input("Age : "))
            gender = str(input("Gender : "))
            wage = float(input("Wage : "))
            telephone_number = str(input("Telephone Number : "))
            new_tel_no = "+9"+telephone_number[0] + " ("+telephone_number[1:4] + ") " + telephone_number[4:7] + " " + telephone_number[7:]
            add_list = ["1",identity_number,name.capitalize(),surname.upper(),age,gender.capitalize(),wage,new_tel_no,self.dateOfStart]
            def id_Reader():
                try:
                    s = 0
                    with open(Employes.file_name,"r",encoding="utf-8") as file:
                        content = file.readlines()
                        if len(content) == 0:
                            self.id = 1
                            self.writerFiles("w",Employes.header_list)
                        else:
                            for lines in content:
                                lines = lines.replace("\n"," ")
                                if s == 0:
                                    s += 1
                                    continue
                                self.id = int(lines[0]) +1
                                add_list[0] = self.id
                except UnsupportedOperation:
                    pass
            id_Reader()
            self.writerFiles("a+",add_list)
        except KeyboardInterrupt:
            self.errorBox("[ CTRL + C ] Detected !")
        except Exception as e:
            self.errorBox(e)

    def removeWorker(self):
        with open(Employes.file_name,"r",encoding="utf-8") as file:
            s = 0
            content = file.readlines()
            for lines in content:
                if s == 0:
                    s+=1
                    continue
                print(lines)


    def clearTerminal(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system("cls")
        else:
            pass
    def readerFile(self):
        try:
            with open(Employes.file_name,"r",encoding="utf-8") as readerfile:
                content = readerfile.readlines()
                if len(content) == 0:
                    self.id = 1
                    self.writerFiles("w",Employes.header_list)
        except UnsupportedOperation:
            self.writerFiles("w",Employes.header_list)
    def fileLocationControl(self):
        try:
            _directory = os.listdir(os.getcwd())
            if Employes.file_name not in _directory:
                self.writerFiles("w",Employes.header_list)

        except Exception as err:
            self.errorBox(err)

    def writerFiles(self,writerMode,value_list):
        try:
            with open(Employes.file_name,writerMode,encoding="utf-8") as files: 
                for writer in value_list:
                    files.write(str(writer))
                    files.write(" " * (25 - len(str(writer))))
                files.write("\n")
        except UnsupportedOperation as e:
            Employes.errorBox(e)

    def errorBox(self,text):
        self.clearTerminal()
        print(f"Message : {text}")
        time.sleep(2)
        sys.exit()
employes = Employes()
# employes.addWorker()
employes.removeWorker()