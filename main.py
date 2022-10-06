import pygame
import moderngl
import sys


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

        self.ctx = moderngl.create_context()

        self.clock = pygame.time.Clock()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18))

        pygame.display.flip()

    def run(self):
        while True:
            self.check_events()
            self.render()
            self.clock.tick(60)


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
