import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_movement(robot: cozmo.robot.Robot):
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()


#http://cozmosdk.anki.com/docs/generated/cozmo.anim.html#module-cozmo.anim
def cozmo_program(robot: cozmo.robot.Robot):

    #positive

    # robot.say_text("i am happy").wait_for_completed()
    # robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHappy).wait_for_completed()
    # robot.say_text("i am excited to be with you").wait_for_completed()
    # robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabExcited).wait_for_completed()

    #neutral

    # robot.say_text("i am thinking about it").wait_for_completed()
    # robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabThinking).wait_for_completed()
    # robot.say_text("sleeping").wait_for_completed()
    # robot.play_anim_trigger(cozmo.anim.Triggers.IdleOnCharger).wait_for_completed()
    # robot.say_text("come sing with me!").wait_for_completed()
    # robot.play_anim_trigger(cozmo.anim.Triggers.Singing_100bpm).wait_for_completed()


    #negative

    # robot.say_text("i failed").wait_for_completed()
    # robot.play_anim_trigger(cozmo.anim.Triggers.FrustratedByFailure).wait_for_completed()
    #
    robot.play_anim_trigger(cozmo.anim.Triggers.PeekABooGetOutSad).wait_for_completed()




cozmo.run_program(cozmo_program)