class MyEnumerate:

    @staticmethod
    def my_enumerate(iterable):
        idx = 0
        for item in iterable:
            yield idx, item
            idx += 1


if __name__ == "__main__":
    subjects = MyEnumerate.my_enumerate(["python", "numpy", "pandas"])
    print(subjects)
    print(dict(subjects))
    print(list(subjects))