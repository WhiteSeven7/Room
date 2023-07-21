import json
from .world import World
from .room import Room

class Level:
    def __init__(self, level_data_path):
        with open(level_data_path, mode='r',encoding='utf-8') as f:
            level_data = json.load(f)
        worlds = [World(world_data) for world_data in level_data['worlds']]
        rooms = [Room(room_data, worlds) for room_data in level_data['rooms']]
        self.worlds = worlds
        self.rooms = rooms
