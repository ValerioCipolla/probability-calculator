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
  for x in range(num_experiments):
    is_successfull = True
    testing_hat = copy.deepcopy(hat)
    balls_drawn_list = testing_hat.draw(num_balls_drawn)
    balls_drawn_dict = dict()
    for ball in balls_drawn_list:
      if ball in balls_drawn_dict:
        continue
      else:
        balls_drawn_dict[ball] = len([x for x in balls_drawn_list if x == ball])
    print(balls_drawn_list)
    print(balls_drawn_dict)
    for color, value in expected_balls.items():
      print(color, value)



hat = Hat(black=6, red=4, green=3)

experiment(hat=hat,expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=10 )