@@ -0,0 +1,6 @@
from homeworktime import homework , time , homeworktime
today = homework.today()
now = homeworktime.now()
print("todays date is", now)
print("\nCurrent date and time is", now)
print("\nDate components", today.year, today.month, today.day)