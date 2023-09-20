from pomodoro import Pomodoro
import os
import settings
import time
import file_io

import sys
import select

#clears the console and introduces the program, calls the main menu when enter is pressed
def start(pom):
    clear_stdout()
    print("Welcome to " + settings.NAME + " v" + settings.VERSION)
    print("This program allows you to set custom pomodoro timers and \ngives you a score based on performance!")
    input("press enter to continue")
    menu(pom)

#recursive menu that allows user to start a pomodoro, view the data for timers that day, view the usage guide
# or exit entirely
def menu(pom):    
    clear_stdout()

    choice = input("Wound you like to (1) start a pomodoro, (2) view day, (3) view usage guide,\n(4) exit\n")

    if choice == "1":
        start_pomo(pom)
    elif choice == "2":
        clear_stdout()
        file_io.view_day()
        print("\n-----------END-----------")
        input("\n\npress enter to continue")
    elif choice == "3":
        clear_stdout()
        display_file_content(settings.USAGE_PATH)
        print("\n-----------END-----------")
        input("\n\npress enter to continue")
    # upon quit write the pomodoro object with its data to the daily file. 
    elif choice == "4":
        file_io.write_pom_to_day(pom)
        return 0
    else:
        bad_input("Invalid choice. Please enter a valid option (1-4).")
    #recursive call
    menu(pom)

#starts a new timer within the pomodoro object
def start_pomo(pom):
    clear_stdout()
    while True:
        focus_time = input("How many minutes would you like to focus for?")
        if is_valid_integer(focus_time):
            pom.start_focus(int(focus_time)*60)
            pomo_focus_loop(pom)
            break
        else:
            bad_input("Invalid input. Please enter a valid integer for focus time (in minutes).")
        

#menu presented after a pomodoro session to allow user to extend timer, take a break, or return to main menu
def pomo_end_focus_menu(pom):
    choice = input("Congrats on finishing! Would you like to (1) extend (2) take break or (3) return to main menu")
    if choice == "1":
        start_pomo(pom)
    elif choice == "2":
        start_break(pom)
    elif choice == "3":
        menu(pom)

#break menu to start a break. No custom break option is presented for the time being      
def start_break(pom):
    clear_stdout()
    break_choice = input("Would you like to take (1) a five minute break or (2) a 20 minute break")
    if break_choice == "1":
        pom.start_break(300)
        pomo_break_loop(pom)
    elif break_choice == "2":
        pom.start_break(1200)
        pomo_break_loop(pom)
    else:
        bad_input("Invalid choice. Please enter 1 or 2.")

#loop for a timer in focus mode
def pomo_focus_loop(pom):
    running = True
    while running:
        clear_stdout()
        #represents time left in a minute second format to help user
        print("You have "+str(round(pom.get_remaining_time())//60) + "m"+str(round(pom.get_remaining_time())%60)+"s remaining! stay strong!")
        #allows for early quit
        if quit_wait("Press enter for early break:"):
            running = False
            pom.stop()
            rate_focus(pom)
            start_break(pom)
        #when time is less than zero ends the timer and calls the end menu
        elif pom.get_remaining_time() <= 0:
            running = False
            pom.stop()
            rate_focus(pom)
            pomo_end_focus_menu(pom)

#loop to run break. does not end early and user will lose points if break goes too long
def pomo_break_loop(pom):
    running = True
    while running:
        clear_stdout()
        print("You have "+str(round(pom.get_remaining_time())//60) + "m"+str(round(pom.get_remaining_time())%60)+"s remaining")
        if quit_wait("Press enter to end break:"):
            running = False
            pom.stop()
            end_break_update(pom)


# Function to clear the standard output
def clear_stdout():
    os.system('cls' if os.name == 'nt' else 'clear')

#menu for user to self evaluate their focus level and passes that into the pom object which will scale points gained based on 
# focus level. Outputs the gained points
def rate_focus(pom):
    clear_stdout()
    old_score = pom.score
    while True:
        focus = input("How would you rate your focus (1) bad (2) poor (3) average (4) good (5) extreme")
        if focus in settings.FOCUS_NUMBER_DICT:
            clear_stdout()
            print("you got " + str(pom.calculate_score(settings.FOCUS_NUMBER_DICT[focus])-old_score)+" points.")
            input("press enter to continue")
            break
        else:
            bad_input("Invalid input. Please enter a valid focus rating (1-5).")

#ends the currently running break timer and calculates its score
def end_break_update(pom):
    pom.calculate_score()
    
#prints file to console
def display_file_content(file_path):
   clear_stdout()
   if os.name == 'nt':  # Windows
      os.system('type ' + file_path)
   else:  # Unix
      os.system('cat ' + file_path)

def is_valid_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#allows for user to quit early without stopping the program from progressing
def quit_wait(message, timeout=1):
    print(message)

    # Set up input handling with a timeout
    input_ready, _, _ = select.select([sys.stdin], [], [], timeout)
    
    if input_ready:
        # User pressed Enter, but check if there's any input
        if sys.stdin.read(1) == "\n":
            return True  # Return True only when Enter is pressed
    return False  # No input received within the timeout or input was not Enter

def bad_input(message="BAD INPUT. Please try again."):
    print(message)
    input("Press enter to retry")

def clear_stdin():
    try:
        while True:
            # Read and discard any remaining input
            if sys.stdin.read(1) == "":
                break
    except KeyboardInterrupt:
        pass