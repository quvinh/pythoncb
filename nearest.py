"pip-updater.PackagesAndVersions": [
    {
        "packageName": "numpy"
    },
    {
        "packageName": "pandas",
        "version": "latest"
    },
    {
        "packageName": "setuptools",
        "version": "27.0.0"
    }
]
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
ketqua = np.random.randint(0,2,(25,1)).astype(np.float32)
red = trainData[ketqua.ravel()==1]
blue = trainData[ketqua.ravel()==0]
nemMember = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(red[:,0],red[:,1],100,'r','s')
plt.scatter(blue[:,0],blue[:,1],100,'b','^')
plt.scatter(newMember[:,0],newMember[:,1],100,'g','o')

knn = cv2.ml.KNearest_create()
knn.train(trainData,0,ketqua)
temp,ketqua,hangxom,khoangcach = knn.findNearest(newMember,3)

print("result: {}\n".format(ketqua))
print("hangxom: {}\n".format(hangxom))
print("khoangcach: {}\n".format(khoangcach))

plt.show()