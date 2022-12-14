from model import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

        self.skybox = Skybox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        n, s = 50, 3
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        # add(Cat(app, pos=(0, -2, -10)))
        add(IronMan(app, pos=(0, -2, -10)))

    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()
