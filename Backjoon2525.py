hours, minutes = map(int, input().split())
time = int(input())
resultHours = hours
resultMitutes = minutes + time

if resultMitutes >= 60:
  resultHours += int(resultMitutes / 60)
  resultMitutes = int(resultMitutes % 60)

if resultHours >= 24:
  resultHours = int(resultHours % 24)

print(resultHours, resultMitutes)