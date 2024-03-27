import asyncio
from gymnasium.wrappers import RecordVideo
import os
import torch

from composabl import Agent, Runtime

from sim.sim import MultiWalkerEnv
license_key = os.environ["COMPOSABL_LICENSE"]


async def start():
    os.environ["COMPOSABL_EULA_AGREED"] = "1"
    config = {
        "license": license_key,
        "target": {
            "local": {
                "address": "localhost:1337",
            }
        },
        "env": {
            "name": "multi-walker",
        },
        "training": {}
    }

    runtime = Runtime(config)

    # Export the agent to the specified directory then re-load it and resume training
    directory = os.path.join(os.getcwd(), "model")

    agent = Agent.load(directory)

    # call the original agent to prepare, since we didn't add all the skill groups
    trained_agent = await runtime.package(agent)

    env = RecordVideo(env=MultiWalkerEnv(), video_folder='video', episode_trigger=lambda x: True, video_length=0)
    obs, _info = env.reset()

    for _episode_idx in range(5):
        obs, _info = env.reset()
        env.start_video_recorder()
        done = False
        steps = 0
        while not done:
            env.render()
            action = await trained_agent.execute(obs)
            obs, _reward, done, _truncated, _info = env.step(action)
            steps += 1
            if steps > 1000:
                # sometimes the robots get stuck and we need to break out of the loop
                break
        env.close_video_recorder()
    env.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start())
