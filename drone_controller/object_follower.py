from .basic_pid import PID




class ObjectFollower:
    # Setpoints for yaw and thrust PIDs are 160 to keep detected
    # object in the center of a 320x320 frame.
    # Pitch setpoint of 70 to keep detected object at 70 cm distance
    def __init__(self):
        self.yaw_pid = PID(160, 0.5, 0.0, 0.0, -1000, 1000)
        self.thrust_pid = PID(160, 0.5, 0.0, 0.0, 300, 700)
        self.pitch_pid = PID(70, 0.5, 0.0, 0.0, -1000, 1000)
        self.yaw_out = 0
        self.thrust_out = 0
        self.pitch_out = 0

    def __call__(self, x, y, distance):
        if (x != -1):
            self.yaw_out = int(self.yaw_pid(x))
            self.thrust_out = int(self.thrust_pid(y))
            self.pitch_out = int(self.pitch_pid(distance))
        # if x = -1 no object is being detected, drone should
        # move slowly towards ground with 300 thrust (500 is neutral thrust)
        else:
            self.yaw_out = 0
            self.thrust_out = 300
            self.pitch_out = 0

    def tune_yaw(self, kp, ki, kd):
        self.yaw_pid.tune(kp, ki, kd)

    def tune_thrust(self, kp, ki, kd):
        self.thrust_pid.tune(kp, ki, kd)

    def tune_pitch(self, kp, ki, kd):
        self.pitch_pid.tune(kp, ki, kd)



