class Meta(type):
    def __new__(self, name, bases, attrs):
        if name in globals().keys():
            return globals()[name](attrs)
        globals()[name] = type(name, bases, attrs)

class DynamicAttributes:
    def __init__(self, *args, **kwargs): 
        if args: 
            kwargs, args = [args[0], ()] \
                if isinstance(args[0], dict) \
                    else [args[0][-1], args[0][:-1]]
        self.__dict__ = dict(filter(lambda item: item[0] not in args, kwargs.items()))
    
    def __str__(self):
        return '\n'.join([f'{k}: {v}' for k, v in self.__dict__.items()])


Meta('Dog', (DynamicAttributes,), {'id':1, 'specy':'hound', 'weight':8, 'height':55, 'bark': lambda : print('\nWoof\n')})
print(globals()['Dog'])
dog = Meta('Dog', (), ('height', {**globals()['Dog'].__dict__, 'id':2}))
dog.bark()
dog.weight *= 2
print(dog)

Meta('Cat', (DynamicAttributes,), {'id': 1, 'age': 1, 'weight': 2, 'specy': 'Siamese', 'meow': lambda : print('\nMeow\n')})
print(globals()['Cat'])
cat = Meta('Cat', (), ('weight', 'specy', {**globals()['Cat'].__dict__, 'id': 2}))
cat.meow()
cat.age *= 2
print(cat)
