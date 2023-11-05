import random

def initialize_floor_queues_manually(num_floors):
    floor_queues = []
    print("Enter a list of destinations for each floor:")
    print("Floor numbers:", [i for i in range(num_floors)])
    for i in range(num_floors):
        valid_destinations = False
        while not valid_destinations:
            destinations = input(f"Enter destinations for Floor {i} (comma-separated): ")
            # Check if the input is empty (user pressed Enter)
            if not destinations:
                break
            destinations = destinations.strip().split(',')
            # Check if all characters are digits
            if all(char.isdigit() for char in ''.join(destinations)):
                destinations = [int(dest) for dest in destinations]
                # Check if any destination matches the current floor or is out of range
                if all(0 <= dest < num_floors and dest != i for dest in destinations):
                    valid_destinations = True
                else:
                    print("Invalid destinations. Destinations must be different from the current floor and within the valid range.")
            else:
                print("Invalid input. Please enter only numbers (no letters).")  
        # If the input is empty (user pressed Enter), add an empty list to floor_queues
        if not destinations:
            floor_queues.append([])
            print(f"Floor {i} is empty")
        else:
            floor_queues.append(destinations)    
    return floor_queues

def initialize_floor_queues(num_floors, capacity):    
    if capacity <= 0:
        raise ValueError("Elevator capacity must be greater than 0")
    if num_floors < 2:
        raise ValueError("Number of floors must be at least 2")
    floor_queues = [[] for i in range(num_floors)]  # create a list of queues for each floor i
    # random.seed(42)  # Use the seed() method to customize the start number of the random number generator.
    for i in range(num_floors):
        num_people = random.randint(0, 6)  # Maximum number of people on a floor
        possible_destinations = [x for x in range(num_floors) if x != i]
        # initialize destinations except the current floor i
        for j in range(num_people):
            destination = random.choice(possible_destinations)
            floor_queues[i].append(destination)  # create a list of queues for each floor i
    return floor_queues

def isListEmpty(inList):
    if isinstance(inList, list):
        return all( map(isListEmpty, inList) )
    return False

def change_dir(current_floor, direction):
  if current_floor == len(floor_queues) or current_floor == 0:
    direction = -direction

def check(i, direction, floor):
  if direction > 0:
    return i > floor
  else:
    return i < floor
  
def calculate_direction(floor, total_floors, direction):
  # print("floor",floor,"len floor_queues",total_floors)
  if floor+1 == total_floors and direction==1:
    return -1
  if floor == 0 and direction==-1:
    return +1
  return direction

# Define the number of floors and capacity
print('''Number of floors must be at least 2\nElevator capacity must be greater than 0\n''')
num_floors = int(input("Enter the number of floors: "))
capacity = int(input("Enter the elevator capacity: "))
manual_entry = input("Do you want to manually enter floor queues? (yes/no): ").lower()
        
if manual_entry == "yes":
    floor_queues = initialize_floor_queues_manually(num_floors)
else:
    floor_queues = initialize_floor_queues(num_floors, capacity)
        
move = True
floor = 0
elevator = []
direction = 1
stops=[]
print("\n---------- Initial floor queues: ----------")
while(move):
  print("Elevator:", elevator)
  print(f"Elevator moves {'upwards' if direction == 1 else 'downwards'}")
  for i in range(0,len(floor_queues)):
    print("Floor",i,":",floor_queues[i])
  
  print(f"\n---------- Current Floor: {floor} ----------")
  stops.append(floor)
  # throw people
  elevator = [person for person in elevator if person != floor]
  
  # take people
  to_take = capacity - len(elevator)
  print("People to take:",to_take)
  # if elevator is going up take all you can

  direction = calculate_direction(floor,len(floor_queues), direction)
  
  for person in floor_queues[floor][:]:
    if to_take > 0 and check(person, direction, floor):
      elevator.append(person)
      floor_queues[floor].remove(person)
      to_take -= 1

  # if all floor empty
  move = not(isListEmpty(floor_queues)) or elevator
  
  # if moves change direction
  if(move):
    floor = floor + direction
  print("Direction:",direction)
  
  # if does not move go to base
  if not move:
    floor = 0
print("\nStops Order:",stops)
input("Press Enter to exit...")