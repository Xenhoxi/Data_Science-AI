import pandas as pd
import numpy as np
import math


class Dataset:
    def __init__(self, path: pd.DataFrame):
        if type(path) is str and not None:
            self.__dataset = self.read_dataset(path)
        else:
            self.__dataset = pd.DataFrame()
    

    def read_dataset(self, path: str) -> pd.DataFrame:
        try:
            data = pd.read_csv(path)
            return (data)
        except FileNotFoundError:
            print("Unexpected error, impossible to read the dataset check the given path !")
            return (pd.DataFrame())


    # Select all collums of a specific types
    # Remove all na row
    # reindex de 0 a n-1 toutes les row du tableau
    def clean_data_describe(self):
        float_set = self.__dataset.select_dtypes(include=float)
        set = float_set.dropna()
        set.reset_index(drop=True)
        return set


    def display_statistics(self):
        set = self.clean_data_describe()
        # Recupere le nom de toutes les collumns
        col_name = set.columns
        # Cree le dataframe pour afficher les stats
        stats = pd.DataFrame(columns=col_name, index=["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"])
        # Remplis les cols du dataframe
        for col in col_name:
            set = set.sort_values(by=col).reset_index(drop=True)
            stats.loc['Count', col] = len(set[col])
            stats.loc['Mean', col] = sum(set[col]) / len(set[col])
            stats.loc['Std', col] = math.sqrt(sum((set[col] - stats.loc['Mean', col]) ** 2) / (len(set[col]) - 1))
            stats.loc['Min', col] = self.min_of_col(set[col])
            stats.loc['25%', col] = (set.loc[round(len(set[col]) / 4), col] + set.loc[round(len(set[col]) / 4) - 1, col]) / 2
            stats.loc['50%', col] = set.loc[round(len(set[col]) / 2) - 1, col]
            stats.loc['75%', col] = (set.loc[round(len(set[col]) / 4 * 3), col] + set.loc[round(len(set[col]) / 4 * 3) - 1, col]) / 2
            stats.loc['Max', col] = self.max_of_col(set[col])
        print(f"{stats}")


    def get_dataset(self):
        return self.__dataset


    def display_set(self):
        if not self.__dataset.empty:
            print(self.__dataset)


    def min_of_col(self, col: pd.DataFrame) -> float:
        if not col.empty:
            min = col.loc[0]
        else:
            return None
        for i in col:
            if i < min:
                min = i
        return min


    def max_of_col(self, col: pd.DataFrame) -> float:
        if not col.empty:
            max = col.loc[0]
        else:
            return None
        for i in col:
            if i > max:
                max = i
        return max