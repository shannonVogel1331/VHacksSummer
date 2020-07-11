import os

filename = 'image-asset_img_5eb0af2d092e0.jpg'
os.system('cp static/' + filename + ' /Users/ethannguyen/Desktop/College/SyBBURE/2020\ Summer/darknet/')
os.system('cd ..; cd darknet; ./darknet detect cfg/model.cfg model.weights ' + filename)
os.system('cp /Users/ethannguyen/Desktop/College/SyBBURE/2020\ Summer/darknet/predictions.jpg /Users/ethannguyen/Desktop/College/SyBBURE/2020\ Summer/VHacksSummer/static/' + filename)