import greeting
import run

mode = input('Mode (production, testing, silent): ')
if mode == 'production':
    name = greeting.greetproduction()
if mode == 'testing':
    name = greeting.greettest()
if mode == 'silent': 
    name = greeting.greetsilent()
run.run(name, mode)


