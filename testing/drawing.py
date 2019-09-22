from kivy.app import App 
from kivy.uix.relativelayout import RelativeLayout

class DrawingBoard(RelativeLayout):
    pass

class DrawingTestApp(App):
    def build(self):
        return DrawingBoard()

if __name__ == "__main__":
        DrawingTestApp().run()
