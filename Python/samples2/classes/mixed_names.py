class MixedNames:
  data = "spam"
  def __init__(self, value):
    self.data = value
  def display(self):
    print((self.data, MixedNames.data))

x = MixedNames(1)
y = MixedNames(2)

x.display()
y.display()
