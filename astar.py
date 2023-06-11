
full_world = [
    ['.', '.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.'],
    ['.', '.', '.', '.', 'x', 'x', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'x', 'x', 'x', '#', '#', '#', 'x', 'x', '#', '#'],
    ['.', '.', '.', '.', '#', 'x', 'x', 'x', '*', '*', '*', '*', '~', '~', '*', '*', '*', '*', '*', '.', '.', '#', '#', 'x', 'x', '#', '.'],
    ['.', '.', '.', '#', '#', 'x', 'x', '*', '*', '.', '.', '~', '~', '~', '~', '*', '*', '*', '.', '.', '.', '#', 'x', 'x', 'x', '#', '.'],
    ['.', '#', '#', '#', 'x', 'x', '#', '#', '.', '.', '.', '.', '~', '~', '~', '~', '~', '.', '.', '.', '.', '.', '#', 'x', '#', '.', '.'],
    ['.', '#', '#', 'x', 'x', '#', '#', '.', '.', '.', '.', '#', 'x', 'x', 'x', '~', '~', '~', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '.', '.', '.', '#', 'x', 'x', 'x', '~', '~', '~', '.', '.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#', 'x', 'x', '.', '~', '~', '.', '.', '#', '#', '#', '.', '.', '.'],
    ['.', '.', '.', '~', '~', '~', '.', '.', '#', '#', '#', 'x', 'x', 'x', 'x', '.', '.', '.', '~', '.', '#', '#', '#', '.', '.', '.', '.'],
    ['.', '.', '~', '~', '~', '~', '~', '.', '#', '#', 'x', 'x', 'x', '#', '.', '.', '.', '.', '.', '#', 'x', 'x', 'x', '#', '.', '.', '.'],
    ['.', '~', '~', '~', '~', '~', '.', '.', '#', 'x', 'x', '#', '.', '.', '.', '.', '~', '~', '.', '.', '#', 'x', 'x', '#', '.', '.', '.'],
    ['~', '~', '~', '~', '~', '.', '.', '#', '#', 'x', 'x', '#', '.', '~', '~', '~', '~', '.', '.', '.', '#', 'x', '#', '.', '.', '.', '.'],
    ['.', '~', '~', '~', '~', '.', '.', '#', '*', '*', '#', '.', '.', '.', '.', '~', '~', '~', '~', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'x', '.', '.', '*', '*', '*', '*', '#', '#', '#', '#', '.', '~', '~', '~', '.', '.', '#', 'x', '#', '.', '.', '.'],
    ['.', '.', '.', 'x', 'x', 'x', '*', '*', '*', '*', '*', '*', 'x', 'x', 'x', '#', '#', '.', '~', '.', '#', 'x', 'x', '#', '.', '.', '.'],
    ['.', '.', 'x', 'x', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'x', 'x', 'x', '.', '.', 'x', 'x', 'x', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'x', 'x', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'x', 'x', 'x', 'x', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'x', 'x', 'x', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'x', 'x', 'x', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '~', '~', '~', '~'],
    ['.', '.', '#', '#', '#', '#', 'x', 'x', '*', '*', '*', '*', '*', '.', 'x', '.', '.', '.', '.', '.', '~', '~', '~', '~', '~', '~', '~'],
    ['.', '.', '.', '.', '#', '#', '#', 'x', 'x', 'x', '*', '*', 'x', 'x', '.', '.', '.', '.', '.', '.', '~', '~', '~', '~', '~', '~', '~'],
    ['.', '.', '.', '.', '.', '.', '#', '#', '#', 'x', 'x', 'x', 'x', '.', '.', '.', '.', '#', '#', '.', '.', '~', '~', '~', '~', '~', '~'],
    ['.', '#', '#', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '.', '.', '#', '#', 'x', 'x', '#', '#', '.', '~', '~', '~', '~', '~'],
    ['#', 'x', '#', '#', '#', '#', '.', '.', '.', '.', '.', 'x', 'x', 'x', '#', '#', 'x', 'x', '.', 'x', 'x', '#', '#', '~', '~', '~', '~'],
    ['#', 'x', 'x', 'x', '#', '.', '.', '.', '.', '.', '#', '#', 'x', 'x', 'x', 'x', '#', '#', '#', '#', 'x', 'x', 'x', '~', '~', '~', '~'],
    ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.']]

test_world = [['.', '*', '*', '*', '*', '*', '*'],
              ['.', '*', '*', '*', '*', '*', '*'],
              ['.', '*', '*', '*', '*', '*', '*'],
              ['.', '.', '.', '.', '.', '.', '.'],
              ['*', '*', '*', '*', '*', '*', '.'],
              ['*', '*', '*', '*', '*', '*', '.'],
              ['*', '*', '*', '*', '*', '*', '.']]

test_solution = [(0,1), (0,1), (0,1), (1,0), (1,0), (1,0), (1,0), (1,0), (1,0), (0,1), (0,1), (0,1)]
test_solution_diagnonal = [(0,1), (0,1), (1,1), (1,0), (1,0), (1,0), (1,0), (1,1), (0,1), (0,1)]

def solution_to_path(solution):
    last = (0,0)
    for move in solution:
        move = (move[0] + last[0], move[1] + last[1])
        last = move
    return solution      

test_solution = solution_to_path(test_solution)
test_solution_diagnonal = solution_to_path(test_solution_diagnonal)

# token   terrain    cost
# .       plains     1
# *       forest     3
# #       hills      5
# ~       swamp      7
# x       mountains  impassible

cardinal_moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
diagonal_moves = [(1, -1), (1, 1), (-1, 1), (-1, -1)]

moves = cardinal_moves + diagonal_moves
costs = {'.': 1, '*': 3, '#': 5, '~': 7, 'x': -1}

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def neighbors(world, current, moves):
    neighbors = []
    for move in moves:
        neighbor = (current[0] + move[0], current[1] + move[1])
        if neighbor[0] < 0 or neighbor[0] >= len(world[0]) or neighbor[1] < 0 or neighbor[1] >= len(world):
            continue
        neighbors.append(neighbor)
    return neighbors

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

class Set:
    def __init__(self, elements):
        self.elements = elements

    def add(self, element):
        self.elements.append(element)

    def remove(self, element):
        self.elements.remove(element)

    def pop(self):
        element = self.elements[0]
        self.elements = self.elements[1:]
        return element

    def __len__(self):
        return len(self.elements)

    def __contains__(self, element):
        return element in self.elements

def a_star_search(world, start, goal, costs, moves, heuristic):
    openset = Set([start])

    camfrom = {}

    g_score = {start: 0}

    f_score = {start: heuristic(start, goal)}

    while len(openset) > 0:
        current = openset.pop()
       
        if current == goal:
            return reconstruct_path(camfrom, current)

        #openset.remove(current)
        for neighbor in neighbors(world, current, moves):
            g_current = g_score[current]
            g_neighbor = costs[world[neighbor[1]][neighbor[0]]]
            if g_neighbor < 0:
                continue
            tentative_g_score = g_current + g_neighbor
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                camfrom[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in openset:
                    openset.add(neighbor)
    return None    

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        
colors = {'.': bcolors.OKGREEN, '*': bcolors.OKCYAN, '#': bcolors.WARNING, '~': bcolors.OKBLUE, 'x': bcolors.FAIL}

def print_pretty_world(world, current):
    for y in range(len(world)):
        for x in range(len(world[0])):
            if (x, y) == current:
                print(bcolors.HEADER +'['+ 'S' +']'+ bcolors.ENDC, end='')
            else:
                print(colors[world[y][x]] +'['+ world[y][x] +']'+ bcolors.ENDC, end='')
        print()

def print_move(world, current, neighbors):
    for y in range(len(world)):
        for x in range(len(world[0])):
            if (x, y) == current:
                print(bcolors.HEADER +'['+ 'S' +']'+ bcolors.ENDC, end='')
            elif (x, y) in neighbors:
                print(bcolors.BOLD +'['+ 'X' +']'+ bcolors.ENDC, end='')
            else:
                print(colors[world[y][x]] +'['+ world[y][x] +']'+ bcolors.ENDC, end='')
        print()

def print_presentable_world(world, current):
    for y in range(len(world)):
        for x in range(len(world[0])):
            if (x, y) == current:
                print('['+'S'+']', end='')
            else:
                print('['+world[y][x]+']', end='')
        print()

def pretty_print_solution( world, path, start):
        
    for y in range(len(world)):
        for x in range(len(world[0])):
            if (x, y) == start:
                print(bcolors.HEADER +'['+ 'S' +']'+ bcolors.ENDC, end='')
            elif (x, y) in path:
                print(bcolors.BOLD +'['+ 'X' +']'+ bcolors.ENDC, end='')
            else:
                print(colors[world[y][x]] +'['+ world[y][x] +']'+ bcolors.ENDC, end='')
        print()

    print('Path length: ' + str(len(path)))
    print('Path: ' + str(path))

    return None

test_path = a_star_search(test_world, (0, 0), (6, 6), costs, cardinal_moves, heuristic)
#print(test_path)

pretty_print_solution( test_world, test_path, (0, 0))

test_path = a_star_search(test_world, (0, 0), (6, 6), costs, moves, heuristic)
#print(test_path)

pretty_print_solution( test_world, test_path, (0, 0))

full_path = a_star_search( full_world, (0, 0), (26, 26), costs, cardinal_moves, heuristic)
#print(full_path)

pretty_print_solution( full_world, full_path, (0, 0))

full_path = a_star_search( full_world, (0, 0), (26, 26), costs, moves, heuristic)
#print(full_path)

pretty_print_solution( full_world, full_path, (0, 0))
