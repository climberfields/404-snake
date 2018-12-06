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
