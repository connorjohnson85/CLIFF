import ArcReactor.diagonisticsCheck as ARC
import HUD.diagnosticsCheck as HUD
import flightSystems.diagnosticsCheck as flight
import heatdispersionsystems.diagnosticsCheck as hds
import inertialSystems.diagnoisticsCheck as inertia
import repulsorSystems.diagonisticsCheck as repulsor

logFile = open('hardware/project Iron Man/logfile.txt', 'w+')

ArcReactorInfo = ARC.ALL()
RepulsorInfo=repulsor.checkALL()
logFile.write(ArcReactorInfo)
logFile.write(RepulsorInfo)
logFile.write(inertia.checkALL())
logFile.write(HUD.checkALL())
logFile.write(hds.checkALL())
logFile.write(flight.checkAll())
logFile.close()