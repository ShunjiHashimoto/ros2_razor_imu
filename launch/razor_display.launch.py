

import os
import sys

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():
    """
    Launch file for visualizing Razor IMU data
    """
    return LaunchDescription([
        Node(
            package='ros2_razor_imu',
            node_executable='display_3D_visualization_node',
            name='display_3D_visualization_node',
            output='screen',
        )
        
        
    ])
