from composabl.core import Agent, Skill, Sensor, Scenario
from composabl.ray import Runtime
from .airplane_teacher import NavigationTeacher

from composabl_core.agent import Teacher

import os

license_key = os.environ["COMPOSABL_KEY"]

def start():
    y1 = Sensor("y1", "air speed")
    y2 = Sensor("y2", "climb rate")
    u1 = Sensor("u1", "horizontal velocity")
    u2 = Sensor("u2", "vertical velocity")
    u3 = Sensor("u3", "rotation")
    u4 = Sensor("u4", "angle")

    sensors = [y1, y2, u1, u2, u3, u4]

    Navigation_scenarios = [
        {
            "y1": 0,
            "y2": 0,
            "u1": 0,
            "u2": 0,
            "u3": 0,
            "u4": 0          
        }
    ]

    Navigation_skill = Skill("Navigation", NavigationTeacher, trainable=True)

    for scenario_dict in Navigation_scenarios:
        scenario = Scenario(scenario_dict)
        Navigation_skill.add_scenario(scenario)
        

    config = {
        "env": {
            "name": "airplane",
            "compute": "local",  # "docker", "kubernetes", "local"
            "strategy": "local",  # "docker", "kubernetes", "local"
            "config": {
                "address": "localhost:1337",
                # "image": "composabl.ai/sim-gymnasium:latest"
            }
        },
        "license": license_key,
        "training": {}
    }
    runtime = Runtime(config)
    agent = Agent(runtime, config)
    agent.add_sensors(sensors)

    agent.add_skill(Navigation_skill)

    agent.train(train_iters=10)