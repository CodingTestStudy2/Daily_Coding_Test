right_dict = {(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1)}
left_dict = {(0,1):(-1,0),(-1,0):(0,-1),(0,-1):(1,0),(1,0):(0,1)}
        
class Solution:
    x = 0
    y = 0
    direction = (0,1)

    def play(self, instructions):
        for i in instructions:
            if i == 'G':
                x_dir, y_dir = self.direction
                self.x += x_dir
                self.y += y_dir
            elif i == 'L':
                self.direction = left_dict[self.direction]
            else:
                self.direction = right_dict[self.direction]

    def isRobotBounded(self, instructions: str) -> bool:
        self.play(instructions)
        for _ in range(4):
            self.play(instructions)
            if self.x ==0 and self.y == 0:
                return True
        
        return False
        