import os 
import json
import gdown

from abc import *
from enum import Enum

PATH = os.path.dirname(os.path.realpath(__file__))+"/"

url = "https://drive.google.com/file/d/1CPt0YMDN6mOZR9NlwDZ-NdgCOZSGNiiM/view"
parsed_url = url.split('/')

for index, url in enumerate(parsed_url): 
    if url == 'd' and parsed_url[index+2] == 'view': 
        FILE_ID = parsed_url[index+1]

FILE_ID = "1CPt0YMDN6mOZR9NlwDZ-NdgCOZSGNiiM"
savename = "bread.json"
json_savepath = PATH + savename
gdown.download(id=FILE_ID, output=json_savepath, quiet=False)

class Bread():
    def __init__(self):
        pass

class Cream(Bread):
    def __init__(self, name, recipe):
        self.name = name
        self.recipe = recipe
        #print("Make a Cream Instance")

class Sugar(Bread):
    def __init__(self, name, recipe):
        self.name = name
        self.recipe = recipe    
        #print("Make a Sugar Instance")

class Butter(Bread):
    def __init__(self, name, recipe):
        self.name = name
        self.recipe = recipe    
        #print("Make a Butter Instance")

class BreadFactory(metaclass=ABCMeta):
  @abstractmethod
  def createBread(self):
    pass

class CreamFactory(BreadFactory):
    def __init__(self):
        pass
    @classmethod
    def createBread(self, name, recipe):
        return Cream(name, recipe)
    @classmethod 
    def print_cream_recipe(self, bread):
        print(f"breadType: ",bread.name)
        print(f"recipe")
        print(f"flour:",bread.recipe['flour'])
        print(f"water:",bread.recipe['water'])
        print(f"cream:",bread.recipe['cream'])
        print("")  

class SugarFactory(BreadFactory):
    def __init__(self):
        pass
    @classmethod
    def createBread(self, name, recipe):
        return Sugar(name, recipe)
    @classmethod   
    def print_sugar_recipe(self, recipe):
        print(f"breadType: ",bread.name)
        print(f"recipe")
        print(f"flour:",bread.recipe['flour'])
        print(f"water:",bread.recipe['water'])
        print(f"sugar:",bread.recipe['sugar'])
        print("")   

class ButterFactory(BreadFactory):
    def __init__(self):
        pass
    @classmethod
    def createBread(self, name, recipe):
        return Butter(name, recipe) 
    @classmethod
    def print_butter_recipe(self, recipe):
        print(f"breadType: ",bread.name)
        print(f"recipe")
        print(f"flour:",bread.recipe['flour'])
        print(f"water:",bread.recipe['water'])
        print(f"butter:",bread.recipe['butter'])
        print("")  
    
def CreateFactoryFn(bread_name, recipe):
    if bread_name == 'cream':
        return CreamFactory.createBread('cream', recipe)
    elif bread_name == 'butter':
        return ButterFactory.createBread('butter', recipe)
    elif bread_name == 'sugar':
        return SugarFactory.createBread('sugar', recipe)

def PrintFactoryStatusFn(bread):
    if bread.name == 'cream':
        return CreamFactory.print_cream_recipe(bread)
    elif bread.name == 'butter':
        return ButterFactory.print_butter_recipe(bread)
    elif bread.name == 'sugar':
        return SugarFactory.print_sugar_recipe(bread)


#-----
with open(json_savepath,'r') as f:
    json_data = json.load(f)

bread_list = [] 
for data in json_data : 
    bread_list.append(CreateFactoryFn(data['breadType'], data['recipe']))

for bread in bread_list :
    PrintFactoryStatusFn(bread)


