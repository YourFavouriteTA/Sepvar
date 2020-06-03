
from manimlib.imports import *
import os
import pyclbr

class Intro2(Scene):
    def construct(self):
        
        Maintext=TextMobject("Physics in action!")
        Maintext.scale(2)
        Maintext.move_to(UP)
        belowtext=TextMobject("Newton's 2nd law and separation of variables")
        belowtext.next_to(Maintext,2*DOWN)
        title=VGroup(Maintext,belowtext)
        self.wait(0.5)
        self.play(Write(title))
        self.wait(4)        
class FallingBall(Scene):
    def construct(self):
        
        forcecolor=RED
        speedcolor=BLUE
        
        speedlabel=TexMobject("\\vec{v}",color=speedcolor)
        draglabel=TexMobject("\\vec{F_d}","=-c","\\vec{v}")
        draglabel.set_color_by_tex_to_color_map({
            "{F_d}": forcecolor,
            "{v}":speedcolor
            })

        gravlabel=TexMobject("\\vec{F_g}=m\\vec{g}",color=GREEN)
        
        ball=Circle(color=GREEN)
        speedarrow=Arrow(np.array([-0.2,-1,0]),np.array([-0.2,-4,0]),color=speedcolor)
        dragarrow=Arrow(np.array([0,1,0]),np.array([0,4,0]),color=forcecolor)
        gravarrow=Arrow(np.array([0.2,-1,0]),np.array([0.2,-4,0]),color=GREEN)
        
        speedlabel.next_to(speedarrow,LEFT)
        draglabel.next_to(dragarrow,RIGHT)
        gravlabel.next_to(gravarrow,RIGHT)
        
        questiontext=TexMobject("\\text{How does }","\\vec{v}","\\text{ change with time?}")
        questiontext.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        questiontext.move_to(ball.get_center())
        rectangle = Rectangle(height=0.75, width=7,fill_color=BLACK, fill_opacity=1, color=GOLD_A)
        rectangle.move_to(ball.get_center())

        Exptext1=TextMobject("Imagine letting")
        Exptext2=TextMobject("go of a ball.")
        Exptext1.to_edge(LEFT)
        Exptext2.next_to(Exptext1,DOWN)
        
        Exptext3=TexMobject("\\text{The force of }","\\text{gravity}")
        Exptext4=TextMobject("will make it fall.")

        Exptext3.set_color_by_tex_to_color_map({
            "{gravity}": GREEN})        
        
        Exptext3.to_edge(LEFT)
        Exptext4.next_to(Exptext1,DOWN)
        
        
        
        #self.add(ball,speedlabel,draglabel,gravlabel)
        self.play(ShowCreation(ball),Write(Exptext1),Write(Exptext2))
        self.wait(3)
        self.play(ShowCreation(gravarrow),ShowCreation(gravlabel),Transform(Exptext1,Exptext3),Transform(Exptext2,Exptext4))
        self.wait(3) 
        
        Exptext5=TexMobject("\\text{As it picks up }", "\\text{speed}",",")
        Exptext6=TexMobject("\\text{it feels a }","\\text{drag force}",".")

        Exptext5.set_color_by_tex_to_color_map({
            "{speed}": BLUE})
        Exptext6.set_color_by_tex_to_color_map({
            "{drag force}": RED})
                

        Exptext5.to_edge(LEFT)
        Exptext6.next_to(Exptext1,DOWN)




        Exptext7=TexMobject("\\text{Small }", "\\text{speed}")
        Exptext8=TexMobject("\\text{means  small }","\\text{drag force}",".")

        Exptext7.set_color_by_tex_to_color_map({
            "{speed}": BLUE})
        Exptext8.set_color_by_tex_to_color_map({
            "{drag force}": RED})
                

        Exptext7.to_edge(LEFT)
        Exptext8.next_to(Exptext1,DOWN)

        Exptext9=TexMobject("\\text{Large }", "\\text{speed}")
        Exptext10=TexMobject("\\text{means  large }","\\text{drag force}",".")

        Exptext9.set_color_by_tex_to_color_map({
            "{speed}": BLUE})
        Exptext10.set_color_by_tex_to_color_map({
            "{drag force}": RED})
                

        Exptext9.to_edge(LEFT)
        Exptext10.next_to(Exptext1,DOWN)

        Exptext11=TexMobject("  ")
        Exptext12=TexMobject("  ")

                

        Exptext11.to_edge(LEFT)
        Exptext12.next_to(Exptext1,DOWN)


        

                
        
        self.play(ShowCreation(speedarrow),ShowCreation(speedlabel),ShowCreation(dragarrow),ShowCreation(draglabel),Transform(Exptext1,Exptext5),Transform(Exptext2,Exptext6),run_time=3)
        self.wait(5)

        speedarrow2=Arrow(np.array([-0.2,-1,0]),np.array([-0.2,-2,0]),color=speedcolor)
        dragarrow2=Arrow(np.array([0,1,0]),np.array([0,2,0]),color=forcecolor)
        
        speedarrow3=Arrow(np.array([-0.2,-1,0]),np.array([-0.2,-5,0]),color=speedcolor)
        dragarrow3=Arrow(np.array([0,1,0]),np.array([0,5,0]),color=forcecolor)
        
        speedarrow4=Arrow(np.array([-0.2,-1,0]),np.array([-0.2,-4,0]),color=speedcolor)
        dragarrow4=Arrow(np.array([0,1,0]),np.array([0,4,0]),color=forcecolor)
        
        self.play(Transform(Exptext1,Exptext7),Transform(Exptext2,Exptext8))
        self.play(Transform(speedarrow,speedarrow2),Transform(dragarrow,dragarrow2),run_time=3)
        self.wait(1)
        self.play(Transform(Exptext1,Exptext9),Transform(Exptext2,Exptext10))
        self.play(Transform(speedarrow,speedarrow3),Transform(dragarrow,dragarrow3),run_time=3)
        self.wait(1)
        self.play(Transform(Exptext1,Exptext11),Transform(Exptext2,Exptext12))
        self.play(Transform(speedarrow,speedarrow4),Transform(dragarrow,dragarrow4),run_time=3)
        self.wait(1)
        
        

        
        self.play(ShowCreation(rectangle),Write(questiontext),run_time=3)
        self.wait(4)

class N2_V2(Scene):
    def construct(self):  
        
        
        
        forcecolor=RED
        speedcolor=BLUE
        
        speedlabel=TexMobject("\\vec{v}",color=speedcolor)
        draglabel=TexMobject("\\vec{F_d}","=-c","\\vec{v}")
        draglabel.set_color_by_tex_to_color_map({
            "{F_d}": forcecolor,
            "{v}":speedcolor
            })

        gravlabel=TexMobject("\\vec{F_g}=m\\vec{g}",color=GREEN)
        
        ball=Circle(color=GREEN)
        ball.to_edge(LEFT,buff=1.5)
        
        speedarrow=Arrow(np.array([-0.2-4.5,-1,0]),np.array([-0.2-4.5,-4,0]),color=speedcolor)
        dragarrow=Arrow(np.array([0-4.5,1,0]),np.array([0-4.5,4,0]),color=forcecolor)
        gravarrow=Arrow(np.array([0.2-4.5,-1,0]),np.array([0.2-4.5,-4,0]),color=GREEN)
        
        speedlabel.next_to(speedarrow,LEFT)
        draglabel.next_to(dragarrow,RIGHT)
        gravlabel.next_to(gravarrow,RIGHT)
        
        questiontext=TexMobject("\\text{How does }","\\vec{v}","\\text{ change with time?}")
        questiontext.set_color_by_tex_to_color_map({
            "v": BLUE})
        questiontext.move_to(ball.get_center())
        
        self.play(ShowCreation(ball),ShowCreation(gravarrow),ShowCreation(gravlabel))
        self.wait(1)
        self.play(ShowCreation(speedarrow),ShowCreation(speedlabel),ShowCreation(dragarrow),ShowCreation(draglabel),run_time=2)
        self.wait(1) #"We can find the change in speed using Newton's 2nd Law"
        
        
        cleartext=TextMobject("   ")
        
        Headtext=TextMobject("Newton's 2nd law:")
        Headtext.move_to(3*UP+2*RIGHT)
        N2eq1=TexMobject("\\sum \\vec{F} = m \\vec{a}")
        N2eq1.next_to(Headtext,DOWN)
        
        
        N2eq2=TexMobject("\\vec{F_d}","+","\\vec{F_g}=","\\sum \\vec{F} = m \\vec{a} ")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq2.set_color_by_tex_to_color_map({
            "{v}": BLUE, "{F_d}":RED, "{F_g}":GREEN})
        N2eq2.next_to(N2eq1,DOWN)
        
        N2eq3=TexMobject("-c","\\vec{v}","+m\\vec{g}= m ","{d ","\\vec{v}","\\over dt","} ")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq3.next_to(N2eq2,DOWN)
        N2eq3.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        N2eq4=TexMobject("c","{v}","\\hat{y}+mg (-\\hat{y})= m(-\\hat{y})","{d ","{v}","\\over dt","} "," (-\\vec{y}) ")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq4.next_to(N2eq3,DOWN)
        N2eq4.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        N2eq5=TexMobject("c","{v}","-mg= -m","{d ","{v}","\\over dt","} ","")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq5.next_to(N2eq4,DOWN)
        N2eq5.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        N2eq6=TexMobject("m","{d ","{v}","\\over dt","} ","=-c","{v}","+mg")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq6.next_to(N2eq4,DOWN)
        N2eq6.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        N2eq7=TexMobject("{d ","{v}","\\over dt","} ","=- \\frac{c}{m} ","{v}","+g")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq7.next_to(N2eq4,DOWN)
        N2eq7.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        
        
        
        
       
        
        
        
        
        
        
        self.play(Write(Headtext), Write(N2eq1)) #N2 draws on screen
        self.wait(3) #"It says: How much the ball changes its speed depends on all the forces acting on it"
        self.play(Write(N2eq2))
        self.wait(3)# The Gravity and Drag on the ball are given by these expressions
        self.play(Write(N2eq3))
        self.wait(3)# Let us write the vectors as the product of their magnitude and directions
        self.play(Write(N2eq4))
        self.wait(3)#Let us look only at the magnitudes since they are all in the y-direction 
        self.play(Write(N2eq5))
        self.wait(3)#Rearrange this to isolate the derivative
        self.play(Transform(N2eq5,N2eq6))
        self.wait(3)
        self.play(Transform(N2eq5,N2eq7))
        self.wait(3) #Let us tidy things up a bit
#        
        self.play(Transform(Headtext,cleartext),
                  Transform(N2eq1,cleartext),
                  Transform(N2eq2,cleartext),
                  Transform(N2eq3,cleartext),
                  Transform(N2eq4,cleartext),
                  ApplyMethod(N2eq5.move_to,Headtext),run_time=3)
        self.wait(3) 
        Pred1=TexMobject("\\text{Pred. 1: Cst. acc. when }","{v}","\\text{ is small.}")
        Pred1.next_to(N2eq5,1.2*DOWN)
        Pred1.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        self.play(Write(Pred1),run_time=3)
        
        Pred1_eq1=TexMobject("{d ","{v}","\\over dt","} ","=- \\frac{c}{m} 0+g")#= m \\frac{d\\vec{v}}{dt^2} 
        Pred1_eq1.move_to(N2eq5)
        Pred1_eq1.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        Pred1_eq2=TexMobject("{d ","{v}","\\over dt","} ","=g")#= m \\frac{d\\vec{v}}{dt^2} 
        Pred1_eq2.move_to(N2eq5)
        Pred1_eq2.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        Pred1_eq3=TexMobject("{v}","(t)=gt")#= m \\frac{d\\vec{v}}{dt^2} 
        Pred1_eq3.move_to(N2eq5)
        Pred1_eq3.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        Reset_eq=TexMobject("{d ","{v}","\\over dt","} ","=- \\frac{c}{m} ","{v}","+g")#= m \\frac{d\\vec{v}}{dt^2} 
        Reset_eq.move_to(N2eq5)
        Reset_eq.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        Pred2=TextMobject("Pred. 2: Constant terminal speed for large $t$.")
        Pred2.next_to(Pred1,DOWN)
        
        
        self.play(Transform(N2eq5,Pred1_eq1),run_time=3)
        self.play(Transform(N2eq5,Pred1_eq2),run_time=3)
        self.play(Transform(N2eq5,Pred1_eq3),run_time=3)
        self.wait(3)#What is the second prediction?        
        self.play(Transform(N2eq5,Reset_eq),Transform(Pred1,Pred2),run_time=3)        
    
        
        N2eq7.next_to(N2eq4,DOWN)
#        
#        
#        
        Pred2=TextMobject("Pred. 2: Cst. speed for large $t$.")
        Pred2.next_to(Pred1,DOWN)
#        
        Question=TextMobject("What is this terminal speed?")
        Question.next_to(Pred2,DOWN)
        self.play(Write(Question),run_time=3)
        
        N2eq8=TexMobject("0=- \\frac{c}{m} v_t+g")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq8.next_to(Question,DOWN)
        N2eq8.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        N2eq9=TexMobject("\\frac{c}{m} v_t= g")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq9.next_to(N2eq8,DOWN)
        N2eq9.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        N2eq10=TexMobject("v_t= \\frac{mg}{c} ")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq10.next_to(N2eq9,DOWN)        
        N2eq10.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        self.play(Write(N2eq8))
        self.wait(3)
        self.play(Write(N2eq9))
        self.wait(3)
        self.play(Write(N2eq10))
        self.wait(3)
        N2eq5_update1=TexMobject("{d ","{v}","\\over dt","} ","= g\\left(1-\\frac{c}{mg} ","{v}","\\right)")
        N2eq5_update2=TexMobject("{d ","{v}","\\over dt","} ","= g\\left(1-{","{v}","\\over v_t","}\\right)")
        N2eq5_update1.move_to(3*UP+2*RIGHT)
        N2eq5_update2.move_to(3*UP+2*RIGHT)
        
        N2eq5_update1.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        N2eq5_update2.set_color_by_tex_to_color_map({
            "{v}": BLUE})
#        
#        
        self.play(Transform(N2eq8,cleartext),
                  Transform(N2eq9,cleartext))
        self.wait(3)
        self.play(Transform(N2eq5,N2eq5_update1))
        self.wait(3)
        self.play(Transform(N2eq5,N2eq5_update2))
        self.wait(3)
        
        Pred3=TextMobject("How do we solve this")
        Pred3.next_to(Pred1,DOWN)
#        
        diffeq=TextMobject("differential equation?")
        diffeq.next_to(Pred2,DOWN)      
        
        self.play(Transform(Question,diffeq),Transform(Pred1,Pred3))
        self.wait(5)        
     
        
        
class Solution_Scene(Scene):
    def construct(self):  
        
        
        
        forcecolor=RED
        speedcolor=BLUE
        
        speedlabel=TexMobject("\\vec{v}",color=speedcolor)
        draglabel=TexMobject("\\vec{F_d}","=-c","\\vec{v}")
        draglabel.set_color_by_tex_to_color_map({
            "{F_d}": forcecolor,
            "{v}":speedcolor
            })

        gravlabel=TexMobject("\\vec{F_g}=m\\vec{g}",color=GREEN)
        
        ball=Circle(color=GREEN)
        ball.to_edge(RIGHT,buff=1.5)
        
        speedarrow=Arrow(np.array([-0.2+4.5,-1,0]),np.array([-0.2+4.5,-4,0]),color=speedcolor)
        dragarrow=Arrow(np.array([0+4.5,1,0]),np.array([0+4.5,4,0]),color=forcecolor)
        gravarrow=Arrow(np.array([0.2+4.5,-1,0]),np.array([0.2+4.5,-4,0]),color=GREEN)
        
        speedlabel.next_to(speedarrow,LEFT)
        draglabel.next_to(dragarrow,RIGHT)
        gravlabel.next_to(gravarrow,RIGHT)
        
        
        
        self.play(ShowCreation(ball),ShowCreation(gravarrow),ShowCreation(gravlabel))
        
        self.play(ShowCreation(speedarrow),ShowCreation(speedlabel),ShowCreation(dragarrow),ShowCreation(draglabel),run_time=2)
        self.wait(3) #"We can find the change in speed using Newton's 2nd Law"
        
        
        
        ### Define and write main equation ###
        Main_eq=TexMobject("{d ","{v}","\\over dt}","=g \\left(1-{","{v}","\\over v_t}\\right)")# =g ( 1- {d ","{v}","\\over dt} )"
        Main_eq.move_to(3*UP+2*LEFT)
        Main_eq.set_color_by_tex_to_color_map({"{v}": BLUE})
        self.play(Write(Main_eq),run_time=1)
        self.wait(3)    
        
        ### Separate variables ###
        Eq1=TexMobject("{d ","{v}","\\over \\left(1-{","{v}","\\over v_t}\\right) } = g dt")        
        Eq1.next_to(Main_eq,DOWN)
        Eq1.set_color_by_tex_to_color_map({"{v}": BLUE})        
        self.play(Write(Eq1),run_time=2)
        self.wait(4)
        ### Write integral ### #"\int_{0}^{ ","{v}","(t)}
        Eq2=TexMobject("\int^","{v}","_0{d ","{v}","\\over \\left(1-{","{v}","\\over v_t}\\right) } = g \int_{0}^{t} dt")        
        Eq2.next_to(Main_eq,DOWN)
        Eq2.set_color_by_tex_to_color_map({"{v}": BLUE})        
        self.play(Transform(Eq1,Eq2),run_time=2)
        
        ### Define substitution ###
        definetext=TextMobject("Define the substitution:")
        definetext.next_to(Eq2,DOWN)
        Eq3=TexMobject("{u}","=\\left(1-{","{v}","\\over v_t}\\right)")
        Eq3.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":PURPLE_E})
        Eq3.next_to(definetext,DOWN)
        self.play(Write(definetext),run_time=2)
        self.play(Write(Eq3),run_time=2)
        self.wait(3)
        
        ### Take derivative w.r.t. v ###
        Eq4=TexMobject("{d ","{u}","\\over d","{v}","} =-{1 \\over v_t} ")
        Eq4.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":PURPLE_E})
        Eq4.next_to(Eq3,DOWN)
        self.play(Write(Eq4),run_time=2)
        self.wait(3)
        
        ### Solve for du ###
        Eq5=TexMobject("d ","{u}"," =-{d","{v}"," \\over v_t} ")
        Eq5.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":PURPLE_E})
        Eq5.next_to(Eq3,DOWN)
        self.play(Transform(Eq4,Eq5),run_time=2)
        self.wait(3)
        
        ### Solve for dv ###
        Eq6=TexMobject("d ","{v}"," =-v_t d","{u}")
        Eq6.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":PURPLE_E})
        Eq6.next_to(Eq3,DOWN)
        self.play(Transform(Eq4,Eq6),run_time=2)
        self.wait(3)        

        ### Rewrite Text ###
        rewritetext=TextMobject("Rewrite Integral")
        rewritetext.next_to(Eq2,DOWN)
        emptytext=TextMobject("   ")
        emptytext.next_to(rewritetext,DOWN)
        self.play(Transform(definetext,rewritetext),Transform(Eq3,emptytext) ,run_time=2)
        
        ### Rewrite Integral ###
        Eq7=TexMobject("\int^","{1-","{v}","/v_t}","_0{-v_t d ","{u}","\\over ","{u}"," } = g \int_{0}^{t} dt")    #{-v_t d ","{u}","\\over ","{u}"," }     
        Eq7.next_to(Main_eq,DOWN)
        Eq7.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":PURPLE_E}) 
        Eq8=TexMobject("-v_t\int^","{1-","{v}","/v_t}","_0{d ","{u}","\\over ","{u}"," } = g \int_{0}^{t} dt")    #{-v_t d ","{u}","\\over ","{u}"," }     
        Eq8.next_to(Main_eq,DOWN)
        Eq8.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":PURPLE_E}) 
        Eq9=TexMobject("\int^","{1-","{v}","/v_t}","_0{d ","{u}","\\over ","{u}"," } = -{g\\over v_t}  \int_{0}^{t} dt")    #{-v_t d ","{u}","\\over ","{u}"," }     
        Eq9.next_to(Main_eq,DOWN)
        Eq9.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":PURPLE_E}) 
        
        
        self.play(Transform(Eq1,Eq7),run_time=3)
        self.play(Transform(Eq1,Eq8),run_time=3)
        self.play(Transform(Eq1,Eq9),run_time=3)
        
                
        ### Compute Integral ### #       
        computetext=TextMobject("Compute Integral")
        computetext.next_to(Eq2,DOWN)       
        Eq10=TexMobject("\ln \\left( 1-{","{v}","\\over v_t}  \\right) = -{g\\over v_t}  t")    #{-v_t d ","{u}","\\over ","{u}"," }     
        Eq10.next_to(Main_eq,DOWN)
        Eq10.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":GOLD_A}) 
        self.play(Transform(definetext,computetext),run_time=3)
        self.play(Transform(Eq1,Eq10),run_time=3)
                
        ### Take exponential ###
        solvetext=TextMobject("Solve for the speed")
        solvetext.next_to(Eq2,DOWN)       
        Eq11=TexMobject(" 1-{","{v}","\\over v_t}   = \\exp \left(-{g\\over v_t}  t\\right)")    #{-v_t d ","{u}","\\over ","{u}"," }     
        Eq11.next_to(Main_eq,DOWN)
        Eq11.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":GREEN}) 
        self.play(Transform(definetext,solvetext),run_time=3)
        self.play(Transform(Eq1,Eq11),run_time=3)
        
        ### Solve for v(t) ###
        Eq11=TexMobject(" 1- \\exp \left(-{g\\over v_t}  t\\right)   ={","{v}","\\over v_t}")    #{-v_t d ","{u}","\\over ","{u}"," }     
        Eq11.next_to(Main_eq,DOWN)
        Eq11.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":GREEN}) 
        
        Eq12=TexMobject("{v}","(t)= v_t\\left(1- \\exp \left(-{g\\over v_t}  t\\right)\\right)" )    #{-v_t d ","{u}","\\over ","{u}"," }     
        Eq12.next_to(Main_eq,DOWN)
        Eq12.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":GREEN}) 
        
        nicetext=TextMobject("NICE!")
        nicetext.next_to(Eq2,DOWN)               
        self.play(Transform(definetext,solvetext),run_time=3)
        self.play(Transform(Eq1,Eq12),run_time=3)
        self.play(Transform(definetext,nicetext),run_time=1.5)
        self.wait(3)
        
        ### Beautify ###
        beautifytext=TextMobject("Beautify!      ")
        beautifytext.next_to(Eq2,DOWN)               
        
        Eq13=TexMobject("{v}","(t)= v_t\\left(1- \\exp \left(-{g\\over (mg/c)}  t\\right)\\right)" )    #{-v_t d ","{u}","\\over ","{u}"," }     
        Eq13.next_to(Main_eq,DOWN)
        Eq13.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":GREEN}) 
        
        self.play(Transform(definetext,beautifytext),run_time=1.5)
        self.play(Transform(Eq1,Eq13),run_time=3)
        
        Eq14=TexMobject("{v}","(t)= v_t\\left(1- \\exp \left(-{c\\over m}  t\\right)\\right)" )    #{-v_t d ","{u}","\\over ","{u}"," }     
        Eq14.next_to(Main_eq,DOWN)
        Eq14.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":GREEN}) 
        
        self.play(Transform(Eq1,Eq14),run_time=3)
        
        ### Characteristic time ###
        Expl1=TexMobject("(v_t -","{v}",")\\text{ decreases exponentially.}" )
        Expl1.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":GREEN})         
        Expl2=TexMobject("\\text{Characteristic time:}" )
        
        Expl1.next_to(Eq2,DOWN)
        Expl2.next_to(Expl1,DOWN)
        
        eq4replacement=TexMobject("\\tau={m\\over c}")
        eq4replacement.next_to(Expl2,DOWN)
        
        
        

        
        
        
        Eq15=TexMobject("{v}","(t)= v_t\\left(1- \\exp \left(-{t\\over \\tau} \\right)\\right)" )    #{-v_t d ","{u}","\\over ","{u}"," }     
        Eq15.next_to(Main_eq,DOWN)
        Eq15.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":GREEN}) 
        
        self.play(Transform(Eq1,Eq15),run_time=3)  
        self.play(Transform(definetext,Expl1),run_time=1.5)
        self.play(Write(Expl2),Transform(Eq4,eq4replacement),run_time=5)
        self.wait(3)
              
        
        
        
                      
        
class VtermGraph(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 6,
        "y_min" : 0,
        "y_max" : 1.3,
        "graph_origin" : DL*3+2*LEFT ,
        "function_color" : RED ,
        "axes_color" : GOLD_E,
        "y_tick_frequency" : 0.1 ,
        "y_labeled_nums" : range(0,2),
        "y_label_decimal":3,
        "y_axis_label": "${v \\over v_t}$",
        "y_label_direction":2*LEFT,
        "exclude_zero_label": True,


        "x_labeled_nums" :range(0,7,1),        
        "x_axis_label": "${t\\over\\tau}$",
        "x_label_direction":DOWN ,
        
                        

    }   
    def construct(self):
        ### Set up the graph ###
        self.setup_axes(animate=True)
        
        
        ### Add Top text ###
        Toptext=TexMobject("\\text{Let's draw the graph of }","{v}","(t)")
        Toptext.move_to(3*UP+1*RIGHT)
        Toptext.set_color_by_tex_to_color_map({"{v}": BLUE}) 
        
        Eq15=TexMobject("{v}","(t)= v_t\\left(1- \\exp \left(-{t\\over \\tau} \\right)\\right)" )    #{-v_t d ","{u}","\\over ","{u}"," }     
        Eq15.next_to(Toptext,12.5*DOWN)
        Eq15.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        self.play(Write(Toptext),Write(Eq15),run_time=3)        
        
        ### Draw v(t) ###
        func_graph=self.get_graph(self.vgraph,color=BLUE)
        graph_lab = self.get_graph_label(func_graph,label="v(t)" )
        self.play(ShowCreation(func_graph),Write(graph_lab))
        self.wait(5)
        
        ### Explain the graph ###        
        Toptext2=TexMobject("\\text{Remember the first prediction?}")
        Toptext2.move_to(Toptext)
        
        self.play(Transform(Toptext,Toptext2))

        Pred1=TexMobject("\\text{\"Pred. 1: Cst. acc. when }","{v}","\\text{ is small.\"}")
        Pred1.next_to(Toptext,DOWN)
        Pred1.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        self.play(Write(Pred1),run_time=1.5)
        
        Pred1_eq1=TexMobject("{d ","{v}","\\over dt","} =- \\frac{c}{m} 0+g")#= m \\frac{d\\vec{v}}{dt^2} 
        Pred1_eq1.next_to(Pred1,3.5*DOWN)
        Pred1_eq1.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        
        Pred1_eq2=TexMobject("{d ","{v}","\\over dt","} =g")#= m \\frac{d\\vec{v}}{dt^2} 
        Pred1_eq2.next_to(Pred1,3.5*DOWN)
        Pred1_eq2.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        Pred1_eq3=TexMobject("{v}","(t)=gt")#= m \\frac{d\\vec{v}}{dt^2} 
        Pred1_eq3.next_to(Pred1,3.5*DOWN)
        Pred1_eq3.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        self.play(Write(Pred1_eq1),run_time=1.5)
        self.wait(1)
        self.play(Transform(Pred1_eq1,Pred1_eq2),run_time=1.5)
        self.wait(1)
        self.play(Transform(Pred1_eq1,Pred1_eq3),run_time=1.5)
        
        ### Change toptext ###
        Toptext3=TexMobject("\\text{Let's graph this }","\\text{approximation}")
        Toptext3.set_color_by_tex_to_color_map({
            "{approximation}": RED})
        Toptext3.move_to(Toptext)
        cleartext=TexMobject("   ")
        self.play(Transform(Pred1,cleartext),Transform(Toptext,Toptext3),run_time=2)
        func_graph2=self.get_graph(self.vapprox,color=RED)
        self.play(ShowCreation(func_graph2))
        graph_lab2=self.get_graph_label(func_graph2,label = "v(t)\\approx gt", x_val=0.5, direction=UP/2)        
        ### Reset and prepare for next prediction ###
        
        looksgood=TexMobject("\\text{Looks good!}")
        looksgood.next_to(Toptext,DOWN)
        self.play(Transform(Pred1,looksgood))
        self.wait(1.5)
        self.play(Transform(Pred1,cleartext),Transform(Pred1_eq1,cleartext),run_time=1.5)
        
        ### Second approximation ###
        Toptext4=TexMobject("\\text{What about the second prediction?}")
        Toptext4.move_to(Toptext)
        
        self.play(Transform(Toptext,Toptext4))

        Pred2=TexMobject("\\text{ \"Pred. 2: Cst. speed for large } t\\text{.\"} ")
        Pred2.next_to(Toptext,DOWN)
        
        Toptext5=TexMobject("\\text{Let's graph this }","\\text{limit}")
        Toptext5.move_to(Toptext)
        Toptext5.set_color_by_tex_to_color_map({"{limit}":GREEN})
        
        self.play(Transform(Pred1,Pred2),run_time=1.5)
        self.wait(1.5)
        self.play(Transform(Toptext,Toptext5),run_time=1.5)
        
        func_graph3=self.get_graph(self.vterm,color=GREEN)
        self.play(ShowCreation(func_graph3),run_time=2)
        self.wait(2)
        
        questiontext=TextMobject("Thanks for watching!")
        
        rectangle = Rectangle(height=0.75, width=7,fill_color=BLACK, fill_opacity=1, color=GOLD_A)
        rectangle.move_to(questiontext.get_center())
        
        self.play(ShowCreation(rectangle),Write(questiontext),run_time=3)
        self.wait(5)        
#        Toptext4=TexMobject("\\text{Let's graph this }","\\text{limit}")
#        Toptext4.set_color_by_tex_to_color_map({
#            "{limit}": RED})
        
        
        

    def vgraph(self,x):
        return 1-np.exp(-x)
    def vapprox(self,x):
        return x
    def vterm(self,x):
        return 1
