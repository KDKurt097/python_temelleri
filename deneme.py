import re

s = "A message from csev@umich.edu to cwen@iupi.edu"
lst = re.findall("\\S+@\\S+", s)
print(lst)