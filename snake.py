class Computer:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0 

    def __init__(self, length):
        self.length = length
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)
        
        self.x[0] = 1*44
        self.y[0] = 4*44

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount &gt; self.updateCountMax:

            for i in range(self.lenght-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

                if self.direction == 0:
                    self.x[0] = self.x[0] + self.step
                if self.direction == 1:
                    self.x[0] = self.x[0] - self.step
                if self.direction == 2:
                    self.y[0] = self.y[0] - self.step
                if self.direction == 3:
                    self.y[0] = self.y[0] - self.step
        
        
        self.updateCount = 0

veRight(self):
if.direction = 0 

veLeft(self):
if.direction = 1

veUp(self):
if.direction = 2

veDown(self):
if.direction = 3

aw(self, surface, image):
r in range(0, self.length):
    surface.blit(image,(self.x[i], self.y[i]))

def on_loop(self):
    self.player.update()
    self.Computer.update(
    )


    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surg)
        self.apple.draw(self._display_surf, self._apple_surf)
        self.computer.draw(self._display_surf, self._image_surf)
        pygame.display.flip()
def target(self,dx,dy):
    if self.x[0] &gt; dx:
        self.moveLeft()

    if self.x[0] &lt; dx:
        self.moveRight()

    if self.x[0] == dx:
        self.moveDown()

    if self.y[0] &gt; dy:
        self.moveUp()
        