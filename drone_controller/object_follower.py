from basic_pid import PID




class ObjectFollower:

    def __init__(self):
        self.yaw_pid = PID(150, 1, 0.5, 0.0, -1000, 1000)
        self.altitude_pid = PID(0, 0.2, 0.0, 0.2, 0, 1000)
        self.velocity_pid = PID(0, 0.2, 0.0, 0.2, -1000, 1000)
        self.yaw_out = 0.0
        self.altitude_out = 0.0
        self.velocity_out = 0.0

    def __call__(self, x, y, distance):
        self.yaw_out = self.yaw_pid(x)
        self.altitude_out = self.altitude_pid(y)
        self.velocity_out = self.velocity_pid(distance)

    def tune_yaw(self, kp, ki, kd):
        self.yaw_pid.tune(kp, ki, kd)

    def tune_altitude(self, kp, ki, kd):
        self.altitude_pid.tune(kp, ki, kd)

    def tune_velocity(self, kp, ki, kd):
        self.velocity_pid.tune(kp, ki, kd)
