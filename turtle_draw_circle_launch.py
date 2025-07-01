from launch import LaunchDescription
from launch_ros.actions import Node

###        METHOD 1:       ------------------------------------------------------------------
# def generate_launch_description():
#     return LaunchDescription([
#         Node(
#             package = "turtlesim",
#             namespace = '',
#             executable = 'turtlesim_node',
#             name = 'sim'
#         ),
#         Node(
#             package = "turtlesim",
#             namespace = 't',
#             executable = 'turtlesim_node',
#             name = 'sim'
#         ),        
#         Node(
#             package = "my_robot_controller",
#             namespace = 't',
#             executable = 'draw_circle',
#             name = 'draw_circle'
#         ),

#     ])

###        METHOD 2:       ------------------------------------------------------------------
def generate_launch_description():
    ld = LaunchDescription()    

    t1 = Node(
        package = "turtlesim",
        executable = 'turtlesim_node',
        remappings = [
            ("turtle1/cmd_vel", "speed")
        ]

    )
    t2 = Node(
        package = "my_robot_controller",
        executable = 'draw_circle',
        remappings = [
            ("turtle1/cmd_vel", "speed")
        ],
        parameters = [
            {"linear_velocity": 5.0},
            {"angular_angular": 2.0}
        ]
    )
    #ld = LaunchDescription([t1, t2])
    ld.add_action(t1)
    ld.add_action(t2)
    return ld