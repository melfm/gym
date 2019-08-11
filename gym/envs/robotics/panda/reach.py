import os
from gym import utils
from gym.envs.robotics import panda_env


# Ensure we get the path separator correct on windows
MODEL_XML_PATH = os.path.join('panda/panda_mjcf', 'panda.xml')


class PandaReachEnv(panda_env.PandaEnv, utils.EzPickle):
    def __init__(self, reward_type='sparse'):
        initial_qpos = {
            'panda_joint1': 0.4049,
            'panda_joint2': 0.48,
            'panda_joint3': 0.0,
            'panda_joint4': 0.4049,
            'panda_joint5': 0.48,
            'panda_joint6': 0.0,
            'panda_joint7': 0.0,
            'panda_finger_joint1': 0.0,
            'panda_finger_joint2': 0.0,
        }
        panda_env.PandaEnv.__init__(
            self, MODEL_XML_PATH, has_object=False, block_gripper=True, n_substeps=20,
            gripper_extra_height=0.2, target_in_the_air=True, target_offset=0.0,
            obj_range=0.15, target_range=0.15, distance_threshold=0.05,
            initial_qpos=initial_qpos, reward_type=reward_type)
        utils.EzPickle.__init__(self)
