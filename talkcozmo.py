import levenstein

import cozmo
import time
import sys


import voiceParse


#We can stay on the charger
cozmo.robot.Robot.drive_off_charger_on_connect = False

#Strings required for holding bits and pieces of the conversation later.
cozmoString = ""
humanString = ""

#Function to get the log started
def initLog():
    log = 0
    #Let's try to open the log file to append to. If we fail, we are forced to
    #exit the program. Otherwise, we state that the log file is opened.
    try:
        log = open("log.txt", "a")

    except:
        print("Error opening log file!")
        sys.exit()
    else:
        print("Log file opened.")

    return log



#Function to add entry to the log file.
def addEntry(log, entry):
    entryTime = time.gmtime()

    #Time format: Day-Month-Year Hour:Minute:Second
    parsedTime = str(entryTime.tm_mday) + "-" + str(entryTime.tm_mon) + "-" + \
                str(entryTime.tm_year) + " " + str(entryTime.tm_hour) + ":" + \
                str(entryTime.tm_min) + ":" + str(entryTime.tm_sec)

    #Now we patch together the log message
    logMessage = parsedTime + "# " + entry

    #Let's try to log it. If it fails, we simply skip logging the message
    try:
        log.write(logMessage + "\n")
    except:
        print("Error logging message! Skipping...")


#The main loop to our program. Runs after all the initialization.
def mainLoop(robot: cozmo.robot.Robot):

    #robot.say_text("Hey John, good job on your homework. Some of your friends still need help on the website, how about logging in there to help them?", voice_pitch=-1, duration_scalar=0.0001).wait_for_completed()


    while True:
        found=False
        #In a loop, we grab the user input
        print("Listening...")
        humanString = voiceParse.parseVoice()

        #Check it for a quit condition.
        if humanString.lower() == "bye":
            #If we quit, we log the quit and leave the program.
            addEntry(log, "Conversation ended.")
            sys.exit()

        #Else, we log what the human said.
        addEntry(log, "Human says: " + humanString)
        print("Human says: " + humanString)

        for k, v in dictionary.items():
            print(k, levenstein.minimumEditDistance(humanString, k))
            if levenstein.minimumEditDistance(humanString, k) <= 5:
                found=True
                cozmoString = v
                print(v)
                break
            print("going back in the for loop")

        if found is False:
            cozmoString="What?"

        #Print the response to the screen and add it to the log
        print("Cozmo says: " + cozmoString)
        addEntry(log, "Cozmo says: " + cozmoString)

        #Then we make Cozmo say it.
        robot.say_text(cozmoString,duration_scalar=0.6).wait_for_completed()

#This is where our code begins. We can first initialize everything,
#Then once it's all started, we log that the conversation has started
#and print the quit instructions to the user.
voiceParse.initSpeech()
log = initLog()

filename = sys.argv[1]
print("file name :: ",filename)
###
dictionary = {}
f = open(filename, "r")
pair = ''
#create the dictionary
while True:
    # read line
    line = f.readline()

    # check if line is not empty
    if not line:
        break

    #strip out the \n at the end
    l1=line.rstrip('\n')

    #split by ":"
    l2=l1.split(":")
    #print(l2)

    if l2[0] == 'human':
        key = l2[1]
        #print('human : ',key)
    else:
        pair = l2[1];
        #print('key : ',pair)
        dictionary[key] = pair

print(dictionary)

###
addEntry(log, "Conversation started.")
print("######################")
print("#Type 'quit' to exit.#")
print("######################")

cozmo.run_program(mainLoop)
