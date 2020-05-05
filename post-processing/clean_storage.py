
dir = '/home/ubuntu/ksc_test/beam/output/sf-light'
import os

for parent, dirnames, filenames in os.walk(dir):
  for fn in filenames:
    if fn.lower().endswith('.gz'):
      os.remove(os.path.join(parent,fn))










