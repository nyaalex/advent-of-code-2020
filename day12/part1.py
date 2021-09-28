class Ship:
    def __init__(self):
        self.bearing = 90
        self.x = 0
        self.y = 0

        self.code_lookup = {
            'N': (0, 1),
            'E': (1, 0),
            'S': (0, -1),
            'W': (-1, 0),
        }

        self.bearing_lookup = {
            0: (0, 1),
            90: (1, 0),
            180: (0, -1),
            270: (-1, 0),
        }

    def read_instr(self, instr):
        code = instr[0]
        val = int(instr[1:])

        if code in self.code_lookup:
            dx, dy = self.code_lookup[code]
            self.x += dx * val
            self.y += dy * val
        elif code == 'R':
            self.bearing = (self.bearing + val) % 360
        elif code == 'L':
            self.bearing = (self.bearing - val) % 360
        else:
            dx, dy = self.bearing_lookup[self.bearing]
            self.x += dx * val
            self.y += dy * val

    def run_file(self, filename):
        file = open(filename)
        for line in file:
            line = line.strip()
            self.read_instr(line)

    def get_dist(self):
        return abs(self.x) + abs(self.y)


if __name__ == '__main__':
    SS_Enterprise = Ship()
    SS_Enterprise.run_file("input")

    print(SS_Enterprise.get_dist())
