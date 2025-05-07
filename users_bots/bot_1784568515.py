import TgBotMapi as tbm

tg = tbm.TgBot('1784568515')       

f = {}
names_funcs = {}
def func1_func(message):
    global tg

    tg.message('1', message)

names_funcs['func1'] = func1_func
    
def func2_func(message):
    global tg

    tg.message('2', message)

names_funcs['func2'] = func2_func
    
def func3_func(message):
    global tg

    tg.message('3', message)

names_funcs['func3'] = func3_func
    
def func4_func(message):
    global tg

    tg.message('4', message)

names_funcs['func4'] = func4_func
    
def startik_func(message):
    global tg

    tg.message('90', message)

names_funcs['startik'] = startik_func
    
def mazucht_func(message):
    global tg

    tg.message('unzucht', message)

names_funcs['mazucht'] = mazucht_func
    
def unzucht_func(message):
    global tg

    tg.message('kaputt', message)

names_funcs['unzucht'] = unzucht_func
    
def erdling_func(message):
    global tg

    tg.message('weissglut', message)

names_funcs['erdling'] = erdling_func
    

def ty1_but_0(message):
    global tg

    tg.message("1", message)
    names_funcs['unzucht'](message)
    
ty1_dict = {}
ty1_dict["0"] = ty1_but_0

def ty1_but_1(message):
    global tg

    tg.message("3", message)
    names_funcs['unzucht'](message)

ty1_dict["1"] = ty1_but_1

def ty1_but_2(message):
    global tg

    tg.message("2", message)
    names_funcs['unzucht'](message)

ty1_dict["2"] = ty1_but_2

f['ty1'] = 0
def ty1_func(message):
    global ty1_kb
    global f

    if f['ty1'] == 0:
        ty1_kb = tbm.Keyboard(
        buts=['erste', 'dritte', 'zweite'],
        values=list(ty1_dict.values()),
        row_width=2,
        name="ty1",
        text="nummer",
        message=message,
        bot=tg)

        f['ty1'] = 1

    ty1_kb.send()

names_funcs['deutsch'] = ty1_func


def ty2_but_0(message):
    global tg

    tg.message("erste", message)
ty2_dict = {}
ty2_dict["0"] = ty2_but_0

def ty2_but_1(message):
    global tg

    tg.message("zweite", message)
ty2_dict["1"] = ty2_but_1

def ty2_but_2(message):
    global tg

    tg.message("dritte", message)
ty2_dict["2"] = ty2_but_2

f['ty2'] = 0
def ty2_func(message):
    global ty2_kb
    global f

    if f['ty2'] == 0:
        ty2_kb = tbm.Keyboard(
        buts=['one', 'two', 'three'],
        values=list(ty2_dict.values()),
        row_width=2,
        name="ty2",
        text="englisch nummer",
        message=message,
        bot=tg)

        f['ty2'] = 1

    ty2_kb.send()

names_funcs['englisch'] = ty2_func


def ty2_but_0(message):
    global tg

    tg.message("erste", message)
    names_funcs['mazucht'](message)
    
ty2_dict = {}
ty2_dict["0"] = ty2_but_0

def ty2_but_1(message):
    global tg

    tg.message("zweite", message)
    names_funcs['mazucht'](message)

ty2_dict["1"] = ty2_but_1

def ty2_but_2(message):
    global tg

    tg.message("dritte", message)
    names_funcs['mazucht'](message)

ty2_dict["2"] = ty2_but_2

f['ty2'] = 0
def ty2_func(message):
    global ty2_kb
    global f

    if f['ty2'] == 0:
        ty2_kb = tbm.Keyboard(
        buts=['one', 'two'],
        values=list(ty2_dict.values()),
        row_width=2,
        name="ty2",
        text="englisch nummer",
        message=message,
        bot=tg)

        f['ty2'] = 1

    ty2_kb.send()

names_funcs['englisch'] = ty2_func


def ty2_but_0(message):
    global tg

    tg.message("erste", message)
ty2_dict = {}
ty2_dict["0"] = ty2_but_0

def ty2_but_1(message):
    global tg

    tg.message("zweite", message)
ty2_dict["1"] = ty2_but_1

def ty2_but_2(message):
    global tg

    tg.message("dritte", message)
ty2_dict["2"] = ty2_but_2

f['ty2'] = 0
def ty2_func(message):
    global ty2_kb
    global f

    if f['ty2'] == 0:
        ty2_kb = tbm.Keyboard(
        buts=['one'],
        values=list(ty2_dict.values()),
        row_width=2,
        name="ty2",
        text="englisch nummer",
        message=message,
        bot=tg)

        f['ty2'] = 1

    ty2_kb.send()

names_funcs['englisch'] = ty2_func


def kl_but_0(message):
    global tg

    tg.message("ba", message)
kl_dict = {}
kl_dict["0"] = kl_but_0

def kl_but_1(message):
    global tg

    tg.message("by", message)
kl_dict["1"] = kl_but_1

f['kl'] = 0
def kl_func(message):
    global kl_kb
    global f

    if f['kl'] == 0:
        kl_kb = tbm.Keyboard(
        buts=['op', 'ko'],
        values=list(kl_dict.values()),
        row_width=1,
        name="kl",
        text="txtu",
        message=message,
        bot=tg)

        f['kl'] = 1

    kl_kb.send()

names_funcs['testi'] = kl_func


def g_but_0(message):
    global tg

    tg.message("1", message)
g_dict = {}
g_dict["0"] = g_but_0

f['g'] = 0
def g_func(message):
    global g_kb
    global f

    if f['g'] == 0:
        g_kb = tbm.Keyboard(
        buts=['h'],
        values=list(g_dict.values()),
        row_width=2,
        name="g",
        text="ty",
        message=message,
        bot=tg)

        f['g'] = 1

    g_kb.send()

names_funcs['klop'] = g_func


def g_but_0(message):
    global tg

    tg.message("1", message)
g_dict = {}
g_dict["0"] = g_but_0

f['g'] = 0
def g_func(message):
    global g_kb
    global f

    if f['g'] == 0:
        g_kb = tbm.Keyboard(
        buts=[''],
        values=list(g_dict.values()),
        row_width=2,
        name="g",
        text="ty",
        message=message,
        bot=tg)

        f['g'] = 1

    g_kb.send()

names_funcs['klop'] = g_func


def keyboard_but_0(message):
    global tg

    tg.message("1", message)
keyboard_dict = {}
keyboard_dict["0"] = keyboard_but_0

def keyboard_but_1(message):
    global tg

    tg.message("2", message)
keyboard_dict["1"] = keyboard_but_1

def keyboard_but_2(message):
    global tg

    tg.message("3", message)
keyboard_dict["2"] = keyboard_but_2

def keyboard_but_3(message):
    global tg

    tg.message("4", message)
keyboard_dict["3"] = keyboard_but_3

f['keyboard'] = 0
def keyboard_func(message):
    global keyboard_kb
    global f

    if f['keyboard'] == 0:
        keyboard_kb = tbm.Keyboard(
        buts=['But1', 'But2', 'But3', 'But4'],
        values=list(keyboard_dict.values()),
        row_width=2,
        name="keyboard",
        text="txt",
        message=message,
        bot=tg)

        f['keyboard'] = 1

    keyboard_kb.send()

names_funcs['keyboard_test'] = keyboard_func


def in1_menu_but_0(message):
    global tg

    tg.message_edit("en", message)
in1_menu_dict = {}
in1_menu_dict["0"] = in1_menu_but_0

def in1_menu_but_1(message):
    global tg

    tg.message_edit("de", message)
in1_menu_dict["1"] = in1_menu_but_1

f['in1_menu'] = 0
def in1_menu_func(message):
    global in1_menu_kb
    global f

    if f['in1_menu'] == 0:
        in1_menu_kb = tbm.InlineKeyboard(
        buts=['in', 'im'],
        values=list(in1_menu_dict.values()),
        row_width=2,
        name="in1_menu",
        text="txtin",
        message=message,
        bot=tg)

        f['in1_menu'] = 1

    in1_menu_kb.send()

names_funcs['inli'] = in1_menu_func


def test_but_0(message):
    global tg

    tg.message_edit("немецкий", message)
test_dict = {}
test_dict["0"] = test_but_0

def test_but_1(message):
    global tg

    tg.message_edit("английский", message)
test_dict["1"] = test_but_1

f['test'] = 0
def test_func(message):
    global test_kb
    global f

    if f['test'] == 0:
        test_kb = tbm.InlineKeyboard(
        buts=['deutsche', 'englische'],
        values=list(test_dict.values()),
        row_width=2,
        name="test",
        text="testtxt",
        message=message,
        bot=tg)

        f['test'] = 1

    test_kb.send()

names_funcs['testiinline'] = test_func


tg.handlers(list(names_funcs.keys()), list(names_funcs.values()))

tg.start_bot()