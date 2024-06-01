print('hello world')

def func1(name:str) -> str:
    if name == "":
        return f"empty name"
    else:
        return f"Hello, {name}"


if __name__ == '__main__':
    result = func1(12)

    print("Result is :")
    print(result)
