# Introduction


# Firmware

### Schematic diagram

![alt text](artifacts/motion_detection_schematic_diagram.png)

### Bread board layout

![alt text](artifacts/motion_detection_bb_layout.png)

### Terminal commands to capture the sensor readings
- `sudo lsof | grep <device_file_path>`
- `sudo kill -9 <PID>`
- `arduino-cli monitor --port <device_file_path> --config baudrate=9600 > motion_tracker_log.csv`
