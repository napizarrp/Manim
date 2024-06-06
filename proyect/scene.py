from manim import *
from manim_chemistry import *


# Constants
h = 6.62607015e-34  # Planck's constant (m^2 kg / s)
c = 299792458  # Speed of light in vacuum (m/s)
k = 1.380649e-23  # Boltzmann's constant (m^2 kg s^-2 K^-1)

def create_glow(vmobject, rad=1, col=YELLOW):
    glow_group = VGroup()
    for idx in range(60):
        new_circle = Circle(radius=rad*(1.002**(idx**2))/200, stroke_opacity=0, fill_color=col,
        fill_opacity=0.2-idx/300).move_to(vmobject)
        glow_group.add(new_circle)
    return glow_group

def planck_law_nm(wavelength):
    T = 5778  # Temperature of the Sun (K)

    return (2 * h * c**2) / ((wavelength*1e-9)**5 * (np.exp((h * c) / ((wavelength*1e-9) * k * T)) - 1)) *1e-13

def shift_left(mobject):
    return mobject.shift(3*LEFT)
def shift_right(mobject):
    return mobject.shift(3*RIGHT)
def gaussian(Amplitude=1,mu=700,sigma=20):
    return lambda x: Amplitude * np.exp(-((x - mu)** 2) / (2 * sigma ** 2)) 


class DrawPeriodicTable(Scene):
    def construct(self):
        self.camera.background_color = WHITE

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

class Create_dessin(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        svg = SVGMobject("hybr.svg")

        self.play(Write(svg),run_time=3)
        self.wait(1)

class Create_svg(Scene):
    def construct(self):

        text = Tex("SleepAble")
        text.set_color(PURPLE)
        text.scale(1.5)
        self.play(Write(text),run_time=2)
        self.wait(1)

        lit = SVGMobject("cama.svg")
        dessin = SVGMobject("dessin-2.svg")
        bruit = SVGMobject("bruit.svg")

        dessin.scale(1.5)
        lit.scale(1.5)
        bruit.scale(1.5)

        lit.shift(RIGHT*2)
        dessin.shift(RIGHT*2)
        bruit.shift(RIGHT*2)

        self.play(ApplyFunction(shift_left,text))
        self.play(Write(lit),run_time=3)
        self.play(Write(bruit),run_time=0.5)
        self.play(Wiggle(bruit),run_time=0.5)
        self.play(FadeIn(dessin),FadeOut(lit),Unwrite(bruit),run_time=3)

        self.wait(1)
        self.play(FadeOut(dessin),Unwrite(text))
        self.wait(1)




    


class CreateComparation(Scene):
    def construct(self):
        text = Tex("What makes the lasers different from other sources?")
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))    
        dot = Dot(point=[-4,0,0])
        glow = create_glow(dot, rad=1, col=RED)
        self.add(dot)
        self.play(Transform(dot,glow))
        self.wait(0.5)
        
        self.play(FadeToColor(dot, YELLOW))
        self.play(FadeToColor(dot, GREEN))




class Graph(Scene):
    def construct(self):

        # Wavelength range (m)

        axes = Axes(x_range=[100,  1400,400], y_range=[0, 3.1],x_length=5,y_length=4,axis_config={
                'color' : WHITE,
                'stroke_width' : 2,
                'include_numbers' : True,
                'include_tip' : False,

                'decimal_number_config' : {
                    'num_decimal_places' : 0,
                    'include_sign' : False,
                    'color' : WHITE
                }
            },)
        y_label = axes.get_y_axis_label(
            Tex("Spectra Radiance").scale(0.65).rotate(90 * DEGREES),
            edge=LEFT,
            direction=LEFT,
            buff=0.3,
        )
        x_label = axes.get_x_axis_label(
            Tex("Wavelength(nm)").scale(0.65),
            edge=DOWN,
            direction=DOWN,
            buff=0.4,
        )
        self.play(FadeIn(axes, y_label, x_label))
    
        graph = axes.plot(planck_law_nm, color=BLUE)
        self.play(Create(graph))
        # colored area under the curve
        area = axes.get_area(graph,x_range=[380, 750])
        area.set_color_by_gradient((RED,RED,ORANGE,YELLOW,GREEN,GREEN,BLUE,PURPLE))
        area.set_sheen_direction(LEFT)
        self.play(Create(area))
        self.wait(1)

        # create a gaussian function
        gaussian_graph = axes.plot(gaussian(Amplitude=2), x_range=(100, 1400,1), color=RED, use_smoothing=False)

        self.play(Transform(graph,gaussian_graph),FadeOut(area))

        self.wait(2)


#& C:/ProgramData/anaconda3/python.exe -m manim 'C:\Users\pizarron\Documents\Manim\proyect\scene.py' Create_svg  