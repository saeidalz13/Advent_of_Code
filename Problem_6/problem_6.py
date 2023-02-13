PATH_OUTPUT = r'output'
PATHNAME = r'input.txt'

def read_input(pathname):
    ls= []
    with open(pathname, 'r') as f:
        for line in f:
            ls.append(line)
    return ls


def solve(text:list):
    txt = text[0]

    ######################## First Section ########################
    all_txt_1 = []
    final_ls_idx_1 = []
    final_ls_txt_1 = []

    for i in range(0,len(txt)):
        _temp = txt[i:i+4]
        all_txt_1.append(_temp)
        if len(set(_temp)) == len(_temp):
            final_ls_idx_1.append(i+4)
            final_ls_txt_1.append(_temp)
        
    ######################## Second Section ########################
    all_txt_2 = []
    final_ls_idx_2 = []
    final_ls_txt_2 = []


    for i in range(0,len(txt)):
        _temp = txt[i:i+14]
        all_txt_2.append(_temp)
        if len(set(_temp)) == len(_temp):
            final_ls_idx_2.append(i+14)
            final_ls_txt_2.append(_temp)

    return all_txt_1, final_ls_idx_1, final_ls_txt_1, all_txt_2, final_ls_idx_2, final_ls_txt_2



def write_solution(
                    path_output,
                    final_ls_idx_1,
                    final_ls_txt_1,
                    final_ls_idx_2,
                    final_ls_txt_2,
                    ):
    _file = path_output+r'/solution.txt'
    with open(_file, 'w') as f:
        f.write('==============================================================================\n\n')
        f.write('The solution, Section 1:\n')
        f.write(f'--> {final_ls_idx_1[0]}')
        f.write('\nThe solution, Section 2:\n')
        f.write(f'--> {final_ls_idx_2[0]}')

        f.write('\n---------------\n')

        f.write('The text of the solution, Section 1:\n')
        f.write(f'--> {final_ls_txt_1[0]}')
        f.write('\n')
        f.write('The text of the solution, Section 2:\n')
        f.write(f'--> {final_ls_txt_2[0]}')
        f.write('\n')

        f.write('\n==============================================================================')
    pass


def main():
    TEXT = read_input(pathname=PATHNAME)
    ALL_TXT_1 , FINAL_LS_IDX_1, FINAL_LS_TXT_1 , ALL_TXT_2 , FINAL_LS_IDX_2, FINAL_LS_TXT_2 = solve(TEXT)
    write_solution(
        PATH_OUTPUT,
        FINAL_LS_IDX_1, 
        FINAL_LS_TXT_1 , 
        FINAL_LS_IDX_2, 
        FINAL_LS_TXT_2
    )

    pass


if __name__ == '__main__': main()