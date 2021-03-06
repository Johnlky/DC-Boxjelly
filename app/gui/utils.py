from datetime import datetime
from PyQt5.QtCore import QFile, QIODevice
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import sys
import pandas as pd
import os
import logging
from app.core.models import Job, Equipment, ConstantFile
import dateutil.parser

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def loadUI(str, window):
    ui_file_name = str
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        logger.critical(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loadedWindow = loadUi(ui_file, window)
    ui_file.close()
    if not loadedWindow:
        #print(loader.errorString())
        sys.exit(-1)
    return loadedWindow


def getHomeTableData():
    '''
    Return client info data as Dataframe
    '''
    # data = {
    #     'status': [False, False, False],
    #     'CAL Number': ['CAL 001', 'CAL 002', 'CAL 003'],
    #     'Client Name': ['Amy', 'Jay', 'Jack'],
    #     'Clinet Address': ['8 Leonerd Street', '12 Collins Street', '5 Sutherland Street']
    # }

    data = {
        'CAL Number': [],
        'Client Name': []
    }
    for job in Job:
        data['CAL Number'].append(job.id),
        data['Client Name'].append(job.client_name),
        # data['Clinet Address'].append(str(job.client_address_1)+' '+str(job.client_address_2)),
        # data['Client Address'].append(''),
    
    df = pd.DataFrame(data)
    return df

def getEquipmentsTableData(job: Job):
    '''
    Return equipments data as Dataframe
    '''
    #job = Job[jobID]
    data = {
        'Serial Num': [],
        'Make/Model': [],
        'ID': []
    }
    for equip in job:
        data['Make/Model'].append(equip.model),
        data['Serial Num'].append(equip.serial),
        data['ID'].append(equip.id),
    df = pd.DataFrame(data)
    return df

def getRunsTableData(equip: Equipment):
    '''
    Return runs data as Dataframe
    '''
    #equip = Job[jobID][equipID]
    data = {
        'ID': [],
        # 'Added Time': [],
        'Edited Time': [],
        'Measurement Date': [],
        'Operator': [],
    }
    for run in equip.mex:
        data['ID'].append(run.id),
        # data['Added Time'].append(converTimeFormat(run.added_at)),
        data['Edited Time'].append(converTimeFormat(run.edited_at)),
        data['Measurement Date'].append(converTimeFormat(run.measured_at).split()[0]),
        data['Operator'].append(run.operator),
    df = pd.DataFrame(data)
    return df

def getResultData():
    data = {
        "Beam quality": ["NXJ40", "NXJ50"],
        "E_eff": [40.1, 40.1],
        "Run1_NK": [33.1, 33.1],
        "Run2_NK": [33.6, 33.5],
        "Average": [36.0, 36.0],
        "Run1/Average": [0.920, 0.920],
        "Run2/Average": [0.933, 0.933],
    }
    return pd.DataFrame(data)

def converTimeFormat(time: str):
    
    if time:
        dateTime = dateutil.parser.isoparse(time)
        return dateTime.strftime('%d-%m-%Y %H:%M:%S')
    else:
        return None

def getConstantsTableData():
    '''
    Return contants data as Dataframe
    '''
    data = {
        'ID': [],
        'Create time': [],
        'Description': [],
    }
    # insert templete constants
    data['ID'].append("Template")
    data['Create time'].append("01-10-2021 00:00:00")
    data['Description'].append("Templete Constants")
    # get all other constants obj
    for constantsFile in ConstantFile:
        data['ID'].append(constantsFile.id)
        data['Create time'].append(converTimeFormat(constantsFile.added_at))
        if constantsFile.note == None:
            data['Description'].append("")
        else:
            data['Description'].append(constantsFile.note)
    
    df = pd.DataFrame(data)
    return df