from prettytable import PrettyTable
import csv


#importamos datos

def read():
    data = list()
    with open('C:/Users/javoe/PycharmProjects/ayudaprograavanzada/ex4/iris.csv', newline='') as f:
        reader = csv.reader(f)
        for linea in reader:
            data.append(linea)
    x = PrettyTable()
    data[0][0] = "id"
    print(data)
    x.field_names = data[0]
    for i in range(1,len(data),1):
        x.add_row(data[i])
    print(x)



if __name__=="__main__":
    read()