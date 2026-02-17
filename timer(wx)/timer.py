import playsound
import time
import wx
import json
import threading
import os
import sys
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
ap = wx.App()
timer_title = wx.Frame(None, title="timer", size=(400, 600))
panel = wx.Panel(timer_title)
size = wx.BoxSizer(wx.VERTICAL)
with open(resource_path("english.json"), "r", encoding="utf-8") as english0:
    english = json.load(english0)
with open(resource_path("persian.json"), "r", encoding="utf-8") as persian0:
    persian = json.load(persian0)
all_languages = {"english": english, "persian": persian}
language_selected = "english"
user_value = 0
chosed_user = None
get_choose_user = None
get_sound_user = None
def get_languages_key(key):
    if language_selected:
        return all_languages[language_selected][key]
    return ""
panel0 = wx.Panel(panel)
size.Add(panel0, 0, wx.ALL, 5)
panel_sizer0 = wx.BoxSizer(wx.VERTICAL)
language_label = wx.StaticText(panel0, label="please select a language")
panel_sizer0.Add(language_label, 0, wx.ALL, 5)
def get_radio(event):
    global language_selected
    language_selected = event.GetEventObject().GetLabel()
    refresh_texts()
radio_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
radio_button1 = wx.RadioButton(panel0, style=wx.RB_GROUP, label="english")
radio_button2 = wx.RadioButton(panel0, label="persian")
radio_button_sizer.Add(radio_button1, 0, wx.ALL, 5)
radio_button_sizer.Add(radio_button2, 0, wx.ALL, 5)
panel_sizer0.Add(radio_button_sizer, 0, wx.ALL, 5)
radio_button1.Bind(wx.EVT_RADIOBUTTON, get_radio)
radio_button2.Bind(wx.EVT_RADIOBUTTON, get_radio)
panel0.SetSizer(panel_sizer0)
panel1 = wx.Panel(panel)
size.Add(panel1, 0, wx.ALL, 5)
panel_sizer1 = wx.BoxSizer(wx.VERTICAL)
choose_time = wx.StaticText(panel1, label="")
panel_sizer1.Add(choose_time, 0, wx.ALL, 5)
list_number_time = wx.SpinCtrl(panel1, min=0, max=1000000, initial=0)
panel_sizer1.Add(list_number_time, 0, wx.ALL, 5)
def spin1(event):
    global user_value
    user_value = list_number_time.GetValue()
list_number_time.Bind(wx.EVT_SPINCTRL, spin1)
panel1.SetSizer(panel_sizer1)
panel2 = wx.Panel(panel)
size.Add(panel2, 0, wx.ALL, 5)
panel_sizer2 = wx.BoxSizer(wx.VERTICAL)
choose_minit_second = wx.StaticText(panel2, label="")
panel_sizer2.Add(choose_minit_second, 0, wx.ALL, 5)
list_options = wx.Choice(panel2, choices=[])
panel_sizer2.Add(list_options, 0, wx.ALL, 5)
def user_choose(event):
    global chosed_user
    chosed_user = list_options.GetString(list_options.GetSelection())
list_options.Bind(wx.EVT_CHOICE, user_choose)
panel2.SetSizer(panel_sizer2)
panel3 = wx.Panel(panel)
size.Add(panel3, 0, wx.ALL, 5)
panel_sizer3 = wx.BoxSizer(wx.VERTICAL)
question = wx.StaticText(panel3, label="")
panel_sizer3.Add(question, 0, wx.ALL, 5)
question_chooser = wx.Choice(panel3, choices=[])
panel_sizer3.Add(question_chooser, 0, wx.ALL, 5)
def question_event(event):
    global get_choose_user
    get_choose_user = question_chooser.GetString(question_chooser.GetSelection())
question_chooser.Bind(wx.EVT_CHOICE, question_event)
panel3.SetSizer(panel_sizer3)
panel4 = wx.Panel(panel)
size.Add(panel4, 0, wx.ALL, 5)
panel_sizer4 = wx.BoxSizer(wx.VERTICAL)
sound_ask = wx.StaticText(panel4, label="")
panel_sizer4.Add(sound_ask, 0, wx.ALL, 5)
sound_chooser = wx.Choice(panel4, choices=[])
panel_sizer4.Add(sound_chooser, 0, wx.ALL, 5)
def sound_event(event):
    global get_sound_user
    get_sound_user = sound_chooser.GetString(sound_chooser.GetSelection())
sound_chooser.Bind(wx.EVT_CHOICE, sound_event)
panel4.SetSizer(panel_sizer4)
panel5 = wx.Panel(panel)
size.Add(panel5, 0, wx.ALL, 5)
panel_sizer5 = wx.BoxSizer(wx.VERTICAL)
button_confirm = wx.Button(panel5, label="")
status_label = wx.StaticText(panel5, label="")
panel_sizer5.Add(button_confirm, 0, wx.ALL, 5)
panel_sizer5.Add(status_label, 0, wx.ALL, 5)
def start_click(event):
    if user_value > 0 and chosed_user and get_choose_user and get_sound_user:
        threading.Thread(target=run_timer, daemon=True).start()
button_confirm.Bind(wx.EVT_BUTTON, start_click)
panel5.SetSizer(panel_sizer5)
def refresh_texts():
    choose_time.SetLabel(get_languages_key("time choose"))
    choose_minit_second.SetLabel(get_languages_key("question about time"))
    list_options.SetItems([get_languages_key("minute"), get_languages_key("second")])
    question.SetLabel(get_languages_key("question about seeing seconds"))
    question_chooser.SetItems([get_languages_key("yes"), get_languages_key("no")])
    sound_ask.SetLabel(get_languages_key("question about alarm"))
    sound_chooser.SetItems([get_languages_key("yes"), get_languages_key("no")])
    button_confirm.SetLabel(get_languages_key("confirm"))
    panel.Layout()
def run_timer():
    wx.CallAfter(status_label.SetLabel, get_languages_key("timer start working"))
    total = user_value * 60 if chosed_user == get_languages_key("minute") else user_value
    while total > 0:
        time.sleep(1)
        total -= 1
        if get_choose_user == get_languages_key("yes"):
            wx.CallAfter(status_label.SetLabel, f"{total} {get_languages_key('left')}")
    wx.CallAfter(status_label.SetLabel, get_languages_key("time end"))
    if get_sound_user == get_languages_key("yes"):
        try:
            for i in range(2):
                playsound.playsound(resource_path("Mobile_Ringtones.mp3"))
                if i == 0: time.sleep(0.2)
            playsound.playsound(resource_path("Victory-Sound-Effect.mp3"))
        except: pass
    wx.CallAfter(wx.MessageBox, get_languages_key("thanks for using"), get_languages_key("exit"))
refresh_texts()
panel.SetSizer(size)
timer_title.Layout()
timer_title.Show()
ap.MainLoop()