class CameraSimulator:
    """
    Simulates the logic for toggling between front and back camera resources.
    """
    def __init__(self):
        self.camera_position = "BACK"
        self.is_running = False

    def start_camera(self):
        """Initializes and 'binds' the camera resource."""
        self.is_running = True
        print("--- Camera App Initialized ---")
        self._bind_use_cases()

    def _bind_use_cases(self):
        """
        Internal function that simulates the CameraX binding process.
        """
        if not self.is_running:
            print("ERROR: Camera must be started first.")
            return

        print(f"Began binding process...")
        print(f"  - Using resource selector: {self.camera_position}")
        print(f"  - Preview stream connected.")
        print(f"  - Image capture use case attached.")
        print(f"Binding complete. Camera ready to capture.")

    def toggle_camera(self):
        """Switches the camera selector and re-binds the use cases."""
        if not self.is_running:
            print("ERROR: Camera is not running.")
            return

        # 1. Unbind (Simulated)
        print("\nUnbinding existing resources...")

        # 2. Determine the new camera selector
        if self.camera_position == "BACK":
            self.camera_position = "FRONT"
        else:
            self.camera_position = "BACK"

        # 3. Rebind the use cases with the new selector
        print(f"Switching to new camera position: {self.camera_position}")
        self._bind_use_cases()

    def stop_camera(self):
        """Stops the camera."""
        if self.is_running:
            self.is_running = False
            print("\nCamera resources released. App shut down.")
        else:
            print("Camera is already stopped.")


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    app = CameraSimulator()
    app.start_camera()

    # Toggle 1: Switch from BACK to FRONT
    app.toggle_camera()

    # Toggle 2: Switch from FRONT back to BACK
    app.toggle_camera()

    app.stop_camera()