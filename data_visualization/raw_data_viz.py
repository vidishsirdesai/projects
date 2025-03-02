import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import sys
import plotly.graph_objects as go

sns.set_theme(style = "darkgrid")
warnings.filterwarnings("ignore")

def create_visualization(subject):

    # read data
    df_lift = pd.read_csv(f"data/subject_{subject}/lift.csv")
    df_roll_left = pd.read_csv(f"data/subject_{subject}/roll_left.csv")
    df_roll_right = pd.read_csv(f"data/subject_{subject}/roll_right.csv")
    df_tilt_up = pd.read_csv(f"data/subject_{subject}/tilt_up.csv")
    df_tilt_down = pd.read_csv(f"data/subject_{subject}/tilt_down.csv")
    df_yaw_left = pd.read_csv(f"data/subject_{subject}/yaw_left.csv")
    df_yaw_right = pd.read_csv(f"data/subject_{subject}/yaw_right.csv")

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
    plt.text(0.05, 0.95, f'x: max = {df_roll_right["x"].max()}, min = {df_roll_right["x"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
    plt.text(0.05, 0.90, f'y: max = {df_roll_right["y"].max()}, min = {df_roll_right["y"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
    plt.text(0.05, 0.85, f'z: max = {df_roll_right["z"].max()}, min = {df_roll_right["z"].min()}', transform = plt.gca().transAxes, verticalalignment = "top")
    plt.legend()

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

    # save plot
    plt.savefig(f"artifacts/raw_sensor_data_subject_{subject}.png")

def create_visualization_3d(subject):

    # read data
    df_lift = pd.read_csv(f"data/subject_{subject}/lift.csv")
    df_roll_left = pd.read_csv(f"data/subject_{subject}/roll_left.csv")
    df_roll_right = pd.read_csv(f"data/subject_{subject}/roll_right.csv")
    df_tilt_up = pd.read_csv(f"data/subject_{subject}/tilt_up.csv")
    df_tilt_down = pd.read_csv(f"data/subject_{subject}/tilt_down.csv")
    df_yaw_left = pd.read_csv(f"data/subject_{subject}/yaw_left.csv")
    df_yaw_right = pd.read_csv(f"data/subject_{subject}/yaw_right.csv")

    # plot
    fig = go.Figure(
        data = [
            go.Scatter3d(x = df_lift["x"], y = df_lift["y"], z = df_lift["z"], mode = "markers", marker = dict(color = "red"), name = "Lift"),
            go.Scatter3d(x = df_roll_left["x"], y = df_roll_left["y"], z = df_roll_left["z"], mode = "markers", marker = dict(color = "yellow"), name = "Roll Left"),
            go.Scatter3d(x = df_roll_right["x"], y = df_roll_right["y"], z = df_roll_right["z"], mode = "markers", marker = dict(color = "green"), name = "Roll Right"),
            go.Scatter3d(x = df_tilt_up["x"], y = df_tilt_up["y"], z = df_tilt_up["z"], mode = "markers", marker = dict(color = "blue"), name = "Tilt Up"),
            go.Scatter3d(x = df_tilt_down["x"], y = df_tilt_down["y"], z = df_tilt_down["z"], mode = "markers", marker = dict(color = "orange"), name = "Tilt Down"),
            go.Scatter3d(x = df_yaw_left["x"], y = df_yaw_left["y"], z = df_yaw_left["z"], mode = "markers", marker = dict(color = "cyan"), name = "Yaw Left"),
            go.Scatter3d(x = df_yaw_right["x"], y = df_yaw_right["y"], z = df_yaw_right["z"], mode = "markers", marker = dict(color = "grey"), name = "Yaw Right")
        ]
    )
    fig.update_layout(title = f"Subject {subject}")
    fig.write_html(f"artifacts/interactive_3d_plot_subject_{subject}.html")

if __name__ == "__main__":
    subject = None
    for arg in sys.argv[1:]:
        if arg.startswith("subject="):
            try:
                subject = arg.split("=")[1]
            except (ValueError, IndexError):
                print("Error: Invalid subject format. Use subject=<integer>.")
                sys.exit(1)
            break

    if subject is None:
        print("Usage: python3 script.py subject=<subject_id>")
        sys.exit(1)
    
    create_visualization(subject)
    # create_visualization_3d(subject)
    