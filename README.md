# ROS 2 Robotics Basics

A simple ROS 2 project developed in Python to learn the fundamentals
of robotic software development.

## Features

- Publisher node that sends robot status messages.
- Subscriber node that receives and processes messages.
- Communication through ROS 2 topics.

## Requirements

- Ubuntu 26.04
- ROS 2 Lyrical Luth
- Python 3
- Colcon

## Project Structure

```text
robotics_ws/
└── src/
    └── robotics_basics/
        ├── package.xml
        ├── setup.py
        └── robotics_basics/
            ├── talker.py
            └── listener.py
