#when user clicks done: for days selected off: testDict[day] = 0 --> change values in dictionary for selected days to 0    lettersList = checkWeek(list(testDict.values())) --> runs func with list of days on and off and assigns to variable to be refrenced later
#using month of march as a sample
#might be able to find online dictionary with all days of every year or smt
datesDict = {3/1: 1, 3/2: 1, 3/3: 1, 3/4: 1, 3/5: 1, 3/6: 1, 3/7: 1, 3/8: 1, 3/9: 1, 3/10: 1, 3/11: 1, 3/12: 1, 3/13: 1, 3/14: 1, 3/15: 1, 3/16: 1, 3/17: 1, 3/18: 1, 3/19: 1, 3/20: 1, 3/21: 1, 3/22: 1, 3/23: 1, 3/24: 1, 3/25: 1, 3/26: 1, 3/27: 1, 3/28: 1, 3/29: 1}

#ask user to input how many letter days there are
#days = user input
days = ["A", "B", "C", "D"]

def checkWeek(week):
  current = []
  count = 0
  #while new list is less than old list
  while len(current) != len(week):
    for i in week:
      if i == 0:
        current.append("Weekend")
      elif i == 1:
        if count < 3:
          current.append(days[count])
          count += 1
        elif count == 3:
          current.append(days[count])
          count = 0
  return current

#returns whole calendar year
checkWeek([1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0])