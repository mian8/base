import subprocess

print('nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])
print('人生不满百，常怀千岁忧%s'%r)