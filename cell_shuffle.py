import os
import pandas as pd

epiCellsAll = os.listdir('epiCellsAll')

naive_cells = pd.read_csv('naive_cells.csv', header=None, names = ['cell_id'])
pd_cells = pd.read_csv('pd_cells.csv', header=None, names = ['cell_id'])
pr_cells = pd.read_csv('pr_cells.csv', header=None, names = ['cell_id'])

naive_cells = list(naive_cells['cell_id'])
pd_cells = list(pd_cells['cell_id'])
pr_cells = list(pr_cells['cell_id'])

for cell in epiCellsAll:
    if cell in naive_cells:
        cmd = 'cp epiCellsAll/' + cell + '/ ' + 'TN_tumor/ --recursive'
        #print(cmd)
        os.system(cmd)
    elif cell in pd_cells:
        cmd = 'cp epiCellsAll/' + cell + '/ ' + 'PD_tumor/ --recursive'
        #print(cmd)
        os.system(cmd)
    elif cell in pr_cells:
        cmd = 'cp epiCellsAll/' + cell + '/ ' + 'PER_tumor/ --recursive'
        #print(cmd)
        os.system(cmd)