class World:
    def __init__(self, world_data):
        self.name = world_data['name']
        self.color = tuple(world_data['color'])
