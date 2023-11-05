# Elevator Simulation

**Number of Floors:** First, specify the number of floors in the building.

**Elevator Capacity:** Determine the maximum number of people the elevator can hold at a time.

**Floor Queues:** For each floor in the building, a list of destinations for the people waiting on that floor is created. These destinations indicate the floors to which people on a particular floor want to travel. This list can be empty. The values of each floor can be selected manually or generated automatically.

If values are selected manually, the input for each floor should be a comma-separated list of valid destinations. For example, for Floor 0, you might enter "1,2,3" to indicate that people on Floor 0 want to go to Floors 1, 2, and 3. Make sure that the destinations provided for each floor are within the valid range (i.e., not equal to the current floor and not exceeding the total number of floors).

**Example of automatic behavior:**

```plaintext
Number of floors must be at least 2
Elevator capacity must be greater than 0
Enter the number of floors: 2
Enter the elevator capacity: 2
Do you want to manually enter floor queues? (yes/no): no

---------- Initial floor queues: ----------
```

*(User selects automatic and the script runs with random values)*

**Example of manual behavior:**
```plaintext
- Number of floors must be at least 2
- Elevator capacity must be greater than 0
- Enter the number of floors: 2
- Enter the elevator capacity: 2
- Do you want to manually enter floor queues? (yes/no): yes

*(User selects manual and then values need to be selected)*
- Enter a list of destinations for each floor:
- Floor numbers: [0, 1]
- Enter destinations for Floor 0 (comma-separated): 1,1,1,1,1
- Enter destinations for Floor 1 (comma-separated): [Enter] *(user can press Enter for an empty list)*
- Floor 1 is empty

---------- Initial floor queues: ----------
- Elevator: []
- Elevator moves upwards
- Floor 0 : [1, 1, 1, 1, 1]
- Floor 1 : []
```
*(The program continues)*
