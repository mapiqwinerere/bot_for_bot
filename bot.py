import TgBotMapi as tbm

tg = tbm.TgBot('test')       

f = {}
names_funcs = {}
def mazucht_func(message):
    global tg

    tg.message('unzucht', message)

names_funcs['mazucht'] = mazucht_func
    
def deutschebahn_func(message):
    global tg

    tg.message('hallo meine lieblings Menschen', message)

names_funcs['deutschebahn'] = deutschebahn_func
    

def mapi_one(message):
    global tg

    tg.message("Haus", message, True)
    names_funcs['mazucht'](message)

mapi_dict = {}
mapi_dict["one"] = mapi_one

def mapi_two(message):
    global tg

    tg.message("Eps", message, True)
    names_funcs['mazucht'](message)

mapi_dict["two"] = mapi_two

def mapi_three(message):
    global tg

    tg.message("Robert", message, True)
    names_funcs['mazucht'](message)

mapi_dict["three"] = mapi_three

f['mapi'] = 0
def mapi_func(message):
    global mapi_kb
    global f

    if f['mapi'] == 0:
        mapi_kb = tbm.Keyboard(
        buts=list(mapi_dict.keys()),
        values=list(mapi_dict.values()),
        row_width=2,
        name="mapi",
        text="Актёры Хауса",
        send_or_not=False,
        message=message,
        bot=tg)

        f['mapi'] = 1

    mapi_kb.send()

names_funcs['mapiqwinerere'] = mapi_func


def mazucht_eins(message):
    global tg

    tg.message("eins", message, True)
    names_funcs['mazucht'](message)

mazucht_dict = {}
mazucht_dict["eins"] = mazucht_eins

def mazucht_zwei(message):
    global tg

    tg.message("zwei", message, True)
    names_funcs['mazucht'](message)

mazucht_dict["zwei"] = mazucht_zwei

def mazucht_drei(message):
    global tg

    tg.message("drei", message, True)
    names_funcs['mazucht'](message)

mazucht_dict["drei"] = mazucht_drei

f['mazucht'] = 0
def mazucht_func(message):
    global mazucht_kb
    global f

    if f['mazucht'] == 0:
        mazucht_kb = tbm.Keyboard(
        buts=list(mazucht_dict.keys()),
        values=list(mazucht_dict.values()),
        row_width=3,
        name="mazucht",
        text="Wie geht es dir?",
        send_or_not=False,
        message=message,
        bot=tg)

        f['mazucht'] = 1

    mazucht_kb.send()

names_funcs['deutsch'] = mazucht_func


def kb_erste(message):
    global tg

    tg.message("erste", message, True)
kb_dict = {}
kb_dict["erste"] = kb_erste

def kb_zwitte(message):
    global tg

    tg.message("zwitte", message, True)
kb_dict["zwitte"] = kb_zwitte

def kb_dritte(message):
    global tg

    tg.message("dritte", message, True)
kb_dict["dritte"] = kb_dritte

f['kb'] = 0
def kb_func(message):
    global kb_kb
    global f

    if f['kb'] == 0:
        kb_kb = tbm.Keyboard(
        buts=list(kb_dict.keys()),
        values=list(kb_dict.values()),
        row_width=2,
        name="kb",
        text="textik",
        send_or_not=False,
        message=message,
        bot=tg)

        f['kb'] = 1

    kb_kb.send()

names_funcs['wort'] = kb_func


tg.handlers(list(names_funcs.keys()), list(names_funcs.values()))

tg.start_bot()