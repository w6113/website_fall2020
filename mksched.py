from dateutil.parser import parse
from datetime import *

start = parse("01-22-2019")
end = parse("05-06-2019")

recess = [
    parse("03-18-2019"),
    parse("03-22-2019")
]

colors = [
  "#fdf3fd", "white"
]

j = 0
print "color,date,slug,title,readings,optional,assigned,due"
for i in xrange(150):
  d = start + timedelta(i)
  if d > end: break
  if d >= recess[0] and d <= recess[1]: continue
  if d.weekday() in [1,3]: 
    print """%s,%s,,,,,,""" % (colors[(j%4)/2], d.strftime("%m/%d"))
    j += 1

