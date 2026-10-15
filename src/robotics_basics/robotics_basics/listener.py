import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotStatusMonitor(Node):

    def __init__(self):
        super().__init__('robot_status_monitor')

        self.subscription = self.create_subscription(
            String,
            'robot_status',
            self.status_callback,
            10
        )

        self.get_logger().info('Robot status monitor started')

    def status_callback(self, msg):
        status = msg.data

        self.get_logger().info(f'Received: {status}')

        if 'operational' in status:
            self.get_logger().info('Robot is operational')
        else:
            self.get_logger().warning('Robot status requires attention')


def main(args=None):
    rclpy.init(args=args)

    node = RobotStatusMonitor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
