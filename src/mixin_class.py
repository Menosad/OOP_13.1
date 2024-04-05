class MixinRepr:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        lst = []
        for key, value in self.__dict__.items():
            lst.append(f'{key}=\'{value}\'')
        return f"Создан объект класса {self.__class__.__name__} с аттрибутами: {', '.join(lst)}"
