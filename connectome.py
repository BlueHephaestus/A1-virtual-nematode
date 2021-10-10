# GoPiGo Connectome
# Written by Timothy Busbice, Gabriel Garrett, Geoffrey Churchill (c) 2014, in Python 2.7
# The GoPiGo Connectome uses a postSynaptic dictionary based on the C Elegans Connectome Model
# This application can be ran on the Raspberry Pi GoPiGo robot with a Sonar that represents Nose Touch when activated
# To run standalone without a GoPiGo robot, simply comment out the sections with Start and End comments 

# TIME STATE EXPERIMENTAL OPTIMIZATION
# The previous version had a logic error whereby if more than one neuron fired into the same neuron in the next time state,
# it would overwrite the contribution from the previous neuron. Thus, only one neuron could fire into the same neuron at any given time state.
# This version also explicitly lists all left and right muscles, so that during the muscle checks for the motor control function, instead of 
# iterating through each neuron, we now iterate only through the relevant muscle neurons.

# This logic error took it's place via doing neuron[nextstate] = neuron[thisState] + 2
# so if there were ever any neurons from this state that were going to influence the next state,
# this would not get counted because it would reassign it.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='count', default=0)
# three levels of verbosity: [], -v, -vv
# 0: only print starting and exiting messages
# 1: print only when obstacles/food found
# 2: print speed, left and right every time
verbosity = parser.parse_args().verbose

from body import Body
body = Body()

import time
import copy
import signal
import sys
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

class Nematode:

    def __init__(self):
        # The postSynaptic dictionary contains the accumulated weighted values as the
        # connectome is executed
        self.post_synaptic = {}

        # todo make this self.curr and self.next
        self.thisState = 0
        self.nextState = 1

        # The Threshold is the maximum sccumulated value that must be exceeded before
        # the Neurite will fire
        threshold = 30

        time_delays = False
        # Accumulators are used to decide the value to send to the Left and Right motors
        # of the GoPiGo robot
        accumleft = 0
        accumright = 0

        # Used to remove from Axon firing since muscles cannot fire.
        muscles = ['MVU', 'MVL', 'MDL', 'MVR', 'MDR']

        mLeft =  ['MDL01', 'MDL02', 'MDL03', 'MDL04', 'MDL05', 'MDL06', 'MDL07', 'MDL08', 'MDL09', 'MDL10',
                  'MDL11', 'MDL12', 'MDL13', 'MDL14', 'MDL15', 'MDL16', 'MDL17', 'MDL18', 'MDL19', 'MDL20',
                  'MDL21', 'MDL22', 'MDL23', 'MDL24', 'MVL01', 'MVL02', 'MVL03', 'MVL04', 'MVL05', 'MVL06',
                  'MVL07', 'MVL08', 'MVL09', 'MVL10', 'MVL11', 'MVL12', 'MVL13', 'MVL14', 'MVL15', 'MVL16',
                  'MVL17', 'MVL18', 'MVL19', 'MVL20', 'MVL21', 'MVL22', 'MVL23']

        mRight = ['MDR01', 'MDR02', 'MDR03', 'MDR04', 'MDR05', 'MDR06', 'MDR07', 'MDR08', 'MDR09', 'MDR10',
                  'MDR11', 'MDR12', 'MDR13', 'MDR14', 'MDR15', 'MDR16', 'MDR17', 'MDR18', 'MDR19', 'MDR20',
                  'MDR21', 'MDR22', 'MDR23', 'MDR24', 'MVR01', 'MVR02', 'MVR03', 'MVR04', 'MVR05', 'MVR06',
                  'MVR07', 'MVR08', 'MVR09', 'MVR10', 'MVR11', 'MVR12', 'MVR13', 'MVR14', 'MVR15', 'MVR16',
                  'MVR17', 'MVR18', 'MVR19', 'MVR20', 'MVR21', 'MVR22', 'MVR23']
        # Used to accumulate muscle weighted values in body muscles 07-23 = worm locomotion


        """This is the full C Elegans Connectome as expresed in the form of the Presynatptic
        neurite and the postSynaptic neurites.

        postSynaptic['ADAR'][nextState] = (2 + postSynaptic['ADAR'][thisState])
        arr=postSynaptic['AIBR'] potential optimization
        """




    def createpostSynaptic():
        # The postSynaptic dictionary maintains the accumulated values for
        # each neuron and muscle. The Accumulated values are initialized to Zero
        postSynaptic['ADAL'] = [0, 0]
        postSynaptic['ADAR'] = [0, 0]
        postSynaptic['ADEL'] = [0, 0]
        postSynaptic['ADER'] = [0, 0]
        postSynaptic['ADFL'] = [0, 0]
        postSynaptic['ADFR'] = [0, 0]
        postSynaptic['ADLL'] = [0, 0]
        postSynaptic['ADLR'] = [0, 0]
        postSynaptic['AFDL'] = [0, 0]
        postSynaptic['AFDR'] = [0, 0]
        postSynaptic['AIAL'] = [0, 0]
        postSynaptic['AIAR'] = [0, 0]
        postSynaptic['AIBL'] = [0, 0]
        postSynaptic['AIBR'] = [0, 0]
        postSynaptic['AIML'] = [0, 0]
        postSynaptic['AIMR'] = [0, 0]
        postSynaptic['AINL'] = [0, 0]
        postSynaptic['AINR'] = [0, 0]
        postSynaptic['AIYL'] = [0, 0]
        postSynaptic['AIYR'] = [0, 0]
        postSynaptic['AIZL'] = [0, 0]
        postSynaptic['AIZR'] = [0, 0]
        postSynaptic['ALA'] = [0, 0]
        postSynaptic['ALML'] = [0, 0]
        postSynaptic['ALMR'] = [0, 0]
        postSynaptic['ALNL'] = [0, 0]
        postSynaptic['ALNR'] = [0, 0]
        postSynaptic['AQR'] = [0, 0]
        postSynaptic['AS1'] = [0, 0]
        postSynaptic['AS10'] = [0, 0]
        postSynaptic['AS11'] = [0, 0]
        postSynaptic['AS2'] = [0, 0]
        postSynaptic['AS3'] = [0, 0]
        postSynaptic['AS4'] = [0, 0]
        postSynaptic['AS5'] = [0, 0]
        postSynaptic['AS6'] = [0, 0]
        postSynaptic['AS7'] = [0, 0]
        postSynaptic['AS8'] = [0, 0]
        postSynaptic['AS9'] = [0, 0]
        postSynaptic['ASEL'] = [0, 0]
        postSynaptic['ASER'] = [0, 0]
        postSynaptic['ASGL'] = [0, 0]
        postSynaptic['ASGR'] = [0, 0]
        postSynaptic['ASHL'] = [0, 0]
        postSynaptic['ASHR'] = [0, 0]
        postSynaptic['ASIL'] = [0, 0]
        postSynaptic['ASIR'] = [0, 0]
        postSynaptic['ASJL'] = [0, 0]
        postSynaptic['ASJR'] = [0, 0]
        postSynaptic['ASKL'] = [0, 0]
        postSynaptic['ASKR'] = [0, 0]
        postSynaptic['AUAL'] = [0, 0]
        postSynaptic['AUAR'] = [0, 0]
        postSynaptic['AVAL'] = [0, 0]
        postSynaptic['AVAR'] = [0, 0]
        postSynaptic['AVBL'] = [0, 0]
        postSynaptic['AVBR'] = [0, 0]
        postSynaptic['AVDL'] = [0, 0]
        postSynaptic['AVDR'] = [0, 0]
        postSynaptic['AVEL'] = [0, 0]
        postSynaptic['AVER'] = [0, 0]
        postSynaptic['AVFL'] = [0, 0]
        postSynaptic['AVFR'] = [0, 0]
        postSynaptic['AVG'] = [0, 0]
        postSynaptic['AVHL'] = [0, 0]
        postSynaptic['AVHR'] = [0, 0]
        postSynaptic['AVJL'] = [0, 0]
        postSynaptic['AVJR'] = [0, 0]
        postSynaptic['AVKL'] = [0, 0]
        postSynaptic['AVKR'] = [0, 0]
        postSynaptic['AVL'] = [0, 0]
        postSynaptic['AVM'] = [0, 0]
        postSynaptic['AWAL'] = [0, 0]
        postSynaptic['AWAR'] = [0, 0]
        postSynaptic['AWBL'] = [0, 0]
        postSynaptic['AWBR'] = [0, 0]
        postSynaptic['AWCL'] = [0, 0]
        postSynaptic['AWCR'] = [0, 0]
        postSynaptic['BAGL'] = [0, 0]
        postSynaptic['BAGR'] = [0, 0]
        postSynaptic['BDUL'] = [0, 0]
        postSynaptic['BDUR'] = [0, 0]
        postSynaptic['CEPDL'] = [0, 0]
        postSynaptic['CEPDR'] = [0, 0]
        postSynaptic['CEPVL'] = [0, 0]
        postSynaptic['CEPVR'] = [0, 0]
        postSynaptic['DA1'] = [0, 0]
        postSynaptic['DA2'] = [0, 0]
        postSynaptic['DA3'] = [0, 0]
        postSynaptic['DA4'] = [0, 0]
        postSynaptic['DA5'] = [0, 0]
        postSynaptic['DA6'] = [0, 0]
        postSynaptic['DA7'] = [0, 0]
        postSynaptic['DA8'] = [0, 0]
        postSynaptic['DA9'] = [0, 0]
        postSynaptic['DB1'] = [0, 0]
        postSynaptic['DB2'] = [0, 0]
        postSynaptic['DB3'] = [0, 0]
        postSynaptic['DB4'] = [0, 0]
        postSynaptic['DB5'] = [0, 0]
        postSynaptic['DB6'] = [0, 0]
        postSynaptic['DB7'] = [0, 0]
        postSynaptic['DD1'] = [0, 0]
        postSynaptic['DD2'] = [0, 0]
        postSynaptic['DD3'] = [0, 0]
        postSynaptic['DD4'] = [0, 0]
        postSynaptic['DD5'] = [0, 0]
        postSynaptic['DD6'] = [0, 0]
        postSynaptic['DVA'] = [0, 0]
        postSynaptic['DVB'] = [0, 0]
        postSynaptic['DVC'] = [0, 0]
        postSynaptic['FLPL'] = [0, 0]
        postSynaptic['FLPR'] = [0, 0]
        postSynaptic['HSNL'] = [0, 0]
        postSynaptic['HSNR'] = [0, 0]
        postSynaptic['I1L'] = [0, 0]
        postSynaptic['I1R'] = [0, 0]
        postSynaptic['I2L'] = [0, 0]
        postSynaptic['I2R'] = [0, 0]
        postSynaptic['I3'] = [0, 0]
        postSynaptic['I4'] = [0, 0]
        postSynaptic['I5'] = [0, 0]
        postSynaptic['I6'] = [0, 0]
        postSynaptic['IL1DL'] = [0, 0]
        postSynaptic['IL1DR'] = [0, 0]
        postSynaptic['IL1L'] = [0, 0]
        postSynaptic['IL1R'] = [0, 0]
        postSynaptic['IL1VL'] = [0, 0]
        postSynaptic['IL1VR'] = [0, 0]
        postSynaptic['IL2L'] = [0, 0]
        postSynaptic['IL2R'] = [0, 0]
        postSynaptic['IL2DL'] = [0, 0]
        postSynaptic['IL2DR'] = [0, 0]
        postSynaptic['IL2VL'] = [0, 0]
        postSynaptic['IL2VR'] = [0, 0]
        postSynaptic['LUAL'] = [0, 0]
        postSynaptic['LUAR'] = [0, 0]
        postSynaptic['M1'] = [0, 0]
        postSynaptic['M2L'] = [0, 0]
        postSynaptic['M2R'] = [0, 0]
        postSynaptic['M3L'] = [0, 0]
        postSynaptic['M3R'] = [0, 0]
        postSynaptic['M4'] = [0, 0]
        postSynaptic['M5'] = [0, 0]
        postSynaptic['MANAL'] = [0, 0]
        postSynaptic['MCL'] = [0, 0]
        postSynaptic['MCR'] = [0, 0]
        postSynaptic['MDL01'] = [0, 0]
        postSynaptic['MDL02'] = [0, 0]
        postSynaptic['MDL03'] = [0, 0]
        postSynaptic['MDL04'] = [0, 0]
        postSynaptic['MDL05'] = [0, 0]
        postSynaptic['MDL06'] = [0, 0]
        postSynaptic['MDL07'] = [0, 0]
        postSynaptic['MDL08'] = [0, 0]
        postSynaptic['MDL09'] = [0, 0]
        postSynaptic['MDL10'] = [0, 0]
        postSynaptic['MDL11'] = [0, 0]
        postSynaptic['MDL12'] = [0, 0]
        postSynaptic['MDL13'] = [0, 0]
        postSynaptic['MDL14'] = [0, 0]
        postSynaptic['MDL15'] = [0, 0]
        postSynaptic['MDL16'] = [0, 0]
        postSynaptic['MDL17'] = [0, 0]
        postSynaptic['MDL18'] = [0, 0]
        postSynaptic['MDL19'] = [0, 0]
        postSynaptic['MDL20'] = [0, 0]
        postSynaptic['MDL21'] = [0, 0]
        postSynaptic['MDL22'] = [0, 0]
        postSynaptic['MDL23'] = [0, 0]
        postSynaptic['MDL24'] = [0, 0]
        postSynaptic['MDR01'] = [0, 0]
        postSynaptic['MDR02'] = [0, 0]
        postSynaptic['MDR03'] = [0, 0]
        postSynaptic['MDR04'] = [0, 0]
        postSynaptic['MDR05'] = [0, 0]
        postSynaptic['MDR06'] = [0, 0]
        postSynaptic['MDR07'] = [0, 0]
        postSynaptic['MDR08'] = [0, 0]
        postSynaptic['MDR09'] = [0, 0]
        postSynaptic['MDR10'] = [0, 0]
        postSynaptic['MDR11'] = [0, 0]
        postSynaptic['MDR12'] = [0, 0]
        postSynaptic['MDR13'] = [0, 0]
        postSynaptic['MDR14'] = [0, 0]
        postSynaptic['MDR15'] = [0, 0]
        postSynaptic['MDR16'] = [0, 0]
        postSynaptic['MDR17'] = [0, 0]
        postSynaptic['MDR18'] = [0, 0]
        postSynaptic['MDR19'] = [0, 0]
        postSynaptic['MDR20'] = [0, 0]
        postSynaptic['MDR21'] = [0, 0]
        postSynaptic['MDR22'] = [0, 0]
        postSynaptic['MDR23'] = [0, 0]
        postSynaptic['MDR24'] = [0, 0]
        postSynaptic['MI'] = [0, 0]
        postSynaptic['MVL01'] = [0, 0]
        postSynaptic['MVL02'] = [0, 0]
        postSynaptic['MVL03'] = [0, 0]
        postSynaptic['MVL04'] = [0, 0]
        postSynaptic['MVL05'] = [0, 0]
        postSynaptic['MVL06'] = [0, 0]
        postSynaptic['MVL07'] = [0, 0]
        postSynaptic['MVL08'] = [0, 0]
        postSynaptic['MVL09'] = [0, 0]
        postSynaptic['MVL10'] = [0, 0]
        postSynaptic['MVL11'] = [0, 0]
        postSynaptic['MVL12'] = [0, 0]
        postSynaptic['MVL13'] = [0, 0]
        postSynaptic['MVL14'] = [0, 0]
        postSynaptic['MVL15'] = [0, 0]
        postSynaptic['MVL16'] = [0, 0]
        postSynaptic['MVL17'] = [0, 0]
        postSynaptic['MVL18'] = [0, 0]
        postSynaptic['MVL19'] = [0, 0]
        postSynaptic['MVL20'] = [0, 0]
        postSynaptic['MVL21'] = [0, 0]
        postSynaptic['MVL22'] = [0, 0]
        postSynaptic['MVL23'] = [0, 0]
        postSynaptic['MVR01'] = [0, 0]
        postSynaptic['MVR02'] = [0, 0]
        postSynaptic['MVR03'] = [0, 0]
        postSynaptic['MVR04'] = [0, 0]
        postSynaptic['MVR05'] = [0, 0]
        postSynaptic['MVR06'] = [0, 0]
        postSynaptic['MVR07'] = [0, 0]
        postSynaptic['MVR08'] = [0, 0]
        postSynaptic['MVR09'] = [0, 0]
        postSynaptic['MVR10'] = [0, 0]
        postSynaptic['MVR11'] = [0, 0]
        postSynaptic['MVR12'] = [0, 0]
        postSynaptic['MVR13'] = [0, 0]
        postSynaptic['MVR14'] = [0, 0]
        postSynaptic['MVR15'] = [0, 0]
        postSynaptic['MVR16'] = [0, 0]
        postSynaptic['MVR17'] = [0, 0]
        postSynaptic['MVR18'] = [0, 0]
        postSynaptic['MVR19'] = [0, 0]
        postSynaptic['MVR20'] = [0, 0]
        postSynaptic['MVR21'] = [0, 0]
        postSynaptic['MVR22'] = [0, 0]
        postSynaptic['MVR23'] = [0, 0]
        postSynaptic['MVULVA'] = [0, 0]
        postSynaptic['NSML'] = [0, 0]
        postSynaptic['NSMR'] = [0, 0]
        postSynaptic['OLLL'] = [0, 0]
        postSynaptic['OLLR'] = [0, 0]
        postSynaptic['OLQDL'] = [0, 0]
        postSynaptic['OLQDR'] = [0, 0]
        postSynaptic['OLQVL'] = [0, 0]
        postSynaptic['OLQVR'] = [0, 0]
        postSynaptic['PDA'] = [0, 0]
        postSynaptic['PDB'] = [0, 0]
        postSynaptic['PDEL'] = [0, 0]
        postSynaptic['PDER'] = [0, 0]
        postSynaptic['PHAL'] = [0, 0]
        postSynaptic['PHAR'] = [0, 0]
        postSynaptic['PHBL'] = [0, 0]
        postSynaptic['PHBR'] = [0, 0]
        postSynaptic['PHCL'] = [0, 0]
        postSynaptic['PHCR'] = [0, 0]
        postSynaptic['PLML'] = [0, 0]
        postSynaptic['PLMR'] = [0, 0]
        postSynaptic['PLNL'] = [0, 0]
        postSynaptic['PLNR'] = [0, 0]
        postSynaptic['PQR'] = [0, 0]
        postSynaptic['PVCL'] = [0, 0]
        postSynaptic['PVCR'] = [0, 0]
        postSynaptic['PVDL'] = [0, 0]
        postSynaptic['PVDR'] = [0, 0]
        postSynaptic['PVM'] = [0, 0]
        postSynaptic['PVNL'] = [0, 0]
        postSynaptic['PVNR'] = [0, 0]
        postSynaptic['PVPL'] = [0, 0]
        postSynaptic['PVPR'] = [0, 0]
        postSynaptic['PVQL'] = [0, 0]
        postSynaptic['PVQR'] = [0, 0]
        postSynaptic['PVR'] = [0, 0]
        postSynaptic['PVT'] = [0, 0]
        postSynaptic['PVWL'] = [0, 0]
        postSynaptic['PVWR'] = [0, 0]
        postSynaptic['RIAL'] = [0, 0]
        postSynaptic['RIAR'] = [0, 0]
        postSynaptic['RIBL'] = [0, 0]
        postSynaptic['RIBR'] = [0, 0]
        postSynaptic['RICL'] = [0, 0]
        postSynaptic['RICR'] = [0, 0]
        postSynaptic['RID'] = [0, 0]
        postSynaptic['RIFL'] = [0, 0]
        postSynaptic['RIFR'] = [0, 0]
        postSynaptic['RIGL'] = [0, 0]
        postSynaptic['RIGR'] = [0, 0]
        postSynaptic['RIH'] = [0, 0]
        postSynaptic['RIML'] = [0, 0]
        postSynaptic['RIMR'] = [0, 0]
        postSynaptic['RIPL'] = [0, 0]
        postSynaptic['RIPR'] = [0, 0]
        postSynaptic['RIR'] = [0, 0]
        postSynaptic['RIS'] = [0, 0]
        postSynaptic['RIVL'] = [0, 0]
        postSynaptic['RIVR'] = [0, 0]
        postSynaptic['RMDDL'] = [0, 0]
        postSynaptic['RMDDR'] = [0, 0]
        postSynaptic['RMDL'] = [0, 0]
        postSynaptic['RMDR'] = [0, 0]
        postSynaptic['RMDVL'] = [0, 0]
        postSynaptic['RMDVR'] = [0, 0]
        postSynaptic['RMED'] = [0, 0]
        postSynaptic['RMEL'] = [0, 0]
        postSynaptic['RMER'] = [0, 0]
        postSynaptic['RMEV'] = [0, 0]
        postSynaptic['RMFL'] = [0, 0]
        postSynaptic['RMFR'] = [0, 0]
        postSynaptic['RMGL'] = [0, 0]
        postSynaptic['RMGR'] = [0, 0]
        postSynaptic['RMHL'] = [0, 0]
        postSynaptic['RMHR'] = [0, 0]
        postSynaptic['SAADL'] = [0, 0]
        postSynaptic['SAADR'] = [0, 0]
        postSynaptic['SAAVL'] = [0, 0]
        postSynaptic['SAAVR'] = [0, 0]
        postSynaptic['SABD'] = [0, 0]
        postSynaptic['SABVL'] = [0, 0]
        postSynaptic['SABVR'] = [0, 0]
        postSynaptic['SDQL'] = [0, 0]
        postSynaptic['SDQR'] = [0, 0]
        postSynaptic['SIADL'] = [0, 0]
        postSynaptic['SIADR'] = [0, 0]
        postSynaptic['SIAVL'] = [0, 0]
        postSynaptic['SIAVR'] = [0, 0]
        postSynaptic['SIBDL'] = [0, 0]
        postSynaptic['SIBDR'] = [0, 0]
        postSynaptic['SIBVL'] = [0, 0]
        postSynaptic['SIBVR'] = [0, 0]
        postSynaptic['SMBDL'] = [0, 0]
        postSynaptic['SMBDR'] = [0, 0]
        postSynaptic['SMBVL'] = [0, 0]
        postSynaptic['SMBVR'] = [0, 0]
        postSynaptic['SMDDL'] = [0, 0]
        postSynaptic['SMDDR'] = [0, 0]
        postSynaptic['SMDVL'] = [0, 0]
        postSynaptic['SMDVR'] = [0, 0]
        postSynaptic['URADL'] = [0, 0]
        postSynaptic['URADR'] = [0, 0]
        postSynaptic['URAVL'] = [0, 0]
        postSynaptic['URAVR'] = [0, 0]
        postSynaptic['URBL'] = [0, 0]
        postSynaptic['URBR'] = [0, 0]
        postSynaptic['URXL'] = [0, 0]
        postSynaptic['URXR'] = [0, 0]
        postSynaptic['URYDL'] = [0, 0]
        postSynaptic['URYDR'] = [0, 0]
        postSynaptic['URYVL'] = [0, 0]
        postSynaptic['URYVR'] = [0, 0]
        postSynaptic['VA1'] = [0, 0]
        postSynaptic['VA10'] = [0, 0]
        postSynaptic['VA11'] = [0, 0]
        postSynaptic['VA12'] = [0, 0]
        postSynaptic['VA2'] = [0, 0]
        postSynaptic['VA3'] = [0, 0]
        postSynaptic['VA4'] = [0, 0]
        postSynaptic['VA5'] = [0, 0]
        postSynaptic['VA6'] = [0, 0]
        postSynaptic['VA7'] = [0, 0]
        postSynaptic['VA8'] = [0, 0]
        postSynaptic['VA9'] = [0, 0]
        postSynaptic['VB1'] = [0, 0]
        postSynaptic['VB10'] = [0, 0]
        postSynaptic['VB11'] = [0, 0]
        postSynaptic['VB2'] = [0, 0]
        postSynaptic['VB3'] = [0, 0]
        postSynaptic['VB4'] = [0, 0]
        postSynaptic['VB5'] = [0, 0]
        postSynaptic['VB6'] = [0, 0]
        postSynaptic['VB7'] = [0, 0]
        postSynaptic['VB8'] = [0, 0]
        postSynaptic['VB9'] = [0, 0]
        postSynaptic['VC1'] = [0, 0]
        postSynaptic['VC2'] = [0, 0]
        postSynaptic['VC3'] = [0, 0]
        postSynaptic['VC4'] = [0, 0]
        postSynaptic['VC5'] = [0, 0]
        postSynaptic['VC6'] = [0, 0]
        postSynaptic['VD1'] = [0, 0]
        postSynaptic['VD10'] = [0, 0]
        postSynaptic['VD11'] = [0, 0]
        postSynaptic['VD12'] = [0, 0]
        postSynaptic['VD13'] = [0, 0]
        postSynaptic['VD2'] = [0, 0]
        postSynaptic['VD3'] = [0, 0]
        postSynaptic['VD4'] = [0, 0]
        postSynaptic['VD5'] = [0, 0]
        postSynaptic['VD6'] = [0, 0]
        postSynaptic['VD7'] = [0, 0]
        postSynaptic['VD8'] = [0, 0]
        postSynaptic['VD9'] = [0, 0]


    # todo make class for brain with these as class variables
    def motorcontrol():
        global accumright
        global accumleft
        global body

        # accumulate left and right muscles and the accumulated values are
        # used to move the left and right motors of the robot

        for muscle in postSynaptic:  # if this doesn't work, do muscle in postSynaptic
            if muscle in mLeft:
                accumleft += postSynaptic[muscle][nextState]

                # print muscle, "Before", postSynaptic[muscle][thisState], accumleft
                # og version uses thisState to reset to 0
                # might be related to bug that would have infinite firing, in fireNeuron
                postSynaptic[muscle][nextState] = 0
                # print muscle, "After", postSynaptic[muscle][thisState], accumleft

            elif muscle in mRight:
                accumright += postSynaptic[muscle][nextState]

                # postSynaptic[muscle][thisState] = 0
                postSynaptic[muscle][nextState] = 0

        angle, mag = body.move(accumleft, accumright)
        accumleft = 0
        accumright = 0


    def dendriteAccumulate(dneuron):
        f = eval(dneuron)
        f()


    def fireNeuron(fneuron):
        # Could use DP for string -> function sigs rather than repeated Evals if this costs time
        # The threshold has been exceeded and we fire the neurite
        if fneuron != "MVULVA":
            f = eval(fneuron)
            f()
            # og version didn't have this
            # I think they added it b/c otherwise it would just have infinite firing
            # postSynaptic[fneuron][thisState] = 0
            postSynaptic[fneuron][nextState] = 0


    def runconnectome():
        """Each time a set of neuron is stimulated, this method will execute
            The weigted values are accumulated in the postSynaptic array
            Once the accumulation is read, we see what neurons are greater
            then the threshold and fire the neuron or muscle that has exceeded
            the threshold.
            """
        global thisState
        global nextState

        for ps in postSynaptic:
            if ps[:3] not in muscles and abs(postSynaptic[ps][thisState]) > threshold:
                fireNeuron(ps)
                # og version resets the entire postsynaptic array at this point
                # fucking why???
        motorcontrol()

        # swap from previous state to next state
        # this data structure could use some improvement
        for ps in postSynaptic:
            # if postSynaptic[ps][thisState] != 0:
            #         print ps
            #         print "Before Clone: ", postSynaptic[ps][thisState]

            # fired neurons keep getting reset to previous weight
            # wtf deepcopy -- So, the concern is that the deepcopy doesnt
            # scale up to larger neural networks??
            # I guess it wasn't working for them when they did it on the entire array?
            postSynaptic[ps][thisState] = copy.deepcopy(postSynaptic[ps][nextState])

            # this deep copy is not in the functioning version currently.
            # print "After Clone: ", postSynaptic[ps][thisState]

        thisState, nextState = nextState, thisState


    # Create the dictionary
    createpostSynaptic()

    def trigger_food_sensors():
        dendriteAccumulate("ADFL")
        dendriteAccumulate("ADFR")

        dendriteAccumulate("ASGL")
        dendriteAccumulate("ASGR")
        dendriteAccumulate("ASIL")
        dendriteAccumulate("ASIR")

        dendriteAccumulate("ASJL")
        dendriteAccumulate("ASJR")

    def trigger_nose_touch_sensors():

        dendriteAccumulate("FLPR")
        dendriteAccumulate("FLPL")
        dendriteAccumulate("ASHL")
        dendriteAccumulate("ASHR")
        dendriteAccumulate("IL1VL")
        dendriteAccumulate("IL1VR")
        dendriteAccumulate("OLQDL")
        dendriteAccumulate("OLQDR")
        dendriteAccumulate("OLQVR")
        dendriteAccumulate("OLQVL")

    def trigger_anterior_harsh_touch_sensors():
        #untested, unused
        dendriteAccumulate("FLPL")
        dendriteAccumulate("FLPR")
        dendriteAccumulate("BDUL")
        dendriteAccumulate("BDUR")
        dendriteAccumulate("SDQR")

    def main(self):
        timestep_n = 5000000000000000000
        #timestep_n = 100000
        food_x = 200
        food_y = 0
        food_r = 50
        #while timestep < timestep_n if timestep_n > 0 else True:
        for timestep in tqdm(range(timestep_n)):
            #print(f"TIMESTEP: {timestep}")
            #if timestep % 6000 == 0:
            #body.clear()
            #turtle.update()


            # Check if it is bumping into the wall, and if so, trigger nose touch
            if body.nose_touching():
                body.cagecolor("black")
                body.pencolor("black")
                trigger_nose_touch_sensors()
                runconnectome()
            else:
                # Otherwise do nothing, unless we encounter food
                # todo we need to handle case where its on the wall and there's food
                #if timestep < 15 or body.distance(food_x,food_y) < food_r:
                if timestep < 15:
                    body.cagecolor("red")
                    body.pencolor("red")
                    trigger_food_sensors()
                    runconnectome()
                    if time_delays:
                        time.sleep(0.5)
                else:
                    body.cagecolor("blue")
                    body.pencolor("blue")
                    # no food sensors, but still run the brain
                    runconnectome()

        body.exit()

        print(np.mean(body.lefts))
        print(np.mean(body.rights))
        print(np.mean(body.rights)-np.mean(body.lefts))

def main():
    nematode = Nematode()
    nematode.main()

if __name__ == '__main__':
    main()
