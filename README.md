# Run Instructions 

run train with 

python scripts/rsl_rl/train.py --task=Template-Quadrrl-Velocity-Flat-Unitree-Go2-v0


run play with


python scripts/rsl_rl/play --task=Template-Quadrrl-Velocity-Flat-Unitree-Go2-v0

Change path of the .usd file in the script robots/unitree.py. Search for variable 'usd_path'.

Import GO2 URDF from this repo https://github.com/unitreerobotics/unitree_ros/tree/master
In the GUI, select Moveable Base, None for all joints except hip, Allow Collision and Allow Collision Visuals.

D1 documentation here: https://support.unitree.com/home/en/developer/D1Arm_services
Download the URDF and paste it in the unitree_ros folder where the other descriptions are. 

Task names are registered in the __init__.py file inside the tasks/manager_based/go2_policy folder


## Notes

* Used Quadrrlm framework to train locomotion policy for both Go2 and Go2 with arm. Operations involved
    * Merged Go2 and D1 URDFs into one
    * Converted URDF into USD file
    * Created separate CFG in robots/unitree.py
2) Used Openarm previous work to train reach pose policy for D1 arm
    * Converted D1 urdf into usd
    * Added CFG based on openarm 
    * Decreased weight of the rotational reward from -0.1 to -0.2
3) Modified Go2+D1 urdf for manipulation only by making all quadruped joints fixed 
