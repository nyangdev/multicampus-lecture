def subject_generator():
    yield "python"
    yield "numpy"
    yield "pandas"

if __name__ == "__main__":
    subjects = subject_generator()
    print(subjects)
    print(dir(subjects))
    print(type(subjects))

    # for subject in subjects:
    #     print(subject)

    print(subjects.__next__())
    print(subjects.__next__())
    print(subjects.__next__())
    # print(subjects.__next__())
