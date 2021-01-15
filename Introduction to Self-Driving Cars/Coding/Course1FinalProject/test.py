import pandas as pd
import os
import csv
import matplotlib.pyplot as plt
import numpy as np


os.getcwd()

df = pd.read_csv("./Course1FinalProject/racetrack_waypoints.txt",names=["x","y","speed"])
plt.figure()
plt.plot(df[df.columns[0]], df[df.columns[1]], "-*")
plt.show()


with open("./Course1FinalProject/racetrack_waypoints.txt") as f:
    cnt = csv.reader(f)
    # for line in cnt:
    #     print(line)
    waypoints = list(cnt)



waypoints_file =  "./Course1FinalProject/racetrack_waypoints.txt"
with open(waypoints_file) as waypoints_file_handle:
    waypoints = list(csv.reader(waypoints_file_handle, delimiter=',', quoting=csv.QUOTE_NONNUMERIC))
waypoints_np = np.array(waypoints)

dist_vec = waypoints_np[1:,:2]-waypoints_np[:-1,:2]
dist = np.linalg.norm(dist_vec, axis=-1)
