from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(size):
    value = i
    for j in range(i+1,size):
      if array[j] < array[value]:
        value = j
    array[value],array[i]=array[i],array[value]
  return array

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
