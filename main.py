class F:
    def function1(self):
        print('Class F')


class G:
    def function2(self):
        print('Class G')


class E(G, F):
    def function3(self):
        print('Class E')


class B(F):
    def function4(self):
        print('Class B')


class A(B):
    def function5(self):
        print('Class A')


class C(B):
    def function6(self):
        print('Class C')


object = B()
object.function4()
