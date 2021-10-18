from ast import parse
from typing import Text
import re, sys

keywords=['CREATE','INSERT','PRINT_TREE','CONTAINS','SEARCH','CONTAINED_BY','INTERSECTS','WHERE','EXIT']

class Interpreter(object):
    def __init__(self,text):
        self.text=Text
    def interpreter(self,text):
        text.replace(';',"")
        text=text.split(' ')
        command=text[0]
        if command.upper()==keywords[0]:#create
                if(analyzer(self,command)==True):
                          collection_name = text[text.index(command)+1]
                          print("Collection "+ collection_name +" has been created")                   
                
        elif command.upper() == keywords[1]:#insert
                if(analyzer(self,command)==True):
                        collection_name =text[1]
                        values=re.findall(r'\d+',command)
                        print("Set has been added to " + collection_name)
                        print(values)        
                
        elif command.upper() == keywords[2]:#print_tree
                print("Printing tree....")
                
        elif command.upper() == keywords[3]:#contains
                collection_name =text[1]
                print()
                
        elif command.upper() == keywords[4]:#search
                collection_name =text[1]
                print()
                
        elif command.upper() == keywords[8]:#exit
                print("Work finished")                
                sys.exit()
        else:
                print("Error, command not exist")
    def analyzer(command):
        if(re.match(r'CREATE \w+',command)):
                return True
        elif(re.match(r'INSERT \w+',command)):
                return True
        elif(re.match(r'PRINT_TREE \w+',command)):
                return True
        elif(re.match(r'SEARCH \w+ WHERE (INTERSECTS|CONTAINS|CONTAINED_BY)',command)):
                return True
    


