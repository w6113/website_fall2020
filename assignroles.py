import random
x = ['Ziao', 'Yiliang', 'Dean', 'Siyang', 'Xinyue', 'Yiru', 'Jennifer', 'Amita', 'Alan', 'Xiao', 'Haneen', 'Maryam', 'Andrew', 'Shikun']
random.shuffle(x)
for i in xrange(len(x)/2):
  print ", ".join([x[i*2], x[i*2+1]])