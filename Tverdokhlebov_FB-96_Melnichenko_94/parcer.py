from typing import Text
import re, sys
from RDtree import *

l=[]

keywords=['CREATE','INSERT','PRINT_TREE','CONTAINS','SEARCH','EXIT']
keywords_search =['CONTAINED_BY','INTERSECTS','WHERE','EXIT']
buffer =[]
tree = RDtree()
class Interpreter(object):
    interpreter_buff = {}
    def __init__(self,text):
        self.text=Text
    def interpreter(self,text):
        k=text.split(';')
        for i in range(len(text.split(';'))-1):
            text=k[i]
            text=text.replace(';', "")
            text =  text.replace('\n', ' ')
            text =  text.replace('  ', ' ')
            text =  text.replace('  ', ' ')
            text =  text.replace('   ', ' ')
            text=text.replace(',', "")
            text=text.split()
            command = text[0]
            if command.upper()==keywords[0]:#create               
                try:
                        self.Create(text)
                except:
                        print("Error. Can`t create collection")
            elif command.upper() == keywords[1]:#insert 
                self.Insert(text)
                print("Set has been added " )
            elif command.upper() == keywords[2]:#print_tree  
                self.Print(text)              
            elif command.upper() == keywords[3]:#contains
                print("Contains")
                self.Contains(text)               
            elif command.upper() == keywords[4]:#search
                if text[3]==keywords_search[0]:
                    self.Intersects(text)
                if text[3]==keywords_search[1]:
                    self.CONTAINS_where(text)
                if text[3]==keywords_search[2]:
                    self.CONTAINED_BY(text)
            elif command.upper() == keywords[8]:#exit
                try:
                    print("Work finished")                
                    sys.exit()
                except:
                    pass
            else:
                print("Error, command not exist")
#     def analyzer(command):
#         if(re.match(r'CREATE \w+',command)):
#                 return True
#         elif(re.match(r'INSERT \w+',command)):
#                 return True
#         elif(re.match(r'PRINT_TREE \w+',command)):
#                 return True
#         elif(re.match(r'SEARCH \w+ WHERE (INTERSECTS|CONTAINS|CONTAINED_BY)',command)):
#                 return True
        
    def Create(self,text):
        try:
                buffer.append({text[1]:[]})
                collection_name=text[1]
                collection_name=collection_name.replace(';',"")
                print(print("Collection "+ collection_name +" has been created"))
                self.interpreter_buff[collection_name]=None
        except:
                print("Error in creating ")  
    def Insert(self, text):
        try:
            k=text[3:-1]
            #print(k)
            ch=[]
            for ik in range(len(k)):
                ch.append(int(k[ik]))
            self.insert_data(text[1], ch)
            for i in range(len(l)):
                if text[1] == list(l[i].keys())[0]:
                    for j in range(len(k)):
                        l[i][text[1]].append(int(k[j]))
                    break
            #print(l)
        except:
            pass
    def insert_data(self,collection_name, data):
            root = self.interpreter_buff[collection_name]
            self.interpreter_buff[collection_name]=RDtree().insert(root,set(data))
    def Print(self,text):
        # try:
            self.print_tree(text[1])
            m=[]
            for i in range(len(l)):
                if text[1] == list(l[i].keys())[0]:
                    m=l[i][text[1]]
                    break
        # except:
        #     print('Error')
    def print_tree(self, collection_name: str):
        print(f"Printing {collection_name} tree:")
        root = self.interpreter_buff[collection_name]
        RDtree().tree_to_dict(root)
        print(" ")

    def Contains(self,text):
        try:
            k = text[3:-1]
            print(k)
            m=[]
            for i in range(len(l)):
                if text[1] == list(l[i].keys())[0]:
                    m=l[i][text[1]]
                    break
            for i in range(len(k)):
                k[i]=int(k[i])
            print(set(k).issubset(m))
        except:
            print("Error")
    def Intersects(self, text):
        try:
            k = text[5:-1]
        #     print(k)
            m=[]
            for i in range(len(l)):
                if text[1] == list(l[i].keys())[0]:
                    m=l[i][text[1]]
                    break
            for i in range(len(k)):
                k[i]=int(k[i])
            print(set(k).issubset(m))
        except:
            print("Error")
    def Contained_By(self,text):
        try:
            k = text[5:-1]
        #     print(k)
            m=[]
            for i in range(len(l)):
                if text[1] == list(l[i].keys())[0]:
                    m=l[i][text[1]]
                    break
            for i in range(len(k)):
                k[i]=int(k[i])
            print(set(m).issubset(k))
        except:
            print("Error") 
    def Contains_Where(self,text):
        try:
            k = text[5:-1]
        #     print(k)
            m=[]
            for i in range(len(l)):
                if text[1] == list(l[i].keys())[0]:
                    m=l[i][text[1]]
                    break
            for i in range(len(k)):
                k[i]=int(k[i])
            print(set(m).issubset(k))
        except:
            print("Error")    
