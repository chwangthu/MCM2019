from cal_dist import cal_dist
import xlwt

pos = [[39.13351867, -83.65330251], [ 38.74559338, -78.22235584],
 [ 37.12770507, -87.76848175],
 [ 37.43699502, -80.08788502],
 [ 40.92452231,-83.24117392],
 [ 37.60271802,-85.0685606 ],
 [ 40.25538249, -80.51673779],
 [ 40.83477436, -76.66933811],
 [ 37.27353771, -77.10510008],
 [ 37.63341533, -82.61039282]]

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("distance")
for i in range(0, len(pos)):
    worksheet.write(0, i+1, i)
    worksheet.write(i+1, 0, i)

for i in range(0, len(pos)):
    for j in range(0, len(pos)):
        worksheet.write(i+1, j+1, cal_dist(pos[i], pos[j]))
workbook.save("../data/adj_matrix.xls")