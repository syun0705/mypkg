# SPDX-FileCopyrightText: 2025 Syun Naitou
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Bool, "receive", 10)


time  = 6 * 60

def clock_and_judge():
    global time

    hour = (time // 60) % 24
    minute = time % 60

    msg = Bool()

    if hour >= 18 or hour < 6:
        msg.data = True
        state = "ON"
    else:
        msg.data = False
        state = "OFF"

    pub.publish(msg)

    node.get_logger().info(
            f"{state}"
    )

    time += 1
    if time >= 24 * 60:
        time = 0


def main():
    node.create_timer(1.0, clock_and_judge)
    rclpy.spin(node)


if __name__ == "__main__":
    main()

