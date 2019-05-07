def multiple_letter_count(word):
  return { l: word.count(l) for l in word }



def multiple_letter_count1(word):
  return {ll: word.count(ll) for ll in { l for l in word }}

string = 's' * 300000

print(multiple_letter_count(string))