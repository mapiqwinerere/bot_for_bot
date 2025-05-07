import TgBotMapi as tbm
import sys
import subprocess
from telebot import types

tg = tbm.TgBot('mapi')
user_id = 'mapi'
users_bots = {user_id:'test'}
inline_markup = {}
markup_kb= {}
markup = {}
msgs = {}
word_markup = None
start_kb_sf = False
start_kb_f = False
mode_create = None


def write_funcs_for_markup(name_markup, msg, num, mode, next_step=None):
    global users_bots
    global user_id
    print('mode', mode)
    if mode == 'rm':
        standart_txt = f'''
def {name_markup}_but_{num}(message):
    global tg

    tg.message("{msg}", message)'''
    else:
        
        standart_txt = f'''
def {name_markup}_but_{num}(message):
    global tg

    tg.message_edit("{msg}", message)'''

    if next_step == None and num == 0:
        func = standart_txt + f'''
{name_markup}_dict = {{}}
{name_markup}_dict["{num}"] = {name_markup}_but_{num}
'''
    elif next_step == None and num > 0:
        func = standart_txt + f'''
{name_markup}_dict["{num}"] = {name_markup}_but_{num}
'''

    elif next_step != None and num == 0:
        func = standart_txt + f'''
    names_funcs['{next_step}'](message)
    
{name_markup}_dict = {{}}
{name_markup}_dict["{num}"] = {name_markup}_but_{num}
'''

    elif next_step != None and num > 0:
        func = standart_txt + f'''
    names_funcs['{next_step}'](message)

{name_markup}_dict["{num}"] = {name_markup}_but_{num}
'''
    
    return func

def write_func_markup(name_markup, text, words, row_width, values, word, next_step, message, mode):
    global tg

    print(words)
    print(mode)
    words.pop()
    print('write_func_markup')
    print(name_markup, text, words, row_width, values, word, next_step, mode)
    txt = f'''{name_markup}%%{text}%%{'&'.join(words)}%%{str(row_width)}%%{'&'.join(values)}%%{word}%%{next_step}
$$$
'''
    write_code_instruction(file=r'C:\programming\school_project\users_bots\keyboards_' + str(message.from_user.id) + '.txt' if mode == 'rm' else r'C:\programming\school_project\users_bots\inline_keyboards_' + str(message.from_user.id) + '.txt', 
                           txt=txt)


def write_func_msg(word, text):
    w = word if word[0] != '/' else word[1:]
    return  f'''\ndef {w}_func(message):
    global tg\n
    tg.message('{text}', message)\n
names_funcs['{w}'] = {w}_func
    '''

def write_code(message):
    global users_bots
    global user_id
    global mode_create

    tg.message('Происходит запись кода вашего телеграм-бота...', message)
    #start
    start_part = f'''import TgBotMapi as tbm

tg = tbm.TgBot('{str(message.from_user.id)}')       

f = {{}}
names_funcs = {{}}'''

    end_part =  f'''

tg.handlers(list(names_funcs.keys()), list(names_funcs.values()))

tg.start_bot()'''

    main_part = str()


    #write command function
    words = []
    funcs = []

    with open(r'C:\programming\school_project\users_bots\commands_' + str(message.from_user.id) + '.txt', 'r', encoding='utf-8') as f:
        for s in f.readlines():
            words.append(s.split(' - ')[0])
            funcs.append(s.split(' - ')[1].split('\n')[0])

    for i in range(len(words)):
        main_part += write_func_msg(words[i], funcs[i])

    with open(r'C:\programming\school_project\users_bots\keyboards_' + str(message.from_user.id) + '.txt','r+', encoding='utf-8') as f:
        txt = str()
        for i in f.readlines():
            txt += i
        kbs = list(txt.split('\n$$$\n'))
        for i in kbs:
            if i == '':
                kbs.remove(i)
    try:
        for i in kbs:
            parts = list(i.split(r'%%'))
            try:
                name_markup = parts[0].split('\n')[1]
            except:
                name_markup = parts[0]
            text = parts[1]
            words = list(parts[2].split('&'))
            row_width = parts[3]
            values = list(parts[4].split('&'))
            word = parts[5]
            next_step = parts[6]

            txt_markup = '\n'
            if next_step == "Оставить без следующего шага":
                for i in range(len(values)):
                    txt_markup += write_funcs_for_markup(name_markup = name_markup,
                                       msg = values[i].replace('\n', '-'),
                                       num = i, 
                                       mode = 'rm')

            elif next_step in [_.split(' - ')[0] for _ in open(r'C:\programming\school_project\users_bots\commands_' + str(message.from_user.id) + '.txt', 'r', encoding='utf-8')]:
                for i in range(len(values)):
                    txt_markup += write_funcs_for_markup(name_markup = name_markup,
                                       msg = list(values)[i].replace('\n', '-'),
                                       num = i, 
                                       mode = 'rm',
                                       next_step = next_step)
            else:
                print('error', next_step, parts)                                   
                #tg.message('Приносим извинения, процесс создания клавиатуры прекращён, Вы не корректно ввели слово-активатор.', message)

            main_part += txt_markup

            #create keyboard
            func = f'''
f['{name_markup}'] = 0
def {name_markup}_func(message):
    global {name_markup}_kb
    global f

    if f['{name_markup}'] == 0:
        {name_markup}_kb = tbm.Keyboard(
        buts={words},
        values=list({name_markup}_dict.values()),
        row_width={row_width},
        name="{name_markup}",
        text="{text}",
        message=message,
        bot=tg)

        f['{name_markup}'] = 1

    {name_markup}_kb.send()

names_funcs['{word}'] = {name_markup}_func
'''
            main_part += func


        with open(r'C:\programming\school_project\users_bots\inline_keyboards_' + str(message.from_user.id) + '.txt','r+', encoding='utf-8') as f:
            txt = str()
            for i in f.readlines():
                txt += i
            kbs_inline = list(txt.split('\n$$$\n'))
            for i in kbs_inline:
                if i == '':
                    kbs_inline.remove(i)
        #write keyboard function

        for i in kbs_inline:
            parts_inline = list(i.split(r'%%'))
            try:
                name_markup_inline = parts_inline[0].split('\n')[1]
            except:
                name_markup_inline = parts_inline[0]
            text_inline = parts_inline[1]
            words_inline = list(parts_inline[2].split('&'))
            row_width_inline = parts_inline[3]
            values_inline = list(parts_inline[4].split('&'))
            word_inline = parts_inline[5]
            next_step_inline = parts_inline[6].split('\n')[0]

            txt_inline_markup = '\n'
            if next_step_inline == "Оставить без следующего шага":
                for i in range(len(values_inline)):
                    txt_inline_markup += write_funcs_for_markup(name_markup = name_markup_inline,
                                       msg = values_inline[i].replace('\n', '-'),
                                       num = i, 
                                       mode = 'im')

            elif next_step_inline in [_.split(' - ')[0] for _ in open(r'C:\programming\school_project\users_bots\commands_' + str(message.from_user.id) + '.txt', 'r', encoding='utf-8')]:
                for i in range(len(values_inline)):
                    txt_inline_markup += write_funcs_for_markup(name_markup = name_markup_inline,
                                       msg = list(values_inline)[i],
                                       num = i, 
                                       mode = 'im',
                                       next_step = next_step_inline)
            else:     
                print('next_step_inline', next_step_inline)                              
                tg.message('Приносим извинения, процесс создания клавиатуры прекращён, Вы не корректно ввели слово-активатор.', message)
            main_part += txt_inline_markup

            #create inline keyboard
            func_inline = f'''
f['{name_markup_inline}'] = 0
def {name_markup_inline}_func(message):
    global {name_markup_inline}_kb
    global f

    if f['{name_markup_inline}'] == 0:
        {name_markup_inline}_kb = tbm.InlineKeyboard(
        buts={words_inline},
        values=list({name_markup_inline}_dict.values()),
        row_width={row_width_inline},
        name="{name_markup_inline}",
        text="{text_inline}",
        message=message,
        bot=tg)

        f['{name_markup_inline}'] = 1

    {name_markup_inline}_kb.send()

names_funcs['{word_inline}'] = {name_markup_inline}_func
'''
            main_part += func_inline
    except IndexError:
        pass

    #final
    code = start_part + main_part + end_part
    with open(r'C:\programming\school_project\users_bots\bot_' + str(message.from_user.id) + '.py', 'w', encoding='utf-8') as f:
        f.write(code)
        f.close()

def write_code_instruction(file, txt):
    print('write_code_instruction')
    print(txt)
    with open(file, 'r+', encoding='utf-8') as f:
        if f.readlines() != []:
            f.write(f'\n{txt}')
        else:
            f.write(f'{txt}')

def change_accept_yes(message):
    global tg

    write_code(message)

    tg.message('Изменения применены', message)

    startik(message)
    
def change_accept_no(message): 
    global tg
    global markup

    #markup doing
    tg.message('Изменения пропущены',message)

    startik(message)

def change_accept(message):
    global tg
    global accept_kb

    accept_kb = tbm.Keyboard(name='accept_kb',
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
    global accept_kb

    msgs[list(msgs.keys())[-1]] = message.text
    print('wc')
    write_code_instruction(r'C:\programming\school_project\users_bots\commands_' + str(message.from_user.id) + '.txt', f'{list(msgs.keys())[-1]} - {list(msgs.values())[-1]}')
    
    change_accept(message)

def create_message_func_2(message):
    global tg
    global msgs
    if message.text != '/start':
        msgs[message.text] = None
        tg.message('Введите сообщение, которое будет отправлено при активации команды', message)
        print('wc')

        tg.next_step(create_message_func_total, message)
    else:
        startik(message)

def create_message_func(message):
    global tg
    global start_kb_sf
    global markup
    global mode_create

    print('wc')
    mode_create = 'wc'

    start_kb_sf = False

    tg.message('Введите слово-активатор для команды (к примеру /inf), запишите слово без "/"', message, True)
    tg.next_step(create_message_func_2, message)



def next_markups_func(message, word):
    global tg
    global markup
    print('rm')
    print('REPLY!!!')
    write_func_markup(name_markup = markup[list(markup.keys())[-1]]['name'],
                      text = markup[list(markup.keys())[-1]]['text'],
                      words = markup[list(markup.keys())[-1]]['words'],
                      values = markup[list(markup.keys())[-1]]['values'].values(),
                      word = markup[list(markup.keys())[-1]]['word'], 
                      row_width = markup[list(markup.keys())[-1]]['row_width'], 
                      next_step = word,
                      message = message,
                      mode = 'rm')
    
    change_accept(message)

def create_markup_func_final_4(message):
    global tg
    global markup
    global next_markups_kb
    
    print('rm')
    markup[list(markup.keys())[-1]]['word'] = message.text
    
    cms = [_.split(' - ')[0] for _ in open(r'C:\programming\school_project\users_bots\commands_' + str(message.from_user.id) + '.txt', 'r', encoding='utf-8')]
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
    
    print('rm')
    markup[list(markup.keys())[-1]]['row_width'] = message.text
    tg.message('Введите слово-активатор, при котором будет отправлятьтся данная клавиатура:', message)
    tg.next_step(create_markup_func_final_4, message)

def create_markup_func_final_2(message):
    global tg
    global markup
    
    print('rm')
    markup[list(markup.keys())[-1]]['text'] = message.text
    tg.message('Введите количество кнопок в 1 ряду клавиатуры:', message)
    tg.next_step(create_markup_func_final_3, message)

def create_markup_func_final(message):
    global tg
    
    print('rm')
    tg.message('Введите текст, который будет отправлен при появлении клавитуры:', message, True)
    tg.next_step(create_markup_func_final_2, message)
    
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
        name=f'markup_{markup[list(markup.keys())[-1]]['name']}_kb',
        text='Выберите кнопку, которую хотите назначить (или нажмите "Окончить", в случае заверешения присвоения функций кнопкам)',
        message=message,
        bot=tg
    )

    print('rm')
    markup_kb.send()

def create_markup_func_2(message):
    global markup

    if message.text != '/start':
        markup[message.text] = {}
        tg.message('Введите названия кнопок через энтер: ', message)
        tg.next_step(create_markup_func3, message)
        print('rm')
    else:
        startik(message)

def create_markup_func(message):
    global tg
    global start_kb_sf
    global markup
    global mode_create

    mode_create = 'rm'

    start_kb_sf = False

    print('rm')
    tg.message('Начался процесс ввода параметров для создания клавиатуры под полем ввода. Введите название для вашей клавиатуры: ', message, True)
    tg.next_step(create_markup_func_2, message)


#create inline markups

def next_inline_markups_func(message, word):
    global tg
    print('next_inline_markups_func')
    print('INLINE!!!')
    write_func_markup(name_markup = inline_markup[list(inline_markup.keys())[-1]]['name'],
                      text = inline_markup[list(inline_markup.keys())[-1]]['text'],
                      words = inline_markup[list(inline_markup.keys())[-1]]['buts'],
                      values = inline_markup[list(inline_markup.keys())[-1]]['values'].values(),
                      word = inline_markup[list(inline_markup.keys())[-1]]['word'], 
                      row_width = inline_markup[list(inline_markup.keys())[-1]]['row_width'], 
                      next_step = word, 
                      message = message,
                      mode = 'im')
    
    print('im')
    change_accept(message)


def create_inline_markup_func_7(message):
    global tg

    cms = [_.split(' - ')[0] for _ in open(r'C:\programming\school_project\users_bots\commands_' + str(message.from_user.id) + '.txt', 'r', encoding='utf-8')]
    cms.append('Оставить без следующего шага')

    next_inline_markups_kb = tbm.Keyboard(name='next_markups',
                                   row_width=2,
                                   buts=cms,
                                   values=[lambda message=message, w=w: next_inline_markups_func(message, w) for w in cms],
                                   text='Выберите слово-активатор для следующего шага после нажатия кнопки клавиатуры, либо оставьте без него, нажав соответсвующую кнопку.',
                                   message=message,
                                   bot=tg)
    
    print('im')
    next_inline_markups_kb.send()

def create_func_for_inline_markup_2(message):
    global tg
    global inline_but
    global inline_markup
    global inline_markup_kb

    inline_markup[list(inline_markup.keys())[-1]]['values'][inline_but] = message.text
    tg.message('Ваш запрос принят. Производится возврат в меню конфигурации клавиатуры...', message)
    inline_markup_kb.send()
    

def create_func_for_inline_markup(message, but):
    global tg
    global inline_but

    inline_but = but
    tg.message(f'Введите текст для кнопки "{but}"', message)
    tg.next_step(create_func_for_inline_markup_2, message)

def create_inline_markup_func_6(message):
    global tg
    global inline_markup
    global inline_markup_kb

    buts = list(message.text.split('\n')) 
    inline_markup[list(inline_markup.keys())[-1]]['buts'] =  buts
    inline_markup[list(inline_markup.keys())[-1]]['values'] = {}

    values_jetzt = [(lambda m=message, b=but: create_func_for_inline_markup(m, b)) for but in buts]

    buts.append('Окончить')

    values_jetzt.append(create_inline_markup_func_7)

    print('im')
    inline_markup_kb = tbm.Keyboard(name = f'inline_markup_{inline_markup[list(inline_markup.keys())[-1]]['name']}_kb',
                                    row_width = 2,
                                    buts = buts,
                                    values = values_jetzt,
                                    text = 'Выберите кнопку, которую хотите назначить (или нажмите "Окончить", в случае заверешения присвоения функций кнопкам)',
                                    message = message,
                                    bot = tg)
    
    inline_markup_kb.send()

def create_inline_markup_func_5(message):
    global tg
    global inline_markup

    inline_markup[list(inline_markup.keys())[-1]]['word'] = message.text

    print('im')
    tg.message('Введите названия кнопок через энтер:', message)
    tg.next_step(create_inline_markup_func_6, message)

def create_inline_markup_func_4(message):
    global tg
    global inline_markup

    inline_markup[list(inline_markup.keys())[-1]]['row_width'] = message.text

    print('im')
    tg.message('Введите слово-активатор, при котором будет отправлятьтся данная клавиатура:', message)

    tg.next_step(create_inline_markup_func_5, message)

def create_inline_markup_func_3(message):
    global tg
    global inline_markup

    inline_markup[list(inline_markup.keys())[-1]]['text'] = message.text
    
    print('im')
    tg.message('Введите количество кнопок в 1 ряду клавиатуры:', message)

    tg.next_step(create_inline_markup_func_4, message)

def create_inline_markup_func_2(message):
    global tg
    global inline_markup

    if message.text != '/start':
        name = message.text  
        inline_markup[name] = {}
        inline_markup[name]['name'] = name
        print('im')
        tg.message('Введите текст, который будет отправлен при появлении клавитуры:', message)  
        tg.next_step(create_inline_markup_func_3, message)
    else:
        startik(message)

def create_inline_markup_func(message):
    global tg
    global mode_create

    print('im')
    mode_create = 'im'
    tg.message('Начался процесс ввода параметров для создания клавиатуры под сообщением. Введите название клавиатуры:', message)
    tg.next_step(create_inline_markup_func_2, message)



def registrtion_2(message):
    global tg

    with open(r'C:\programming\school_project\users_bots\users_bot.txt', 'a', encoding='utf-8') as f:
        if f.readlines() != []:
            f.write(f'\n{f'{str(message.from_user.id)} - {message.text}'}')
        else:
            f.write(f'{str(message.from_user.id)} - {message.text}')
    with open(r'C:\programming\school_project\users_bots\bot_' + str(message.from_user.id) + '.py', 'w', encoding='utf-8') as f:
        pass
    with open(r'C:\programming\school_project\users_bots\keyboards_' + str(message.from_user.id) + '.txt', 'w', encoding='utf-8') as f:
        pass
    with open(r'C:\programming\school_project\users_bots\inline_keyboards_' + str(message.from_user.id) + '.txt', 'w', encoding='utf-8') as f:
        pass
    with open(r'C:\programming\school_project\users_bots\commands_' + str(message.from_user.id) + '.txt', 'w', encoding='utf-8') as f:
        pass

    tg.message('Регистрация прошла успешно', message)
    startik(message)

def registration(message):
    global tg
    
    tg.message('Похоже вы новый пользоваетль. Для начала работы необходим API-токен от Вашего телеграм-бота. Для регистрации бота в системе отправьте его API-токен (его нужно взять из @BotFather)', message)
    tg.next_step(registrtion_2, message)


def startik(message: types.Message):
    global start_kb
    global tg
    global start_kb_f
    global start_kb_sf
    global mode_create
    global msgs
    global markup 
    global markup_kb

    if str(message.from_user.id) in [_.split(' - ')[0] for _ in open(r"C:\programming\school_project\users_bots\users_bot.txt", 'r')]:

        mode_create = None

        if start_kb_f == False:

            start_kb = tbm.Keyboard(
                buts=['Создать команду-сообщение', 'Создать клавиатуру под полем ввода', 'Создать клавиатуру под сообщением'],
                values=[create_message_func,  create_markup_func, create_inline_markup_func],
                row_width=2,
                name='start_markup',
                text='Выберите желаемое действие',
                message=message,
                bot=tg
            )

            start_kb.send()

            tg.message('Здравствуйте, данный бот представляет из себя инструмент создания телеграм-ботов текстового назначения (например для создания магазинов)', message, False)

        else:
            if start_kb_sf == False:
                start_kb.send()
            else:
                tg.message('Выберите желаемое действие', message)
            start_kb_sf = bool(start_kb_sf-1)

        start_kb_f = True
    else:
        registration(message)

def start_user_bot(message):
    command = [sys.executable, r'C:\programming\school_project\users_bots\bot_' + str(message.from_user.id) + '.py']
    user_bot = subprocess.Popen(command)

tg.handlers(['start', 'total', 'cerate_comand_word', 'create_reply_markup', 'create_inline_markup', 'start_bot'], 
            [startik, write_code, create_message_func,  create_markup_func, create_inline_markup_func, start_user_bot])

tg.start_bot()