def is_all_strings(items):
  return all([isinstance(item, str) for item in items])


print(is_all_strings(['a', 'b']))