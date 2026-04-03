# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import math

from isaaclab.utils import configclass

##
# Pre-defined configs
##
from . import mdp
from GO2_policy.robots.unitree import D1_550_CFG  # noqa: F401
from .reach_env_cfg import ReachEnvCfg

from isaaclab.assets.articulation import ArticulationCfg

##
# Environment configuration
##


@configclass
class D1550ReachEnvCfg(ReachEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()

        # switch robot to OpenArm
        self.scene.robot = D1_550_CFG.replace(
            prim_path="{ENV_REGEX_NS}/Robot",
            init_state=ArticulationCfg.InitialStateCfg(
                joint_pos={
                    "Joint1": 0.0,
                    "Joint2": 0.0,
                    "Joint3": 0.0,
                    "Joint4": 0.0,
                    "Joint5": 0.0,
                    "Joint6": 0.0,
                    "Joint_L": 0.0,
                    "Joint_R": 0.0
                },  
            ),
        )

        # override rewards
        self.rewards.end_effector_position_tracking.params["asset_cfg"].body_names = ["Empty_Link6"]
        self.rewards.end_effector_position_tracking_fine_grained.params["asset_cfg"].body_names = ["Empty_Link6"]
        self.rewards.end_effector_orientation_tracking.params["asset_cfg"].body_names = ["Empty_Link6"]

        # override actions
        self.actions.arm_action = mdp.JointPositionActionCfg(
            asset_name="robot",
            joint_names=[
                ".*",
            ],
            scale=0.5,
            use_default_offset=True,
        )

        # override command generator body
        # end-effector is along z-direction
        self.commands.ee_pose.body_name = "Empty_Link6"


@configclass
class D1550ReachEnvCfg_PLAY(D1550ReachEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # make a smaller scene for play
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        # disable randomization for play
        self.observations.policy.enable_corruption = False
