from glob import glob
import os
from setuptools import setup, find_packages

package_name = "ros2_razor_imu"
SHARE_DIR = os.path.join("share", package_name)

setup(
    name=package_name,
    version='1.3.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, "launch"), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, "config"), glob('config/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        ],
    
    install_requires=['setuptools',
                        'pyserial',
                        'pyyaml',
                        'transforms3d',
                        'vpython',
                        'wxPython'],
    zip_safe=True,
    author='Kristof Robot, Tang Tiong Yew, Paul Bouchier, Peter Bartz',
    maintainer='Kristof Robot',
    keywords=['ROS2'],
    description='ros2_razor_imu is a package that provides a ROS2 driver for the Sparkfun Razor IMU 9DOF.',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['imu_node = ros2_razor_imu.imu_node:main',
                            'imu_to_tf_node = ros2_razor_imu.imu_to_tf_node:main',
                            'display_3D_visualization_node = ros2_razor_imu.display_3D_visualization:main',
                            ],
    }
)
