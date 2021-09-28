import part1


class Waypoint(part1.Ship):

    def __init__(self):
        super().__init__()

        self.waypoint_x = 10
        self.waypoint_y = 1
        self.rotate_lookup = {
            90: (0,1,-1,0),
            180: (-1,0,0,-1),
            270: (0,-1,1,0),
        }

    def read_instr(self, instr):
        code = instr[0]
        val = int(instr[1:])

        if code in self.code_lookup:
            dx, dy = self.code_lookup[code]
            self.waypoint_x += dx * val
            self.waypoint_y += dy * val
        elif code == 'R':
            self.rotate_waypoint(val)
        elif code == 'L':
            self.rotate_waypoint(-val)
        else:
            self.x += self.waypoint_x * val
            self.y += self.waypoint_y * val

    def rotate_waypoint(self, val):
        val %= 360
        a, b, c, d = self.rotate_lookup[val]
        new_x = a * self.waypoint_x + b * self.waypoint_y
        new_y = c * self.waypoint_x + d * self.waypoint_y

        self.waypoint_x, self.waypoint_y = new_x, new_y


if __name__ == '__main__':
    SS_Enterprise = Waypoint()
    SS_Enterprise.run_file("input")

    print(SS_Enterprise.get_dist())
