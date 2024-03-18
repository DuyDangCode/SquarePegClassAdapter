class RoundHole:
    def __init__(self, r):
        self.radius = r

    def fits(self, peg):
        if peg.radius < self.radius:
            print("This peg is fit")
        else:
            print("This peg is not fit")
