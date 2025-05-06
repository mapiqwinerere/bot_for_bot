import TgBotMapi as tbm
from os import path

def write_funcs_for_markup(name_markup, word, msg, num, next_step=None):
    global users_bots
    global user_id

    standart_txt = f'''
def {name_markup}_{word}(message):
    global tg

    tg.message("{msg}", message, True)'''

    if next_step == None and num == 0:
        func = standart_txt + f'''
{name_markup}_dict = {{}}
{name_markup}_dict["{word}"] = {name_markup}_{word}
'''
    elif next_step == None and num > 0:
        func = standart_txt + f'''
{name_markup}_dict["{word}"] = {name_markup}_{word}
'''

    elif next_step != None and num == 0:
        func = standart_txt + f'''
    names_funcs['{next_step}'](message)

{name_markup}_dict = {{}}
{name_markup}_dict["{word}"] = {name_markup}_{word}
'''
    elif next_step != None and num > 0:
        func = standart_txt + f'''
    names_funcs['{next_step}'](message)

{name_markup}_dict["{word}"] = {name_markup}_{word}
'''
    
    return func

def write_func_markup(name_markup, text, words, row_width, values, word, next_step):
    global tg

    words.pop()

    txt = f'''{name_markup}
{text}
{' '.join(words)}
{str(row_width)}
{' '.join(values)}
{word}
{next_step}
'''

    write_code_instruction(file=r"C:\Users\toleg\programming\school_project\keyboards.txt", txt=txt)


def write_func_msg(word, text):
    return  f'''\ndef {word}_func(message):
    global tg\n
    tg.message('{text}', message)\n
names_funcs['{word}'] = {word}_func
    '''

def write_code(message):
    global users_bots
    global user_id
    global mode_create

    print('total')
    #start
    start_part = f'''import TgBotMapi as tbm

tg = tbm.TgBot('{users_bots[user_id]}')       

f = {{}}
names_funcs = {{}}'''

    end_part =  f'''

tg.handlers(list(names_funcs.keys()), list(names_funcs.values()))

tg.start_bot()'''

    main_part = str()


    #write command function
    words = []
    funcs = []

    with open(r'C:\Users\toleg\programming\school_project\commands.txt', 'r', encoding='utf-8') as f:
        for s in f.readlines():
            words.append(s.split(' - ')[0])
            funcs.append(s.split(' - ')[1].split('\n')[0])

    for i in range(len(words)):
        main_part += write_func_msg(words[i], funcs[i])

    keyboards = [[]]
    with open(r'C:\Users\toleg\programming\school_project\keyboards.txt','r+', encoding='utf-8') as f:
        for i in f.readlines():
            if i != '\n':
                keyboards[-1].append(i.split('\n')[0])
            else:
                keyboards.append([])
    print(keyboards)
    for i in keyboards:
    #write keyboard function
        name_markup = i[0]
        text = i[1]
        words = i[2].split()
        row_width = i[3]
        values = i[4].split()
        word = i[5]
        next_step = i[6]
        print(f'''{name_markup}
{text}
{words}
{row_width}
{values}
{word}
{next_step}''')
        txt_markup = '\n'

        if next_step == "Оставить без следующего шага":
            for i in range(len(values)):
                txt_markup += write_funcs_for_markup(name_markup = name_markup,
                                   word = words[i],
                                   msg = values[i],
                                   num = i)

        elif next_step in [_.split(' - ')[0] for _ in open(r'C:\Users\toleg\programming\school_project\commands.txt', 'r')]:
            for i in range(len(values)):
                txt_markup += write_funcs_for_markup(name_markup = name_markup,
                                   msg = list(values)[i],
                                   word = words[i],
                                   num = i,
                                   next_step = next_step)
                print('total if')
        else:                                   
            tg.message('Приносим извинения, процесс создания клавиатуры прекращён, Вы не корректно ввели слово-активатор.', message)

        main_part += txt_markup

        #create keyboard
        func = f'''
f['{name_markup}'] = 0
def {name_markup}_func(message):
    global {name_markup}_kb
    global f

    if f['{name_markup}'] == 0:
        {name_markup}_kb = tbm.Keyboard(
        buts=list({name_markup}_dict.keys()),
        values=list({name_markup}_dict.values()),
        row_width={row_width},
        name="{name_markup}",
        text="{text}",
        send_or_not=False,
        message=message,
        bot=tg)

        f['{name_markup}'] = 1

    {name_markup}_kb.send()

names_funcs['{word}'] = {name_markup}_func
'''
        main_part += func

    #final
    code = start_part + main_part + end_part
    with open(r'C:\Users\toleg\programming\school_project\bot.py', 'w', encoding='utf-8') as f:
        f.write(code)
        f.close()

def write_code_instruction(file, txt):
    with open(file, 'r+', encoding='utf-8') as f:
        if f.readlines() != []:
            f.write(f'\n{txt}')
        else:
            f.write(f'{txt}')
        f.close()

tg = tbm.TgBot('mapi')
user_id = 'mapi'
users_bots = {user_id:'test'}
markup = {}
msgs = {}
word_markup = None
start_kb_sf = False
start_kb_f = False
mode_create = None

def change_accept_yes(message):
    global tg

    write_code(message)

    tg.message('Изменения применены', message)

    startik(message)
    
def change_accept_no(): pass

def change_accept(message):
    global tg
    global accept_kb

    accept_kb = tbm.Keyboard(name='accept',
                             row_width=2,
                             buts=['Да', 'Нет'],
                             values=[change_accept_yes, change_accept_no],
                             text='Внести изменения в бота?',
                             message=message,
                             bot=tg)

    accept_kb.send()

def create_message_func_total(message):
    global tg
    global msgs

    msgs[list(msgs.keys())[-1]] = message.text
    write_code_instruction(r'C:\Users\toleg\programming\school_project\commands.txt', f'{list(msgs.keys())[-1]} - {list(msgs.values())[-1]}')

    startik(message)

def create_message_func_2(message):
    global tg
    global msgs
    if message.text != '/start':
        msgs[message.text] = None
        tg.message('Введите сообщение, которое будет отправлено при активации команды', message)

        tg.next_step(create_message_func_total, message)
    else:
        startik()

def create_message_func(message):
    global tg
    global start_kb_sf
    global markup
    global mode_create

    mode_create = 'wc'

    start_kb_sf = False

    tg.message('Введите слово-активатор для команды (к примеру /inf), запишите слово без "/"', message, True)
    tg.next_step(create_message_func_2, message)



def create_func_for_markup2(message):
    global tg
    global markup_kb
    global markup

    markup[list(markup.keys())[-1]]['values'][word_markup] = message.text
    tg.message('Ваш запрос принят. Производится возврат в меню конфигурации клавиатуры...', message)

    markup_kb.send()

def create_func_for_markup(message, word):
    global tg
    global word_markup
    
    word_markup = word

    tg.message(f'Введите текст для кнопки "{word_markup}"', message, True)
    tg.next_step(create_func_for_markup2, message)


def next_markups_func(message, word):
    global tg
    global markup
    
    
    write_func_markup(name_markup = markup[list(markup.keys())[-1]]['name'],
                      text = markup[list(markup.keys())[-1]]['text'],
                      words = markup[list(markup.keys())[-1]]['words'],
                      values = markup[list(markup.keys())[-1]]['values'],
                      word = markup[list(markup.keys())[-1]]['word'], 
                      row_width = markup[list(markup.keys())[-1]]['row_width'], 
                      next_step = word)
    
    change_accept(message)
    #tg.next_step(change_accept, message)

def create_markup_func_final_4(message):
    global tg
    global markup
    global next_markups_kb

    markup[list(markup.keys())[-1]]['word'] = message.text
    
    cms = [_.split(' - ')[0] for _ in open(r'C:\Users\toleg\programming\school_project\commands.txt', 'r')]
    cms.append('Оставить без следующего шага')

    next_markups_kb = tbm.Keyboard(name='next_markups',
                                   row_width=2,
                                   buts=cms,
                                   values=[lambda message=message, w=w: next_markups_func(message, w) for w in cms],
                                   text='Выберите слово-активатор для следующего шага после нажатия кнопки клавиатуры, либо оставьте без него, нажав соответсвующую кнопку.',
                                   message=message,
                                   bot=tg)
    
    next_markups_kb.send()

def create_markup_func_final_3(message):
    global tg
    global markup

    markup[list(markup.keys())[-1]]['row_width'] = message.text
    tg.message('Введите слово-активатор, при котором будет отправлятьтся данная клавиатура:', message)
    tg.next_step(create_markup_func_final_4, message)

def create_markup_func_final_2(message):
    global tg
    global markup

    markup[list(markup.keys())[-1]]['text'] = message.text
    tg.message('Введите количество кнопок в 1 ряду клавиатуры:', message)
    tg.next_step(create_markup_func_final_3, message)

def create_markup_func_final(message):
    global tg

    tg.message('Введите текст, который будет отправлен при появлении клавитуры:', message, True)
    tg.next_step(create_markup_func_final_2, message)
    

def create_markup_func3(message):
    global markup
    global markup_kb

    words = list(message.text.split('\n'))
    values_jetzt = [(lambda m=message, w=word: create_func_for_markup(m, w)) for word in words]

    markup[list(markup.keys())[-1]]['name'] = list(markup.keys())[-1]
    markup[list(markup.keys())[-1]]['words'] = words
    markup[list(markup.keys())[-1]]['values'] = {}
    
    words.append('Окончить')
    values_jetzt.append(create_markup_func_final)
  
    markup_kb = tbm.Keyboard(
        buts=words,
        values=values_jetzt,  
        row_width=2,
        name='start_markup',
        text='Выберите кнопку, которую хотите назначить',
        message=message,
        bot=tg
    )

    markup_kb.send()

def create_markup_func_2(message):
    global markup

    if message.text != '/start':
        markup[message.text] = {}
        tg.message('Введите названия кнопок через энтер: ', message)
        tg.next_step(create_markup_func3, message)
    else:
        startik()

def create_markup_func(message):
    global tg
    global start_kb_sf
    global markup
    global mode_create

    mode_create = 'rm'

    start_kb_sf = False

    tg.message('Начался процесс ввода параметров для создания клавиатуры. Введите название для вашей клавиатуры: ', message, True)
    tg.next_step(create_markup_func_2, message)



def startik(message):
    global start_kb
    global tg
    global start_kb_f
    global start_kb_sf
    global mode_create
    global msgs
    global markup

    mode_create = None
    #msgs = {}
    #markup = {}

    if start_kb_f == False:
        
        start_kb = tbm.Keyboard(
            buts=['Создать команду-сообщение', 'Создать клавиатуру'],
            values=[create_message_func,  create_markup_func],
            row_width=2,
            name='start_markup',
            text='Выберите желаемое действие',
            message=message,
            bot=tg
        )
        
        start_kb.send()

        tg.message('Здравствуйте, данный бот представляет из себя инструмент создания телеграм-ботов текстового назначения (например для создания магазинов)', message)

    else:
        if start_kb_sf == False:
            start_kb.send()
        else:
            tg.message('Выберите желаемое действие', message)
        start_kb_sf = bool(start_kb_sf-1)
    
    start_kb_f = True

tg.handlers(['start', 'total'], [startik, write_code])

tg.start_bot()