import rclpy
from sensor_msgs.msg import LaserScan

def callback(msg):
    range_start_index = 600
    range_end_index = 1000

    if 0 <= range_start_index < len(msg.ranges) and 0 <= range_end_index < len(msg.ranges):
        print(f'Values in the range ({range_start_index} to {range_end_index}):')
        for i in range(range_start_index, range_end_index + 1):
            value = msg.ranges[i]
            print(f'Value at index {i}: {value}')
            if value < 0.5:
                print('Obstacle is detected')
    else:
        print('Invalid indices for the specified range. fine')

def main():
    rclpy.init()
    node = rclpy.create_node('lidar_test_node')

    sub = node.create_subscription(LaserScan, '/scan', callback, 10)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
