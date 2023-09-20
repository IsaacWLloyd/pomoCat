#APP NAME
NAME = "POMO-PRO"
#version number
VERSION = "0.1"
#how much each second will add to your score
TIME_SCORE_MULTIPLIER = 1

#path to usage file
USAGE_PATH = "usage.txt"

#multipliers for each level of focus
BAD_FOCUS_SCORE_MULTIPLIER = 0.25
POOR_FOCUS_SCORE_MULTIPLIER = 0.5
AVERAGE_FOCUS_SCORE_MULTIPLIER = 1
GOOD_FOCUS_SCORE_MULTIPLIER = 1.5
EXTREME_FOCUS_SCORE_MULTIPLIER = 2
#dictionary to access the above multipliers
FOCUS_DICT = {"bad": BAD_FOCUS_SCORE_MULTIPLIER, "poor": POOR_FOCUS_SCORE_MULTIPLIER,
              "average": AVERAGE_FOCUS_SCORE_MULTIPLIER, "good": GOOD_FOCUS_SCORE_MULTIPLIER,
              "extreme": EXTREME_FOCUS_SCORE_MULTIPLIER}
FOCUS_NUMBER_DICT = {"1" : "bad", "2" : "poor", "3" : "average", 
                     "4" : "good", "5" : "extreme"}  
#score multiplier for how much each second 
# that a session is short by counts against you
SHORT_SESSION_MULTIPLIER = 1.75

#score multiplier for how muc each second
# that a break goes over by counts against you
LONG_BREAK_MULTIPLIER = 1.5

#the limit within which you may exit your 
# current timer without being penalize
TIME_ALLOWANCE = 1
#details the path to the scoreboard txt file
SCOREBOARD_PATH = ""
#DAILY folder path
DAILY_FOLDER_PATH = "daily/"

MONTHS_FOLDER_PATH = "months/"