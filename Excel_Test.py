# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:08:47 2021
Practicing pulling data from Excel

@author: Mark.Payne
"""

import xlrd



wb = xlrd.open_workbook("Practice_Sheet")
wb.sheet_names()
sh = wb.sheet_by_index(0)
i = 1
with open("Excel_Output.txt","a") as my_file:
    while sh.cell(i,2).value !=0:
        load = sh.cell(i,11).value
        all_d = sh.col_values(i, 13, 19)
        DB1 = Load + "" + ("".join(all_d))
        my_file.write(DB1 + '\n')
        i+=1
        