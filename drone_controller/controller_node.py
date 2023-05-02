ïmport rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray



class Controller(Node):
    def __init__(self):
        super().__init__('controller')
        self.subscription = self.create_subscription(Int32MultiArray, 'object_pos_and_distance', 10)