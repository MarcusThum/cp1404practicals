"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty

names = ["Stacey", "Peter", "John", "Margo"]

class NamesAsLabels(App):

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 200)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_buttons()
        return self.root

    def create_buttons(self):
        for name in names:
            name_button = Label(text=name)
            self.root.ids.main.add_widget(name_button)

NamesAsLabels().run()
