import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import sys
import plotly.graph_objects as go

sns.set_theme(style = "darkgrid")
warnings.filterwarnings("ignore")

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
                print("Error: Invalid subject format. Use subject=<id>.")
                sys.exit(1)
            break

    if subject is None:
        print("Usage: python3 script.py subject=<subject_id>")
        sys.exit(1)
    
    create_visualization_3d(subject)
    