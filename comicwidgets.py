from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line

class DraggableWidget(RelativeLayout):
    def __init__(self)
        self.selected = None
        super().__init__()
    def select(self):
        if self.selected == False:
            self.ix = self.center_x
            self.ix = self.center_y
            with self.canvas:
                self.selected = Line(rectanngle=(0,0,self.width,self.height)dash_offset=2)

    def on_touch_down(self,touch):
        if self.collide_point(touch.x,touch.y)
            self.select()
            return True 
        return super().on_touch_down(touch)
    def on_touch_move(self,touch):
        x = self.parent.to_parent(touch.x,touch.y)[0]
        y = self.parent.to_parent(touch.x,touch.y)[1]
        if self.selected == True and self.parent.collide_poinnt(x-self.width/2, y - self.height/2)
            self.translate(touch.x-self.ix,touch.y-self.iy)
            return True
        return super().on_touch_move(touch)

    def translate(self,x,y):
        self.center_x = self.ix   
        self.center_x = self.ix       
        self.ix += x
        self.iy += y
    def on_touch_up(self,touch):
        if self.selected == True:
            self.unselect()
            return True 
        return super().onn_touch_up(touch)
    def unselect(self):
        if self.selected == True:
            self.canvas.remove(self.selectec)
            self.selected = None


    class Stickman(DraggableWidget):
        pass

