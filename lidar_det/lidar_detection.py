import rclpy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

move = Twist()

def callback(msg):
    range_start_index = 600
    range_end_index = 1000

    if 0 <= range_start_index < len(msg.ranges) and 0 <= range_end_index < len(msg.ranges):
        print(f'Values in the range ({range_start_index} to {range_end_index}):')
        obstacle_detected = False

        for i in range(range_start_index, range_end_index + 1):
            value = msg.ranges[i]
            print(f'Value at index {i}: {value}')
            
            if value < 2.5:
                print('Obstacle is detected')
                obstacle_detected = True

        if obstacle_detected:
            # Publish cmd_vel with linear.x = 0 and angular.z = 0
            move.linear.x = 0.0
            move.angular.z = 0.0
            pub.publish(move)
    else:
        print('Invalid indices for the specified range.')

def main():
    global pub
    rclpy.init()
    node = rclpy.create_node('lidar_test_node')

    pub = node.create_publisher(Twist, '/cmd_vel', 10)
    sub = node.create_subscription(LaserScan, '/scan', callback, 10)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
