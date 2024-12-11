from pathlib import Path
import pandas as pd

task_dict = {1: 'BEO', 2: 'CLH', 3: 'CRH', 4: 'DLF', 5: 'PLF', 6: 'DRF', 7: 'PRF', 8: 'Rest'}
task_var_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
folders_list = [Path(f'./S{i}') for i in range(1,60+1)]

for j in range(60): 
    for k in [i for i in folders_list[j].glob('*.csv')]:
        for h in k.parts[1]:
            if h in ('M', 'I'):
                next_index: int = (k.parts[1].index('M' if h == 'M' else 'I')) + 1
                task_var_dict[int(k.parts[1][next_index])] += 1
                
                df = pd.read_csv(k)
                df = df.drop(df.columns[0], axis=1)
                df.to_csv(f'./{task_dict[int(k.parts[1][next_index])]}/{task_dict[int(k.parts[1][next_index])]}_{task_var_dict[int(k.parts[1][next_index])]}.csv', index=False, header=False)

print(f'BEO: {task_var_dict[1]}\nCLH: {task_var_dict[2]}\nCRH: {task_var_dict[3]}\nDLF: {task_var_dict[4]}\nPLF: {task_var_dict[5]}\nDRF: {task_var_dict[6]}\nPRF: {task_var_dict[7]}\nRest: {task_var_dict[8]}')