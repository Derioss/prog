import json
import math


class Agent:
    def say_hello(self, first_name):
        return "Bien le bonjour " + first_name + "!"
    def __init__(self, position,**agent_attributes):
        self.position = position
        self.agreableness = agent_attributes['agreeableness']
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)


class Position:
    def __init__(self, longitude_degrees, latitude_degrees):
        self.latitude_degrees = latitude_degrees
        self.longitude_degrees = longitude_degrees
    @property
    def longitude(self):
        return self.longitude_degrees * math.pi / 180


class Zone:
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    WIDTH_DEGREES = 1  # degrees of longitude


    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = 0
def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(longitude, latitude)
        agent = Agent(position,**agent_attributes)

    print(Zone.MIN_LONGITUDE_DEGREES)

main()