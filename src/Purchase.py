
"""
The script calculates product statistics for each department.
Created on Fri Apr. 5th 2018
@author: Huifang Wang
"""

# importing csv module
import csv

# Input/output data file name
FileOrd = "./input/order_products.csv"
FilePro = "./input/products.csv"
FileOutput = "./output/report.csv"

# function that reads files
def ReadFile(FileName,FileData):
    with open(FileName,'r',encoding="utf-8") as Statfile:
        FileRe = csv.reader(Statfile,delimiter=',')
        FieldR = next(FileRe)  # extracting field names
        for row in FileRe:
            FileData.append(row)
        return FieldR, FileData;
    
# function that calculates the product statistics
def ProdStat(OrderList,ProdList,PIDList,DeptID):
    i = 0
    OrderN = [0] * len(DeptID)  
    FirstOrderN = [0] * len(DeptID)  
    for i in range(len(OrderList)):
        IndexTmp = PIDList.index(OrderList[i][1])
        DeptTmp = DeptID.index(int(ProdList[IndexTmp][3]))
        OrderN[DeptTmp] += 1
        if OrderList[i][3]=='0':
            FirstOrderN[DeptTmp] += 1
    return OrderN, FirstOrderN;

# Initialize data lists
OrderList = [] # Data from order_products.csv file
ProdList = [] # Data from products.csv file
FieldOrd = [] # Field of order_products.csv file
FieldProd = [] # Field of products.csv file
PIDList = []  # Product ID list
DeptIDList = [] # Department ID list
OrderNum = []   # Number of orders
FirstOrderNum = []   # Number of first orders
Percentage = []
# output file field name
FieldOut=['department_id','number_of_orders','number_of_first_orders','percentage']


# Read order/products data file
FieldOrd,OrderList = ReadFile(FileOrd,OrderList)
FieldProd,ProdList = ReadFile(FilePro,ProdList)

# Find department ID list
Idtmp = 0
for Idtmp in range(len(ProdList)):
    PIDList.append(ProdList[Idtmp][0])
    DeptIDList.append(int(ProdList[Idtmp][3]))
DeptID = list(set(DeptIDList))

# Calculate product statistics for each department
OrderNum,FirstOrderNum = ProdStat(OrderList,ProdList,PIDList,DeptID)

# Calculate percentage of 1st time order over total order number
Idtmp = 0
for Idtmp in range(len(DeptID)):
    Pertmp = round(FirstOrderNum[Idtmp]/OrderNum[Idtmp],2)
    Percentage.append(format(Pertmp, '.2f'))

# Create output data
OutputData = list(zip(DeptID,OrderNum,FirstOrderNum,Percentage))

# Write to file
with open(FileOutput,'w') as Statfile:
    FileWr = csv.writer(Statfile,delimiter=",")
    FileWr.writerow(FieldOut)
    FileWr.writerows(OutputData)
  