# Template for Isaac Lab Projects

run train with 

python scripts/rsl_rl/train.py --task=Template-Quadrrl-Velocity-Flat-Unitree-Go2-v0


run play with


python scripts/rsl_rl/play --task=Template-Quadrrl-Velocity-Flat-Unitree-Go2-v0

Change path of the .usd file in the script robots/unitree.py. Search for variable 'usd_path'.

Import GO2 URDF from this repo https://github.com/unitreerobotics/unitree_ros/tree/master
In the GUI, select Moveable Base, None for all joints except hip, Allow Collision and Allow Collision Visuals.

D1 documentation here: https://support.unitree.com/home/en/developer/D1Arm_services
Download the URDF and paste it in the unitree_ros folder where the other descriptions are. 

