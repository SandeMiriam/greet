from itertools import product


def multiply_and_greet(*args,**kwargs):
    product =1
    for int in args:
         product *=int
         print(product)
         keys=kwargs.keys()
    if "country" in keys:
         print(f"Hello{kwargs['name']} from {kwargs['country']}")
    elif"age" in keys:
        year=2022-kwargs["age"]
        print(f"hello {kwargs['name']} you were born in {year}")
    elif"name" in keys:
        print(f"hello{kwargs['name']}")
    else:
        print(f"hello Sande")

