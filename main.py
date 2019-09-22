from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder 
Builder.load_file("toolbox.kv")
Builder.load_file("drawingspace.kv")
Builder.load_file("generaloptions.kv")
Builder.load_file("statusbar.kv")
Builder.load_file("comicwidgets.kv")
class MyLayout(AnchorLayout):
    pass



class WeatherApp(App):
    def build(self):
        return MyLayout() 




if __name__ == "__main__":
    WeatherApp().run()
    