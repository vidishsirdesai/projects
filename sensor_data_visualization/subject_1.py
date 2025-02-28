import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

sns.set_theme(style = "darkgrid")
warnings.filterwarnings("ignore")

# lift
df_lift = pd.read_csv("data/subject_1/lift.csv")
print("Action: Lift")
print(df_lift["x"].max(), df_lift["x"].min())
print(df_lift["y"].max(), df_lift["y"].min())
print(df_lift["z"].max(), df_lift["z"].min())

# roll_left
df_roll_left = pd.read_csv("data/subject_1/roll_left.csv")

print("Action: Roll Left")
print(df_roll_left["x"].max(), df_roll_left["x"].min())
print(df_roll_left["y"].max(), df_roll_left["y"].min())
print(df_roll_left["z"].max(), df_roll_left["z"].min())

# roll_right
df_roll_right = pd.read_csv("data/subject_1/roll_right.csv")

print("Action: Roll Right")
print(df_roll_right["x"].max(), df_roll_right["x"].min())
print(df_roll_right["y"].max(), df_roll_right["y"].min())
print(df_roll_right["z"].max(), df_roll_right["z"].min())

# plot
plt.figure(figsize = (20, 15))

plt.subplot(3, 1, 1)
plt.title("Action: Lift")
df_lift["x"].plot()
df_lift["y"].plot()
df_lift["z"].plot()
plt.text(0.05, 0.95, f'x: max = {df_lift["x"].max()}, min = {df_lift["x"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.90, f'y: max = {df_lift["y"].max()}, min = {df_lift["y"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.85, f'z: max = {df_lift["z"].max()}, min = {df_lift["z"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.legend()

plt.subplot(3, 1, 2)
plt.title("Action: Roll Left")
df_roll_left["x"].plot()
df_roll_left["y"].plot()
df_roll_left["z"].plot()
plt.text(0.05, 0.95, f'x: max = {df_roll_left["x"].max()}, min = {df_roll_left["x"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.90, f'y: max = {df_roll_left["y"].max()}, min = {df_roll_left["y"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.85, f'z: max = {df_roll_left["z"].max()}, min = {df_roll_left["z"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.legend()

plt.subplot(3, 1, 3)
plt.title("Action: Roll Right")
df_roll_right["x"].plot()
df_roll_right["y"].plot()
df_roll_right["z"].plot()
plt.legend()
plt.text(0.05, 0.95, f'x: max = {df_roll_right["x"].max()}, min = {df_roll_right["x"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.90, f'y: max = {df_roll_right["y"].max()}, min = {df_roll_right["y"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
plt.text(0.05, 0.85, f'z: max = {df_roll_right["z"].max()}, min = {df_roll_right["z"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")

plt.savefig("artifacts/sensor_data_visualization_subject_1.png")
