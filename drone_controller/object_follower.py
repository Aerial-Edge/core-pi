from basic_pid import PID




class ObjectFollower:

    def __init__(self):
        self.yaw_pid = PID(150, 1, 0.5, 0.0, -1000, 1000)
        self.throttle_pid = PID(150, 0.2, 0.0, 0.2, 0, 1000)
        self.pitch_pid = PID(40, 0.2, 0.0, 0.2, -1000, 1000)
        self.yaw_out = 0.0
        self.throttle_out = 0.0
        self.pitch_out = 0.0

    def __call__(self, x, y, distance):
        self.yaw_out = self.yaw_pid(x)
        self.throttle_out = self.throttle_pid(y)
        self.pitch_out = self.pitch_pid(distance)

    def tune_yaw(self, kp, ki, kd):
        self.yaw_pid.tune(kp, ki, kd)

    def tune_altitude(self, kp, ki, kd):
        self.throttle_pid.tune(kp, ki, kd)

    def tune_velocity(self, kp, ki, kd):
        self.pitch_pid.tune(kp, ki, kd)
