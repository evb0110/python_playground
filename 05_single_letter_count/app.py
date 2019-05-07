def single_letter_count(w, l):
    total = 0
    for letter in w:
        if letter == l:
            total += 1
    return total

print(single_letter_count('piepya', 'e'))