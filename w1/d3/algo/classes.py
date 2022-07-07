class Phone:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    def info(self):
        print(f"color: {self.color}")
        print(f"weight: {self.weight}")
        return self
    def call(self, number):
        print(f"calling {number}")
        return self
    def ring(self):
        print("ringing ringing ringing")
        return self
    def hang_up(self):
        print("hanging up")
        return self

class CellPhone( Phone ):#superceeding class is Phone
    def __init__(self, color, weight):
        super().__init__(color, weight)# will use variables from the superceeding class
        self.type = "cell phone"
    def info(self):
        super().info()
        print(f"type: {self.type}")
        return self
    def text(self, number, msg):
        print(f"sending {number} the message: {msg}")
        return self

class FlipCellPhone( CellPhone ):
    def __init__(self, color, weight):
        super().__init__(color, weight)
        self.flip_status = "close"
    def info(self):
        super().info()
        print(f"flipped status: {self.flip_status}")
        return self
    def flipped_closed(self):
        self.flip_status = "closed"
        return self
    def flipped_open(self):
        self.flip_status = "open"
        return self
    def call(self, number): #this will only aply to flip phones as its a sub class
        if self.flip_status == "closed":
            print("must open phone first")
        else:
            super().call(number)
        return self


phone1 = FlipCellPhone("blue", 5)
phone1.info().flipped_open().call(1234567890).text(1234567890, "Just sending this as a reminder")