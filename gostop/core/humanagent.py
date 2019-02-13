from builtins import input

from .agent import Agent


class HumanAgent(Agent):
    """Agent that prompts the user to select an action at each decision point"""

    def get_action(self, state, possible_actions):
        while True:
            response = input("== Choose action for {0} \n{1}? ".format(
                self.name,
                '/\n'.join(u'({0}){1}'.format(index, action) for index, action in enumerate(possible_actions))
            ))
            if response in (str(n) for n in range(0, len(possible_actions))):
                return possible_actions[int(response)]
