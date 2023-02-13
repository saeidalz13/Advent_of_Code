import pandas as pd
import numpy as np


PATH_OUTPUT = 'output'
PATHNAME = r'input.txt'


def clean_data_and_solve(
        pathname:str,
            ):
    # Read and clean up the data:
    with open(pathname, 'r') as f:
        content = f.readlines()
        df = pd.DataFrame(content)
        df = df.apply(lambda x: x.str.replace('\n',''))
        df.columns = ['values']
        df.fillna(np.nan,inplace=True)
        df[df['values'] == ''] = np.nan
        df['marker'] = None
    
        df = df.astype({'values': 'float32'})
        df.loc[df['values'].isna(), 'marker'] = 'checkpoint'

    # Create a checkpoint before every na-value
        idx = 0
        df['index'] = None
        for row in np.arange(len(df)):
            if df.loc[row, 'marker'] == 'checkpoint':
                idx += 1
            df.loc[row,'index'] = str(idx)
        
    # Use the checkpoints to identify different groups to be able to use ".groupby"

        df.loc[df['marker'] == 'checkpoint','index'] = str(9999)
        df.to_csv('DF.csv', header=True, index=False)
        grp = df.groupby(by = 'index').sum()
        grp.to_csv('GRP.csv', header=True, index=False)

        solution_1 = int(grp['values'].max())
        sorted_df = grp['values'].sort_values(ascending=False)

        solution_2 = int(sorted_df.iloc[0] + sorted_df.iloc[1] + sorted_df.iloc[2])

    return df, grp, solution_1, solution_2



def write_output(
                path_output,
                solution_1,
                solution_2,
                ):
    file = file = path_output + fr'/solutions.txt'
    with open(file, 'w') as f:
        f.write('==============================================================================\n\n')
        f.write('The solution, Section 1:\n')
        f.write('\n')
        f.write(f'--> {solution_1}')
        f.write('\n\n')
        f.write('The solution, Section 2:\n')
        f.write('\n')
        f.write(f'--> {solution_2}')
    pass



def main():
    DF, GRP, SOLUTION_1, SOLUTION_2 = clean_data_and_solve(pathname=PATHNAME)

    write_output(
                path_output=PATH_OUTPUT,
                solution_1=SOLUTION_1,
                solution_2=SOLUTION_2,
                )
    print(f'Solution to problem 1 is = {SOLUTION_1}')
    print(f'Solution to problem 2 is = {SOLUTION_2}')
    pass


if __name__ == '__main__': main()