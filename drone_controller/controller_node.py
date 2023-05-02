import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from object_follower import ObjectFollower



class Controller(Node):
    def __init__(self):
        super().__init__('controller')
        self.subscription = self.create_subscription(Int32MultiArray, 'object_pos_and_distance', self.listener_callback, 10)
        self.publisher = self.create_publisher(Int32MultiArray, 'yaw_throttle_pitch', 10)
        self.object_follower = ObjectFollower()


    def listener_callback(self, data):
        self.object_follower(x=data[0], y=data[1], distance=data[2])
        msg = Int32MultiArray()
        msg.data = [self.object_follower.yaw_out, self.object_follower.throttle_out, self.object_follower.pitch_out ]
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    controller = Controller()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()
    

if (__name__ == "__main__"):
    main()


