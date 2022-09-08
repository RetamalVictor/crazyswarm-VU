import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import time

num_cf = 5
size_x = 6.5
size_y = 4.0
playback_speed = 0.5

logx = sio.loadmat('/home/tugay/icra_results/log_x.mat')
logy = sio.loadmat('/home/tugay/icra_results/log_y.mat')
logh = sio.loadmat('/home/tugay/icra_results/log_h.mat')
logx = logx['x']
logy = logy['y']
logh = logh['h']

harita = sio.loadmat('/home/tugay/Environments/circle_4x65.mat')
harita = harita['I']

plt.ion()
plt.show()
centroid_x = []
centroid_y = []
colors = ["red", "green", "blue", "yellow", "purple", "black"]

plt.imshow(harita, extent=[0, size_x, 0, size_y])

for i in range(logx.shape[0]):
    print(i)
    plt.imshow(harita, extent=[0, size_x, 0, size_y])
    plt.axis([0, size_x, 0, size_y])
    for j in range(6):
        plt.scatter(logx[i, j], logy[i, j], c=colors[j])
    centroid_x.append(np.mean(logx[i, :]))
    centroid_y.append(np.mean(logy[i, :]))
    #  plt.scatter(logx[0:i-1, :], logy[0:i-1, :], c='red', s=0.1)
    # plt.scatter(centroid_x, centroid_y, c='red', s=0.5)
    plt.quiver(logx[i, :], logy[i, :], np.cos(logh[i, :]), np.sin(logh[i, :]))

    plt.draw()
    plt.pause(0.000001)
    time.sleep(0.1/playback_speed)
    plt.clf()
