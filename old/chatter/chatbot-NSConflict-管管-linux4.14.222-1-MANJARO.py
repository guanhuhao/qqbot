# -*- coding: UTF-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer ,ChatterBotCorpusTrainer
import os
bot = ChatBot(
   'Sakura',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        # 'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='mongodb://localhost:27017/chatbot'
)
# trainer = ListTrainer(bot)

# trainer.train(conversation)

#Create a chatbot
trainer = ChatterBotCorpusTrainer(bot)
#training on english dataset
trainingSet = './trainingData/'
# trainingSet = './chinese/'
# trainingSet = './english/'

# for files in os.listdir(trainingSet):
#     trainer.train(trainingSet+files)
#     print(trainingSet+files)

while True:
    try:
        user_input = input(">>> ")
        bot_response = bot.get_response(user_input)
        print(bot_response)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
