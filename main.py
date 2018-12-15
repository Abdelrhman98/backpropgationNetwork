from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import Ellipse
from kivy.app import App
from kivy.graphics import Color, Rectangle, Line
from random import random as r
from functools import partial
import random

MIN_HEIGHT = 100
MAX_HEIGHT = 550 - MIN_HEIGHT
CIRCLE_RADIUS = 15

nEntered = 3
lEntered = 2
mEntered = 3

class DataLists:
    nSet = []
    lSet = []
    mSet = []

dataList = DataLists()

def draw_lines(wid):
    for n in range(len(dataList.nSet)):
        for l in range(len(dataList.lSet)):
            with wid.canvas:
                Color(1, 1, 1, mode='rgb')
                Line(points=[100,dataList.nSet[n],400,dataList.lSet[l]])
    for l in range(len(dataList.lSet)):
        for m in range(len(dataList.mSet)):
            with wid.canvas:
                Line(points=[400,dataList.lSet[l],700,dataList.mSet[m]])

class BackPropagationNetworkApp(App):
    
    def draw(self, wid, *largs):
        nPOS = MIN_HEIGHT
        lPOS = MIN_HEIGHT
        mPOS = MIN_HEIGHT
        nSTEP = MAX_HEIGHT / (nEntered - 1)
        lSTEP = MAX_HEIGHT / (lEntered - 1)
        mSTEP = MAX_HEIGHT / (mEntered - 1)
        with wid.canvas:
            for x in range(nEntered):
                Color(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), mode='rgb')
                Ellipse(pos=(100-CIRCLE_RADIUS, nPOS-CIRCLE_RADIUS), size=(CIRCLE_RADIUS * 2,CIRCLE_RADIUS * 2))
                dataList.nSet.append(nPOS)
                nPOS += nSTEP
            for x in range(lEntered):
                Color(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), mode='rgb')
                Ellipse(pos=(400-CIRCLE_RADIUS, lPOS-CIRCLE_RADIUS), size=(CIRCLE_RADIUS * 2,CIRCLE_RADIUS * 2))
                dataList.lSet.append(lPOS)
                lPOS += lSTEP
            for x in range(mEntered):
                Color(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), mode='rgb')
                Ellipse(pos=(700-CIRCLE_RADIUS, mPOS-CIRCLE_RADIUS), size=(CIRCLE_RADIUS * 2,CIRCLE_RADIUS * 2))
                dataList.mSet.append(mPOS)
                mPOS += mSTEP
        draw_lines(wid)

    def reset(self, wid, *largs):
        wid.canvas.clear()

    def build(self):
        wid = Widget()
        draw = Button(text='Draw',on_press=partial(self.draw, wid))
        reset = Button(text='Reset',on_press=partial(self.reset, wid))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(draw)
        layout.add_widget(reset)

        label1 = Label(text='N:'+str(nEntered))
        label2 = Label(text='L:'+str(lEntered))
        label3 = Label(text='M:'+str(mEntered))

        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)
        return root


if __name__ == '__main__':
    BackPropagationNetworkApp().run()