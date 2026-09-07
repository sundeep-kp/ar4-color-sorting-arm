from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_spawn_controllers_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("ar4_robot_arm", package_name="ar4_robot_arm_moveit_setup").to_moveit_configs()
    return generate_spawn_controllers_launch(moveit_config)
