class Parent:
    def func1(self):
        print('This is function in Parent class')

class Child1(Parent):
    def func2(self):
        print('This is funtion in Child 1 class')

class Child2(Parent):
    def func3(self):
        print('This is funtion in Child 2 class')

object1 = Child1()
object2 = Child2()
object1.func1()
object2.func1()


class Parent:
    def func1(self):
        print('This is function in class Parent')

class Child1(Parent):
    def func2(self):
        print('This is funtion in class Child 1')

class Child2(Child1):
    def func3(self):
        print('This is funtion in class Child 2')


object2 = Child2()
object2.func2()


