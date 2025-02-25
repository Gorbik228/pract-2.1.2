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
    
    def flying_range(self, n):
        if self.flying_ability is False:
            print(self.name,'не летает')
        else:
            print(self.name, (self.size * n),'летает')


birds1 = Birds("Папагай",True , 20)
birds2 = Birds ("Птичка",False, 20)
birds1.flying_range(10)
birds2.flying_range(10)