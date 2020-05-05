import Reactor.start as ARC
import HUD.start as HUD
import flightSystems.start as flight
import heatdispersionsystems.start as hds
import inertialSystems.start as inertia
import repulsorSystems.start as repulsor
import delivery.locate as locate
import delivery.start as start

def initialize():
    ARC.startReactor()
    hds.initializeHeatSystems()
    inertia.initializeInertiaSystems()
    repulsor.initalizeRepuslorSystems()
    flight.initalizeFlightSystems()
    HUD.initalizeHeadsUpDisplay()
    
locate.locate()
start.start()
initialize()
