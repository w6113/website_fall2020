from dateutil.parser import parse
from datetime import *

start = parse("01-19-2023")
end = parse("05-01-2023")

recess = [ ]

holidays = [
    parse("03-16-2023")
]

colors = [
  "#ffe4fc", "white"
]

j = 0
print "color,date,slug,title,readings,optional,assigned,due"
for i in xrange(150):
  d = start + timedelta(i)
  if d > end: break
  if recess and d >= recess[0] and d <= recess[1]: continue

  # 0 is monday
  if d.weekday() in [4]: 
    color = colors[(j%2)]
    day = d.strftime("%a %m-%d")
    title = ""
    if d in holidays: 
      title = "Holiday"

    print """%s,%s,%s,,,,,""" % (color, day, title)
    j += 1

