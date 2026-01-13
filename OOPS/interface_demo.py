import zope.interface

# 1. Correct way to define an Interface
class MyInterface(zope.interface.Interface):

    x = zope.interface.Attribute("foo")

    def method1(x):
        """Takes a number and returns something"""

    def method2():
        """Returns something"""


# 2. Implementing the interface
@zope.interface.implementer(MyInterface)
class MyClass:
    def method1(self, x):
        return x ** 2

    def method2(self):
        return "foo"


# Printing interface metadata
print(type(MyInterface))
print(MyInterface.__module__)
print(MyInterface.__name__)

# get attribute
x = MyInterface['x']
print(x)
print(type(x))

obj = MyClass()

# Correct method calls
print(obj.method1(5))
# print(obj.method1())  # ❌ INVALID → requires argument

# ask whether class implements interface
print(MyInterface.implementedBy(MyClass))

# MyClass implements → objects *provide* the interface
print(MyInterface.providedBy(MyClass))   # ❌ always False (classes don't *provide*)

print(MyInterface.providedBy(obj))       # ✔ True

# interfaces implemented by class
print(list(zope.interface.implementedBy(MyClass)))

# interfaces implemented by object
print(list(zope.interface.providedBy(obj)))

# class does NOT provide interfaces
print(list(zope.interface.providedBy(MyClass)))
