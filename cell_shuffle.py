import os

epiCellsAll = os.listdir('epiCellsAll')
naive_cells = pd.read_csv('naive_cells.csv')
pd_cells = pd.read_csv('pd_cells.csv')
pr_cells = pd.read_csv('pr_cells.csv')

for cell in epiCellsAll:
    if cell in naive_cells:
        cmd = 'cp epiCellsAll/' + cell + '/ ' + 'TN_tumor/ --recursive'
        print(cmd)
        #os.system(cmd)
    elif cell in pd_cells:
        cmd = 'cp epiCellsAll/' + cell + '/ ' + 'PD_tumor/ --recursive'
        print(cmd)
        #os.system(cmd)
    elif cell in pr_cells:
        cmd = 'cp epiCellsAll/' + cell + '/ ' + 'PER_tumor/ --recursive'
        print(cmd)
        #os.system(cmd)