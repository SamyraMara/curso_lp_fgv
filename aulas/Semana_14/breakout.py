import pygame
pygame.init()

import json

class GameManager:
    def __init__(self, config) -> None:
        self.is_running = False
        self.clock = None

    def run(self):
        self.is_running = True
        self.clock = pygame.time.Clock()
        while self.is_running:
            self.events()
            self.draw()
            self.update()
            self.clock.tick()


    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.is_running = False

    def draw(self):
        self.screen.fill((0,0,0))
        pygame.display.flip()

    def update(self):
        pass

    if __name__ == "__main__":
        config_filepath = "/home/samyra/Documentos/curso-lp-fgv/aulas/Semana_14/config/config.json"
        config = json.loads(open(config_filepath).read())
            