import xlrd

def find_county():
    try:
        data = xlrd.open_workbook("../data/MCM_NFLIS_Data.xlsx")
    except FileNotFoundError:
        print("File not found")
        return
    sheet = data.sheet_by_name(u"Data")
    nrows = sheet.nrows
    ncols = sheet.ncols
    state_dict = { 'VA': set(), 'OH': set(), 'PA': set(), 'WV': set(), 'KY': set() }
    for i in range(1, nrows):
        rowdata = sheet.row_values(i)
        # print(rowdata[1], state_dict[rowdata[1]])
        state_dict[rowdata[1]].add(rowdata[5])
    for item in state_dict:
        print(item, state_dict[item], len(state_dict[item]))
    
if __name__ == "__main__":
    find_county()
