noises = {
  "dog": "woof",
  "pig": "oink",
  "duck": "quack",
  "cat": "meow"
}

def speak(animal = "dog"):
  noise = noises.get(animal);
  if noise:
    return noise
  return "?"


print(speak('dog'))
print(speak('banana'))