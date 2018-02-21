import random
# import cozmo
#
# def happy(robot: cozmo.robot.Robot):
#     robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHappy).wait_for_completed()
#
# def cozmo_program(robot: cozmo.robot.Robot):
# #     robot.say_text('That’s rude. It may discourage your friend', use_cozmo_voice=False,duration_scalar=1.5,voice_pitch=1.5).wait_for_completed()
#
#     cozmoString="Great!<CodeLabHappy>"
#
#     if "<" in cozmoString:
#         start = cozmoString.index('<')
#         end = cozmoString.index('>')
#         animation = cozmoString[start + 1:end]
#         print(animation)
#         cozmoString=cozmoString.replace(cozmoString[start:end + 1], "")
#         if animation == 'CodeLabHappy':
#             robot.say_text(cozmoString, duration_scalar=0.6).wait_for_completed()
#             happy(robot)
#         print(cozmoString[start:end + 1])
#         print(cozmoString.replace(cozmoString[start:end + 1], ""))
#         print(start, end)
# # else:
# #     #robot.say_text(cozmoString, duration_scalar=0.6).wait_for_completed()
#
# cozmo.run_program(cozmo_program)

confused_response=['what?', 'Say Again', 'aha!', 'please repeat']
print(confused_response)
index=random.randint(0,3)
print (confused_response[index])



