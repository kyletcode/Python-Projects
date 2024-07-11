class RobotController:
    def __init__(self, actuator, end_effector):
        self.actuator = actuator
        self.end_effector = end_effector
        
    def control_robot(self, force):
        print("Robot controller sending signal to control the actuator...")
        self.actuator.perform_action("Apply Force")
        self.end_effector.apply_force(force)
        print("End effector moved successfully!")


class Sensor:
    def __init__(self, sensor_type):
        self.sensor_type = sensor_type
        self.data_value = None
        
    def set_data_value(self, value):
        self.data_value = value
        
    def get_data_value(self):
        return self.data_value
    
    @classmethod
    def retrieve_data_value(cls, sensor_obj):
        sensor_type = sensor_obj.sensor_type
        data_value = sensor_obj.get_data_value()
        
        print("Retrieving data value from sensor object:")
        print("Sensor type:", sensor_type)
        print("Data value:", data_value)
        print("Data value retrieved successfully!")


class Actuator:
    def __init__(self, actuator_type):
        self.actuator_type = actuator_type
        
    def perform_action(self, action):
        print(f"{self.actuator_type} is performing action: {action}")


class EndEffector:
    def __init__(self, end_effector_type):
        self.end_effector_type = end_effector_type
        
    def apply_force(self, force):
        print(f"Applying force {force} to {self.end_effector_type}")




# Create an object for each component class
temperature_sensor = Sensor("Temperature")
motor_actuator = Actuator("Motor")
gripper_end_effector = EndEffector("Gripper")



temperature_sensor.set_data_value(25.5)
temperature = Sensor.retrieve_data_value(temperature_sensor)
motor_actuator.perform_action("Start")
gripper_end_effector.apply_force(10)


# Create objects for each component class
motor_actuator = Actuator("Motor")
gripper_end_effector = EndEffector("Gripper")

# Create a robot controller with the actuator and end effector objects
robot_controller = RobotController(motor_actuator, gripper_end_effector)

# Simulate the robot controller triggering the actuator to move the end effector
force = 10
robot_controller.control_robot(force)