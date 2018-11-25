import json

class Agent:
    def say_hello(self, first_name):
        return "Bien le bonjour " + first_name + "!"
    def __init__(self, **agent_attributes):
        self.agreableness = agent_attributes['agreeableness']
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)


def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        agent = Agent(**agent_attributes)
        print(agent.agreableness)

main()