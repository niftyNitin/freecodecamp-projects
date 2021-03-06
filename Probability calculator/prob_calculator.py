import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for attr in kwargs.keys():
            for _ in range(kwargs[attr]):
                self.contents.append(attr)

    def draw(self, num):
        num = min(num, len(self.contents))
        balls = []
        for _ in range(num):
            index = random.randint(0, len(self.contents) - 1)
            balls.append(self.contents.pop(index))
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        exp = copy.deepcopy(hat)
        balls = exp.draw(num_balls_drawn)
        num_correct = 0
        for color in expected_balls.keys():
            if balls.count(color) >= expected_balls[color]:
                num_correct += 1
        if num_correct == len(expected_balls):
            success += 1
    probability = float(success) / num_experiments
    return probability
