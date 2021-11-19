from kivy import Config
from kivy.app import  App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

class Covid(FloatLayout):
    def __init__(self, **kwargs):
        super(Covid, self).__init__(**kwargs)


class CovidApp(App):
    def build(self):
        return Covid()
if __name__ == '__main__':
    CovidApp().run()