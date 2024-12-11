# Data to extract
# - movement_left
# - movement_right
# - imagery_left
# - imagery_right
# - rest

# next is nose
# - noise
# It is a 5x1 cell array in matlab

import scipy.io
import pandas as pd


for i in range(1, 53):
    mat = scipy.io.loadmat(f's{i}.mat')
    mat_eeg = mat['eeg']
    
    for j in range(0, 5):
        df_noise = pd.DataFrame(mat_eeg['noise'][0,0][j,0])
        df_noise.to_csv(f'noise/noise_{i}_{j}.csv', index=False, header=False)
        print(f'noise/noise_{i}_{j}.csv')

    df_movement_left = pd.DataFrame(mat_eeg['movement_left'][0, 0])
    # df_movement_left = df_movement_left.drop(labels=df_movement_left.columns[0], axis=1)
    
    df_movement_right = pd.DataFrame(mat_eeg['movement_right'][0, 0])
    # df_movement_right = df_movement_right.drop(df_movement_right.columns[0], axis=1)
    
    df_imagery_left = pd.DataFrame(mat_eeg['imagery_left'][0, 0])
    # df_imagery_left = df_imagery_left.drop(df_imagery_left.columns[0], axis=1)
    
    df_imagery_right = pd.DataFrame(mat_eeg['imagery_right'][0, 0])
    # df_imagery_right = df_imagery_right.drop(df_imagery_right.columns[0], axis=1)
    
    df_rest = pd.DataFrame(mat_eeg['rest'][0, 0])
    # df_rest = df_rest.drop(df_rest.columns[0], axis=1)

    df_movement_left.to_csv(f'movement_left/movement_left_{i}.csv', index=False, header=False)
    print(f'movement_left/movement_left_{i}.csv')
    
    df_movement_right.to_csv(f'movement_right/movement_right_{i}.csv', index=False, header=False)
    print(f'movement_right/movement_right_{i}.csv')
    
    df_imagery_left.to_csv(f'imagery_left/imagery_left_{i}.csv', index=False, header=False)
    print(f'imagery_left/imagery_left_{i}.csv')
    
    df_imagery_right.to_csv(f'imagery_right/imagery_right_{i}.csv', index=False, header=False)
    print(f'imagery_right/imagery_right_{i}.csv')
    
    df_rest.to_csv(f'rest/rest_{i}.csv', index=False, header=False)
    print(f'rest/rest_{i}.csv')