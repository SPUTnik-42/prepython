# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:08:48 2020

@author: ATARAXIA
"""


import kivy 

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols = 2 
        self.add_widget(Label(text="name"))
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)
        
        
        
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__" :
    MyApp().run()