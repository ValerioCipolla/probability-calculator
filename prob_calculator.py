import random
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
    contents_copy = self.contents.copy()
    for x in range(n):
      random_ball = random.choice(contents_copy)
      contents_copy.remove(random_ball)
      removed.append(random_ball)
    return removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  return 1

h = Hat(red=2, blue=1)

print(h.draw(2))