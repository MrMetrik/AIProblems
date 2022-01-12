
allLocations = ['A', 'B']

def nextLoc(current):
    if current == allLocations[0]:
        current = allLocations[1]
    else:
        current = allLocations[0]
    return current
    

def solution(state, location):
    
    cost = 0
    
    if state[location] == 1:
        # check if location is dirty
        print ("Room {} is dirty.".format(location))
        # then suck
        cost += 1
        print ("Room {} has been cleaned.".format(location))
    else:
        print ("Room {} is clean.".format(location))
    
    # Moving to next room
    location = nextLoc(location)
    cost += 1
    print ("Moving to room {}.".format(location))

    if state[location] == 1:
        print ("Room {} is dirty.".format(location))
        cost += 1
        print ("Room {} has been cleaned.".format(location))
    else:
        print ("Room {} is clean.".format(location))
    
    return cost

def main():
    # DEFAULT VALUES
    state = {'A' : 1, 'B': 1}
    location = 'B'

    state['A'] = int(input("Enter the state of room A(1 - dirty / 0 - clean): "))
    state['B'] = int(input("Enter the state of room B(1 - dirty / 0 - clean): "))

    while (1):
        location = input("Enter the location of the vacuum cleaner ('A' or 'B'): ")
        if location in allLocations:
            break
    
    print ("The cost incurred is: {}".format(solution(state, location)))

if __name__ == "__main__":
    main()    