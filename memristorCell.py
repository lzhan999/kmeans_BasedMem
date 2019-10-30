import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


# �Զ��庯��������ʽ
def func(x, a, b):
    return a - b * np.log(x)

def readFiles(filename):
    rawData = pd.read_csv(filename)
    cycle = rawData.iloc[:, 0].values
    currentData = rawData.iloc[:, 1].values
    return cycle, currentData

def funcConducdence():
    # �򿪵��ļ���
    filename = "LiSiO_Data.csv"
    cycle, currentData = readFiles(filename)
    # �������
    # popt���ص��Ǹ���ģ�͵����Ų���
    # ʹ��pcov��ֵ�����ϵ���������Խ���Ԫ��ֵ������ÿ�������ķ��
    popt, pcov = curve_fit(func, cycle[0:100], currentData[0:100])
    # ��ȡpopt���������ϵ��
    #a = popt[0]
    #b = popt[1]
    return popt
    #yvals = a - b * np.log(cycle[0:100])  # ���yֵ



#����������ģ��
def memristorCell(state,pulse_before,pulse_new,Conductance,popt):

    if state == 0:  #�����ʼ��
        Conductance = np.random.rand()
        pulse_after = 0
    elif state ==1:   #��
        Conductance = Conductance
        pulse_after = pulse_before
        pass
    elif state == 2:  #д
        pulse_after = pulse_before + pulse_new
        a = popt[0]
        b = popt[1]
        Conductance = func(pulse_after,a,b)
    return Conductance,pulse_after