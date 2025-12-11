import playsound
import time
while True:
    try:
        user_input_for_time = int(input('Enter the time you want to measure here\n'))
        break
    except ValueError:
        print('Please make sure to enter a number')
while user_input_for_time < 0:
    user_input_for_time = int(input('Please do not enter a number smaller than 0\n'))
    if user_input_for_time > 0:
        break
question = input('Do you want the number you entered to be the minutes for the timer or seconds? Keywords: minute, second\n')
question = question.lower()
while not question == 'minute' and not question == 'second':
    question = input('Dear user, please only enter minute or second in this input box\n')
if question == 'minute':
    count_time = 60
elif question == 'second':
    count_time = 1
all_seconds = count_time * user_input_for_time
question0 = input('Dear user, would you like to see the seconds counting down during the timer? Enter yes or no\n')
question1 = input('Do you want to hear an alarm sound when the time is up? Specify with yes or no\n')
print('Timer started and is running')
if question0 == 'no':
    while all_seconds > 0:
        time.sleep(1)
        all_seconds = all_seconds - 1
elif question0 == 'yes':
    while all_seconds > 0:
        time.sleep(1)
        print(f'{all_seconds} remaining')
        all_seconds = all_seconds - 1
if question1 == 'no':
    print('The entered time has ended')
elif question1 == 'yes':
    print('The entered time has ended')
    finish_timer = 'Mobile_Ringtones.mp3'
    for play_finish_time in range(2):
        playsound.playsound(finish_timer)
        if play_finish_time == 0:
            time.sleep(0.2)
exit1 = input('Timer finished, to exit enter the word exit\n')
while not exit1 == 'exit':
    exit1 = input('I know you dont want the timer program with these limited features to end, but please enter exit to leave the program\n')
    if exit1 == 'exit':
        break
end_of_timer = 'Victory-Sound-Effect.mp3'
playsound.playsound(end_of_timer)
print('Thank you very much for using the timer')
time.sleep(3)