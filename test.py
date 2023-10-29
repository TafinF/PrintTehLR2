leftEnd = 0
rightEnd = 10
target = round((leftEnd + rightEnd)/2)

seq = []

def nextStep(ansver):
  global leftEnd
  global rightEnd
  global target
# while not (rightEnd - leftEnd)<=0:
#   print(f"диапазон: {leftEnd}-{rightEnd}   {rightEnd - leftEnd}")
#   print(f"is: {target}")
  # print(f"----")
  
#   ansver = input()
  if ansver == "t":
    leftEnd = target
  else:
    if target==rightEnd:
      target-=1
      return True
    rightEnd = target
  target = round((leftEnd + rightEnd)/2)
  
  if target == leftEnd:
    return True
    target +=1
#   if target == rightEnd:
#     break
#     target -=1
# print(f"tada-is: {target}!")
  return  (rightEnd - leftEnd)<=0


x = [["t","t","t","t"], #10

["t","t","t","f"], #9

["t","t","f"], #8

["t","f","t","t","t"], #8

["t","f","t","t","f"], #7

["t","f","t","f"], #6

["t","f","f","t"], #6

["f","t","t"], #4

["f","t","f","t","t"], #4

["f","t","f","t","f"], #3

["f","t","f","f"], #2

["f","f","t","t"], #2

["f","f","t","f"], #1

["f","f","f"]] #0

for s in x:
  leftEnd = 0
  rightEnd = 10
  target = round((leftEnd + rightEnd)/2)
  for i in s:
    print(f'{target} ', end='')
    if nextStep(i):
        print(f"tada-is: {target}!")