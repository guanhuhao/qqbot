init()
while True:
    try:
        user_input = input("1>>> ")
        bot_response = ask(user_input)
        print(bot_response)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
