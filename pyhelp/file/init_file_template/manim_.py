def manim_1():
    return "from manim import *\n"

def manim_2():
    return """class Hello(Scene):
    def construct(self):
"""

def manim_3():
    return """        a = Tex('Hello World!')
        self.play(Write(a))"""