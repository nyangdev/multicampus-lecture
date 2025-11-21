class Parent:

    class_val = "class variable"

    @classmethod
    def class_prn(cls):
        print(cls.class_val)

    @staticmethod
    def static_prn():
        print(Parent.class_val)

class Child(Parent):
    class_val = "child's class variable"

if __name__ == "__main__":
    parent = Parent()
    parent.class_prn()
    parent.static_prn()
    print("------------------")

    child = Child()
    child.class_prn()
    child.static_prn()