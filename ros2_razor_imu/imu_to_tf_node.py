# imuデータをsubして、tfをpubするノード

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

class ImuToTfNode(Node):
    def __init__(self):
        super().__init__('imu_to_tf_node')
        self.imu_subscriber = self.create_subscription(
            Imu,
            'imu',
            self.imu_callback,
            10
        )
        self.tf_broadcaster = TransformBroadcaster(self)

    def imu_callback(self, msg):
        t = TransformStamped()
        # 現在の時刻を設定
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'imu_link'
        t.child_frame_id = 'laser'
        # IMUデータから姿勢を取得
        t.transform.translation.x = 0.42
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.2
        t.transform.rotation = msg.orientation
        # TFをブロードキャスト
        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = ImuToTfNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
