# Introduction


# Data collection Using Arduino UNO R3 and ADXL345

### Schematic diagram

![motion_detection_schematic_diagram](artifacts/motion_detection_schematic_diagram.png)

### Firmware code

Link: dynamic_motion_classifier/firmware/firmware.ino

### Terminal commands to capture the sensor readings
- `cd <project_directory_path>`.
- `sudo lsof | grep <device_file_path>`.
- `sudo kill -9 <PID>`.
- `arduino-cli monitor --port <device_file_path> --config baudrate=9600 > <log_file_name>.csv`.
- 
