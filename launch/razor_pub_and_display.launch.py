

import os
import sys

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():
    """
    Launch file for publishing Razor IMU data
    """    
    configs = os.path.join(get_package_share_directory(
        "ros2_razor_imu"), "config", "razor.yaml")
    assert os.path.exists(configs)
    
    return LaunchDescription([
        Node(
            package='ros2_razor_imu',
            node_executable='display_3D_visualization_node',
            name='display_3D_visualization_node',
            output='screen',
        ),
        
        Node(package='ros2_razor_imu',
            node_executable='imu_node', 
            name= 'imu_node', 
            output='screen',
            parameters=[configs]
        ),  
    ])
