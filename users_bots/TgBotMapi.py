import telebot
from telebot import types

def write_token(bot, token):
    with open('tokens.txt', 'a') as file:
       text_for_write = bot + ' ' + token + "\n"
       file.write(text_for_write)
       file.close()

class InlineKeyboard():
   def __init__(self, name, row_width, buts, values, text, message, bot):
      self.name = name
      self.buts = buts
      self.values = values
      self.text = text
      self.message = message
      self.keyboard = types.InlineKeyboardMarkup(row_width=row_width)
      self.bot = bot.bot
      self.actions = {}

      bot.markups[self.name] = self
      print('markups',bot.markups)
      btns = []
      for i, (but, value) in enumerate(zip(self.buts, self.values)):
         identification = f'{self.name}_{i}'
         btn = types.InlineKeyboardButton(text=str(but), callback_data=identification)
         btns.append(btn)
         self.actions[identification] = value

      self.keyboard.add(*btns)
      print(bot.markups)

   def get_action(self, id):
      return self.actions.get(id)

   def send(self):
         self.bot.active_markup = self
         self.bot.send_message(self.message.chat.id,
                                   text = self.text.format(self.message.from_user),
                                   reply_markup=self.keyboard)

class Keyboard():
   def __init__(self, name, row_width, buts, values, text, message, bot):
    self.bot = bot
    self.name = name
    if bot.markups.get(name) == None:
      self.bot = bot
      self.row_width = row_width
      self.buts = buts
      self.values = values
      self.text = text
      self.message = message
      self.keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
      self.actions = {}
      self.signal_reply = []
    
      bot.markups[self.name] = self

      btns = []
      for but, value in zip(self.buts, self.values):
         btn = types.KeyboardButton(text=str(but))
         btns.append(btn)
         bot.signals_reply.append(str(but))
         self.actions[f'{self.name}_{but}'] = value
         
      self.keyboard.add(*btns)

   def get_action(self, id):
      return self.actions.get(id)
   
   def send(self):
      kb = self.bot.markups.get(self.name)
      self.bot.active_markup = kb     
      self.bot.bot.send_message(kb.message.chat.id,
                                text = kb.text.format(kb.message.from_user),
                                reply_markup = kb.keyboard)
       
class TgBot():
    def __init__(self, name_bot): 
        bots_list = []
        bots_dict = {}

        with open(r'C:\programming\school_project\users_bots\users_bot.txt', 'r') as file:
           for i in file.readlines():
              bots_list.append(str(i.split(' - ')[0]))
              bots_dict[str(i.split()[0])] = str(i.split(' - ')[1])
           
        for bot in bots_list:
            if name_bot == bot:
               self.bot = telebot.TeleBot(bots_dict[name_bot])

        self.active_markup = None
        self.markups = {}
        self.signals_reply = []

    def check_function(self):
       print(self.markups)
       @self.bot.callback_query_handler(func= lambda call: True)
       def check_1(call):
          name = call.data[:-len(call.data.split('_')[-1])-1]
          print('name', name)
          print('ans', self.markups)
          kb = self.markups.get(name)
          kb.get_action(call.data)(call)

       @self.bot.message_handler(func= lambda message: message.text in self.signals_reply)
       def check_2(message):
          name = self.active_markup.name
          kb = self.markups.get(name)
          kb.get_action(f'{name}_{message.text}')(message)

    def start_bot(self):
       self.check_function()
       self.bot.polling(timeout=120)
       
    def message(self, text, message, remove_markup=True):
        if remove_markup == True:
         self.bot.send_message(message.chat.id, text, reply_markup=types.ReplyKeyboardRemove()) 
        else:
         self.bot.send_message(message.chat.id, text)

    def message_edit(self, text, call):
         self.bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
         
    def handlers(self, words, funcs):
       for i in range(len(words)):
          self.handler(words[i], funcs[i])         
           
    def handler(self, word, user_function, *args):
       @self.bot.message_handler(commands=[word])
       def command(message):
           user_function(*args, message)

    def next_step(self, func, message):
         self.bot.register_next_step_handler(message=message, callback=func)