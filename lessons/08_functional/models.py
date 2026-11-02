from collections import namedtuple

Product = namedtuple("Product", ["name", "price"])
Line = namedtuple("Line", ["product", "quantity"])
