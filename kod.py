class Birds:
    
    def __init__(self, name, flying_ability, size ):
        self.name = name
        self.flying_ability = flying_ability
        self.size = size

    def souding(self):
        print(self.name, 'будет петь')

    def eating(self):
        print(self.name, 'будет есть')

    def sleeping(self):
        print(self.name, 'будет спать')

    def __del__(self):
        print(self.name,'удален')


Birds1 = Birds("Папагай",True , 20)
