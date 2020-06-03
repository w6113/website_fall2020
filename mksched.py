from dateutil.parser import parse
from datetime import *

start = parse("09-08-2020")
end = parse("12-15-2020")

recess = [ ]

holidays = [
    parse("11-03-2020"),
    parse("11-26-2020")
]

colors = [
  "#fdf3fd", "white"
]

j = 0
print "color,date,slug,title,readings,optional,assigned,due"
for i in xrange(150):
  d = start + timedelta(i)
  if d > end: break
  if recess and d >= recess[0] and d <= recess[1]: continue
  #if d in holidays: continue
  if d.weekday() in [1,3]: 
    print """%s,%s,,,,,,""" % (colors[(j%4)/2], d.strftime("%a %m-%d"))
    j += 1

