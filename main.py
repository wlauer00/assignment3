import sys

def main():
  with open(sys.argv[1], 'r') as f:
    contents = f.readlines()
  parsePlans(contents)

def parsePlans(plans):
  complex_plans = []
  floors = {}
  reached_complex = 0
  for line in plans:
    # print(floors)
    if reached_complex == 0:
      plan = line.split(' ')
      if plan[0] == 'floor':
        # append to the floor dict the name of the floor along with the returned square footage from parseFloor
        floors = parseFloor(plan, floors)
      elif plan[0] == 'complex\n':
        reached_complex = 1
    elif reached_complex == 1:
      complex_plans.append(line)

  parseComplex(complex_plans, floors)

# Get and return the square footage of the floor and name
def parseFloor(plan, floors):
  name = plan[1]
  roomText=''
  for i in range(5, len(plan) - 1):
    roomText += plan[i]
  rooms = roomText.split(',')
  area = parseRoom(rooms)
  floors[name] = area
  return floors

# Get the floor names, then check the dictionary for them and, assuming they exist, add square footage and print the total square footage for each building
def parseComplex(plan, floors_dict):
  list_of_sq_ft = []
  for line in plan:
    line = line.split(' ')
    floor_names = []
    building_name = line[3]
    if line[5]=='floor':
      floor_names.append(line[7])
    elif line[5]=='floors':
      rest_of_names = line[6:]
      for name in rest_of_names:
        if name=='{' or name=='}' or name==',' or name=='}\n':
          continue
        floor_names.append(name)
    else:
      print('Incorrect Syntax In Defining Buildings!')
    total_sq_foot = 0
    for floor_name in floor_names:
      current_sq_ft = floors_dict[floor_name]
      total_sq_foot += current_sq_ft
    print("Area for Building " + str(building_name) + ": " + str(total_sq_foot) + " square feet")
    list_of_sq_ft.append(total_sq_foot) 
  total_usable = 0
  for sq_ft in list_of_sq_ft:
    total_usable += sq_ft
  print("The total usable area is " + str(total_usable) + " square feet.")

def parseRoom(rooms):
  roomArea = 0
  for room in rooms:
    sides = room.split('by')
    roomArea += (int(sides[0]) * int(sides[1]))
  return roomArea

if __name__=='__main__':
  main()