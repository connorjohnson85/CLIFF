import onedimensionalsimulator.main as onedimensionalsimulator
import rocketsimulations.main as rocketsimulations
import twodimensionalsimulator.main as twodimensionalsimulator

def run():
    print('What would you like to simulate today? ')
    print('one dimensions kinematics(o)')
    print('two dimensionsal kinematics(t)')
    print('rocket simulation(r)')
    answer = input('What would you like to simulate? ').lower()
    if answer == 'o':
        onedimensionalsimulator.run()
    if answer == 't':
        twodimensionalsimulator.run()
    if answer == 'r':
        rocketsimulations.run()