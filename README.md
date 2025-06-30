# ROS2 Basics with Turtlesim – my_robot_controller

This repository contains beginner-friendly **ROS2 Python nodes** using the `turtlesim` simulator. It helps in learning core ROS2 concepts like publishers, subscribers, services, and timers.

---

## Project Files
- `my_first_node.py` – Basic timer node that prints a counter every second.
- `pose_subscriber.py` – Subscribes to `/turtle1/pose` and logs the turtle's position.
- `draw_circle.py` – Publishes velocity commands to move the turtle in a circular path.
- `turtle_controller.py` – Turtle controller that changes the turtle's speed based on its position.
- `turtle_controller_service.py` – Advanced controller that changes the turtle’s pen color using ROS2 services based on its position.

```text
my_robot_controller/
├── package.xml
├── setup.py
├── resource/
│   └── my_robot_controller
├── my_robot_controller/
│   ├── __init__.py
│   ├── my_first_node.py
│   ├── pose_subscriber.py
│   ├── draw_circle.py
│   ├── turtle_controller.py
│   └── turtle_controller_service.py
└── README.md
```
