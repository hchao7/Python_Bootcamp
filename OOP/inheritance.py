class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def __repr__(self):
    return f"{self.name} is a {self.species}"

  def make_sound(self, sound):
    print(f"this animal says {sound}")

class Cat(Animal):
  def __init__(self, name, breed, toy):
    # Replace animal().__init__ with super, which runs animal and passes in self as first argument
    super().__init__(name, species = "Cat") # Return animal, 
    self.breed = breed
    self.toy = toy

  def play(self):
    print(f"{self.name} plays with {self.toy}")

blue = Cat("Blue", "Scottish Fold", "String")
blue.play()