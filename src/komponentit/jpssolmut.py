class Jpssolmu:

    # Määrittelee JPS:n käyttämien "solmujen" rakenteen.

    def __init__(self, koordinaatit, tyyppi):
        self.koordinaatit = koordinaatit
        self.tyyppi = tyyppi
        self.naapurit = []
        self.luonnolliset = []
        self.pakolliset = []
        self.seuraajat = []
        self.edellinen = None