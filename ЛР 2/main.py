from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np

def main():
    r = Rectangle("синего", 9, 9)
    c = Circle("зеленого", 9)
    s = Square("красного", 9)
    print(r)
    print(c)
    print(s)
    print(np.ones(5))

if __name__ == "__main__":
    main()
