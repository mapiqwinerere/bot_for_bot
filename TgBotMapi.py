import telebot
from telebot import types

keyboards_names = {}
counts = {}
keyboards_types = {}
buts_value = {}
counts_of_kyboards = {}


keyboards_names_i = {}
counts_i = {}
keyboards_types_i = {}
buts_value_i = {}
counts_of_kyboards_i = {}


class InlineKeyboard():
   def __init__(self, name, row_width, buts, values, text, message, bot):
      global buts_value_i
      global keyboards_names_i
      global keyboards_types_i
      global counts_of_kyboards_i
      global keyboards_i

      self.name = name
      self.row_width = row_width
      self.buts = buts
      self.values = values
      self.text = text
      self.message = message
      self.keyboard = types.InlineKeyboardMarkup(row_width= row_width)
      self.bot = bot
      self.len_buts = 0
      self.len_values = 0
      self.count = 0
    
      keyboards_names_i[name] = {}
      keyboards_types_i[name] = [bot, message, text, self.keyboard]
      counts_of_kyboards_i[name] = 0
      bot.markups.append(str(name))

      for but, value in zip(self.buts, self.values):
         callback_data = str(but)  # Используем текст кнопки как callback_data
         but = types.InlineKeyboardButton(text=str(but), callback_data=callback_data)
         self.keyboard.add(but)
         print(self.text, self.text.format(self.message.from_user))
      #self.bot.bot.send_message(message.chat.id,
      #                          self.text.format(self.message.from_user),
      #                          reply_markup=self.keyboard)

      # Добавляем обработчик callback_query
      @self.bot.bot.callback_query_handler(func=lambda call: True)
      def handle_callback_query(call):
         if call.data in self.buts:  # Проверяем, что callback_data соответствует кнопке
            index = self.buts.index(call.data)
            self.values[index](call.message)  # Вызываем соответствующую функцию
   def send(self):
         self.bot.bot.send_message(self.message.chat.id,
                                   text = self.text.format(self.message.from_user),
                                   reply_markup=self.keyboard)

def write_token(bot, token):
    with open('tokens.txt', 'a') as file:
       text_for_write = bot + ' ' + token + "\n"
       file.write(text_for_write)
       file.close()

def send_keyboard(keyboard):
    global keyboards_types
    args_for_markup = keyboards_types.get(keyboard)
    args_for_markup[0].bot.send_message(args_for_markup[1].chat.id,
                                    text = args_for_markup[2].format(args_for_markup[1].from_user),
                                    reply_markup=args_for_markup[3])


class Keyboard():
   def __init__(self, name, row_width, buts, values, text, message, bot, send_or_not=False):
      global buts_value
      global keyboards_names
      global keyboards_types
      global counts_of_kyboards
      global keyboards

      self.name = name
      self.row_width = row_width
      self.buts = buts
      self.value = values
      self.text = text
      self.send_or_not = send_or_not
      self.message = message
      self.keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
      self.bot = bot
      self.len_buts = 0
      self.len_values = 0
      self.count = 0
    
      keyboards_names[name] = {}
      keyboards_types[name] = [bot, message, text, self.keyboard]
      counts_of_kyboards[name] = 0
      bot.markups.append(str(name))

      if self.len_buts == 0:
         for but in self.buts:
            bot.buts.append(but)
            keyboards_names[name]['but_' + str(but)] = types.KeyboardButton(text = str(but))
         self.len_buts += 1

      if self.len_values == 0:
         for value in self.value:
            bot.values.append(value)
         self.len_values += 1

      for i in range(len(self.buts)):
          buts_value[buts[i]] = self.value[i]

      self.keyboard.add(*list(keyboards_names[name].values()))
      if self.send_or_not and self.count == 0:
         self.send()
         self.count += 1

   def send(self):
         self.bot.bot.send_message(self.message.chat.id,
                                   text = self.text.format(self.message.from_user),
                                   reply_markup=self.keyboard)
       
class TgBot():
    def __init__(self, name_bot): 
        global bot
        global token

        bots_list = []
        bots_dict = {}

        with open('tokens.txt', 'r') as file:
           for i in file.readlines():
              bots_list.append(str(i.split()[0]))
              bots_dict[str(i.split()[0])] = str(i.split()[1])
           
        for bot in bots_list:
            if name_bot == bot:
               self.bot = telebot.TeleBot(bots_dict[name_bot])

        
        self.buts = []
        self.values = []
        self.markups = []
    
    def check_function(self):
       @self.bot.message_handler(content_types='text')
       def check_2(message):
          global buts_value
          for but in self.buts:
             if(message.text == but):
                buts_value.get(but)(message)

    def start_bot(self):
       self.check_function()
       self.bot.polling(timeout=120)
       
    def message(self, text, message, remove_markup=False):
        if remove_markup == False:
         self.bot.send_message(message.chat.id, text)
        else:
         self.bot.send_message(message.chat.id, text, reply_markup=types.ReplyKeyboardRemove()) 
 
    def handlers(self, words, funcs):
       global command
       for i in range(len(words)):
          self.handler(words[i], funcs[i])         
           
    def handler(self, word, user_function, *args):
       global command
       
       @self.bot.message_handler(commands=[word])
       def command(message):
           
           user_function(*args, message)

    def keyboard_hadler(self, word, func, keyboard):
       global command
       global counts

       counts[word] = 0
       @self.bot.message_handler(commands=[word])
       def command(message):
           if counts[word] == 0:
              func(message)
              counts[word] += 1
           else: 
              send_keyboard(keyboard)
              
    def next_step(self, func, message):
         self.bot.register_next_step_handler(message=message, callback=func)
