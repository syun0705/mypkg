import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.create_subscription(Bool, "receive", self.callback, 10)

    def callback(self, msg):
        if msg.data:
            self.get_logger().info("ON")
        else:
            self.get_logger().info("OFF")


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

