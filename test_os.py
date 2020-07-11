import os

filename = 'baby-yoda-print.jpg'
os.system('cp upload/' + filename + ' /Users/ethannguyen/Desktop/College/SyBBURE/2020\ Summer/darknet/')
os.system('cd ..; cd darknet; ./darknet detect cfg/model.cfg model.weights baby-yoda-print.jpg')
os.system('cp /Users/ethannguyen/Desktop/College/SyBBURE/2020\ Summer/darknet/predictions.jpg /Users/ethannguyen/Desktop/College/SyBBURE/2020\ Summer/VHacksSummer/upload')