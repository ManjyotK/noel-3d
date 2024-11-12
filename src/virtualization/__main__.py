# import sys
# from ._schema import Animation


# def main():
#     print(sys.argv)

#     with open(sys.argv[1]) as f:
#         data = f.read()
#     animation = Animation.model_validate_json(data)

#     print(animation)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [5, 6, 2, 3, 13]
    z = [2, 3, 3, 3, 5]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)

    plt.show()

if __name__ == "__main__":
    main()