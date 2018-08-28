from pandas import read_csv
from re import findall
def pajero():
    with open("PAJERO.csv","r") as files:
        with open("wida_result.csv", "w") as files2:
            datas = files.readlines()
            datas3 = []
            head = datas[0]
            files2.write(head)

            for index in datas:
                final_temp = []
                data = index.split(";")
                data2 = index.split(";")
                temp1 = data[4].split(" ")
                splits = len(temp1)

                if splits == 3:
                    temp2 = " ".join([temp1[0],temp1[1]])
                    temp3 = " ".join([temp1[0],temp1[2]])
                    final_temp.append(temp2)
                    final_temp.append(temp3)

                    for i in final_temp:
                        data[4] = i
                        #datas3.append(data)
                        files2.write(";".join(data))
                else:
                    files2.write(";".join(data))


def func_pecah(nama_file,result,posisi):
    with open(nama_file,"r") as files:
        with open(result, "w") as files2:
            datas = files.readlines()
            head = datas[0]
            files2.write(head+"\n")
            finale =[]


            for index in datas[1:]:
                datas2 = index.split(";")
                try:
                    for data in (datas2[posisi]).split(","):
                        data = findall("[^\"]",data)
                        if data != []:
                            datas2[posisi] = "".join(data)
                            print(datas2[posisi])
                            files2.write(";".join(datas2))

                except:
                    files2.write(";".join(datas2))



if __name__ == '__main__':
    list_nama_tabel = [("datas/honda_jazz2004",11)]
    for nama in list_nama_tabel:
        func_pecah(nama[0]+".dsv",nama[0]+"_result.dsv",nama[1])