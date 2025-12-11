import playsound
import time
while True:
    try:
        user_input_for_time = int(input('زمانی که میخوای سنجیده بشه رو اینجا وارد کن\n'))
        break
    except ValueError:
        print('دقت کن تو باید به عدد وارد کنی')
while user_input_for_time <0:
    user_input_for_time = int(input('لطفاً عدد کوچکتر از 0 وارد نکنید\n'))
    if user_input_for_time > 0:
        break
question = input('آیا میخوای اون عددی که توی ادیت باکس وارد کردی، دقیقه ی زمانسنج تو باشه یا ثانیه رو بسنجه؟ کلیدواژه ها، دقیقه، ثانیه\n')
question = question.lower()
while not question == 'دقیقه' and not question == 'ثانیه':
    question = input('کاربر گرامی، لطفاً فقط توی این ادیت باکس دقیقه یا ثانیه رو وارد کنید\n')
if question == 'دقیقه':
    count_time = 60
elif question == 'ثانیه':
    count_time = 1
all_seconds = count_time * user_input_for_time
question0 = input('کاربر گرامی، آیا دوست دارید که در هنگام محاسبه ی زمان ثانیه ها رو هم مشاهده کنید؟ بله و خیر رو توی این ادیت باکس وارد کنید\n')
question1 = input('آیا دوست دارید وقتی زمان تمام شد صدای هشدار رو بشنوید، با بله و خیر مشخص کنید\n')
print('تایمر روشن شده و داره کار میکنه')
if question0 == 'خیر':
    while all_seconds > 0:
        time.sleep(1)
        all_seconds = all_seconds -1
elif question0 == 'بله':
    while all_seconds > 0:
        time.sleep(1)
        print(f'{all_seconds} باقی مونده')
        all_seconds = all_seconds -1
if question1 == 'خیر':
    print('زمان وارد شده به پایان رسید')
elif question1 == 'بله':
    print('زمان وارد شده به پایان رسید')
    finish_timer = 'Mobile_Ringtones.mp3'
    for play_finish_time in range(2):
        playsound.playsound(finish_timer)
        if play_finish_time == 0:
            time.sleep(0.2)
exit1 = input('تایمر تموم شد، برای خارج شدن از تایمر کلمه ی خروج رو وارد کنید\n')
while not exit1 == 'خروج':
    exit1 = input('میدونم دوست ندارید برنامه ی تایمر با این امکانات کم تموم بشه، اما لطفاً برای خارج شدن از برنامه خروج رو توی ادیت باکس وارد کنید\n')
    if exit1 == 'خروج':
        break
end_of_timer = 'Victory-Sound-Effect.mp3'
playsound.playsound(end_of_timer)
print('از اینکه از تایمر استفاده کردید، نهایت تشکر رو دارم')
time.sleep(3)