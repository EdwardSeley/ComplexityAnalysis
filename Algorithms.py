def merge_sort(sequence, first, last):
  if first < last:
      middle = int(0.5 * (first + last))
      merge_sort(sequence, first, middle)
      merge_sort(sequence, middle + 1, last)
      merge(sequence, first, middle, last)

def merge(sequence, first, middle, last):
  subOneLength = middle - first + 1
  subTwoLength = last - middle
  leftSequence = [None] * (subOneLength + 1)
  rightSequence = [None] * (subTwoLength + 1)
  for x in range(subOneLength):
      leftSequence[x] = sequence[first + x]
  for y in range(subTwoLength):
      rightSequence[y] = sequence[middle + 1 + y]

  leftSequence[subOneLength] = 1000
  rightSequence[subTwoLength] = 1000

  x = 0
  y = 0
  i = 0

  for i in range(first, last):
      if leftSequence[x] < rightSequence[y]:
          sequence[i] = leftSequence[x]
          x = x + 1
      else:
          sequence[i] = rightSequence[y]
          y = y + 1
  
  i = i + 1
  # Copy the remaining elements of L[], if there
  # are any
  while x < subOneLength:
      sequence[i] = leftSequence[x]
      x += 1
      i += 1

  # Copy the remaining elements of R[], if there
  # are any
  while y < subTwoLength:
      sequence[i] = rightSequence[y]
      y += 1
      i += 1

random_list = [3, 7, 1, 9, 3, 6, 7, 4, 12, 5, 8]
merge_sort(random_list, 0, len(random_list) - 1)





