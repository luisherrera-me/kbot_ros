import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/serial/by-path/pci-0000:00:14.0-usb-0:1:1.0-port0',
                'frame_id': 'lidar_link',  # Actualizado
                'angle_compensate': True,
                'scan_mode': 'Standard',
                'serial_baudrate': 115200,  # Agregado
                'model': 'A2'                # Agregado
            }]
        )
    ])
