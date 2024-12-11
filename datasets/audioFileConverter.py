import pandas as pd
import soundfile as sf
import os

fs = 125 # sampling frequency
destinationFolder = "./audioFiles/"
sourceFolder = "./orderedDatasets/"

for root, dirs, files in os.walk(sourceFolder):
    if len(files) > 0:
        classCurrent = root[len(sourceFolder):]
        try:
            os.makedirs(destinationFolder + classCurrent)
        except Exception as e:
            pass
        for file in files:
            df: pd.DataFrame = pd.read_csv(sourceFolder+classCurrent+'/'+file, header=None)
            columns = list(df.columns)
            for column in columns:
                sf.write(destinationFolder + classCurrent + '/' + file[:-4] + '_' + str(column) + '.wav', df[column], fs)

