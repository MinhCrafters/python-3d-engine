import pygame
import moderngl
import sys
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene


class GraphicsEngine:
    def __init__(self, window_size=(1600, 900)):
        pygame.init()

        self.WINDOW_SIZE = window_size

        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

        pygame.display.set_mode(
            self.WINDOW_SIZE, flags=pygame.OPENGL | pygame.DOUBLEBUF)

        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)

        self.ctx = moderngl.create_context()

        self.ctx.enable(flags=moderngl.DEPTH_TEST | moderngl.CULL_FACE)

        self.clock = pygame.time.Clock()

        self.FPS = 120

        self.time = 0
        self.delta_time = 0

        self.light = Light()

        self.camera = Camera(self)

        self.mesh = Mesh(self)

        self.scene = Scene(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.mesh.destroy()
                pygame.quit()
                sys.exit()

    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18))

        self.scene.render()

        pygame.display.set_caption(str(round(self.clock.get_fps())) + ' FPS')

        pygame.display.flip()

    def get_time(self):
        self.time = pygame.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
