from dateutil.parser import parse
from datetime import *

start = parse("09-09-2021")
end = parse("12-13-2021")

recess = [ ]

holidays = [
    parse("11-01-2021"),
    parse("11-02-2021"),
    parse("11-24-2021"),
    parse("11-25-2021"),
    parse("11-26-2021")
]

colors = [
  "#fdffe4", "white"
]

j = 0
print "color,date,slug,title,readings,optional,assigned,due"
for i in xrange(150):
  d = start + timedelta(i)
  if d > end: break
  if recess and d >= recess[0] and d <= recess[1]: continue

  # 0 is monday
  if d.weekday() in [0,2]: 
    color = colors[(j%4)/2]
    day = d.strftime("%a %m-%d")
    title = ""
    if d in holidays: 
      title = "Holiday"

    print """%s,%s,%s,,,,,""" % (color, day, title)
    j += 1

