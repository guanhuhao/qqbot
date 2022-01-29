from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer ,ChatterBotCorpusTrainer
import os
bot = []
def init():
    global bot
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

#Create a chatbot
def traning():
    trainer = ChatterBotCorpusTrainer(bot)

    trainingSet = './trainingData/'
    # trainingSet = './chinese/'
    # trainingSet = './english/'

    for files in os.listdir(trainingSet):
        trainer.train(trainingSet+files)
        print(trainingSet+files)


def ask(sentence):
    return bot.get_response(sentence)

# init()
# while True:
#     try:
#         user_input = input("1>>> ")
#         bot_response = ask(user_input)
#         print(bot_response)
#     # Press ctrl-c or ctrl-d on the keyboard to exit
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break
