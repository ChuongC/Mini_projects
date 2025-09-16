
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# sort student list from low to high by age 
def sort(arr):
  item_count = len(arr) 
  # Now let's use bubble sort. Swap pairs iteratively as we loop through the
  # array from the beginning of the array to the second-to-last value
  for i in range(item_count - 1):
    # From arr[i + 1] to the end of the array
    for j in range(i+1, item_count):
      # If the first value is greater than the second value, swap them
      if (arr[i].age > arr[j].age):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
  return arr

# Read the data from the file and print out each line
def read(aFile):
  people = []
  # Defensive programming:
  count_line = aFile.readline().strip()
  print("First line of text file:", count_line)

  if count_line.isdigit():
    count = int(count_line)
  else:
    print("Error: first line of file is not a number")
    return people

  index = 0
  while (index < count):
    name = aFile.readline().strip()
    age = aFile.readline().strip()

    if not age.isdigit():
      print("Error")
      continue

    record = Student(name, int(age))
    people.append(record)
    print(f"Line read: Name={name}, Age={age}")
    index += 1

  return people

def print_array(arr):
  print("Printing array: number of elements: ", len(arr))
  for student in arr:
    print(f"Name: {student.name} - Age: {student.age}")

# Write data to a file then read it in and print it out
def main():
  try:
    with open("data.txt","r", encoding="utf-8") as aFile:
      people = read(aFile)
      if people:
        sorted_people = sort(people)
        print_array(sorted_people)

  except FileNotFoundError:
    print("Error: File 'data.txt' not found.")

main()
