class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

s1 = SingletonClass()
s2 = SingletonClass()

print(s1 is s2)

s1.data1 = "Singleton class variable"
print(s2.data1)