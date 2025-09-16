import copy
import random

class Hat:
    def __init__(self, **kwargs):
        # contents is a list with each ball color repeated according to its count
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # If draw more balls than available → return all
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn
        
        # Randomly sample balls
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Copy hat so original isn’t changed
        hat_copy = copy.deepcopy(hat)

        # Draw balls
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count drawn balls
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        # Check success condition
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    # Probability = successful experiments / total experiments
    return success_count / num_experiments
