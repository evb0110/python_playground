input = """ebacd
fghij
olmkn
trpqs
xywuv""".split('\n')

def gridChallenge(grid):
  sortedGrid = []
  for line in grid:
    lst = list(line)
    sortedLine = ''.join(sorted(lst))
    sortedGrid.append(sortedLine)
  for i in range(len(sortedGrid[0])):
    column = [line[i] for line in sortedGrid]
    for j in range(len(column) - 1):
      if column[j] > column[j + 1]:
        return 'NO'
  return 'YES'


print(gridChallenge(input))