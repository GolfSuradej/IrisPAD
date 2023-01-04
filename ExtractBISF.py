# author: suradej
# create: Jan 4, 2023
# Iris Spoofing Detection 

###.... previous code.... 
##. same as the "fiter.py"

import os


if __name__ == "__main__":
    
    path = "/home/suradej/OpenSourceIrisPAD-master/images"
    i = 0
    myBISF = np.zeros([30,32,1])
    
    for file in os.listdir(path):
        imgfile = os.path.join(path,file)
        src = cv2.imread(imgfile,flags=0)
        hist = np.asarray(generateHistogram(src,3,5))
        myBISF[i] = np.reshape(hist,[32,1])
        i = i+1

    np.save("myBISF.npy",myBISF)
