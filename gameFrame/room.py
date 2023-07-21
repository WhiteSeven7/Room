import pygame

class Room:
    def __init__(self, room_data, worlds):
        index = room_data['belong_world_index']
        self.worlds = worlds
        self.belong_world_index = index
        self.belong_world = worlds[index]

        self.image = pygame.image.load('assert/image/room.png')
