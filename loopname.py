import os

namelist = os.listdir('/Users/alexanderyoung/Desktop/SampleImages/pics')
dir = os.getcwd();

for i in namelist:
    current=dir+"/pics/"+i
    print current
