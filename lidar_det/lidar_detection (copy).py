import rclpy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import time

move = Twist()

def callback(msg):
    if msg.ranges[642] < 1.4 or msg.ranges[542] < 1.4 or msg.ranges[442] < 1.4 or msg.ranges[-542] < 1.4 or msg.ranges[-442] < 1.4:
        move.linear.x = 0.0
        move.angular.z = 0.0
        print("Obstacle is detected")
    else:
        move.linear.x = 0.5
        move.angular.z = 0.0
        print("Robot is moving")

        # Timer for moving forward for 10 seconds
        time.sleep(10)

        move.linear.x = 0.0
        move.angular.z = 0.5
        print("Robot is rotating")

        # Timer for rotating for 5 seconds
        time.sleep(5)

        move.linear.x = 0.0
        move.angular.z = 0.0
        print("Stopping movement and rotation")

    pub.publish(move)

def main():
    rclpy.init()
    node = rclpy.create_node('lidar_test_node')

    sub = node.create_subscription(LaserScan, '/scan', callback, 10)
    global pub
    pub = node.create_publisher(Twist, '/cmd_vel', 10)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


