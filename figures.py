from figures_lib import lib
import pandas as pd
import numpy as np


dataset = pd.read_csv('data/HRDataset_v14.csv')


def manager_number_card():
    return lib.card('Managers Number', len(np.unique(dataset['ManagerName'], return_counts=True)[0]))