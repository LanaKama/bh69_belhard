class Category:
    cotegorias = []

    @classmethod
    def add(cls, new_category):
        if new_category.title() in cls.cotegorias:
            raise ValueError('new_category is not unique')
        else:
            cls.cotegorias.append(new_category.title())
            return len(cls.cotegorias) - 1




