from manim import *
from numpy import *

class SenoQ1(Scene):
   
    def construct(self):
        #EIXOS
        axes2=Axes(x_range=[-2*np.pi,2*np.pi],
                   y_range=[-2,2],
                   x_length=5,
                   y_length=3,
                   axis_config={'include_tip': False, 'include_ticks': True,}).shift(2*UP)
        
        axes=Axes(x_range=[-1,1],
                  y_range=[-1,1],
                  x_length=5,
                  y_length=5,
                  axis_config={'include_tip': False}).scale(0.5).shift(2*DOWN)
      
        #PONTOS E LABELS

        pontoA1=Dot(axes2.c2p(np.pi/4,np.sin(np.pi/4)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelA1=MathTex("A", 
                       color=WHITE,
                       font_size=24).next_to(pontoA1,
                                             UP + RIGHT,
                                             buff=0.2)

        pontoA=Dot(axes.c2p(np.sin(np.pi/4),np.cos(np.pi/4)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelA=MathTex("A", 
                       color=WHITE,
                       font_size=24).next_to(pontoA,
                                             UP + RIGHT,
                                             buff=0.2)
        pontoB=Dot(axes.c2p(sin(-np.pi/4),cos(-np.pi/4)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelB=MathTex("B", 
                       color=WHITE,
                       font_size=24).next_to(pontoB,
                                             UP + LEFT,
                                             buff=0.2)
        pontoC=Dot(axes.c2p(sin(np.pi/2),cos(np.pi/2)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelC=MathTex("C", 
                       color=WHITE,
                       font_size=24).next_to(pontoC,
                                             UP + RIGHT,
                                             buff=0.2)
        pontoD=Dot(axes.c2p(sin(np.pi),cos(np.pi)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelD=MathTex("D", 
                       color=WHITE,
                       font_size=24).next_to(pontoD,
                                             DOWN + RIGHT,
                                             buff=0.2)
        

        #GRÁFICOS

        curva_parametrica=axes.plot_parametric_curve(
            lambda t:[np.sin(-t),np.cos(-t),0],
                   t_range=[3*np.pi/2,7*np.pi/4],
                   color=RED)

        curva_parametrica2=axes.plot_parametric_curve(
            lambda t:[np.sin(t+np.pi/2),np.cos(t+np.pi/2),0],
                    t_range=[0,2*np.pi],
                    color=BLUE)

        seno=axes2.plot(
            lambda x: sin(x),
                   x_range=[-2*np.pi,2*np.pi],
                   color=BLUE)
        

        #LINHAS E ANGULO

        linha1=Line(start=axes.c2p(0,0),
                    end=axes.c2p(0.7,0.7),
                    color=RED)
        
        linha2=Line(start=axes.c2p(0,0),
                    end=axes.c2p(1,0),
                    color=RED)

        angle= Angle(linha1,
                     linha2,
                     radius=0.4,
                     other_angle=True,
                     color=RED)
        
        labelAngle=MathTex("\\frac{\pi}{4}", 
                       color=WHITE,
                       font_size=24).next_to(angle,
                                             DOWN + RIGHT,
                                             buff=0.2)

        
        #ANIMÇÃO

        self.play(Create(axes),Create(axes2))           
        self.play(Create(curva_parametrica2),Create(seno),run_time=3)        
        self.play(Create(curva_parametrica))      
        self.play(Create(linha1),Create(linha2),Create(angle),Write(labelAngle))
        self.play(Create(pontoA),Write(labelA))
        self.play(Create(pontoB),Write(labelB))
        self.play(Create(pontoC),Write(labelC))
        self.play(Create(pontoD),Write(labelD))   
        self.wait(5)