[sundeep:]
I have created urdf/gripper_macro.xacro , this contains the visual and inertial description of the gripper (using simple shapes -- a cylinder and two cuboids). 

To combine the robot and the gripper, I am creating urdf/robot_gripper.urdf.xacro
I have included urdf/gripper_macro.xacro and I have renamed ar4_robot_arm.urdf-->ar4_robot_arm.xacro (with very minimal changes to the code, I'll change it as needed if I encounter any errors)

finally I combined all the macros into a single urdf called "robot_gripper_final.urdf" 
```
xacro src/robot_gripper/urdf/robot_gripper.urdf.xacro > src/robot_gripper/urdf/robot_gripper_final.urdf

```
