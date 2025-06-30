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

---

## How to Download and Run

### 1. Clone the Repository
```bash
cd ~/ros2_ws/src
git clone https://github.com/<your-username>/<your-repo-name>.git
```

### 2. Build the Package
```bash
cd ~/ros2_ws
colcon build --packages-select my_robot_controller
```

### 3. Source the Workspace
```bash
source install/setup.bash
```

### 4. Launch the Turtlesim Node
```bash
ros2 run turtlesim turtlesim_node
```

### 5. Run the ROS2 Nodes
In a new terminal (don’t forget to source the workspace in each terminal):
```bash
source install/setup.bash
```

Run any of the following nodes:
```bash
ros2 run my_robot_controller my_first_node
ros2 run my_robot_controller pose_subscriber
ros2 run my_robot_controller draw_circle
ros2 run my_robot_controller turtle_controller
ros2 run my_robot_controller turtle_controller_service
```

---

## Notes
- Make sure Python files are executable:
```bash
chmod +x *.py
```
- Replace `<your-username>` and `<your-repo-name>` with your actual GitHub username and repository name.

---

## License
MIT License
