import cozmo

def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text('That’s rude. It may discourage your friend', use_cozmo_voice=False,duration_scalar=1.5,voice_pitch=1.5).wait_for_completed()

cozmo.run_program(cozmo_program)

