import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

sns.set_theme(style = "darkgrid")
warnings.filterwarnings("ignore")

# lift
df_lift = pd.read_csv("data/subject_1/lift.csv")

# roll_left
df_roll_left = pd.read_csv("data/subject_1/roll_left.csv")

# roll_right
df_roll_right = pd.read_csv("data/subject_1/roll_right.csv")

# tilt_up
df_tilt_up = pd.read_csv("data/subject_1/tilt_up.csv")

# tilt_down
df_tilt_down = pd.read_csv("data/subject_1/tilt_down.csv")

# yaw_left
df_yaw_left = pd.read_csv("data/subject_1/yaw_left.csv")

# yaw_right
df_yaw_right = pd.read_csv("data/subject_1/yaw_right.csv")

# plot
plt.figure(figsize = (20, 35))

plt.subplot(7, 1, 1)
plt.title("Action: Lift")
df_lift["x"].plot()
df_lift["y"].plot()
df_lift["z"].plot()
plt.text(0.05, 0.95, f'x: max = {df_lift["x"].max()}, min = {df_lift["x"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.90, f'y: max = {df_lift["y"].max()}, min = {df_lift["y"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.85, f'z: max = {df_lift["z"].max()}, min = {df_lift["z"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.legend()

plt.subplot(7, 1, 2)
plt.title("Action: Roll Left")
df_roll_left["x"].plot()
df_roll_left["y"].plot()
df_roll_left["z"].plot()
plt.text(0.05, 0.95, f'x: max = {df_roll_left["x"].max()}, min = {df_roll_left["x"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.90, f'y: max = {df_roll_left["y"].max()}, min = {df_roll_left["y"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.85, f'z: max = {df_roll_left["z"].max()}, min = {df_roll_left["z"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.legend()

plt.subplot(7, 1, 3)
plt.title("Action: Roll Right")
df_roll_right["x"].plot()
df_roll_right["y"].plot()
df_roll_right["z"].plot()
plt.legend()
plt.text(0.05, 0.95, f'x: max = {df_roll_right["x"].max()}, min = {df_roll_right["x"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.90, f'y: max = {df_roll_right["y"].max()}, min = {df_roll_right["y"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.85, f'z: max = {df_roll_right["z"].max()}, min = {df_roll_right["z"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")

plt.subplot(7, 1, 4)
plt.title("Action: Tilt Up")
df_tilt_up["x"].plot()
df_tilt_up["y"].plot()
df_tilt_up["z"].plot()
plt.text(0.05, 0.95, f'x: max = {df_tilt_up["x"].max()}, min = {df_tilt_up["x"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.90, f'y: max = {df_tilt_up["y"].max()}, min = {df_tilt_up["y"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.85, f'z: max = {df_tilt_up["z"].max()}, min = {df_tilt_up["z"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.legend()

plt.subplot(7, 1, 5)
plt.title("Action: Tilt Down")
df_tilt_down["x"].plot()
df_tilt_down["y"].plot()
df_tilt_down["z"].plot()
plt.text(0.05, 0.95, f'x: max = {df_tilt_down["x"].max()}, min = {df_tilt_down["x"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.90, f'y: max = {df_tilt_down["y"].max()}, min = {df_tilt_down["y"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.85, f'z: max = {df_tilt_down["z"].max()}, min = {df_tilt_down["z"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.legend()

plt.subplot(7, 1, 6)
plt.title("Action: Yaw Left")
df_yaw_left["x"].plot()
df_yaw_left["y"].plot()
df_yaw_left["z"].plot()
plt.text(0.05, 0.95, f'x: max = {df_yaw_left["x"].max()}, min = {df_yaw_left["x"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.90, f'y: max = {df_yaw_left["y"].max()}, min = {df_yaw_left["y"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.85, f'z: max = {df_yaw_left["z"].max()}, min = {df_yaw_left["z"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.legend()

plt.subplot(7, 1, 7)
plt.title("Action: Yaw Right")
df_yaw_right["x"].plot()
df_yaw_right["y"].plot()
df_yaw_right["z"].plot()
plt.text(0.05, 0.95, f'x: max = {df_yaw_right["x"].max()}, min = {df_yaw_right["x"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.90, f'y: max = {df_yaw_right["y"].max()}, min = {df_yaw_right["y"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.85, f'z: max = {df_yaw_right["z"].max()}, min = {df_yaw_right["z"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.legend()

plt.savefig("artifacts/sensor_data_visualization_subject_1.png")
