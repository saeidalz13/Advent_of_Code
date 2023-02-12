import pandas as pd

PATH_OUTPUT = r'output'
PATHNAME = r'input.csv'


def read_data(
                pathname:str
                ):
    df = pd.read_csv(pathname, header=None)
    df.columns = ['pair_1', 'pair_2']
    return df



def solve(df):
    df['range_1'] = None
    df['range_2'] = None

    range_p1_ls = list()
    range_p2_ls = list()
    for row in range(len(df)):
        string_p1= df.loc[row, 'pair_1']
        range_1_list = string_p1.split('-')
        range_1_lower= int(range_1_list[0])
        range_1_upper= int(range_1_list[1])
        range_p1 = list(range(range_1_lower,range_1_upper+1))
        range_p1_ls.append(range_p1)


        string_p2= df.loc[row, 'pair_2']
        range_2_list = string_p2.split('-')
        range_2_lower= int(range_2_list[0])
        range_2_upper= int(range_2_list[1])
        range_p2 = range(range_2_lower,range_2_upper+1)
        range_p2_ls.append(range_p2)


        ######################## First Section ########################
        # final_ls = list()
        # for p1, p2 in zip(range_p1_ls, range_p2_ls):
        #     if set(p2).issubset(set(p1)) or set(p1).issubset(set(p2)):
        #         final_ls.append(True)
        #     else:
        #         final_ls.append(False)

        # solution = final_ls.count(True)



        ######################## Second Section ########################
        final_ls = list()
        for p1, p2 in zip(range_p1_ls, range_p2_ls):
            if set(p2).intersection(set(p1)):
                final_ls.append(True)
            else:
                final_ls.append(False)

        solution = final_ls.count(True)


    return df, range_p1_ls, range_p2_ls, final_ls, solution



def main():
    DF = read_data(pathname=PATHNAME)
    DF_FINAL, LSP1, LSP2, FINAL_LS, SOLUTION_1 = solve(DF)
    print(SOLUTION_1)
    pass



if __name__ =='__main__': main()