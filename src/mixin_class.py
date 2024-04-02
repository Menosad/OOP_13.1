
class MixinRepr:

    # def __init__(self):
    #     self.__repr__()

    def __repr__(self):
        lst = []
        for key, value in self.__dict__.items():
            lst.append(f'{key}={value}')
        return (f"Создан объект класса {self.__class__.__name__} с аттрибутами: "
                f"{' '.join(lst)}")

