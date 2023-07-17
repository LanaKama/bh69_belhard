class Category:
    cotegorias = []

    @classmethod
    def add(cls, new_category):
        if new_category.title() in cls.cotegorias:
            raise ValueError('new_category is not unique')
        else:
            cls.cotegorias.append(new_category.title())
            return len(cls.cotegorias) - 1

    @classmethod
    def get(cls, _id):
        return cls.cotegorias[_id]

    @classmethod
    def remove(cls, _id):
        try:
            del cls.cotegorias[_id]
        except IndexError

text = '''
[Section1]
key1=value1
key2=value2
[Section2]
key3=value3
key4=value4
'''


class ConfigParser:

def __init__(self, text: str) -> None:
    self.data = self.loads(text)

@classmethod
def loads(cls, text:str) -> dict[str], dict[str, str]]:
    lines = [line for line in text.split('\n') if line]
    data = {}
    current_section = ''
    for line in lines:
        if line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1]
            data[current_section] = {}
        else:
            key, value = line.split('=')
            data[current_section][key] = value
    return data

def has_section(self, section: str) -> bool:
    return section in self.data

def has_param(self, section: str) ->bool:
    try:
        return param in self.data[section]
    except KeyError
        raise ValueError

def add_section(self, section: str) -> Nane
    if self.has_section(section):
        raise ValueError
    self.data[section] = {}