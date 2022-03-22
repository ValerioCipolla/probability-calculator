import random
import copy
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = self.create_contents(kwargs)

  def create_contents(self, obj):
    contents = []
    for k, v in obj.items():
      n = v
      while n > 0:
        contents.append(k)
        n -= 1
    return contents

  def draw(self, n):
    if n >= len(self.contents):
      return self.contents
    removed = []
    for x in range(n):
      random_ball = random.choice(self.contents)
      self.contents.remove(random_ball)
      removed.append(random_ball)
    return removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successfull_experiments = 0
  for x in range(num_experiments):
    is_successfull = True
    testing_hat = copy.deepcopy(hat)
    balls_drawn_list = testing_hat.draw(num_balls_drawn)
    balls_drawn_dict = dict()
    for ball in balls_drawn_list:
      balls_drawn_dict[ball] = balls_drawn_dict.get(ball, 0) + 1
    for color in expected_balls.keys():
      if color not in balls_drawn_dict:
        is_successfull = False
      elif balls_drawn_dict[color] < expected_balls[color]:
        is_successfull = False
    if is_successfull is True:
      successfull_experiments += 1
  return successfull_experiments / num_experiments