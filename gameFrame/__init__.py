import pygame
import sys
from .level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("混乱空间")
        self.clock = pygame.time.Clock()
        self.level = Level('assert/level/level1.json')

    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    # def control(self):
        # self.state['mouse'] = {
        #     'pos': pygame.mouse.get_pos(), 'pressed': pygame.mouse.get_pressed(5)}
        # self.state['keyboard'] = pygame.key.get_pressed()
        # for event in pygame.event.get():
        #     event_type = event.type
        #     if event.type in self.control_manager_dict:
        #         self.state['event'] = event
        #         for control_manager in self.control_manager_dict[event_type]:
        #             if control_manager.limit_check(self.state):
        #                 control_manager(self.state)
        #     elif event.type in self.level.script:
        #         self.state['event'] = event
        #         for control_manager in self.level.script[event_type]:
        #             if control_manager.limit_check(self.state):
        #                 control_manager(self.state)
        # self.state.pop('event', None)
        # for keyboard_str, control_manager_list in self.keyboard_control_manager_dict.items():
        #     if self.state['keyboard'][getattr(pygame.constants, keyboard_str)]:
        #         for control_manager in control_manager_list:
        #             if control_manager.limit_check(self.state):
        #                 control_manager(self.state)
        # for control_manager in self.control_manager_dict.get(None, []):
        #     if control_manager.limit_check(self.state):
        #         control_manager(self.state)
        # for control_manager in self.level.script.get(None, []):
        #     if control_manager.limit_check(self.state):
        #         control_manager(self.state)

    def run(self):
        while True:
            self.control()
            # self.level.update()

            bg_color = 100, 44, 22
            self.screen.fill(bg_color)
            # self.level.draw(self.screen, bg_color)
    
            pygame.display.flip()
            self.clock.tick(60)


