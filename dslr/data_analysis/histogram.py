from dataset import Dataset
import matplotlib.pyplot as plt
import sys


def main() -> None:
    try:
        dataset = Dataset(sys.argv[1])
        set = dataset.get_dataset()
        print(set.columns)
        print(set.index)
        print(set['Hogwarts House'])
        set.loc[set['Hogwarts House'] == 'Gryffindor'].hist()
        set.loc[set['Hogwarts House'] == 'Ravenclaw'].hist()
        set.loc[set['Hogwarts House'] == 'Slytherin'].hist()
        set.loc[set['Hogwarts House'] == 'Hufflepuff'].hist()
        plt.show()
    except (KeyboardInterrupt) as err:
        pass


if __name__ == '__main__':
    main()