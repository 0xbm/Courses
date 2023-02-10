def funkcja(arg1, arg2="World", *args, **kwargs):
    print(
        arg1, arg2, *args, kwargs
    )  # mozna rowniez wpisac samo args czyli bez gwiazdki
    print(len(args))
    for x in args:
        print(
            x, arg1
        )  # iteracja wykonuje sie tylko do funkcja("Hi", "YouTube", "!", "?")
    for y in kwargs.values():
        print(y)


funkcja("Hello")
funkcja("Hi", "YouTube")
funkcja("Hi", "YouTube", "!", "?", autor="Michał", rok=2020)
