from RoundPeg import RoundPeg
from RoundHole import  RoundHole
from SquarePegAdapter import SquarePegAdapter

if __name__ == '__main__':
    roundHole = RoundHole(5)
    roundPeg = RoundPeg(6)
    suarePegAdapter = SquarePegAdapter(5)

    roundHole.fits(roundPeg)
    roundHole.fits(suarePegAdapter)