class element:
    def __init__(self, atomicName, atomicMass, atomicNumber, atomicSymbol):
        self.atomicName = atomicName
        self.atomicMass = atomicMass
        self.atomicNumber = atomicNumber
        self.atomicSymbol = atomicSymbol
    def massToMoles(self, amount):
        return amount/self.atomicMass
    def molesToMass(self, amount):
        return self.atomicMass*amount
    def litersToMoles(amount):
        return amount/22.4
    def molesToLiters(amount):
        return(22.4 * amount)
    def particlesToMoles(self, amount):
        return(amount/6.03*-10**23)

    def __repr__(self):
        return 'Element: {0} Symbol: {1} Number: {2}'.format(self.atomicName, self.atomicSymbol, self.atomicNumber)
 
hydrogen = element('Hydrogen', 1.00794, '1', 'H'),
helium = element('Helium', 4.002602, '2', 'He'),
lithium = element('Lithium', 6.941, '3', 'Li'),
beryllium = element('Beryllium', 9.0122, '4', 'Be'),
boron = element('Boron', 10.811, '5', 'B'),
carbon = element('Carbon', 12.0107, '6', 'C'),
nitrogen = element('Nitrogen', 14.0067, '7', 'N'),
oxygen = element('Oxygen', 15.9994, '8', 'O'),
flourine = element('Flourine', 18.9984, '9', 'F'),
neon = element('Neon', 20.1797, '10', 'Ne'),
sodium = element('Sodium', 22.9897, '11', 'Na'),
magnesium = element('Magnesium', 24.305, '12', 'Ma'),
alumninum = element('Aluminum', 26.9815, '13', 'Al'),
silicon = element('Silicon', 28.0855, '14', 'Si'),
phosphourous = element('Phosphourous', 30.9738, '15', 'P')
sulfur = element('Sulfur', 32.065, '16', 'S')
Chlorine = element('Chlorine', 35.453, '17', 'Cl')
Potassium = element('Potassium', 39.0983, '19', 'K')
Argon = element('Argon', 39.948, '18', 'Ar')
calcium = element('Calcium', 40.078, '20', 'Ca')
scandium = element('Scandium', 44.9559, '21', 'Sc')
Titanium = element('Titanium', 47.867, '22', 'Ti')
Vanadium = element('Vanadium', 50.9415, '23', 'V')
Chromium = element('Chromium', 51.9961, '24', 'Cr')
Manganese = element('Manganese', 54.938, '25', 'Mn')
elements = '''55.845 Iron Fe 26 }58.6934 Nickel Ni 28 }58.9332 Cobalt Co 27 }63.546 Copper Cu 29 }65.39 Zinc Zn 30 }69.723 Gallium Ga 31 }72.64 Germanium Ge 32 }74.9216 Arsenic As 33 }78.96 Selenium Se 34 }79.904 Bromine Br 35 }83.8 Krypton Kr 36 }85.4678 Rubidium Rb 37 }87.62 Strontium Sr 38 }88.9059 Yttrium Y 39 }91.224 Zirconium Zr 40 }92.9064 Niobium Nb 41 }95.94 Molybdenum Mo 42 }98 Technetium Tc 43 }101.07 Ruthenium Ru 44 }102.9055 Rhodium Rh 45 }106.42 Palladium Pd 46 }107.8682 Silver Ag 47 }112.411 Cadmium Cd 48 }114.818 Indium In 49 }118.71 Tin Sn 50 }121.76 Antimony Sb 51 }126.9045 Iodine I 53 }127.6 Tellurium Te 52 }131.293 Xenon Xe 54 }132.9055 Cesium Cs 55 }137.327 Barium Ba 56 }138.9055 Lanthanum La 57 }140.116 Cerium Ce 58 }140.9077 Praseodymium Pr 59 }144.24 Neodymium Nd 60 }145 Promethium Pm 61 }150.36 Samarium Sm 62 }151.964 Europium Eu 63 }157.25 Gadolinium Gd 64 }158.9253 Terbium Tb 65 }162.5 Dysprosium Dy 66 }164.9303 Holmium Ho 67 }167.259 Erbium Er 68 }168.9342 Thulium Tm 69 }173.04 Ytterbium Yb 70 }174.967 Lutetium Lu 71 }178.49 Hafnium Hf 72 }180.9479 Tantalum Ta 73 }183.84 Tungsten W 74 }186.207 Rhenium Re 75 }190.23 Osmium Os 76 }192.217 Iridium Ir 77 }195.078 Platinum Pt 78 }196.9665 Gold Au 79 }200.59 Mercury Hg 80 }204.3833 Thallium Tl 81 }207.2 Lead Pb 82 }208.9804 Bismuth Bi 83 }209 Polonium Po 84 }210 Astatine At 85 }222 Radon Rn 86 }223 Francium Fr 87 }226 Radium Ra 88 }227 Actinium Ac 89 }231.0359 Protactinium Pa 91 }232.0381 Thorium Th 90 }237 Neptunium Np 93 }238.0289 Uranium U 92 }243 Americium Am 95 }244 Plutonium Pu 94 }247 Curium Cm 96 }247 Berkelium Bk 97 }251 Californium Cf 98 }252 Einsteinium Es 99 }257 Fermium Fm 100 }258 Mendelevium Md 101 }259 Nobelium No 102 }261 Rutherfordium Rf 104 }262 Lawrencium Lr 103 }262 Dubnium Db 105 }264 Bohrium Bh 107 }266 Seaborgium Sg 106 }268 Meitnerium Mt 109 }272 Roentgenium Rg 111 }277 Hassium Hs 108'''.split('}')
print(elements)

NewElements = [hydrogen, helium, lithium, beryllium, boron, carbon, nitrogen, oxygen, flourine, neon, sodium, magnesium, alumninum, silicon, phosphourous, sulfur]
for item in elements:
    elementList = []
    for newItem in item.split(' '):
        if newItem != '':
            elementList.append(newItem)
    NewElements.append(element(elementList[1], elementList[0], elementList[3], elementList[2]))
print(NewElements)

# Returns a list of all the elements
def periodicTable():
    return NewElements
