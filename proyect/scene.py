from manim import *
from manim_chemistry import *

class DrawPeriodicTable(Scene):
    def construct(self):
        Table = PeriodicTable(data_file="Elements.csv")
        self.play(Write(Table))
        carbon = MElementObject.from_csv_file_data(filename="Elementos.csv", atomic_number=6)
        self.play(Transform(Table,carbon))
        self.wait(1)

class CreateSources(Scene):
    def construct(self):
        sun= ImageMobject("sun.jpg")
        bulb= ImageMobject("bulb1.jpg")
        bulb.scale(0.15)
        sun.scale(0.5)
        sun.set_opacity(1)
        dot = Dot()
        glow = create_glow(dot, rad=1, col=YELLOW)
        self.add(dot)
        self.play(Flash(dot),FadeIn(glow))
        circle3 = Circle(radius=2.8,color=None)  # create a circle
        circle3.set_fill([RED,YELLOW], opacity=1,family=True)  # set the color and transparency
        self.wait()
        self.play(Transform(dot, circle3),FadeOut(glow) ) 
        self.play(FadeIn(sun))
    
        #fade out everyrhing on screen together
        self.remove(dot)
        self.play(FadeOut(sun))
        self.play(FadeIn(bulb))
        self.play(FadeOut(bulb))

      
def create_glow(vmobject, rad=1, col=YELLOW):
    glow_group = VGroup()
    for idx in range(60):
        new_circle = Circle(radius=rad*(1.002**(idx**2))/200, stroke_opacity=0, fill_color=col,
        fill_opacity=0.2-idx/300).move_to(vmobject)
        glow_group.add(new_circle)
    return glow_group






class CreateComparation(Scene):
    def construct(self):
        text = Tex("What makes the lasers different from other sources?")
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))    
        dot = Dot()
        glow = create_glow(dot, rad=1, col=RED)
        self.add(dot)
        self.play(Transform(dot,glow))
        self.wait(0.5)
        
        self.play(dot.animate.set_color(YELLOW), run_time=0.5)
        self.wait(1)
        self.play(dot.animate.set_color(ORANGE), run_time=0.5)
        self.wait(1)
        self.play(dot.animate.set_color(GREEN), run_time=0.5)
        self.wait(1)
        self.play(dot.animate.set_color(BLUE), run_time=0.5)
        self.wait(1)
        self.play(dot.animate.set_color(PURPLE), run_time=0.5)
        self.wait(1)



    
        #create a line like it where a laser
        line = Line(start=(0,0,0), end=RIGHT)
        line.set_color(YELLOW)
        self.play(Create(line))



