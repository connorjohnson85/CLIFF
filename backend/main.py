import greeting
import run

# Main function. Start of program. Gets mode, then runs greeting function to get the users name
mode = input('Mode (production, testing, silent): ')
if mode == 'production':
    name = greeting.greetproduction()
if mode == 'testing':
    name = greeting.greettest()
if mode == 'silent':
    name = greeting.greetsilent()

# forwards input into the run function
run.run(name, mode)


