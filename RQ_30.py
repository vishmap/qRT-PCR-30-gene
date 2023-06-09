Developed by Vishma Pratap Sur (vishmapratap.sur@ibt.cas.cz)
import numpy as np

def calculate_fc_and_log2fc(data0, data1, data2, data3, data4, data5, data6, data7):
    te = np.mean([data0, data1])
    he = np.mean([data2, data3])
    tc = np.mean([data4, data5])
    hc = np.mean([data6, data7])
    deltaBtD = te - he
    deltaBtB = tc - hc
    deltadeltaCt = deltaBtD - deltaBtB
    fc = 2**(-deltadeltaCt)
    log2fc = np.log2(fc)
    return fc, log2fc

def main():
    for i in range(30):
        data0 = float(input(f"experimental group technical replicate 1 experimental gene {i+1} Cq/Ct value: "))
        data1 = float(input(f"experimental group technical replicate 2 experimental gene {i+1} Cq/Ct value: "))
        data2 = float(input(f"experimental group technical replicate 1 housekeeping gene {i+1} Cq/Ct value: "))
        data3 = float(input(f"experimental group technical replicate 2 housekeeping gene {i+1} Cq/Ct value: "))
        data4 = float(input(f"control group technical replicate 1 experimental gene {i+1} Cq/Ct value: "))
        data5 = float(input(f"control group technical replicate 2 experimental gene {i+1} Cq/Ct value: "))
        data6 = float(input(f"control group technical replicate 1 housekeeping gene {i+1} Cq/Ct value: "))
        data7 = float(input(f"control group technical replicate 2 housekeeping gene {i+1} Cq/Ct value: "))
        fc, log2fc = calculate_fc_and_log2fc(data0, data1, data2, data3, data4, data5, data6, data7)
        print(f"fold change for gene {i+1} = {fc}")
        print(f"log2 fold change for gene {i+1} = {log2fc}")

main()
r
