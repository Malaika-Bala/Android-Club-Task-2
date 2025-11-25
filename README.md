CamCraft Simulator Console Application
This project is a Python class-based script that simulates the Camera Toggling Feature required in Task 2. Since Android specific libraries like CameraX cannot run in a standard Python environment, this script demonstrates the core programming logic of state management and resource rebinding that underlies the front and back camera switching functionality.

Features
State Management Tracks the camera's current position ("BACK" or "FRONT") and its operational status (is_running).

Resource Binding Simulation Simulates the process of binding camera use cases (Preview, Capture) to the currently selected camera.

Camera Toggle Logic Contains a method to flip the camera state and trigger a simulated rebinding of resources, mirroring the Android development requirement.

Console Output Provides clear print statements to trace the application's lifecycle and the camera switching process.

Technology
Language Python

Getting Started
Prerequisites
Python 3 installed on your system.

Setup and Execution
Save the Code Save the provided Python code into a file named camera_simulator.py.

Run the Script Execute the file from your terminal:

Bash

python camera_simulator.py
Output The script runs automatically, demonstrating the sequence of starting the camera, toggling its position twice, and stopping the application.

Class Structure
CameraSimulator
This class encapsulates all the application logic.

__init__ Initializes the camera state variables.

start_camera Sets the application state to running and calls the binding function.

_bind_use_cases The core function that simulates attaching the camera hardware resources based on the current self.camera_position.

toggle_camera The main feature function. It changes the value of self.camera_position and forces a call to _bind_use_cases to simulate resource switching.

stop_camera Releases the application resources and sets the running state to false.

Example Output Trace
The output when running the script will look like this, demonstrating the state changes:

--- Camera App Initialized ---
Began binding process...
  - Using resource selector: BACK
  - Preview stream connected.
  - Image capture use case attached.
Binding complete. Camera ready to capture.

Unbinding existing resources...
Switching to new camera position: FRONT
Began binding process...
  - Using resource selector: FRONT
  - Preview stream connected.
  - Image capture use case attached.
Binding complete. Camera ready to capture.

Unbinding existing resources...
Switching to new camera position: BACK
Began binding process...
  - Using resource selector: BACK
  - Preview stream connected.
  - Image capture use case attached.
Binding complete. Camera ready to capture.

Camera resources released. App shut down.
Author
Malaika Bala
