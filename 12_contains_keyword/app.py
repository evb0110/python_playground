from keyword import iskeyword

def contains_keyword(*strings):
  return any([iskeyword(string) for string in strings])

print(contains_keyword('hi', 'lol'))