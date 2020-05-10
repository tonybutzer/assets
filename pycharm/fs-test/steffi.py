import fsspec

user='ubuntu'

passw='etrocks'

butz='10.12.69.21'
# print (help(fsspec.filesystem))
fs = fsspec.filesystem('sftp', host=butz, username=user, password=passw)
mylist = fs.ls('/opt/et_data')
#print(mylist)

#for thing in mylist:
 #   print(thing)

# THIS RUNS FOREVER WITH no output - so not that useful
mylist = fs.ls('/opt/et_data/v1DRB_outputs/model_outputs')
print(mylist)

for thing in mylist:
    print(thing)
    mod = fs.info(thing)
    print(mod)
