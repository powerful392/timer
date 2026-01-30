import playsound
import time
language = input("Select language. Type pe or persian for Persian, and en or english for English\n")
if language.lower() == "en" or language.lower() == "english":
    while True:
        try:
            user_input_for_time = int(input("Enter the time you want to measure here\n"))
            break
        except ValueError:
            print("Please make sure to enter a number")
    while user_input_for_time < 0:
        user_input_for_time = int(input("Please do not enter a number smaller than 0\n"))
        if user_input_for_time > 0:
            break
    question = input("Do you want the number you entered to be the minutes for the timer or seconds? Keywords: minute, second\n")
    question = question.lower()
    while not question == "minute" and not question == "second":
        question = input("Dear user, please only enter minute or second in this input box\n")
    if question == "minute":
        count_time = 60
    elif question == "second":
        count_time = 1
    all_seconds = count_time * user_input_for_time
    question0 = input("Dear user, would you like to see the seconds counting down during the timer? Enter yes or no\n")
    question1 = input("Do you want to hear an alarm sound when the time is up? Specify with yes or no\n")
    print("Timer started and is running")
    if question0 == "no":
        while all_seconds > 0:
            time.sleep(1)
            all_seconds = all_seconds - 1
    elif question0 == "yes":
        while all_seconds > 0:
            time.sleep(1)
            print(f"{all_seconds} remaining")
            all_seconds = all_seconds - 1
    if question1 == "no":
        print("The entered time has ended")
    elif question1 == "yes":
        print("The entered time has ended")
        finish_timer = "Mobile_Ringtones.mp3"
        for play_finish_time in range(2):
            playsound.playsound(finish_timer)
            if play_finish_time == 0:
                time.sleep(0.2)
    exit1 = input("Timer finished, to exit enter the word exit\n")
    while not exit1 == "exit":
        exit1 = input("I know you dont want the timer program with these limited features to end, but please enter exit to leave the program\n")
        if exit1 == "exit":
            break
    end_of_timer = "Victory-Sound-Effect.mp3"
    playsound.playsound(end_of_timer)
    print("Thank you very much for using the timer")
    time.sleep(3)
elif language.lower() == "pe" or language.lower() == "persian":
    while True:
        try:
            user_input_for_time = int(input("زمانی که میخوای سنجیده بشه رو اینجا وارد کن\n"))
            break
        except ValueError:
            print("دقت کن تو باید به عدد وارد کنی")
    while user_input_for_time <0:
        user_input_for_time = int(input("لطفاً عدد کوچکتر از 0 وارد نکنید\n"))
        if user_input_for_time > 0:
            break
    question = input("آیا میخوای اون عددی که توی ادیت باکس وارد کردی، دقیقه ی زمانسنج تو باشه یا ثانیه رو بسنجه؟ کلیدواژه ها، دقیقه، ثانیه\n")
    question = question.lower()
    while not question == "دقیقه" and not question == "ثانیه":
        question = input("کاربر گرامی، لطفاً فقط توی این ادیت باکس دقیقه یا ثانیه رو وارد کنید\n")
    if question == "دقیقه":
        count_time = 60
    elif question == "ثانیه":
        count_time = 1
    all_seconds = count_time * user_input_for_time
    question0 = input("کاربر گرامی، آیا دوست دارید که در هنگام محاسبه ی زمان ثانیه ها رو هم مشاهده کنید؟ بله و خیر رو توی این ادیت باکس وارد کنید\n")
    question1 = input("آیا دوست دارید وقتی زمان تمام شد صدای هشدار رو بشنوید، با بله و خیر مشخص کنید\n")
    print("تایمر روشن شده و داره کار میکنه")
    if question0 == "خیر":
        while all_seconds > 0:
            time.sleep(1)
            all_seconds = all_seconds -1
    elif question0 == "بله":
        while all_seconds > 0:
            time.sleep(1)
            print(f"{all_seconds} باقی مونده")
            all_seconds = all_seconds -1
    if question1 == "خیر":
        print("زمان وارد شده به پایان رسید")
    elif question1 == "بله":
        print("زمان وارد شده به پایان رسید")
        finish_timer = "Mobile_Ringtones.mp3"
        for play_finish_time in range(2):
            playsound.playsound(finish_timer)
            if play_finish_time == 0:
                time.sleep(0.2)
    exit1 = input("تایمر تموم شد، برای خارج شدن از تایمر کلمه ی خروج رو وارد کنید\n")
    while not exit1 == "خروج":
        exit1 = input("میدونم دوست ندارید برنامه ی تایمر با این امکانات کم تموم بشه، اما لطفاً برای خارج شدن از برنامه خروج رو توی ادیت باکس وارد کنید\n")
        if exit1 == "خروج":
            break
    end_of_timer = "Victory-Sound-Effect.mp3"
    playsound.playsound(end_of_timer)
    print("از اینکه از تایمر استفاده کردید، نهایت تشکر رو دارم")
    time.sleep(3)
else:
    print("invalid language, please restart program again")
    print("زبان وارد شده نادرست است. لطفاً برنامه را دوباره اجرا کنید")