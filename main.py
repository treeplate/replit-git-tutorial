class Dog:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def speak(self):
    print("Bark Bark")
Dog("Dog", "3yrs").speak()