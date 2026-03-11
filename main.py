class MenuItem:
    def __init__(self, name, description, category, is_available):
        self.name = name
        self.description = description
        self.category = category
        self.is_available = is_available

    def prepare(self):
        print('Ovqat Tayyorlanmoqda...')

    def serve(self):
        print('Mijozga hizmat qilinmoqda...')

    def info(self):
        print(f'Nom: {self.name}')
        print(f'Tavsif: {self.description}')
        print(f'Kategoriya: {self.category}')
        print(f'Mavjudmi: {self.is_available}')

class Pizza(MenuItem):
    def __init__(self, name, description, category, is_available, size, toppings, crust_type):
        super().__init__(name, description, category, is_available)
        self.size = size
        self.toppings = toppings
        self.crust_type = crust_type

    def prepare(self):
        super().prepare()
        print(f'{self.size} o‘lchamdagi {self.crust_type} pizza\nQoshimchalardan {self.toppings} qoshilgan')

    def serve(self):
        super().serve()
        print(f'{self.name} pizza stolga qo‘yildi')

    def info(self):
        super().info()
        print(f'O‘lchami: {self.size}')
        print(f'Qoshimchalar: {self.toppings}')
        print(f'Xamir turi: {self.crust_type}')
