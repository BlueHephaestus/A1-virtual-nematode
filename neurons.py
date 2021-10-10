
# ADAL -> 0, ADAR -> 1?
# but if we start with [ADAL, ADAR] then we can't modify their ordering

# for a neuron
"""
for a neuron

e.g.
ADAL = ['ADAR', 'ADFL', ...] with values [2, 1, ...]
it's a directed outgoing graph node for each neuron
aka an adjacency list, not adjacency matrix
Also we have two graphs, of the same brain. First one is the current timestep, and
    we formulate the next one to replace that via the neurons propagating one timestep forward

So we really just need one that'll represent the brain at a given timestep,
    and then we can easily just use `curr` to update `next`.

We also want this to be an easily mutateable structure, in lots of ways.
    So that we can run genetic algos on it, and add,remove, and edit anything.
        edit the connection weight, remove connection, add connection,
        or even create or remove entire neurons

So it needs to be a data structure to represent a weighted graph.



"""
def ADAL():
    postSynaptic['ADAR'][nextState] += 2
    postSynaptic['ADFL'][nextState] += 1
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['AIBR'][nextState] += 2
    postSynaptic['ASHL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 4
    postSynaptic['AVBR'][nextState] += 7
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 2
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVJR'][nextState] += 5
    postSynaptic['FLPR'][nextState] += 1
    postSynaptic['PVQL'][nextState] += 1
    postSynaptic['RICL'][nextState] += 1
    postSynaptic['RICR'][nextState] += 1
    postSynaptic['RIML'][nextState] += 3
    postSynaptic['RIPL'][nextState] += 1
    postSynaptic['SMDVR'][nextState] += 2


def ADAR():
    postSynaptic['ADAL'][nextState] += 1
    postSynaptic['ADFR'][nextState] += 1
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['ASHR'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 5
    postSynaptic['AVDL'][nextState] += 2
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVJL'][nextState] += 3
    postSynaptic['PVQR'][nextState] += 1
    postSynaptic['RICL'][nextState] += 1
    postSynaptic['RIMR'][nextState] += 5
    postSynaptic['RIPR'][nextState] += 1
    postSynaptic['RIVR'][nextState] += 1
    postSynaptic['SMDVL'][nextState] += 2


def ADEL():
    postSynaptic['ADAL'][nextState] += 1
    postSynaptic['ADER'][nextState] += 1
    postSynaptic['AINL'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVAR'][nextState] += 3
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVKR'][nextState] += 1
    postSynaptic['AVL'][nextState] += 1
    postSynaptic['BDUL'][nextState] += 1
    postSynaptic['CEPDL'][nextState] += 1
    postSynaptic['FLPL'][nextState] += 1
    postSynaptic['IL1L'][nextState] += 1
    postSynaptic['IL2L'][nextState] += 1
    postSynaptic['MDL05'][nextState] += 1
    postSynaptic['OLLL'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 1
    postSynaptic['RIFL'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 5
    postSynaptic['RIGR'][nextState] += 3
    postSynaptic['RIH'][nextState] += 2
    postSynaptic['RIVL'][nextState] += 1
    postSynaptic['RIVR'][nextState] += 1
    postSynaptic['RMDL'][nextState] += 2
    postSynaptic['RMGL'][nextState] += 1
    postSynaptic['RMHL'][nextState] += 1
    postSynaptic['SIADR'][nextState] += 1
    postSynaptic['SIBDR'][nextState] += 1
    postSynaptic['SMBDR'][nextState] += 1
    postSynaptic['URBL'][nextState] += 1


def ADER():
    postSynaptic['ADAR'][nextState] += 1
    postSynaptic['ADEL'][nextState] += 2
    postSynaptic['ALA'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 5
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 2
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['AVJR'][nextState] += 1
    postSynaptic['AVKL'][nextState] += 2
    postSynaptic['AVKR'][nextState] += 1
    postSynaptic['CEPDR'][nextState] += 1
    postSynaptic['FLPL'][nextState] += 1
    postSynaptic['FLPR'][nextState] += 1
    postSynaptic['OLLR'][nextState] += 2
    postSynaptic['PVR'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 7
    postSynaptic['RIGR'][nextState] += 4
    postSynaptic['RIH'][nextState] += 1
    postSynaptic['RMDR'][nextState] += 2
    postSynaptic['SAAVR'][nextState] += 1


def ADFL():
    postSynaptic['ADAL'][nextState] += 2
    postSynaptic['AIZL'][nextState] += 12
    postSynaptic['AUAL'][nextState] += 5
    postSynaptic['OLQVL'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 15
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RIR'][nextState] += 2
    postSynaptic['SMBVL'][nextState] += 2


def ADFR():
    postSynaptic['ADAR'][nextState] += 2
    postSynaptic['AIAR'][nextState] += 1
    postSynaptic['AIYR'][nextState] += 1
    postSynaptic['AIZR'][nextState] += 8
    postSynaptic['ASHR'][nextState] += 1
    postSynaptic['AUAR'][nextState] += 4
    postSynaptic['AWBR'][nextState] += 1
    postSynaptic['PVPR'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 16
    postSynaptic['RIGR'][nextState] += 3
    postSynaptic['RIR'][nextState] += 3
    postSynaptic['SMBDR'][nextState] += 1
    postSynaptic['SMBVR'][nextState] += 2
    postSynaptic['URXR'][nextState] += 1


def ADLL():
    postSynaptic['ADLR'][nextState] += 1
    postSynaptic['AIAL'][nextState] += 6
    postSynaptic['AIBL'][nextState] += 7
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['ALA'][nextState] += 2
    postSynaptic['ASER'][nextState] += 3
    postSynaptic['ASHL'][nextState] += 2
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVAR'][nextState] += 3
    postSynaptic['AVBL'][nextState] += 2
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 4
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['AVJR'][nextState] += 3
    postSynaptic['AWBL'][nextState] += 2
    postSynaptic['OLQVL'][nextState] += 2
    postSynaptic['RIPL'][nextState] += 1
    postSynaptic['RMGL'][nextState] += 1


def ADLR():
    postSynaptic['ADLL'][nextState] += 1
    postSynaptic['AIAR'][nextState] += 10
    postSynaptic['AIBR'][nextState] += 10
    postSynaptic['ASER'][nextState] += 1
    postSynaptic['ASHR'][nextState] += 3
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['AVDL'][nextState] += 5
    postSynaptic['AVDR'][nextState] += 2
    postSynaptic['AVJR'][nextState] += 1
    postSynaptic['AWCR'][nextState] += 3
    postSynaptic['OLLR'][nextState] += 1
    postSynaptic['PVCL'][nextState] += 1
    postSynaptic['RICL'][nextState] += 1
    postSynaptic['RICR'][nextState] += 1


def AFDL():
    postSynaptic['AFDR'][nextState] += 1
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['AINR'][nextState] += 1
    postSynaptic['AIYL'][nextState] += 7


def AFDR():
    postSynaptic['AFDL'][nextState] += 1
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['AIYR'][nextState] += 13
    postSynaptic['ASER'][nextState] += 1


def AIAL():
    postSynaptic['ADAL'][nextState] += 1
    postSynaptic['AIAR'][nextState] += 1
    postSynaptic['AIBL'][nextState] += 10
    postSynaptic['AIML'][nextState] += 2
    postSynaptic['AIZL'][nextState] += 1
    postSynaptic['ASER'][nextState] += 3
    postSynaptic['ASGL'][nextState] += 1
    postSynaptic['ASHL'][nextState] += 1
    postSynaptic['ASIL'][nextState] += 2
    postSynaptic['ASKL'][nextState] += 3
    postSynaptic['AWAL'][nextState] += 1
    postSynaptic['AWCR'][nextState] += 1
    postSynaptic['HSNL'][nextState] += 1
    postSynaptic['RIFL'][nextState] += 1
    postSynaptic['RMGL'][nextState] += 1


def AIAR():
    postSynaptic['ADAR'][nextState] += 1
    postSynaptic['ADFR'][nextState] += 1
    postSynaptic['ADLR'][nextState] += 2
    postSynaptic['AIAL'][nextState] += 1
    postSynaptic['AIBR'][nextState] += 14
    postSynaptic['AIZR'][nextState] += 1
    postSynaptic['ASER'][nextState] += 1
    postSynaptic['ASGR'][nextState] += 1
    postSynaptic['ASIR'][nextState] += 2
    postSynaptic['AWAR'][nextState] += 2
    postSynaptic['AWCL'][nextState] += 1
    postSynaptic['AWCR'][nextState] += 3
    postSynaptic['RIFR'][nextState] += 2


def AIBL():
    postSynaptic['AFDL'][nextState] += 1
    postSynaptic['AIYL'][nextState] += 1
    postSynaptic['ASER'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 5
    postSynaptic['DVC'][nextState] += 1
    postSynaptic['FLPL'][nextState] += 1
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 4
    postSynaptic['RIFL'][nextState] += 1
    postSynaptic['RIGR'][nextState] += 1
    postSynaptic['RIGR'][nextState] += 3
    postSynaptic['RIML'][nextState] += 2
    postSynaptic['RIMR'][nextState] += 13
    postSynaptic['RIMR'][nextState] += 1
    postSynaptic['RIVL'][nextState] += 1
    postSynaptic['SAADL'][nextState] += 2
    postSynaptic['SAADR'][nextState] += 2
    postSynaptic['SMDDR'][nextState] += 4


def AIBR():
    postSynaptic['AFDR'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 3
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['DB1'][nextState] += 1
    postSynaptic['DVC'][nextState] += 2
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 4
    postSynaptic['RIGL'][nextState] += 3
    postSynaptic['RIML'][nextState] += 16
    postSynaptic['RIML'][nextState] += 1
    postSynaptic['RIMR'][nextState] += 1
    postSynaptic['RIS'][nextState] += 1
    postSynaptic['RIVR'][nextState] += 1
    postSynaptic['SAADL'][nextState] += 1
    postSynaptic['SMDDL'][nextState] += 3
    postSynaptic['SMDVL'][nextState] += 1
    postSynaptic['VB1'][nextState] += 3


def AIML():
    postSynaptic['AIAL'][nextState] += 5
    postSynaptic['ALML'][nextState] += 1
    postSynaptic['ASGL'][nextState] += 2
    postSynaptic['ASKL'][nextState] += 2
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['AVFL'][nextState] += 4
    postSynaptic['AVFR'][nextState] += 1
    postSynaptic['AVHL'][nextState] += 2
    postSynaptic['AVHR'][nextState] += 1
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['PVQL'][nextState] += 1
    postSynaptic['RIFL'][nextState] += 1
    postSynaptic['SIBDR'][nextState] += 1
    postSynaptic['SMBVL'][nextState] += 1


def AIMR():
    postSynaptic['AIAR'][nextState] += 5
    postSynaptic['ASGR'][nextState] += 2
    postSynaptic['ASJR'][nextState] += 2
    postSynaptic['ASKR'][nextState] += 3
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVFL'][nextState] += 1
    postSynaptic['AVFR'][nextState] += 1
    postSynaptic['HSNL'][nextState] += 1
    postSynaptic['HSNR'][nextState] += 2
    postSynaptic['OLQDR'][nextState] += 1
    postSynaptic['PVNR'][nextState] += 1
    postSynaptic['RIFR'][nextState] += 1
    postSynaptic['RMGR'][nextState] += 1


def AINL():
    postSynaptic['ADEL'][nextState] += 1
    postSynaptic['AFDR'][nextState] += 5
    postSynaptic['AINR'][nextState] += 2
    postSynaptic['ASEL'][nextState] += 3
    postSynaptic['ASGR'][nextState] += 2
    postSynaptic['AUAR'][nextState] += 2
    postSynaptic['BAGL'][nextState] += 3
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 2


def AINR():
    postSynaptic['AFDL'][nextState] += 4
    postSynaptic['AFDR'][nextState] += 1
    postSynaptic['AIAL'][nextState] += 2
    postSynaptic['AIBL'][nextState] += 2
    postSynaptic['AINL'][nextState] += 2
    postSynaptic['ASEL'][nextState] += 1
    postSynaptic['ASER'][nextState] += 1
    postSynaptic['ASGL'][nextState] += 1
    postSynaptic['AUAL'][nextState] += 1
    postSynaptic['AUAR'][nextState] += 1
    postSynaptic['BAGR'][nextState] += 3
    postSynaptic['RIBL'][nextState] += 2
    postSynaptic['RID'][nextState] += 1


def AIYL():
    postSynaptic['AIYR'][nextState] += 1
    postSynaptic['AIZL'][nextState] += 13
    postSynaptic['AWAL'][nextState] += 3
    postSynaptic['AWCL'][nextState] += 1
    postSynaptic['AWCR'][nextState] += 1
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 7
    postSynaptic['RIBL'][nextState] += 4
    postSynaptic['RIML'][nextState] += 1


def AIYR():
    postSynaptic['ADFR'][nextState] += 1
    postSynaptic['AIYL'][nextState] += 1
    postSynaptic['AIZR'][nextState] += 8
    postSynaptic['AWAR'][nextState] += 1
    postSynaptic['HSNL'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 6
    postSynaptic['RIBR'][nextState] += 2
    postSynaptic['RIMR'][nextState] += 1


def AIZL():
    postSynaptic['AIAL'][nextState] += 3
    postSynaptic['AIBL'][nextState] += 2
    postSynaptic['AIBR'][nextState] += 8
    postSynaptic['AIZR'][nextState] += 2
    postSynaptic['ASEL'][nextState] += 1
    postSynaptic['ASGL'][nextState] += 1
    postSynaptic['ASHL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 5
    postSynaptic['DVA'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 8
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RIML'][nextState] += 4
    postSynaptic['SMBDL'][nextState] += 9
    postSynaptic['SMBVL'][nextState] += 7
    postSynaptic['VB2'][nextState] += 1


def AIZR():
    postSynaptic['AIAR'][nextState] += 1
    postSynaptic['AIBL'][nextState] += 8
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['AIZL'][nextState] += 2
    postSynaptic['ASGR'][nextState] += 1
    postSynaptic['ASHR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 4
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['AWAR'][nextState] += 1
    postSynaptic['DVA'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 7
    postSynaptic['RIMR'][nextState] += 4
    postSynaptic['SMBDR'][nextState] += 5
    postSynaptic['SMBVR'][nextState] += 3
    postSynaptic['SMDDR'][nextState] += 1


def ALA():
    postSynaptic['ADEL'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 2
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['RID'][nextState] += 1
    postSynaptic['RMDR'][nextState] += 1


def ALML():
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVM'][nextState] += 1
    postSynaptic['BDUL'][nextState] += 6
    postSynaptic['CEPDL'][nextState] += 3
    postSynaptic['CEPVL'][nextState] += 2
    postSynaptic['PVCL'][nextState] += 2
    postSynaptic['PVCR'][nextState] += 1
    postSynaptic['PVR'][nextState] += 1
    postSynaptic['RMDDR'][nextState] += 1
    postSynaptic['RMGL'][nextState] += 1
    postSynaptic['SDQL'][nextState] += 1


def ALMR():
    postSynaptic['AVM'][nextState] += 1
    postSynaptic['BDUR'][nextState] += 5
    postSynaptic['CEPDR'][nextState] += 1
    postSynaptic['CEPVR'][nextState] += 1
    postSynaptic['PVCR'][nextState] += 3
    postSynaptic['RMDDL'][nextState] += 1
    postSynaptic['SIADL'][nextState] += 1


def ALNL():
    postSynaptic['SAAVL'][nextState] += 3
    postSynaptic['SMBDR'][nextState] += 2
    postSynaptic['SMBDR'][nextState] += 1
    postSynaptic['SMDVL'][nextState] += 1


def ALNR():
    postSynaptic['ADER'][nextState] += 1
    postSynaptic['RMHR'][nextState] += 1
    postSynaptic['SAAVR'][nextState] += 2
    postSynaptic['SMBDL'][nextState] += 2
    postSynaptic['SMDDR'][nextState] += 1
    postSynaptic['SMDVL'][nextState] += 1


def AQR():
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 3
    postSynaptic['AVBL'][nextState] += 3
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 4
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['AVKL'][nextState] += 2
    postSynaptic['AVKR'][nextState] += 1
    postSynaptic['BAGL'][nextState] += 2
    postSynaptic['BAGR'][nextState] += 2
    postSynaptic['PVCR'][nextState] += 2
    postSynaptic['PVPL'][nextState] += 1
    postSynaptic['PVPL'][nextState] += 7
    postSynaptic['PVPR'][nextState] += 9
    postSynaptic['RIAL'][nextState] += 3
    postSynaptic['RIAR'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 2
    postSynaptic['RIGR'][nextState] += 1
    postSynaptic['URXL'][nextState] += 1


def AS1():
    postSynaptic['AVAL'][nextState] += 3
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['DA1'][nextState] += 2
    postSynaptic['MDL05'][nextState] += 3
    postSynaptic['MDL08'][nextState] += 3
    postSynaptic['MDR05'][nextState] += 3
    postSynaptic['MDR08'][nextState] += 4
    postSynaptic['VA3'][nextState] += 1
    postSynaptic['VD1'][nextState] += 5
    postSynaptic['VD2'][nextState] += 1


def AS2():
    postSynaptic['DA2'][nextState] += 1
    postSynaptic['DB1'][nextState] += 1
    postSynaptic['DD1'][nextState] += 1
    postSynaptic['MDL07'][nextState] += 3
    postSynaptic['MDL08'][nextState] += 2
    postSynaptic['MDR07'][nextState] += 3
    postSynaptic['MDR08'][nextState] += 3
    postSynaptic['VA4'][nextState] += 2
    postSynaptic['VD2'][nextState] += 10


def AS3():
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['DA2'][nextState] += 1
    postSynaptic['DA3'][nextState] += 1
    postSynaptic['DD1'][nextState] += 1
    postSynaptic['MDL09'][nextState] += 3
    postSynaptic['MDL10'][nextState] += 3
    postSynaptic['MDR09'][nextState] += 3
    postSynaptic['MDR10'][nextState] += 3
    postSynaptic['VA5'][nextState] += 2
    postSynaptic['VD2'][nextState] += 1
    postSynaptic['VD3'][nextState] += 15


def AS4():
    postSynaptic['AS5'][nextState] += 1
    postSynaptic['DA3'][nextState] += 1
    postSynaptic['MDL11'][nextState] += 2
    postSynaptic['MDL12'][nextState] += 2
    postSynaptic['MDR11'][nextState] += 3
    postSynaptic['MDR12'][nextState] += 2
    postSynaptic['VD4'][nextState] += 11


def AS5():
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['DD2'][nextState] += 1
    postSynaptic['MDL11'][nextState] += 2
    postSynaptic['MDL14'][nextState] += 3
    postSynaptic['MDR11'][nextState] += 2
    postSynaptic['MDR14'][nextState] += 3
    postSynaptic['VA7'][nextState] += 1
    postSynaptic['VD5'][nextState] += 9


def AS6():
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['DA5'][nextState] += 2
    postSynaptic['MDL13'][nextState] += 3
    postSynaptic['MDL14'][nextState] += 2
    postSynaptic['MDR13'][nextState] += 3
    postSynaptic['MDR14'][nextState] += 2
    postSynaptic['VA8'][nextState] += 1
    postSynaptic['VD6'][nextState] += 13


def AS7():
    postSynaptic['AVAL'][nextState] += 6
    postSynaptic['AVAR'][nextState] += 5
    postSynaptic['AVBL'][nextState] += 2
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['MDL13'][nextState] += 2
    postSynaptic['MDL16'][nextState] += 3
    postSynaptic['MDR13'][nextState] += 2
    postSynaptic['MDR16'][nextState] += 3


def AS8():
    postSynaptic['AVAL'][nextState] += 4
    postSynaptic['AVAR'][nextState] += 3
    postSynaptic['MDL15'][nextState] += 2
    postSynaptic['MDL18'][nextState] += 3
    postSynaptic['MDR15'][nextState] += 2
    postSynaptic['MDR18'][nextState] += 3


def AS9():
    postSynaptic['AVAL'][nextState] += 4
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['DVB'][nextState] += 7
    postSynaptic['MDL17'][nextState] += 2
    postSynaptic['MDL20'][nextState] += 3
    postSynaptic['MDR17'][nextState] += 2
    postSynaptic['MDR20'][nextState] += 3


def AS10():
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['MDL19'][nextState] += 3
    postSynaptic['MDL20'][nextState] += 2
    postSynaptic['MDR19'][nextState] += 3
    postSynaptic['MDR20'][nextState] += 2


# todo: duplicate PDB?
def AS11():
    postSynaptic['MDL21'][nextState] += 1
    postSynaptic['MDL22'][nextState] += 1
    postSynaptic['MDL23'][nextState] += 1
    postSynaptic['MDL24'][nextState] += 1
    postSynaptic['MDR21'][nextState] += 1
    postSynaptic['MDR22'][nextState] += 1
    postSynaptic['MDR23'][nextState] += 1
    postSynaptic['MDR24'][nextState] += 1
    postSynaptic['PDA'][nextState] += 1
    postSynaptic['PDB'][nextState] += 1
    postSynaptic['PDB'][nextState] += 2
    postSynaptic['VD13'][nextState] += 2


def ASEL():
    postSynaptic['ADFR'][nextState] += 1
    postSynaptic['AIAL'][nextState] += 3
    postSynaptic['AIBL'][nextState] += 7
    postSynaptic['AIBR'][nextState] += 2
    postSynaptic['AIYL'][nextState] += 13
    postSynaptic['AIYR'][nextState] += 6
    postSynaptic['AWCL'][nextState] += 4
    postSynaptic['AWCR'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 1


def ASER():
    postSynaptic['AFDL'][nextState] += 1
    postSynaptic['AFDR'][nextState] += 2
    postSynaptic['AIAL'][nextState] += 1
    postSynaptic['AIAR'][nextState] += 3
    postSynaptic['AIBL'][nextState] += 2
    postSynaptic['AIBR'][nextState] += 10
    postSynaptic['AIYL'][nextState] += 2
    postSynaptic['AIYR'][nextState] += 14
    postSynaptic['AWAR'][nextState] += 1
    postSynaptic['AWCL'][nextState] += 1
    postSynaptic['AWCR'][nextState] += 1


def ASGL():
    postSynaptic['AIAL'][nextState] += 9
    postSynaptic['AIBL'][nextState] += 3
    postSynaptic['AINR'][nextState] += 2
    postSynaptic['AIZL'][nextState] += 1
    postSynaptic['ASKL'][nextState] += 1


def ASGR():
    postSynaptic['AIAR'][nextState] += 10
    postSynaptic['AIBR'][nextState] += 2
    postSynaptic['AINL'][nextState] += 1
    postSynaptic['AIYR'][nextState] += 1
    postSynaptic['AIZR'][nextState] += 1


def ASHL():
    postSynaptic['ADAL'][nextState] += 2
    postSynaptic['ADFL'][nextState] += 3
    postSynaptic['AIAL'][nextState] += 7
    postSynaptic['AIBL'][nextState] += 5
    postSynaptic['AIZL'][nextState] += 1
    postSynaptic['ASHR'][nextState] += 1
    postSynaptic['ASKL'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 6
    postSynaptic['AVDL'][nextState] += 2
    postSynaptic['AVDR'][nextState] += 2
    postSynaptic['RIAL'][nextState] += 4
    postSynaptic['RICL'][nextState] += 2
    postSynaptic['RIML'][nextState] += 1
    postSynaptic['RIPL'][nextState] += 1
    postSynaptic['RMGL'][nextState] += 1


def ASHR():
    postSynaptic['ADAR'][nextState] += 3
    postSynaptic['ADFR'][nextState] += 2
    postSynaptic['AIAR'][nextState] += 10
    postSynaptic['AIBR'][nextState] += 3
    postSynaptic['AIZR'][nextState] += 1
    postSynaptic['ASHL'][nextState] += 1
    postSynaptic['ASKR'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 5
    postSynaptic['AVBR'][nextState] += 3
    postSynaptic['AVDL'][nextState] += 5
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVER'][nextState] += 3
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['PVPR'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 2
    postSynaptic['RICR'][nextState] += 2
    postSynaptic['RMGR'][nextState] += 2
    postSynaptic['RMGR'][nextState] += 1


def ASIL():
    postSynaptic['AIAL'][nextState] += 2
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['AIYL'][nextState] += 2
    postSynaptic['AIZL'][nextState] += 1
    postSynaptic['ASER'][nextState] += 1
    postSynaptic['ASIR'][nextState] += 1
    postSynaptic['ASKL'][nextState] += 2
    postSynaptic['AWCL'][nextState] += 1
    postSynaptic['AWCR'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 1


def ASIR():
    postSynaptic['AIAL'][nextState] += 1
    postSynaptic['AIAR'][nextState] += 3
    postSynaptic['AIAR'][nextState] += 2
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['ASEL'][nextState] += 2
    postSynaptic['ASHR'][nextState] += 1
    postSynaptic['ASIL'][nextState] += 1
    postSynaptic['AWCL'][nextState] += 1
    postSynaptic['AWCR'][nextState] += 1


def ASJL():
    postSynaptic['ASJR'][nextState] += 1
    postSynaptic['ASKL'][nextState] += 4
    postSynaptic['HSNL'][nextState] += 1
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['PVQL'][nextState] += 14


def ASJR():
    postSynaptic['ASJL'][nextState] += 1
    postSynaptic['ASKR'][nextState] += 4
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['PVQR'][nextState] += 13


def ASKL():
    postSynaptic['AIAL'][nextState] += 11
    postSynaptic['AIBL'][nextState] += 2
    postSynaptic['AIML'][nextState] += 2
    postSynaptic['ASKR'][nextState] += 1
    postSynaptic['PVQL'][nextState] += 5
    postSynaptic['RMGL'][nextState] += 1


def ASKR():
    postSynaptic['AIAR'][nextState] += 11
    postSynaptic['AIMR'][nextState] += 1
    postSynaptic['ASHR'][nextState] += 1
    postSynaptic['ASKL'][nextState] += 1
    postSynaptic['AWAR'][nextState] += 1
    postSynaptic['CEPVR'][nextState] += 1
    postSynaptic['PVQR'][nextState] += 4
    postSynaptic['RIFR'][nextState] += 1
    postSynaptic['RMGR'][nextState] += 1


def AUAL():
    postSynaptic['AINR'][nextState] += 1
    postSynaptic['AUAR'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 3
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 3
    postSynaptic['AWBL'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 5
    postSynaptic['RIBL'][nextState] += 9


def AUAR():
    postSynaptic['AINL'][nextState] += 1
    postSynaptic['AIYR'][nextState] += 1
    postSynaptic['AUAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVER'][nextState] += 4
    postSynaptic['AWBR'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 6
    postSynaptic['RIBR'][nextState] += 13
    postSynaptic['URXR'][nextState] += 1


def AVAL():
    postSynaptic['AS1'][nextState] += 3
    postSynaptic['AS10'][nextState] += 3
    postSynaptic['AS11'][nextState] += 4
    postSynaptic['AS2'][nextState] += 1
    postSynaptic['AS3'][nextState] += 3
    postSynaptic['AS4'][nextState] += 1
    postSynaptic['AS5'][nextState] += 4
    postSynaptic['AS6'][nextState] += 1
    postSynaptic['AS7'][nextState] += 14
    postSynaptic['AS8'][nextState] += 9
    postSynaptic['AS9'][nextState] += 12
    postSynaptic['AVAR'][nextState] += 7
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVHL'][nextState] += 1
    postSynaptic['AVJL'][nextState] += 2
    postSynaptic['DA1'][nextState] += 4
    postSynaptic['DA2'][nextState] += 4
    postSynaptic['DA3'][nextState] += 6
    postSynaptic['DA4'][nextState] += 10
    postSynaptic['DA5'][nextState] += 8
    postSynaptic['DA6'][nextState] += 21
    postSynaptic['DA7'][nextState] += 4
    postSynaptic['DA8'][nextState] += 4
    postSynaptic['DA9'][nextState] += 3
    postSynaptic['DB5'][nextState] += 2
    postSynaptic['DB6'][nextState] += 4
    postSynaptic['FLPL'][nextState] += 1
    postSynaptic['LUAL'][nextState] += 2
    postSynaptic['PVCL'][nextState] += 12
    postSynaptic['PVCR'][nextState] += 11
    postSynaptic['PVPL'][nextState] += 1
    postSynaptic['RIMR'][nextState] += 3
    postSynaptic['SABD'][nextState] += 4
    postSynaptic['SABVR'][nextState] += 1
    postSynaptic['SDQR'][nextState] += 1
    postSynaptic['URYDL'][nextState] += 1
    postSynaptic['URYVR'][nextState] += 1
    postSynaptic['VA1'][nextState] += 3
    postSynaptic['VA10'][nextState] += 6
    postSynaptic['VA11'][nextState] += 7
    postSynaptic['VA12'][nextState] += 2
    postSynaptic['VA2'][nextState] += 5
    postSynaptic['VA3'][nextState] += 3
    postSynaptic['VA4'][nextState] += 3
    postSynaptic['VA5'][nextState] += 8
    postSynaptic['VA6'][nextState] += 10
    postSynaptic['VA7'][nextState] += 2
    postSynaptic['VA8'][nextState] += 19
    postSynaptic['VA9'][nextState] += 8
    postSynaptic['VB9'][nextState] += 5


def AVAR():
    postSynaptic['ADER'][nextState] += 1
    postSynaptic['AS1'][nextState] += 3
    postSynaptic['AS10'][nextState] += 2
    postSynaptic['AS11'][nextState] += 6
    postSynaptic['AS2'][nextState] += 2
    postSynaptic['AS3'][nextState] += 2
    postSynaptic['AS4'][nextState] += 1
    postSynaptic['AS5'][nextState] += 2
    postSynaptic['AS6'][nextState] += 3
    postSynaptic['AS7'][nextState] += 8
    postSynaptic['AS8'][nextState] += 9
    postSynaptic['AS9'][nextState] += 6
    postSynaptic['AVAL'][nextState] += 6
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 2
    postSynaptic['AVEL'][nextState] += 2
    postSynaptic['AVER'][nextState] += 2
    postSynaptic['DA1'][nextState] += 8
    postSynaptic['DA2'][nextState] += 4
    postSynaptic['DA3'][nextState] += 5
    postSynaptic['DA4'][nextState] += 8
    postSynaptic['DA5'][nextState] += 7
    postSynaptic['DA6'][nextState] += 13
    postSynaptic['DA7'][nextState] += 3
    postSynaptic['DA8'][nextState] += 9
    postSynaptic['DA9'][nextState] += 2
    postSynaptic['DB3'][nextState] += 1
    postSynaptic['DB5'][nextState] += 3
    postSynaptic['DB6'][nextState] += 5
    postSynaptic['LUAL'][nextState] += 1
    postSynaptic['LUAR'][nextState] += 3
    postSynaptic['PDEL'][nextState] += 1
    postSynaptic['PDER'][nextState] += 1
    postSynaptic['PVCL'][nextState] += 7
    postSynaptic['PVCR'][nextState] += 8
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RIML'][nextState] += 2
    postSynaptic['RIMR'][nextState] += 1
    postSynaptic['SABD'][nextState] += 1
    postSynaptic['SABVL'][nextState] += 6
    postSynaptic['SABVR'][nextState] += 1
    postSynaptic['URYDR'][nextState] += 1
    postSynaptic['URYVL'][nextState] += 1
    postSynaptic['VA10'][nextState] += 5
    postSynaptic['VA11'][nextState] += 15
    postSynaptic['VA12'][nextState] += 1
    postSynaptic['VA2'][nextState] += 2
    postSynaptic['VA3'][nextState] += 7
    postSynaptic['VA4'][nextState] += 5
    postSynaptic['VA5'][nextState] += 4
    postSynaptic['VA6'][nextState] += 5
    postSynaptic['VA7'][nextState] += 4
    postSynaptic['VA8'][nextState] += 16
    postSynaptic['VB9'][nextState] += 10
    postSynaptic['VD13'][nextState] += 2


def AVBL():
    postSynaptic['AQR'][nextState] += 1
    postSynaptic['AS10'][nextState] += 1
    postSynaptic['AS3'][nextState] += 1
    postSynaptic['AS4'][nextState] += 1
    postSynaptic['AS5'][nextState] += 1
    postSynaptic['AS6'][nextState] += 1
    postSynaptic['AS7'][nextState] += 2
    postSynaptic['AS9'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 7
    postSynaptic['AVAR'][nextState] += 7
    postSynaptic['AVBR'][nextState] += 4
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 2
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 2
    postSynaptic['AVL'][nextState] += 1
    postSynaptic['DB3'][nextState] += 1
    postSynaptic['DB4'][nextState] += 1
    postSynaptic['DB5'][nextState] += 1
    postSynaptic['DB6'][nextState] += 2
    postSynaptic['DB7'][nextState] += 2
    postSynaptic['DVA'][nextState] += 1
    postSynaptic['PVNR'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RID'][nextState] += 1
    postSynaptic['SDQR'][nextState] += 1
    postSynaptic['SIBVL'][nextState] += 1
    postSynaptic['VA10'][nextState] += 1
    postSynaptic['VA2'][nextState] += 1
    postSynaptic['VA7'][nextState] += 1
    postSynaptic['VB1'][nextState] += 1
    postSynaptic['VB10'][nextState] += 2
    postSynaptic['VB11'][nextState] += 2
    postSynaptic['VB2'][nextState] += 4
    postSynaptic['VB4'][nextState] += 1
    postSynaptic['VB5'][nextState] += 1
    postSynaptic['VB6'][nextState] += 1
    postSynaptic['VB7'][nextState] += 2
    postSynaptic['VB8'][nextState] += 7
    postSynaptic['VB9'][nextState] += 1
    postSynaptic['VC3'][nextState] += 1


def AVBR():
    postSynaptic['AS1'][nextState] += 1
    postSynaptic['AS10'][nextState] += 1
    postSynaptic['AS3'][nextState] += 1
    postSynaptic['AS4'][nextState] += 1
    postSynaptic['AS5'][nextState] += 1
    postSynaptic['AS6'][nextState] += 2
    postSynaptic['AS7'][nextState] += 3
    postSynaptic['AVAL'][nextState] += 6
    postSynaptic['AVAR'][nextState] += 7
    postSynaptic['AVBL'][nextState] += 4
    postSynaptic['DA5'][nextState] += 1
    postSynaptic['DB1'][nextState] += 3
    postSynaptic['DB2'][nextState] += 1
    postSynaptic['DB3'][nextState] += 1
    postSynaptic['DB4'][nextState] += 1
    postSynaptic['DB5'][nextState] += 1
    postSynaptic['DB6'][nextState] += 1
    postSynaptic['DB7'][nextState] += 1
    postSynaptic['DD1'][nextState] += 1
    postSynaptic['DVA'][nextState] += 1
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['PVNL'][nextState] += 2
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RID'][nextState] += 2
    postSynaptic['SIBVL'][nextState] += 1
    postSynaptic['VA4'][nextState] += 1
    postSynaptic['VA8'][nextState] += 1
    postSynaptic['VA9'][nextState] += 2
    postSynaptic['VB10'][nextState] += 1
    postSynaptic['VB11'][nextState] += 1
    postSynaptic['VB2'][nextState] += 1
    postSynaptic['VB3'][nextState] += 1
    postSynaptic['VB4'][nextState] += 1
    postSynaptic['VB6'][nextState] += 2
    postSynaptic['VB7'][nextState] += 2
    postSynaptic['VB8'][nextState] += 3
    postSynaptic['VB9'][nextState] += 6
    postSynaptic['VD10'][nextState] += 1
    postSynaptic['VD3'][nextState] += 1


def AVDL():
    postSynaptic['ADAR'][nextState] += 2
    postSynaptic['AS1'][nextState] += 1
    postSynaptic['AS10'][nextState] += 1
    postSynaptic['AS11'][nextState] += 2
    postSynaptic['AS4'][nextState] += 1
    postSynaptic['AS5'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 13
    postSynaptic['AVAR'][nextState] += 19
    postSynaptic['AVM'][nextState] += 2
    postSynaptic['DA1'][nextState] += 1
    postSynaptic['DA2'][nextState] += 1
    postSynaptic['DA3'][nextState] += 4
    postSynaptic['DA4'][nextState] += 1
    postSynaptic['DA5'][nextState] += 1
    postSynaptic['DA8'][nextState] += 1
    postSynaptic['FLPL'][nextState] += 1
    postSynaptic['FLPR'][nextState] += 1
    postSynaptic['LUAL'][nextState] += 1
    postSynaptic['PVCL'][nextState] += 1
    postSynaptic['SABD'][nextState] += 1
    postSynaptic['SABVL'][nextState] += 1
    postSynaptic['SABVR'][nextState] += 1
    postSynaptic['VA5'][nextState] += 1


def AVDR():
    postSynaptic['ADAL'][nextState] += 2
    postSynaptic['ADLL'][nextState] += 1
    postSynaptic['AS10'][nextState] += 1
    postSynaptic['AS5'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 16
    postSynaptic['AVAR'][nextState] += 15
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVDL'][nextState] += 2
    postSynaptic['AVJL'][nextState] += 2
    postSynaptic['DA1'][nextState] += 2
    postSynaptic['DA2'][nextState] += 1
    postSynaptic['DA3'][nextState] += 1
    postSynaptic['DA4'][nextState] += 1
    postSynaptic['DA5'][nextState] += 2
    postSynaptic['DA8'][nextState] += 1
    postSynaptic['DA9'][nextState] += 1
    postSynaptic['DB4'][nextState] += 1
    postSynaptic['DVC'][nextState] += 1
    postSynaptic['FLPR'][nextState] += 1
    postSynaptic['LUAL'][nextState] += 2
    postSynaptic['PQR'][nextState] += 1
    postSynaptic['SABD'][nextState] += 1
    postSynaptic['SABVL'][nextState] += 3
    postSynaptic['SABVR'][nextState] += 1
    postSynaptic['VA11'][nextState] += 1
    postSynaptic['VA2'][nextState] += 1
    postSynaptic['VA3'][nextState] += 2
    postSynaptic['VA6'][nextState] += 1


def AVEL():
    postSynaptic['AS1'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 12
    postSynaptic['AVAR'][nextState] += 7
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['DA1'][nextState] += 5
    postSynaptic['DA2'][nextState] += 1
    postSynaptic['DA3'][nextState] += 3
    postSynaptic['DA4'][nextState] += 1
    postSynaptic['PVCR'][nextState] += 1
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['RIML'][nextState] += 2
    postSynaptic['RIMR'][nextState] += 3
    postSynaptic['RMDVR'][nextState] += 1
    postSynaptic['RMEV'][nextState] += 1
    postSynaptic['SABD'][nextState] += 6
    postSynaptic['SABVL'][nextState] += 7
    postSynaptic['SABVR'][nextState] += 3
    postSynaptic['VA1'][nextState] += 5
    postSynaptic['VA3'][nextState] += 3
    postSynaptic['VD2'][nextState] += 1
    postSynaptic['VD3'][nextState] += 1


def AVER():
    postSynaptic['AS1'][nextState] += 3
    postSynaptic['AS2'][nextState] += 2
    postSynaptic['AS3'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 7
    postSynaptic['AVAR'][nextState] += 16
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['DA1'][nextState] += 5
    postSynaptic['DA2'][nextState] += 3
    postSynaptic['DA3'][nextState] += 1
    postSynaptic['DB3'][nextState] += 1
    postSynaptic['RIML'][nextState] += 3
    postSynaptic['RIMR'][nextState] += 2
    postSynaptic['RMDVL'][nextState] += 1
    postSynaptic['RMDVR'][nextState] += 1
    postSynaptic['RMEV'][nextState] += 1
    postSynaptic['SABD'][nextState] += 2
    postSynaptic['SABVL'][nextState] += 3
    postSynaptic['SABVR'][nextState] += 3
    postSynaptic['VA1'][nextState] += 1
    postSynaptic['VA2'][nextState] += 1
    postSynaptic['VA3'][nextState] += 2
    postSynaptic['VA4'][nextState] += 1
    postSynaptic['VA5'][nextState] += 1


def AVFL():
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['AVFR'][nextState] += 30
    postSynaptic['AVG'][nextState] += 1
    postSynaptic['AVHL'][nextState] += 4
    postSynaptic['AVHR'][nextState] += 7
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['AVJR'][nextState] += 1
    postSynaptic['AVL'][nextState] += 1
    postSynaptic['HSNL'][nextState] += 1
    postSynaptic['MVL11'][nextState] += 1
    postSynaptic['MVL12'][nextState] += 1
    postSynaptic['PDER'][nextState] += 1
    postSynaptic['PVNL'][nextState] += 2
    postSynaptic['PVQL'][nextState] += 1
    postSynaptic['PVQR'][nextState] += 2
    postSynaptic['VB1'][nextState] += 1


def AVFR():
    postSynaptic['ASJL'][nextState] += 1
    postSynaptic['ASKL'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 5
    postSynaptic['AVFL'][nextState] += 24
    postSynaptic['AVHL'][nextState] += 4
    postSynaptic['AVHR'][nextState] += 2
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['AVJR'][nextState] += 1
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['MVL14'][nextState] += 2
    postSynaptic['MVR14'][nextState] += 2
    postSynaptic['PVQL'][nextState] += 1
    postSynaptic['VC4'][nextState] += 1
    postSynaptic['VD11'][nextState] += 1


def AVG():
    postSynaptic['AVAR'][nextState] += 3
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['AVFL'][nextState] += 1
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['AVL'][nextState] += 1
    postSynaptic['DA8'][nextState] += 1
    postSynaptic['PHAL'][nextState] += 2
    postSynaptic['PVCL'][nextState] += 1
    postSynaptic['PVNR'][nextState] += 1
    postSynaptic['PVPR'][nextState] += 1
    postSynaptic['PVQR'][nextState] += 1
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['RIFL'][nextState] += 1
    postSynaptic['RIFR'][nextState] += 1
    postSynaptic['VA11'][nextState] += 1


def AVHL():
    postSynaptic['ADFR'][nextState] += 3
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVFL'][nextState] += 1
    postSynaptic['AVFL'][nextState] += 2
    postSynaptic['AVFR'][nextState] += 5
    postSynaptic['AVHR'][nextState] += 2
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['AWBR'][nextState] += 1
    postSynaptic['PHBR'][nextState] += 1
    postSynaptic['PVPR'][nextState] += 2
    postSynaptic['PVQL'][nextState] += 1
    postSynaptic['PVQR'][nextState] += 2
    postSynaptic['RIMR'][nextState] += 1
    postSynaptic['RIR'][nextState] += 3
    postSynaptic['SMBDR'][nextState] += 1
    postSynaptic['SMBVR'][nextState] += 1
    postSynaptic['VD1'][nextState] += 1


def AVHR():
    postSynaptic['ADLL'][nextState] += 1
    postSynaptic['ADLR'][nextState] += 2
    postSynaptic['AQR'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 2
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVFL'][nextState] += 1
    postSynaptic['AVFR'][nextState] += 2
    postSynaptic['AVHL'][nextState] += 2
    postSynaptic['AVJR'][nextState] += 4
    postSynaptic['PVNL'][nextState] += 1
    postSynaptic['PVPL'][nextState] += 3
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RIR'][nextState] += 4
    postSynaptic['SMBDL'][nextState] += 1
    postSynaptic['SMBVL'][nextState] += 1


def AVJL():
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 4
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 2
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVFR'][nextState] += 1
    postSynaptic['AVHL'][nextState] += 2
    postSynaptic['AVJR'][nextState] += 4
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['PLMR'][nextState] += 2
    postSynaptic['PVCL'][nextState] += 2
    postSynaptic['PVCR'][nextState] += 5
    postSynaptic['PVNR'][nextState] += 1
    postSynaptic['RIFR'][nextState] += 1
    postSynaptic['RIS'][nextState] += 2


def AVJR():
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 3
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 3
    postSynaptic['AVER'][nextState] += 3
    postSynaptic['AVJL'][nextState] += 5
    postSynaptic['PVCL'][nextState] += 3
    postSynaptic['PVCR'][nextState] += 4
    postSynaptic['PVQR'][nextState] += 1
    postSynaptic['SABVL'][nextState] += 1


def AVKL():
    postSynaptic['ADER'][nextState] += 1
    postSynaptic['AQR'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 2
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['AVKR'][nextState] += 2
    postSynaptic['AVM'][nextState] += 1
    postSynaptic['DVA'][nextState] += 1
    postSynaptic['PDEL'][nextState] += 3
    postSynaptic['PDER'][nextState] += 1
    postSynaptic['PVM'][nextState] += 1
    postSynaptic['PVPL'][nextState] += 1
    postSynaptic['PVPR'][nextState] += 1
    postSynaptic['PVT'][nextState] += 2
    postSynaptic['RICL'][nextState] += 1
    postSynaptic['RICR'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RIML'][nextState] += 2
    postSynaptic['RIMR'][nextState] += 1
    postSynaptic['RMFR'][nextState] += 1
    postSynaptic['SAADR'][nextState] += 1
    postSynaptic['SIAVR'][nextState] += 1
    postSynaptic['SMBDL'][nextState] += 1
    postSynaptic['SMBDR'][nextState] += 1
    postSynaptic['SMBVR'][nextState] += 1
    postSynaptic['SMDDR'][nextState] += 1
    postSynaptic['VB1'][nextState] += 4
    postSynaptic['VB10'][nextState] += 1


def AVKR():
    postSynaptic['ADEL'][nextState] += 1
    postSynaptic['AQR'][nextState] += 1
    postSynaptic['AVKL'][nextState] += 2
    postSynaptic['BDUL'][nextState] += 1
    postSynaptic['MVL10'][nextState] += 1
    postSynaptic['PVPL'][nextState] += 6
    postSynaptic['PVQL'][nextState] += 1
    postSynaptic['RICL'][nextState] += 1
    postSynaptic['RIGR'][nextState] += 1
    postSynaptic['RIML'][nextState] += 2
    postSynaptic['RIMR'][nextState] += 2
    postSynaptic['RMDR'][nextState] += 1
    postSynaptic['RMFL'][nextState] += 1
    postSynaptic['SAADL'][nextState] += 1
    postSynaptic['SMBDL'][nextState] += 2
    postSynaptic['SMBDR'][nextState] += 2
    postSynaptic['SMBVR'][nextState] += 1
    postSynaptic['SMDDL'][nextState] += 1
    postSynaptic['SMDDR'][nextState] += 2


def AVL():
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVFR'][nextState] += 1
    postSynaptic['DA2'][nextState] += 1
    postSynaptic['DD1'][nextState] += 1
    postSynaptic['DD6'][nextState] += 2
    postSynaptic['DVB'][nextState] += 1
    postSynaptic['DVC'][nextState] += 9
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['MVL10'][nextState] += -5
    postSynaptic['MVR10'][nextState] += -5
    postSynaptic['PVM'][nextState] += 1
    postSynaptic['PVPR'][nextState] += 1
    postSynaptic['PVWL'][nextState] += 1
    postSynaptic['SABD'][nextState] += 5
    postSynaptic['SABVL'][nextState] += 4
    postSynaptic['SABVR'][nextState] += 3
    postSynaptic['VD12'][nextState] += 4


def AVM():
    postSynaptic['ADER'][nextState] += 1
    postSynaptic['ALML'][nextState] += 1
    postSynaptic['ALMR'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 6
    postSynaptic['AVBR'][nextState] += 6
    postSynaptic['AVDL'][nextState] += 2
    postSynaptic['AVJR'][nextState] += 1
    postSynaptic['BDUL'][nextState] += 3
    postSynaptic['BDUR'][nextState] += 2
    postSynaptic['DA1'][nextState] += 1
    postSynaptic['PVCL'][nextState] += 4
    postSynaptic['PVCR'][nextState] += 5
    postSynaptic['PVNL'][nextState] += 1
    postSynaptic['PVR'][nextState] += 3
    postSynaptic['RID'][nextState] += 1
    postSynaptic['SIBVL'][nextState] += 1
    postSynaptic['VA1'][nextState] += 2


def AWAL():
    postSynaptic['ADAL'][nextState] += 1
    postSynaptic['AFDL'][nextState] += 5
    postSynaptic['AIAL'][nextState] += 1
    postSynaptic['AIYL'][nextState] += 1
    postSynaptic['AIZL'][nextState] += 10
    postSynaptic['ASEL'][nextState] += 4
    postSynaptic['ASGL'][nextState] += 1
    postSynaptic['AWAR'][nextState] += 1
    postSynaptic['AWBL'][nextState] += 1


def AWAR():
    postSynaptic['ADFR'][nextState] += 3
    postSynaptic['AFDR'][nextState] += 7
    postSynaptic['AIAR'][nextState] += 1
    postSynaptic['AIYR'][nextState] += 2
    postSynaptic['AIZR'][nextState] += 7
    postSynaptic['AIZR'][nextState] += 1
    postSynaptic['ASEL'][nextState] += 1
    postSynaptic['ASER'][nextState] += 2
    postSynaptic['AUAR'][nextState] += 1
    postSynaptic['AWAL'][nextState] += 1
    postSynaptic['AWBR'][nextState] += 1
    postSynaptic['RIFR'][nextState] += 2
    postSynaptic['RIGR'][nextState] += 1
    postSynaptic['RIR'][nextState] += 2


def AWBL():
    postSynaptic['ADFL'][nextState] += 9
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['AIZL'][nextState] += 9
    postSynaptic['AUAL'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AWBR'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 3
    postSynaptic['RMGL'][nextState] += 1
    postSynaptic['SMBDL'][nextState] += 1


def AWBR():
    postSynaptic['ADFR'][nextState] += 4
    postSynaptic['AIZR'][nextState] += 4
    postSynaptic['ASGR'][nextState] += 1
    postSynaptic['ASHR'][nextState] += 2
    postSynaptic['AUAR'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['AWBL'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 1
    postSynaptic['RICL'][nextState] += 1
    postSynaptic['RIR'][nextState] += 2
    postSynaptic['RMGR'][nextState] += 1
    postSynaptic['SMBVR'][nextState] += 1


def AWCL():
    postSynaptic['AIAL'][nextState] += 2
    postSynaptic['AIAR'][nextState] += 4
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['AIYL'][nextState] += 10
    postSynaptic['ASEL'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AWCR'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 3


def AWCR():
    postSynaptic['AIAR'][nextState] += 1
    postSynaptic['AIBR'][nextState] += 4
    postSynaptic['AIYL'][nextState] += 4
    postSynaptic['AIYR'][nextState] += 9
    postSynaptic['ASEL'][nextState] += 1
    postSynaptic['ASGR'][nextState] += 1
    postSynaptic['AWCL'][nextState] += 5


def BAGL():
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 4
    postSynaptic['BAGR'][nextState] += 2
    postSynaptic['RIAR'][nextState] += 5
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 7
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RIGR'][nextState] += 4
    postSynaptic['RIGR'][nextState] += 1
    postSynaptic['RIR'][nextState] += 1


def BAGR():
    postSynaptic['AIYL'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 2
    postSynaptic['BAGL'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 5
    postSynaptic['RIBL'][nextState] += 4
    postSynaptic['RIGL'][nextState] += 5
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RIR'][nextState] += 1


def BDUL():
    postSynaptic['ADEL'][nextState] += 3
    postSynaptic['AVHL'][nextState] += 1
    postSynaptic['AVJR'][nextState] += 1
    postSynaptic['HSNL'][nextState] += 1
    postSynaptic['PVNL'][nextState] += 2
    postSynaptic['PVNR'][nextState] += 2
    postSynaptic['SAADL'][nextState] += 1
    postSynaptic['URADL'][nextState] += 1


def BDUR():
    postSynaptic['ADER'][nextState] += 1
    postSynaptic['ALMR'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 3
    postSynaptic['AVHL'][nextState] += 1
    postSynaptic['AVJL'][nextState] += 2
    postSynaptic['HSNR'][nextState] += 4
    postSynaptic['PVCL'][nextState] += 1
    postSynaptic['PVNL'][nextState] += 2
    postSynaptic['PVNR'][nextState] += 1
    postSynaptic['SDQL'][nextState] += 1
    postSynaptic['URADR'][nextState] += 1


def CEPDL():
    postSynaptic['AVER'][nextState] += 5
    postSynaptic['IL1DL'][nextState] += 4
    postSynaptic['OLLL'][nextState] += 2
    postSynaptic['OLQDL'][nextState] += 6
    postSynaptic['OLQDL'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 2
    postSynaptic['RICL'][nextState] += 1
    postSynaptic['RICR'][nextState] += 2
    postSynaptic['RIH'][nextState] += 1
    postSynaptic['RIPL'][nextState] += 2
    postSynaptic['RIS'][nextState] += 1
    postSynaptic['RMDVL'][nextState] += 3
    postSynaptic['RMGL'][nextState] += 4
    postSynaptic['RMHR'][nextState] += 4
    postSynaptic['SIADR'][nextState] += 1
    postSynaptic['SMBDR'][nextState] += 1
    postSynaptic['URADL'][nextState] += 2
    postSynaptic['URBL'][nextState] += 4
    postSynaptic['URYDL'][nextState] += 2


def CEPDR():
    postSynaptic['AVEL'][nextState] += 6
    postSynaptic['BDUR'][nextState] += 1
    postSynaptic['IL1DR'][nextState] += 5
    postSynaptic['IL1R'][nextState] += 1
    postSynaptic['OLLR'][nextState] += 8
    postSynaptic['OLQDR'][nextState] += 5
    postSynaptic['OLQDR'][nextState] += 2
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RICL'][nextState] += 4
    postSynaptic['RICR'][nextState] += 3
    postSynaptic['RIH'][nextState] += 1
    postSynaptic['RIS'][nextState] += 1
    postSynaptic['RMDDL'][nextState] += 1
    postSynaptic['RMDVR'][nextState] += 2
    postSynaptic['RMGR'][nextState] += 1
    postSynaptic['RMHL'][nextState] += 4
    postSynaptic['RMHR'][nextState] += 1
    postSynaptic['SIADL'][nextState] += 1
    postSynaptic['SMBDR'][nextState] += 1
    postSynaptic['URADR'][nextState] += 1
    postSynaptic['URBR'][nextState] += 2
    postSynaptic['URYDR'][nextState] += 1


def CEPVL():
    postSynaptic['ADLL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 3
    postSynaptic['IL1VL'][nextState] += 2
    postSynaptic['MVL03'][nextState] += 1
    postSynaptic['OLLL'][nextState] += 4
    postSynaptic['OLQVL'][nextState] += 6
    postSynaptic['OLQVL'][nextState] += 1
    postSynaptic['RICL'][nextState] += 7
    postSynaptic['RICR'][nextState] += 4
    postSynaptic['RIH'][nextState] += 1
    postSynaptic['RIPL'][nextState] += 1
    postSynaptic['RMDDL'][nextState] += 4
    postSynaptic['RMHL'][nextState] += 1
    postSynaptic['SIAVL'][nextState] += 1
    postSynaptic['URAVL'][nextState] += 2


def CEPVR():
    postSynaptic['ASGR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 5
    postSynaptic['IL1VR'][nextState] += 1
    postSynaptic['IL2VR'][nextState] += 2
    postSynaptic['MVR04'][nextState] += 1
    postSynaptic['OLLR'][nextState] += 7
    postSynaptic['OLQVR'][nextState] += 3
    postSynaptic['OLQVR'][nextState] += 1
    postSynaptic['RICL'][nextState] += 2
    postSynaptic['RICR'][nextState] += 2
    postSynaptic['RIH'][nextState] += 1
    postSynaptic['RIPR'][nextState] += 1
    postSynaptic['RIVL'][nextState] += 1
    postSynaptic['RMDDR'][nextState] += 2
    postSynaptic['RMHR'][nextState] += 2
    postSynaptic['SIAVR'][nextState] += 2
    postSynaptic['URAVR'][nextState] += 1


def DA1():
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVAR'][nextState] += 6
    postSynaptic['DA4'][nextState] += 1
    postSynaptic['DD1'][nextState] += 4
    postSynaptic['MDL08'][nextState] += 8
    postSynaptic['MDR08'][nextState] += 8
    postSynaptic['SABVL'][nextState] += 2
    postSynaptic['SABVR'][nextState] += 3
    postSynaptic['VD1'][nextState] += 17
    postSynaptic['VD2'][nextState] += 1


def DA2():
    postSynaptic['AS2'][nextState] += 2
    postSynaptic['AS3'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['DD1'][nextState] += 1
    postSynaptic['MDL07'][nextState] += 2
    postSynaptic['MDL08'][nextState] += 1
    postSynaptic['MDL09'][nextState] += 2
    postSynaptic['MDL10'][nextState] += 2
    postSynaptic['MDR07'][nextState] += 2
    postSynaptic['MDR08'][nextState] += 2
    postSynaptic['MDR09'][nextState] += 2
    postSynaptic['MDR10'][nextState] += 2
    postSynaptic['SABVL'][nextState] += 1
    postSynaptic['VA1'][nextState] += 2
    postSynaptic['VD1'][nextState] += 2
    postSynaptic['VD2'][nextState] += 11
    postSynaptic['VD3'][nextState] += 5


def DA3():
    postSynaptic['AS4'][nextState] += 2
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['DA4'][nextState] += 2
    postSynaptic['DB3'][nextState] += 1
    postSynaptic['DD2'][nextState] += 1
    postSynaptic['MDL09'][nextState] += 5
    postSynaptic['MDL10'][nextState] += 5
    postSynaptic['MDL12'][nextState] += 5
    postSynaptic['MDR09'][nextState] += 5
    postSynaptic['MDR10'][nextState] += 5
    postSynaptic['MDR12'][nextState] += 5
    postSynaptic['VD3'][nextState] += 25
    postSynaptic['VD4'][nextState] += 6


def DA4():
    postSynaptic['AVAL'][nextState] += 3
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['DA1'][nextState] += 1
    postSynaptic['DA3'][nextState] += 1
    postSynaptic['DB3'][nextState] += 2
    postSynaptic['DD2'][nextState] += 1
    postSynaptic['MDL11'][nextState] += 4
    postSynaptic['MDL12'][nextState] += 4
    postSynaptic['MDL14'][nextState] += 5
    postSynaptic['MDR11'][nextState] += 4
    postSynaptic['MDR12'][nextState] += 4
    postSynaptic['MDR14'][nextState] += 5
    postSynaptic['VB6'][nextState] += 1
    postSynaptic['VD4'][nextState] += 12
    postSynaptic['VD5'][nextState] += 15


def DA5():
    postSynaptic['AS6'][nextState] += 2
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 5
    postSynaptic['DB4'][nextState] += 1
    postSynaptic['MDL13'][nextState] += 5
    postSynaptic['MDL14'][nextState] += 4
    postSynaptic['MDR13'][nextState] += 5
    postSynaptic['MDR14'][nextState] += 4
    postSynaptic['VA4'][nextState] += 1
    postSynaptic['VA5'][nextState] += 2
    postSynaptic['VD5'][nextState] += 1
    postSynaptic['VD6'][nextState] += 16


def DA6():
    postSynaptic['AVAL'][nextState] += 10
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['MDL11'][nextState] += 6
    postSynaptic['MDL12'][nextState] += 4
    postSynaptic['MDL13'][nextState] += 4
    postSynaptic['MDL14'][nextState] += 4
    postSynaptic['MDL16'][nextState] += 4
    postSynaptic['MDR11'][nextState] += 4
    postSynaptic['MDR12'][nextState] += 4
    postSynaptic['MDR13'][nextState] += 4
    postSynaptic['MDR14'][nextState] += 4
    postSynaptic['MDR16'][nextState] += 4
    postSynaptic['VD4'][nextState] += 4
    postSynaptic['VD5'][nextState] += 3
    postSynaptic['VD6'][nextState] += 3


def DA7():
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['MDL15'][nextState] += 4
    postSynaptic['MDL17'][nextState] += 4
    postSynaptic['MDL18'][nextState] += 4
    postSynaptic['MDR15'][nextState] += 4
    postSynaptic['MDR17'][nextState] += 4
    postSynaptic['MDR18'][nextState] += 4


def DA8():
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['DA9'][nextState] += 1
    postSynaptic['MDL17'][nextState] += 4
    postSynaptic['MDL19'][nextState] += 4
    postSynaptic['MDL20'][nextState] += 4
    postSynaptic['MDR17'][nextState] += 4
    postSynaptic['MDR19'][nextState] += 4
    postSynaptic['MDR20'][nextState] += 4


def DA9():
    postSynaptic['DA8'][nextState] += 1
    postSynaptic['DD6'][nextState] += 1
    postSynaptic['MDL19'][nextState] += 4
    postSynaptic['MDL21'][nextState] += 4
    postSynaptic['MDL22'][nextState] += 4
    postSynaptic['MDL23'][nextState] += 4
    postSynaptic['MDL24'][nextState] += 4
    postSynaptic['MDR19'][nextState] += 4
    postSynaptic['MDR21'][nextState] += 4
    postSynaptic['MDR22'][nextState] += 4
    postSynaptic['MDR23'][nextState] += 4
    postSynaptic['MDR24'][nextState] += 4
    postSynaptic['PDA'][nextState] += 1
    postSynaptic['PHCL'][nextState] += 1
    postSynaptic['RID'][nextState] += 1
    postSynaptic['VD13'][nextState] += 1


def DB1():
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['AS1'][nextState] += 1
    postSynaptic['AS2'][nextState] += 1
    postSynaptic['AS3'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 3
    postSynaptic['DB2'][nextState] += 1
    postSynaptic['DB4'][nextState] += 1
    postSynaptic['DD1'][nextState] += 10
    postSynaptic['DVA'][nextState] += 1
    postSynaptic['MDL07'][nextState] += 1
    postSynaptic['MDL08'][nextState] += 1
    postSynaptic['MDR07'][nextState] += 1
    postSynaptic['MDR08'][nextState] += 1
    postSynaptic['RID'][nextState] += 1
    postSynaptic['RIS'][nextState] += 1
    postSynaptic['VB3'][nextState] += 1
    postSynaptic['VB4'][nextState] += 1
    postSynaptic['VD1'][nextState] += 21
    postSynaptic['VD2'][nextState] += 15
    postSynaptic['VD3'][nextState] += 1


def DB2():
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['DA3'][nextState] += 5
    postSynaptic['DB1'][nextState] += 1
    postSynaptic['DB3'][nextState] += 6
    postSynaptic['DD2'][nextState] += 3
    postSynaptic['MDL09'][nextState] += 3
    postSynaptic['MDL10'][nextState] += 3
    postSynaptic['MDL11'][nextState] += 3
    postSynaptic['MDL12'][nextState] += 3
    postSynaptic['MDR09'][nextState] += 3
    postSynaptic['MDR10'][nextState] += 3
    postSynaptic['MDR11'][nextState] += 3
    postSynaptic['MDR12'][nextState] += 3
    postSynaptic['VB1'][nextState] += 2
    postSynaptic['VD3'][nextState] += 23
    postSynaptic['VD4'][nextState] += 14
    postSynaptic['VD5'][nextState] += 1


def DB3():
    postSynaptic['AS4'][nextState] += 1
    postSynaptic['AS5'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['DA4'][nextState] += 1
    postSynaptic['DB2'][nextState] += 6
    postSynaptic['DB4'][nextState] += 1
    postSynaptic['DD2'][nextState] += 4
    postSynaptic['DD3'][nextState] += 10
    postSynaptic['MDL11'][nextState] += 3
    postSynaptic['MDL12'][nextState] += 3
    postSynaptic['MDL13'][nextState] += 4
    postSynaptic['MDL14'][nextState] += 3
    postSynaptic['MDR11'][nextState] += 3
    postSynaptic['MDR12'][nextState] += 3
    postSynaptic['MDR13'][nextState] += 4
    postSynaptic['MDR14'][nextState] += 3
    postSynaptic['VD4'][nextState] += 9
    postSynaptic['VD5'][nextState] += 26
    postSynaptic['VD6'][nextState] += 7


def DB4():
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['DB1'][nextState] += 1
    postSynaptic['DB3'][nextState] += 1
    postSynaptic['DD3'][nextState] += 3
    postSynaptic['MDL13'][nextState] += 2
    postSynaptic['MDL14'][nextState] += 2
    postSynaptic['MDL16'][nextState] += 2
    postSynaptic['MDR13'][nextState] += 2
    postSynaptic['MDR14'][nextState] += 2
    postSynaptic['MDR16'][nextState] += 2
    postSynaptic['VB2'][nextState] += 1
    postSynaptic['VB4'][nextState] += 1
    postSynaptic['VD6'][nextState] += 13


def DB5():
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['MDL15'][nextState] += 2
    postSynaptic['MDL17'][nextState] += 2
    postSynaptic['MDL18'][nextState] += 2
    postSynaptic['MDR15'][nextState] += 2
    postSynaptic['MDR17'][nextState] += 2
    postSynaptic['MDR18'][nextState] += 2


def DB6():
    postSynaptic['AVAL'][nextState] += 3
    postSynaptic['AVBL'][nextState] += 2
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['MDL17'][nextState] += 2
    postSynaptic['MDL19'][nextState] += 2
    postSynaptic['MDL20'][nextState] += 2
    postSynaptic['MDR17'][nextState] += 2
    postSynaptic['MDR19'][nextState] += 2
    postSynaptic['MDR20'][nextState] += 2


def DB7():
    postSynaptic['AVBL'][nextState] += 2
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['MDL19'][nextState] += 2
    postSynaptic['MDL21'][nextState] += 2
    postSynaptic['MDL22'][nextState] += 2
    postSynaptic['MDL23'][nextState] += 2
    postSynaptic['MDL24'][nextState] += 2
    postSynaptic['MDR19'][nextState] += 2
    postSynaptic['MDR21'][nextState] += 2
    postSynaptic['MDR22'][nextState] += 2
    postSynaptic['MDR23'][nextState] += 2
    postSynaptic['MDR24'][nextState] += 2
    postSynaptic['VD13'][nextState] += 2


def DD1():
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['DD2'][nextState] += 3
    postSynaptic['MDL07'][nextState] += -6
    postSynaptic['MDL08'][nextState] += -6
    postSynaptic['MDL09'][nextState] += -7
    postSynaptic['MDL10'][nextState] += -6
    postSynaptic['MDR07'][nextState] += -6
    postSynaptic['MDR08'][nextState] += -6
    postSynaptic['MDR09'][nextState] += -7
    postSynaptic['MDR10'][nextState] += -6
    postSynaptic['VD1'][nextState] += 4
    postSynaptic['VD2'][nextState] += 1
    postSynaptic['VD2'][nextState] += 2


def DD2():
    postSynaptic['DA3'][nextState] += 1
    postSynaptic['DD1'][nextState] += 1
    postSynaptic['DD3'][nextState] += 2
    postSynaptic['MDL09'][nextState] += -6
    postSynaptic['MDL11'][nextState] += -7
    postSynaptic['MDL12'][nextState] += -6
    postSynaptic['MDR09'][nextState] += -6
    postSynaptic['MDR11'][nextState] += -7
    postSynaptic['MDR12'][nextState] += -6
    postSynaptic['VD3'][nextState] += 1
    postSynaptic['VD4'][nextState] += 3


def DD3():
    postSynaptic['DD2'][nextState] += 2
    postSynaptic['DD4'][nextState] += 1
    postSynaptic['MDL11'][nextState] += -7
    postSynaptic['MDL13'][nextState] += -9
    postSynaptic['MDL14'][nextState] += -7
    postSynaptic['MDR11'][nextState] += -7
    postSynaptic['MDR13'][nextState] += -9
    postSynaptic['MDR14'][nextState] += -7


def DD4():
    postSynaptic['DD3'][nextState] += 1
    postSynaptic['MDL13'][nextState] += -7
    postSynaptic['MDL15'][nextState] += -7
    postSynaptic['MDL16'][nextState] += -7
    postSynaptic['MDR13'][nextState] += -7
    postSynaptic['MDR15'][nextState] += -7
    postSynaptic['MDR16'][nextState] += -7
    postSynaptic['VC3'][nextState] += 1
    postSynaptic['VD8'][nextState] += 1


def DD5():
    postSynaptic['MDL17'][nextState] += -7
    postSynaptic['MDL18'][nextState] += -7
    postSynaptic['MDL20'][nextState] += -7
    postSynaptic['MDR17'][nextState] += -7
    postSynaptic['MDR18'][nextState] += -7
    postSynaptic['MDR20'][nextState] += -7
    postSynaptic['VB8'][nextState] += 1
    postSynaptic['VD10'][nextState] += 1
    postSynaptic['VD9'][nextState] += 1


def DD6():
    postSynaptic['MDL19'][nextState] += -7
    postSynaptic['MDL21'][nextState] += -7
    postSynaptic['MDL22'][nextState] += -7
    postSynaptic['MDL23'][nextState] += -7
    postSynaptic['MDL24'][nextState] += -7
    postSynaptic['MDR19'][nextState] += -7
    postSynaptic['MDR21'][nextState] += -7
    postSynaptic['MDR22'][nextState] += -7
    postSynaptic['MDR23'][nextState] += -7
    postSynaptic['MDR24'][nextState] += -7


def DVA():
    postSynaptic['AIZL'][nextState] += 3
    postSynaptic['AQR'][nextState] += 4
    postSynaptic['AUAL'][nextState] += 1
    postSynaptic['AUAR'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 3
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 2
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 9
    postSynaptic['AVER'][nextState] += 5
    postSynaptic['DB1'][nextState] += 1
    postSynaptic['DB2'][nextState] += 1
    postSynaptic['DB3'][nextState] += 2
    postSynaptic['DB4'][nextState] += 1
    postSynaptic['DB5'][nextState] += 1
    postSynaptic['DB6'][nextState] += 2
    postSynaptic['DB7'][nextState] += 1
    postSynaptic['PDEL'][nextState] += 3
    postSynaptic['PVCL'][nextState] += 3
    postSynaptic['PVCL'][nextState] += 1
    postSynaptic['PVCR'][nextState] += 1
    postSynaptic['PVR'][nextState] += 3
    postSynaptic['PVR'][nextState] += 2
    postSynaptic['RIAL'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 1
    postSynaptic['RIMR'][nextState] += 1
    postSynaptic['RIR'][nextState] += 3
    postSynaptic['SAADR'][nextState] += 1
    postSynaptic['SAAVL'][nextState] += 1
    postSynaptic['SAAVR'][nextState] += 1
    postSynaptic['SABD'][nextState] += 1
    postSynaptic['SMBDL'][nextState] += 3
    postSynaptic['SMBDR'][nextState] += 2
    postSynaptic['SMBVL'][nextState] += 3
    postSynaptic['SMBVR'][nextState] += 2
    postSynaptic['VA12'][nextState] += 1
    postSynaptic['VA2'][nextState] += 1
    postSynaptic['VB1'][nextState] += 1
    postSynaptic['VB11'][nextState] += 2


def DVB():
    postSynaptic['AS9'][nextState] += 7
    postSynaptic['AVL'][nextState] += 5
    postSynaptic['AVL'][nextState] += 1
    postSynaptic['DA8'][nextState] += 2
    postSynaptic['DD6'][nextState] += 3
    postSynaptic['DVC'][nextState] += 3
    # postSynaptic['MANAL'][nextState] += -5 - just not needed or used
    postSynaptic['PDA'][nextState] += 1
    postSynaptic['PHCL'][nextState] += 1
    postSynaptic['PVPL'][nextState] += 1
    postSynaptic['VA9'][nextState] += 1
    postSynaptic['VB9'][nextState] += 1


def DVC():
    postSynaptic['AIBL'][nextState] += 2
    postSynaptic['AIBR'][nextState] += 5
    postSynaptic['AVAL'][nextState] += 5
    postSynaptic['AVAR'][nextState] += 7
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVKL'][nextState] += 2
    postSynaptic['AVKR'][nextState] += 1
    postSynaptic['AVL'][nextState] += 9
    postSynaptic['PVPL'][nextState] += 2
    postSynaptic['PVPR'][nextState] += 13
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 5
    postSynaptic['RIGR'][nextState] += 5
    postSynaptic['RMFL'][nextState] += 2
    postSynaptic['RMFR'][nextState] += 4
    postSynaptic['VA9'][nextState] += 1
    postSynaptic['VD1'][nextState] += 5
    postSynaptic['VD10'][nextState] += 4


def FLPL():
    postSynaptic['ADEL'][nextState] += 2
    postSynaptic['ADER'][nextState] += 2
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['AIBR'][nextState] += 2
    postSynaptic['AVAL'][nextState] += 15
    postSynaptic['AVAR'][nextState] += 17
    postSynaptic['AVBL'][nextState] += 4
    postSynaptic['AVBR'][nextState] += 5
    postSynaptic['AVDL'][nextState] += 7
    postSynaptic['AVDR'][nextState] += 13
    postSynaptic['DVA'][nextState] += 1
    postSynaptic['FLPR'][nextState] += 3
    postSynaptic['RIH'][nextState] += 1


def FLPR():
    postSynaptic['ADER'][nextState] += 1
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 12
    postSynaptic['AVAR'][nextState] += 5
    postSynaptic['AVBL'][nextState] += 5
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['AVDL'][nextState] += 10
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 2
    postSynaptic['AVEL'][nextState] += 4
    postSynaptic['AVER'][nextState] += 2
    postSynaptic['AVJR'][nextState] += 1
    postSynaptic['DVA'][nextState] += 1
    postSynaptic['FLPL'][nextState] += 4
    postSynaptic['PVCL'][nextState] += 2
    postSynaptic['VB1'][nextState] += 1


def HSNL():
    postSynaptic['AIAL'][nextState] += 1
    postSynaptic['AIZL'][nextState] += 2
    postSynaptic['AIZR'][nextState] += 1
    postSynaptic['ASHL'][nextState] += 1
    postSynaptic['ASHR'][nextState] += 2
    postSynaptic['ASJR'][nextState] += 1
    postSynaptic['ASKL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 2
    postSynaptic['AVFL'][nextState] += 6
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['AWBL'][nextState] += 1
    postSynaptic['AWBR'][nextState] += 2
    postSynaptic['HSNR'][nextState] += 3
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['MVULVA'][nextState] += 7
    postSynaptic['RIFL'][nextState] += 3
    postSynaptic['RIML'][nextState] += 2
    postSynaptic['SABVL'][nextState] += 2
    postSynaptic['VC5'][nextState] += 3


def HSNR():
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['AIZL'][nextState] += 1
    postSynaptic['AIZR'][nextState] += 1
    postSynaptic['AS5'][nextState] += 1
    postSynaptic['ASHL'][nextState] += 2
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVFL'][nextState] += 1
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['AVL'][nextState] += 1
    postSynaptic['AWBL'][nextState] += 1
    postSynaptic['BDUR'][nextState] += 1
    postSynaptic['DA5'][nextState] += 1
    postSynaptic['DA6'][nextState] += 1
    postSynaptic['HSNL'][nextState] += 2
    postSynaptic['MVULVA'][nextState] += 6
    postSynaptic['PVNR'][nextState] += 2
    postSynaptic['PVQR'][nextState] += 1
    postSynaptic['RIFR'][nextState] += 4
    postSynaptic['RMGR'][nextState] += 1
    postSynaptic['SABD'][nextState] += 1
    postSynaptic['SABVR'][nextState] += 1
    postSynaptic['VA6'][nextState] += 1
    postSynaptic['VC2'][nextState] += 3
    postSynaptic['VC3'][nextState] += 1
    postSynaptic['VD4'][nextState] += 2


def I1L():
    postSynaptic['I1R'][nextState] += 1
    postSynaptic['I3'][nextState] += 1
    postSynaptic['I5'][nextState] += 1
    postSynaptic['RIPL'][nextState] += 1
    postSynaptic['RIPR'][nextState] += 1


def I1R():
    postSynaptic['I1L'][nextState] += 1
    postSynaptic['I3'][nextState] += 1
    postSynaptic['I5'][nextState] += 1
    postSynaptic['RIPL'][nextState] += 1
    postSynaptic['RIPR'][nextState] += 1


def I2L():
    postSynaptic['I1L'][nextState] += 1
    postSynaptic['I1R'][nextState] += 1
    postSynaptic['M1'][nextState] += 4


def I2R():
    postSynaptic['I1L'][nextState] += 1
    postSynaptic['I1R'][nextState] += 1
    postSynaptic['M1'][nextState] += 4


def I3():
    postSynaptic['M1'][nextState] += 4
    postSynaptic['M2L'][nextState] += 2
    postSynaptic['M2R'][nextState] += 2


def I4():
    postSynaptic['I2L'][nextState] += 5
    postSynaptic['I2R'][nextState] += 5
    postSynaptic['I5'][nextState] += 2
    postSynaptic['M1'][nextState] += 4


def I5():
    postSynaptic['I1L'][nextState] += 4
    postSynaptic['I1R'][nextState] += 3
    postSynaptic['M1'][nextState] += 2
    postSynaptic['M5'][nextState] += 2
    postSynaptic['MI'][nextState] += 4


def I6():
    postSynaptic['I2L'][nextState] += 2
    postSynaptic['I2R'][nextState] += 2
    postSynaptic['I3'][nextState] += 1
    postSynaptic['M4'][nextState] += 1
    postSynaptic['M5'][nextState] += 2
    postSynaptic['NSML'][nextState] += 2
    postSynaptic['NSMR'][nextState] += 2


def IL1DL():
    postSynaptic['IL1DR'][nextState] += 1
    postSynaptic['IL1L'][nextState] += 1
    postSynaptic['MDL01'][nextState] += 1
    postSynaptic['MDL02'][nextState] += 1
    postSynaptic['MDL04'][nextState] += 2
    postSynaptic['OLLL'][nextState] += 1
    postSynaptic['PVR'][nextState] += 1
    postSynaptic['RIH'][nextState] += 1
    postSynaptic['RIPL'][nextState] += 2
    postSynaptic['RMDDR'][nextState] += 1
    postSynaptic['RMDVL'][nextState] += 4
    postSynaptic['RMEV'][nextState] += 1
    postSynaptic['URYDL'][nextState] += 1


def IL1DR():
    postSynaptic['IL1DL'][nextState] += 1
    postSynaptic['IL1R'][nextState] += 1
    postSynaptic['MDR01'][nextState] += 4
    postSynaptic['MDR02'][nextState] += 3
    postSynaptic['OLLR'][nextState] += 1
    postSynaptic['RIPR'][nextState] += 5
    postSynaptic['RMDVR'][nextState] += 5
    postSynaptic['RMEV'][nextState] += 1


def IL1L():
    postSynaptic['AVER'][nextState] += 2
    postSynaptic['IL1DL'][nextState] += 2
    postSynaptic['IL1VL'][nextState] += 1
    postSynaptic['MDL01'][nextState] += 3
    postSynaptic['MDL03'][nextState] += 3
    postSynaptic['MDL05'][nextState] += 4
    postSynaptic['MVL01'][nextState] += 3
    postSynaptic['MVL03'][nextState] += 3
    postSynaptic['RMDDL'][nextState] += 5
    postSynaptic['RMDL'][nextState] += 1
    postSynaptic['RMDR'][nextState] += 3
    postSynaptic['RMDVL'][nextState] += 4
    postSynaptic['RMDVR'][nextState] += 2
    postSynaptic['RMER'][nextState] += 1


def IL1R():
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['IL1DR'][nextState] += 2
    postSynaptic['IL1VR'][nextState] += 1
    postSynaptic['MDR01'][nextState] += 3
    postSynaptic['MDR03'][nextState] += 3
    postSynaptic['MVR01'][nextState] += 3
    postSynaptic['MVR03'][nextState] += 3
    postSynaptic['RMDDL'][nextState] += 3
    postSynaptic['RMDDR'][nextState] += 2
    postSynaptic['RMDL'][nextState] += 4
    postSynaptic['RMDR'][nextState] += 2
    postSynaptic['RMDVL'][nextState] += 1
    postSynaptic['RMDVR'][nextState] += 4
    postSynaptic['RMEL'][nextState] += 2
    postSynaptic['RMHL'][nextState] += 1
    postSynaptic['URXR'][nextState] += 2


def IL1VL():
    postSynaptic['IL1L'][nextState] += 2
    postSynaptic['IL1VR'][nextState] += 1
    postSynaptic['MVL01'][nextState] += 5
    postSynaptic['MVL02'][nextState] += 4
    postSynaptic['RIPL'][nextState] += 4
    postSynaptic['RMDDL'][nextState] += 5
    postSynaptic['RMED'][nextState] += 1
    postSynaptic['URYVL'][nextState] += 1


def IL1VR():
    postSynaptic['IL1R'][nextState] += 2
    postSynaptic['IL1VL'][nextState] += 1
    postSynaptic['IL2R'][nextState] += 1
    postSynaptic['IL2VR'][nextState] += 1
    postSynaptic['MVR01'][nextState] += 5
    postSynaptic['MVR02'][nextState] += 5
    postSynaptic['RIPR'][nextState] += 6
    postSynaptic['RMDDR'][nextState] += 10
    postSynaptic['RMER'][nextState] += 1


def IL2DL():
    postSynaptic['AUAL'][nextState] += 1
    postSynaptic['IL1DL'][nextState] += 7
    postSynaptic['OLQDL'][nextState] += 2
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIPL'][nextState] += 10
    postSynaptic['RMEL'][nextState] += 4
    postSynaptic['RMER'][nextState] += 3
    postSynaptic['URADL'][nextState] += 3


def IL2DR():
    postSynaptic['CEPDR'][nextState] += 1
    postSynaptic['IL1DR'][nextState] += 7
    postSynaptic['RICR'][nextState] += 1
    postSynaptic['RIPR'][nextState] += 11
    postSynaptic['RMED'][nextState] += 1
    postSynaptic['RMEL'][nextState] += 2
    postSynaptic['RMER'][nextState] += 2
    postSynaptic['RMEV'][nextState] += 1
    postSynaptic['URADR'][nextState] += 3


def IL2L():
    postSynaptic['ADEL'][nextState] += 2
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['IL1L'][nextState] += 1
    postSynaptic['OLQDL'][nextState] += 5
    postSynaptic['OLQVL'][nextState] += 8
    postSynaptic['RICL'][nextState] += 1
    postSynaptic['RIH'][nextState] += 7
    postSynaptic['RMDL'][nextState] += 3
    postSynaptic['RMDR'][nextState] += 1
    postSynaptic['RMER'][nextState] += 2
    postSynaptic['RMEV'][nextState] += 2
    postSynaptic['RMGL'][nextState] += 1
    postSynaptic['URXL'][nextState] += 2


def IL2R():
    postSynaptic['ADER'][nextState] += 1
    postSynaptic['IL1R'][nextState] += 1
    postSynaptic['IL1VR'][nextState] += 1
    postSynaptic['OLLR'][nextState] += 1
    postSynaptic['OLQDR'][nextState] += 2
    postSynaptic['OLQVR'][nextState] += 7
    postSynaptic['RIH'][nextState] += 6
    postSynaptic['RMDL'][nextState] += 1
    postSynaptic['RMEL'][nextState] += 2
    postSynaptic['RMEV'][nextState] += 1
    postSynaptic['RMGR'][nextState] += 1
    postSynaptic['URBR'][nextState] += 1
    postSynaptic['URXR'][nextState] += 1


def IL2VL():
    postSynaptic['BAGR'][nextState] += 1
    postSynaptic['IL1VL'][nextState] += 7
    postSynaptic['IL2L'][nextState] += 1
    postSynaptic['OLQVL'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 1
    postSynaptic['RIH'][nextState] += 2
    postSynaptic['RIPL'][nextState] += 1
    postSynaptic['RMEL'][nextState] += 1
    postSynaptic['RMER'][nextState] += 4
    postSynaptic['RMEV'][nextState] += 1
    postSynaptic['URAVL'][nextState] += 3


def IL2VR():
    postSynaptic['IL1VR'][nextState] += 6
    postSynaptic['OLQVR'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 2
    postSynaptic['RIH'][nextState] += 3
    postSynaptic['RIPR'][nextState] += 15
    postSynaptic['RMEL'][nextState] += 3
    postSynaptic['RMER'][nextState] += 2
    postSynaptic['RMEV'][nextState] += 3
    postSynaptic['URAVR'][nextState] += 4
    postSynaptic['URXR'][nextState] += 1


def LUAL():
    postSynaptic['AVAL'][nextState] += 6
    postSynaptic['AVAR'][nextState] += 6
    postSynaptic['AVDL'][nextState] += 4
    postSynaptic['AVDR'][nextState] += 2
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['PHBL'][nextState] += 1
    postSynaptic['PLML'][nextState] += 1
    postSynaptic['PVNL'][nextState] += 1
    postSynaptic['PVR'][nextState] += 1
    postSynaptic['PVWL'][nextState] += 1


def LUAR():
    postSynaptic['AVAL'][nextState] += 3
    postSynaptic['AVAR'][nextState] += 7
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 3
    postSynaptic['AVJR'][nextState] += 1
    postSynaptic['PLMR'][nextState] += 1
    postSynaptic['PQR'][nextState] += 1
    postSynaptic['PVCR'][nextState] += 3
    postSynaptic['PVR'][nextState] += 2
    postSynaptic['PVWL'][nextState] += 1


def M1():
    postSynaptic['I2L'][nextState] += 2
    postSynaptic['I2R'][nextState] += 2
    postSynaptic['I3'][nextState] += 1
    postSynaptic['I4'][nextState] += 1


def M2L():
    postSynaptic['I1L'][nextState] += 3
    postSynaptic['I1R'][nextState] += 3
    postSynaptic['I3'][nextState] += 3
    postSynaptic['M2R'][nextState] += 1
    postSynaptic['M5'][nextState] += 1
    postSynaptic['MI'][nextState] += 4


def M2R():
    postSynaptic['I1L'][nextState] += 3
    postSynaptic['I1R'][nextState] += 3
    postSynaptic['I3'][nextState] += 3
    postSynaptic['M3L'][nextState] += 1
    postSynaptic['M3R'][nextState] += 1
    postSynaptic['M5'][nextState] += 1
    postSynaptic['MI'][nextState] += 4


def M3L():
    postSynaptic['I1L'][nextState] += 4
    postSynaptic['I1R'][nextState] += 4
    postSynaptic['I4'][nextState] += 2
    postSynaptic['I5'][nextState] += 3
    postSynaptic['I6'][nextState] += 1
    postSynaptic['M1'][nextState] += 2
    postSynaptic['M3R'][nextState] += 1
    postSynaptic['MCL'][nextState] += 1
    postSynaptic['MCR'][nextState] += 1
    postSynaptic['MI'][nextState] += 2
    postSynaptic['NSML'][nextState] += 2
    postSynaptic['NSMR'][nextState] += 3


def M3R():
    postSynaptic['I1L'][nextState] += 4
    postSynaptic['I1R'][nextState] += 4
    postSynaptic['I3'][nextState] += 2
    postSynaptic['I4'][nextState] += 6
    postSynaptic['I5'][nextState] += 3
    postSynaptic['I6'][nextState] += 1
    postSynaptic['M1'][nextState] += 2
    postSynaptic['M3L'][nextState] += 1
    postSynaptic['MCL'][nextState] += 1
    postSynaptic['MCR'][nextState] += 1
    postSynaptic['MI'][nextState] += 2
    postSynaptic['NSML'][nextState] += 2
    postSynaptic['NSMR'][nextState] += 3


def M4():
    postSynaptic['I3'][nextState] += 1
    postSynaptic['I5'][nextState] += 13
    postSynaptic['I6'][nextState] += 3
    postSynaptic['M2L'][nextState] += 1
    postSynaptic['M2R'][nextState] += 1
    postSynaptic['M4'][nextState] += 6
    postSynaptic['M5'][nextState] += 1
    postSynaptic['NSML'][nextState] += 1
    postSynaptic['NSMR'][nextState] += 1


def M5():
    postSynaptic['I5'][nextState] += 3
    postSynaptic['I5'][nextState] += 1
    postSynaptic['I6'][nextState] += 1
    postSynaptic['M1'][nextState] += 2
    postSynaptic['M2L'][nextState] += 2
    postSynaptic['M2R'][nextState] += 2
    postSynaptic['M5'][nextState] += 4


def MCL():
    postSynaptic['I1L'][nextState] += 3
    postSynaptic['I1R'][nextState] += 3
    postSynaptic['I2L'][nextState] += 1
    postSynaptic['I2R'][nextState] += 1
    postSynaptic['I3'][nextState] += 1
    postSynaptic['M1'][nextState] += 2
    postSynaptic['M2L'][nextState] += 2
    postSynaptic['M2R'][nextState] += 2


def MCR():
    postSynaptic['I1L'][nextState] += 3
    postSynaptic['I1R'][nextState] += 3
    postSynaptic['I3'][nextState] += 1
    postSynaptic['M1'][nextState] += 2
    postSynaptic['M2L'][nextState] += 2
    postSynaptic['M2R'][nextState] += 2


def MI():
    postSynaptic['I1L'][nextState] += 1
    postSynaptic['I1R'][nextState] += 1
    postSynaptic['I3'][nextState] += 1
    postSynaptic['I4'][nextState] += 1
    postSynaptic['I5'][nextState] += 2
    postSynaptic['M1'][nextState] += 1
    postSynaptic['M2L'][nextState] += 2
    postSynaptic['M2R'][nextState] += 2
    postSynaptic['M3L'][nextState] += 1
    postSynaptic['M3R'][nextState] += 1
    postSynaptic['MCL'][nextState] += 2
    postSynaptic['MCR'][nextState] += 2


def NSML():
    postSynaptic['I1L'][nextState] += 1
    postSynaptic['I1R'][nextState] += 2
    postSynaptic['I2L'][nextState] += 6
    postSynaptic['I2R'][nextState] += 6
    postSynaptic['I3'][nextState] += 2
    postSynaptic['I4'][nextState] += 3
    postSynaptic['I5'][nextState] += 2
    postSynaptic['I6'][nextState] += 2
    postSynaptic['M3L'][nextState] += 2
    postSynaptic['M3R'][nextState] += 2


def NSMR():
    postSynaptic['I1L'][nextState] += 2
    postSynaptic['I1R'][nextState] += 2
    postSynaptic['I2L'][nextState] += 6
    postSynaptic['I2R'][nextState] += 6
    postSynaptic['I3'][nextState] += 2
    postSynaptic['I4'][nextState] += 3
    postSynaptic['I5'][nextState] += 2
    postSynaptic['I6'][nextState] += 2
    postSynaptic['M3L'][nextState] += 2
    postSynaptic['M3R'][nextState] += 2


def OLLL():
    postSynaptic['AVER'][nextState] += 21
    postSynaptic['CEPDL'][nextState] += 3
    postSynaptic['CEPVL'][nextState] += 4
    postSynaptic['IL1DL'][nextState] += 1
    postSynaptic['IL1VL'][nextState] += 2
    postSynaptic['OLLR'][nextState] += 2
    postSynaptic['RIBL'][nextState] += 8
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RMDDL'][nextState] += 7
    postSynaptic['RMDL'][nextState] += 2
    postSynaptic['RMDVL'][nextState] += 1
    postSynaptic['RMEL'][nextState] += 2
    postSynaptic['SMDDL'][nextState] += 3
    postSynaptic['SMDDR'][nextState] += 4
    postSynaptic['SMDVR'][nextState] += 4
    postSynaptic['URYDL'][nextState] += 1


def OLLR():
    postSynaptic['AVEL'][nextState] += 16
    postSynaptic['CEPDR'][nextState] += 1
    postSynaptic['CEPVR'][nextState] += 6
    postSynaptic['IL1DR'][nextState] += 3
    postSynaptic['IL1VR'][nextState] += 1
    postSynaptic['IL2R'][nextState] += 1
    postSynaptic['OLLL'][nextState] += 2
    postSynaptic['RIBR'][nextState] += 10
    postSynaptic['RIGR'][nextState] += 1
    postSynaptic['RMDDR'][nextState] += 10
    postSynaptic['RMDL'][nextState] += 3
    postSynaptic['RMDVR'][nextState] += 3
    postSynaptic['RMER'][nextState] += 2
    postSynaptic['SMDDR'][nextState] += 1
    postSynaptic['SMDVL'][nextState] += 4
    postSynaptic['SMDVR'][nextState] += 3


def OLQDL():
    postSynaptic['CEPDL'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 2
    postSynaptic['RICR'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RMDDR'][nextState] += 4
    postSynaptic['RMDVL'][nextState] += 1
    postSynaptic['SIBVL'][nextState] += 3
    postSynaptic['URBL'][nextState] += 1


def OLQDR():
    postSynaptic['CEPDR'][nextState] += 2
    postSynaptic['RIBR'][nextState] += 2
    postSynaptic['RICL'][nextState] += 1
    postSynaptic['RICR'][nextState] += 1
    postSynaptic['RIGR'][nextState] += 1
    postSynaptic['RIH'][nextState] += 1
    postSynaptic['RMDDL'][nextState] += 3
    postSynaptic['RMDVR'][nextState] += 1
    postSynaptic['RMHR'][nextState] += 1
    postSynaptic['SIBVR'][nextState] += 2
    postSynaptic['URBR'][nextState] += 1


def OLQVL():
    postSynaptic['ADLL'][nextState] += 1
    postSynaptic['CEPVL'][nextState] += 1
    postSynaptic['IL1VL'][nextState] += 1
    postSynaptic['IL2VL'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RICL'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RIH'][nextState] += 1
    postSynaptic['RIPL'][nextState] += 1
    postSynaptic['RMDDL'][nextState] += 1
    postSynaptic['RMDVR'][nextState] += 4
    postSynaptic['SIBDL'][nextState] += 3
    postSynaptic['URBL'][nextState] += 1


def OLQVR():
    postSynaptic['CEPVR'][nextState] += 1
    postSynaptic['IL1VR'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RICR'][nextState] += 1
    postSynaptic['RIGR'][nextState] += 1
    postSynaptic['RIH'][nextState] += 2
    postSynaptic['RIPR'][nextState] += 2
    postSynaptic['RMDDR'][nextState] += 1
    postSynaptic['RMDVL'][nextState] += 4
    postSynaptic['RMER'][nextState] += 1
    postSynaptic['SIBDR'][nextState] += 4
    postSynaptic['URBR'][nextState] += 1

# todo: instance of MDL21
def PDA():
    postSynaptic['AS11'][nextState] += 1
    postSynaptic['DA9'][nextState] += 1
    postSynaptic['DD6'][nextState] += 1
    postSynaptic['MDL21'][nextState] += 2
    postSynaptic['PVNR'][nextState] += 1
    postSynaptic['VD13'][nextState] += 3

# TODO: instance of MVR21
def PDB():
    postSynaptic['AS11'][nextState] += 2
    postSynaptic['MVL22'][nextState] += 1
    postSynaptic['MVR21'][nextState] += 1
    postSynaptic['RID'][nextState] += 2
    postSynaptic['VD13'][nextState] += 2


# todo: note: large neuron firings here
def PDEL():
    postSynaptic['AVKL'][nextState] += 6
    postSynaptic['DVA'][nextState] += 24
    postSynaptic['PDER'][nextState] += 1
    postSynaptic['PDER'][nextState] += 3
    postSynaptic['PVCR'][nextState] += 1
    postSynaptic['PVM'][nextState] += 2
    postSynaptic['PVM'][nextState] += 1
    postSynaptic['PVR'][nextState] += 2
    postSynaptic['VA9'][nextState] += 1
    postSynaptic['VD11'][nextState] += 1


def PDER():
    postSynaptic['AVKL'][nextState] += 16
    postSynaptic['DVA'][nextState] += 35
    postSynaptic['PDEL'][nextState] += 3
    postSynaptic['PVCL'][nextState] += 1
    postSynaptic['PVCR'][nextState] += 1
    postSynaptic['PVM'][nextState] += 1
    postSynaptic['VA8'][nextState] += 1
    postSynaptic['VD9'][nextState] += 1


def PHAL():
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVFL'][nextState] += 3
    postSynaptic['AVG'][nextState] += 5
    postSynaptic['AVHL'][nextState] += 1
    postSynaptic['AVHR'][nextState] += 1
    postSynaptic['DVA'][nextState] += 2
    postSynaptic['PHAR'][nextState] += 5
    postSynaptic['PHAR'][nextState] += 2
    postSynaptic['PHBL'][nextState] += 5
    postSynaptic['PHBR'][nextState] += 5
    postSynaptic['PVQL'][nextState] += 2


def PHAR():
    postSynaptic['AVG'][nextState] += 3
    postSynaptic['AVHR'][nextState] += 1
    postSynaptic['DA8'][nextState] += 1
    postSynaptic['DVA'][nextState] += 1
    postSynaptic['PHAL'][nextState] += 6
    postSynaptic['PHAL'][nextState] += 2
    postSynaptic['PHBL'][nextState] += 1
    postSynaptic['PHBR'][nextState] += 5
    postSynaptic['PVPL'][nextState] += 3
    postSynaptic['PVQL'][nextState] += 2


def PHBL():
    postSynaptic['AVAL'][nextState] += 9
    postSynaptic['AVAR'][nextState] += 6
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['PHBR'][nextState] += 1
    postSynaptic['PHBR'][nextState] += 3
    postSynaptic['PVCL'][nextState] += 13
    postSynaptic['VA12'][nextState] += 1


def PHBR():
    postSynaptic['AVAL'][nextState] += 7
    postSynaptic['AVAR'][nextState] += 7
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVFL'][nextState] += 1
    postSynaptic['AVHL'][nextState] += 1
    postSynaptic['DA8'][nextState] += 1
    postSynaptic['PHBL'][nextState] += 1
    postSynaptic['PHBL'][nextState] += 3
    postSynaptic['PVCL'][nextState] += 6
    postSynaptic['PVCR'][nextState] += 3
    postSynaptic['VA12'][nextState] += 2


def PHCL():
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['DA9'][nextState] += 7
    postSynaptic['DA9'][nextState] += 1
    postSynaptic['DVA'][nextState] += 6
    postSynaptic['LUAL'][nextState] += 1
    postSynaptic['PHCR'][nextState] += 1
    postSynaptic['PLML'][nextState] += 1
    postSynaptic['PVCL'][nextState] += 2
    postSynaptic['VA12'][nextState] += 3


def PHCR():
    postSynaptic['AVHR'][nextState] += 1
    postSynaptic['DA9'][nextState] += 2
    postSynaptic['DVA'][nextState] += 8
    postSynaptic['LUAR'][nextState] += 1
    postSynaptic['PHCL'][nextState] += 2
    postSynaptic['PVCR'][nextState] += 9
    postSynaptic['VA12'][nextState] += 2


def PLML():
    postSynaptic['HSNL'][nextState] += 1
    postSynaptic['LUAL'][nextState] += 1
    postSynaptic['PHCL'][nextState] += 1
    postSynaptic['PVCL'][nextState] += 1


def PLMR():
    postSynaptic['AS6'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 4
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 4
    postSynaptic['DVA'][nextState] += 5
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['LUAR'][nextState] += 1
    postSynaptic['PDEL'][nextState] += 2
    postSynaptic['PDER'][nextState] += 3
    postSynaptic['PVCL'][nextState] += 2
    postSynaptic['PVCR'][nextState] += 1
    postSynaptic['PVR'][nextState] += 2


def PLNL():
    postSynaptic['SAADL'][nextState] += 5
    postSynaptic['SMBVL'][nextState] += 6


def PLNR():
    postSynaptic['SAADR'][nextState] += 4
    postSynaptic['SMBVR'][nextState] += 6


def PQR():
    postSynaptic['AVAL'][nextState] += 8
    postSynaptic['AVAR'][nextState] += 11
    postSynaptic['AVDL'][nextState] += 7
    postSynaptic['AVDR'][nextState] += 6
    postSynaptic['AVG'][nextState] += 1
    postSynaptic['LUAR'][nextState] += 1
    postSynaptic['PVNL'][nextState] += 1
    postSynaptic['PVPL'][nextState] += 4


def PVCL():
    postSynaptic['AS1'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 3
    postSynaptic['AVAR'][nextState] += 4
    postSynaptic['AVBL'][nextState] += 5
    postSynaptic['AVBR'][nextState] += 12
    postSynaptic['AVDL'][nextState] += 5
    postSynaptic['AVDR'][nextState] += 2
    postSynaptic['AVEL'][nextState] += 3
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['AVJL'][nextState] += 4
    postSynaptic['AVJR'][nextState] += 2
    postSynaptic['DA2'][nextState] += 1
    postSynaptic['DA5'][nextState] += 1
    postSynaptic['DA6'][nextState] += 1
    postSynaptic['DB2'][nextState] += 3
    postSynaptic['DB3'][nextState] += 4
    postSynaptic['DB4'][nextState] += 3
    postSynaptic['DB5'][nextState] += 2
    postSynaptic['DB6'][nextState] += 2
    postSynaptic['DB7'][nextState] += 3
    postSynaptic['DVA'][nextState] += 5
    postSynaptic['PLML'][nextState] += 1
    postSynaptic['PVCR'][nextState] += 7
    postSynaptic['RID'][nextState] += 5
    postSynaptic['RIS'][nextState] += 2
    postSynaptic['SIBVL'][nextState] += 2
    postSynaptic['VB10'][nextState] += 3
    postSynaptic['VB11'][nextState] += 1
    postSynaptic['VB3'][nextState] += 1
    postSynaptic['VB4'][nextState] += 1
    postSynaptic['VB5'][nextState] += 1
    postSynaptic['VB6'][nextState] += 2
    postSynaptic['VB8'][nextState] += 1
    postSynaptic['VB9'][nextState] += 2


def PVCR():
    postSynaptic['AQR'][nextState] += 1
    postSynaptic['AS2'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 12
    postSynaptic['AVAR'][nextState] += 10
    postSynaptic['AVBL'][nextState] += 8
    postSynaptic['AVBR'][nextState] += 6
    postSynaptic['AVDL'][nextState] += 5
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['AVJL'][nextState] += 3
    postSynaptic['AVL'][nextState] += 1
    postSynaptic['DA9'][nextState] += 1
    postSynaptic['DB2'][nextState] += 1
    postSynaptic['DB3'][nextState] += 3
    postSynaptic['DB4'][nextState] += 4
    postSynaptic['DB5'][nextState] += 1
    postSynaptic['DB6'][nextState] += 2
    postSynaptic['DB7'][nextState] += 1
    postSynaptic['FLPL'][nextState] += 1
    postSynaptic['LUAR'][nextState] += 1
    postSynaptic['PDEL'][nextState] += 2
    postSynaptic['PHCR'][nextState] += 1
    postSynaptic['PLMR'][nextState] += 1
    postSynaptic['PVCL'][nextState] += 8
    postSynaptic['PVDL'][nextState] += 1
    postSynaptic['PVR'][nextState] += 1
    postSynaptic['PVWL'][nextState] += 2
    postSynaptic['PVWR'][nextState] += 2
    postSynaptic['RID'][nextState] += 5
    postSynaptic['SIBVR'][nextState] += 2
    postSynaptic['VA8'][nextState] += 2
    postSynaptic['VA9'][nextState] += 1
    postSynaptic['VB10'][nextState] += 1
    postSynaptic['VB4'][nextState] += 3
    postSynaptic['VB6'][nextState] += 2
    postSynaptic['VB7'][nextState] += 3
    postSynaptic['VB8'][nextState] += 1


def PVDL():
    postSynaptic['AVAL'][nextState] += 6
    postSynaptic['AVAR'][nextState] += 6
    postSynaptic['DD5'][nextState] += 1
    postSynaptic['PVCL'][nextState] += 1
    postSynaptic['PVCR'][nextState] += 6
    postSynaptic['VD10'][nextState] += 6


def PVDR():
    postSynaptic['AVAL'][nextState] += 6
    postSynaptic['AVAR'][nextState] += 9
    postSynaptic['DVA'][nextState] += 3
    postSynaptic['PVCL'][nextState] += 13
    postSynaptic['PVCR'][nextState] += 10
    postSynaptic['PVDL'][nextState] += 1
    postSynaptic['VA9'][nextState] += 1


def PVM():
    postSynaptic['AVKL'][nextState] += 11
    postSynaptic['AVL'][nextState] += 1
    postSynaptic['AVM'][nextState] += 1
    postSynaptic['DVA'][nextState] += 3
    postSynaptic['PDEL'][nextState] += 7
    postSynaptic['PDEL'][nextState] += 1
    postSynaptic['PDER'][nextState] += 8
    postSynaptic['PDER'][nextState] += 1
    postSynaptic['PVCL'][nextState] += 2
    postSynaptic['PVR'][nextState] += 1


def PVNL():
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVBR'][nextState] += 3
    postSynaptic['AVDL'][nextState] += 3
    postSynaptic['AVDR'][nextState] += 3
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVFR'][nextState] += 1
    postSynaptic['AVG'][nextState] += 1
    postSynaptic['AVJL'][nextState] += 5
    postSynaptic['AVJR'][nextState] += 5
    postSynaptic['AVL'][nextState] += 2
    postSynaptic['BDUL'][nextState] += 1
    postSynaptic['BDUR'][nextState] += 2
    postSynaptic['DD1'][nextState] += 2
    postSynaptic['MVL09'][nextState] += 3
    postSynaptic['PQR'][nextState] += 1
    postSynaptic['PVCL'][nextState] += 1
    postSynaptic['PVNR'][nextState] += 5
    postSynaptic['PVQR'][nextState] += 1
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['PVWL'][nextState] += 1
    postSynaptic['RIFL'][nextState] += 1


def PVNR():
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 3
    postSynaptic['AVJL'][nextState] += 4
    postSynaptic['AVJR'][nextState] += 1
    postSynaptic['AVL'][nextState] += 2
    postSynaptic['BDUL'][nextState] += 1
    postSynaptic['BDUR'][nextState] += 2
    postSynaptic['DD3'][nextState] += 1
    postSynaptic['HSNR'][nextState] += 2
    postSynaptic['MVL12'][nextState] += 1
    postSynaptic['MVL13'][nextState] += 2
    postSynaptic['PQR'][nextState] += 2
    postSynaptic['PVCL'][nextState] += 1
    postSynaptic['PVNL'][nextState] += 1
    postSynaptic['PVT'][nextState] += 2
    postSynaptic['PVWL'][nextState] += 2
    postSynaptic['VC2'][nextState] += 1
    postSynaptic['VC3'][nextState] += 1
    postSynaptic['VD12'][nextState] += 1
    postSynaptic['VD6'][nextState] += 1
    postSynaptic['VD7'][nextState] += 1


def PVPL():
    postSynaptic['ADAL'][nextState] += 1
    postSynaptic['AQR'][nextState] += 8
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 5
    postSynaptic['AVBR'][nextState] += 6
    postSynaptic['AVDR'][nextState] += 2
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['AVHR'][nextState] += 1
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['AVKR'][nextState] += 6
    postSynaptic['DVC'][nextState] += 2
    postSynaptic['PHAR'][nextState] += 3
    postSynaptic['PQR'][nextState] += 4
    postSynaptic['PVCR'][nextState] += 3
    postSynaptic['PVPR'][nextState] += 1
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 2
    postSynaptic['VD13'][nextState] += 2
    postSynaptic['VD3'][nextState] += 1


def PVPR():
    postSynaptic['ADFR'][nextState] += 1
    postSynaptic['AQR'][nextState] += 11
    postSynaptic['ASHR'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 4
    postSynaptic['AVBR'][nextState] += 5
    postSynaptic['AVHL'][nextState] += 3
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['AVL'][nextState] += 4
    postSynaptic['DD2'][nextState] += 1
    postSynaptic['DVC'][nextState] += 14
    postSynaptic['PVCL'][nextState] += 4
    postSynaptic['PVCR'][nextState] += 7
    postSynaptic['PVPL'][nextState] += 1
    postSynaptic['PVQR'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 2
    postSynaptic['RIGR'][nextState] += 1
    postSynaptic['RIMR'][nextState] += 1
    postSynaptic['RMGR'][nextState] += 1
    postSynaptic['VD4'][nextState] += 1
    postSynaptic['VD5'][nextState] += 1


def PVQL():
    postSynaptic['ADAL'][nextState] += 1
    postSynaptic['AIAL'][nextState] += 3
    postSynaptic['ASJL'][nextState] += 1
    postSynaptic['ASKL'][nextState] += 4
    postSynaptic['ASKL'][nextState] += 5
    postSynaptic['HSNL'][nextState] += 2
    postSynaptic['PVQR'][nextState] += 2
    postSynaptic['RMGL'][nextState] += 1


def PVQR():
    postSynaptic['ADAR'][nextState] += 1
    postSynaptic['AIAR'][nextState] += 7
    postSynaptic['ASER'][nextState] += 1
    postSynaptic['ASKR'][nextState] += 8
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVFL'][nextState] += 1
    postSynaptic['AVFR'][nextState] += 1
    postSynaptic['AVL'][nextState] += 1
    postSynaptic['AWAR'][nextState] += 2
    postSynaptic['DD1'][nextState] += 1
    postSynaptic['DVC'][nextState] += 1
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['PVNL'][nextState] += 1
    postSynaptic['PVQL'][nextState] += 1
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['RIFR'][nextState] += 1
    postSynaptic['VD1'][nextState] += 1


def PVR():
    postSynaptic['ADAL'][nextState] += 1
    postSynaptic['ALML'][nextState] += 1
    postSynaptic['AS6'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 4
    postSynaptic['AVBR'][nextState] += 4
    postSynaptic['AVJL'][nextState] += 3
    postSynaptic['AVJR'][nextState] += 2
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['DA9'][nextState] += 1
    postSynaptic['DB2'][nextState] += 1
    postSynaptic['DB3'][nextState] += 1
    postSynaptic['DVA'][nextState] += 3
    postSynaptic['IL1DL'][nextState] += 1
    postSynaptic['IL1DR'][nextState] += 1
    postSynaptic['IL1VL'][nextState] += 1
    postSynaptic['IL1VR'][nextState] += 1
    postSynaptic['LUAL'][nextState] += 1
    postSynaptic['LUAR'][nextState] += 1
    postSynaptic['PDEL'][nextState] += 1
    postSynaptic['PDER'][nextState] += 1
    postSynaptic['PLMR'][nextState] += 2
    postSynaptic['PVCR'][nextState] += 1
    postSynaptic['RIPL'][nextState] += 3
    postSynaptic['RIPR'][nextState] += 3
    postSynaptic['SABD'][nextState] += 1
    postSynaptic['URADL'][nextState] += 1


def PVT():
    postSynaptic['AIBL'][nextState] += 3
    postSynaptic['AIBR'][nextState] += 5
    postSynaptic['AVKL'][nextState] += 9
    postSynaptic['AVKR'][nextState] += 7
    postSynaptic['AVL'][nextState] += 2
    postSynaptic['DVC'][nextState] += 2
    postSynaptic['PVPL'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 2
    postSynaptic['RIGR'][nextState] += 3
    postSynaptic['RIH'][nextState] += 1
    postSynaptic['RMEV'][nextState] += 1
    postSynaptic['RMFL'][nextState] += 2
    postSynaptic['RMFR'][nextState] += 3
    postSynaptic['SMBDR'][nextState] += 1


def PVWL():
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['PVCR'][nextState] += 2
    postSynaptic['PVT'][nextState] += 2
    postSynaptic['PVWR'][nextState] += 1
    postSynaptic['VA12'][nextState] += 1


def PVWR():
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['PVCR'][nextState] += 2
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['VA12'][nextState] += 1


def RIAL():
    postSynaptic['CEPVL'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 1
    postSynaptic['RIVL'][nextState] += 2
    postSynaptic['RIVR'][nextState] += 4
    postSynaptic['RMDDL'][nextState] += 12
    postSynaptic['RMDDR'][nextState] += 7
    postSynaptic['RMDL'][nextState] += 6
    postSynaptic['RMDR'][nextState] += 6
    postSynaptic['RMDVL'][nextState] += 9
    postSynaptic['RMDVR'][nextState] += 11
    postSynaptic['SIADL'][nextState] += 2
    postSynaptic['SMDDL'][nextState] += 8
    postSynaptic['SMDDR'][nextState] += 10
    postSynaptic['SMDVL'][nextState] += 6
    postSynaptic['SMDVR'][nextState] += 11


def RIAR():
    postSynaptic['CEPVR'][nextState] += 1
    postSynaptic['IL1R'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 4
    postSynaptic['RIVL'][nextState] += 1
    postSynaptic['RMDDL'][nextState] += 10
    postSynaptic['RMDDR'][nextState] += 11
    postSynaptic['RMDL'][nextState] += 3
    postSynaptic['RMDR'][nextState] += 8
    postSynaptic['RMDVL'][nextState] += 12
    postSynaptic['RMDVR'][nextState] += 10
    postSynaptic['SAADR'][nextState] += 1
    postSynaptic['SIADL'][nextState] += 1
    postSynaptic['SIADR'][nextState] += 1
    postSynaptic['SIAVL'][nextState] += 1
    postSynaptic['SMDDL'][nextState] += 7
    postSynaptic['SMDDR'][nextState] += 7
    postSynaptic['SMDVL'][nextState] += 13
    postSynaptic['SMDVR'][nextState] += 7


def RIBL():
    postSynaptic['AIBR'][nextState] += 2
    postSynaptic['AUAL'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['AVDR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 5
    postSynaptic['BAGR'][nextState] += 1
    postSynaptic['OLQDL'][nextState] += 2
    postSynaptic['OLQVL'][nextState] += 1
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 3
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 3
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['SIADL'][nextState] += 1
    postSynaptic['SIAVL'][nextState] += 1
    postSynaptic['SIBDL'][nextState] += 1
    postSynaptic['SIBVL'][nextState] += 1
    postSynaptic['SIBVR'][nextState] += 1
    postSynaptic['SMBDL'][nextState] += 1
    postSynaptic['SMDDL'][nextState] += 1
    postSynaptic['SMDVR'][nextState] += 4


def RIBR():
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['AIZR'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 3
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['BAGL'][nextState] += 1
    postSynaptic['OLQDR'][nextState] += 2
    postSynaptic['OLQVR'][nextState] += 1
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 2
    postSynaptic['RIBL'][nextState] += 3
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RIGR'][nextState] += 2
    postSynaptic['RIH'][nextState] += 1
    postSynaptic['SIADR'][nextState] += 1
    postSynaptic['SIAVR'][nextState] += 1
    postSynaptic['SIBDR'][nextState] += 1
    postSynaptic['SIBVR'][nextState] += 1
    postSynaptic['SMBDR'][nextState] += 1
    postSynaptic['SMDDL'][nextState] += 2
    postSynaptic['SMDDR'][nextState] += 1
    postSynaptic['SMDVL'][nextState] += 2


def RICL():
    postSynaptic['ADAR'][nextState] += 1
    postSynaptic['ASHL'][nextState] += 2
    postSynaptic['AVAL'][nextState] += 5
    postSynaptic['AVAR'][nextState] += 6
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['AVKR'][nextState] += 2
    postSynaptic['AWBR'][nextState] += 1
    postSynaptic['RIML'][nextState] += 1
    postSynaptic['RIMR'][nextState] += 3
    postSynaptic['RIVR'][nextState] += 1
    postSynaptic['RMFR'][nextState] += 1
    postSynaptic['SMBDL'][nextState] += 2
    postSynaptic['SMDDL'][nextState] += 3
    postSynaptic['SMDDR'][nextState] += 3
    postSynaptic['SMDVR'][nextState] += 1


def RICR():
    postSynaptic['ADAR'][nextState] += 1
    postSynaptic['ASHR'][nextState] += 2
    postSynaptic['AVAL'][nextState] += 5
    postSynaptic['AVAR'][nextState] += 5
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['SMBDR'][nextState] += 1
    postSynaptic['SMDDL'][nextState] += 4
    postSynaptic['SMDDR'][nextState] += 3
    postSynaptic['SMDVL'][nextState] += 2
    postSynaptic['SMDVR'][nextState] += 1

# todo: instance of MDL21
def RID():
    postSynaptic['ALA'][nextState] += 1
    postSynaptic['AS2'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['DA6'][nextState] += 3
    postSynaptic['DA9'][nextState] += 1
    postSynaptic['DB1'][nextState] += 1
    postSynaptic['DD1'][nextState] += 4
    postSynaptic['DD2'][nextState] += 4
    postSynaptic['DD3'][nextState] += 3
    #postSynaptic['MDL14'][nextState] += -2
    #postSynaptic['MDL21'][nextState] += -3
    postSynaptic['PDB'][nextState] += 2
    postSynaptic['VD13'][nextState] += 1
    postSynaptic['VD5'][nextState] += 1


def RIFL():
    postSynaptic['ALML'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 10
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['AVG'][nextState] += 1
    postSynaptic['AVHR'][nextState] += 1
    postSynaptic['AVJR'][nextState] += 2
    postSynaptic['PVPL'][nextState] += 3
    postSynaptic['RIML'][nextState] += 4
    postSynaptic['VD1'][nextState] += 1


def RIFR():
    postSynaptic['ASHR'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 17
    postSynaptic['AVFL'][nextState] += 1
    postSynaptic['AVG'][nextState] += 1
    postSynaptic['AVHL'][nextState] += 1
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['AVJR'][nextState] += 2
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['PVCL'][nextState] += 1
    postSynaptic['PVCR'][nextState] += 1
    postSynaptic['PVPR'][nextState] += 4
    postSynaptic['RIMR'][nextState] += 4
    postSynaptic['RIPR'][nextState] += 1


def RIGL():
    postSynaptic['AIBR'][nextState] += 3
    postSynaptic['AIZR'][nextState] += 1
    postSynaptic['ALNL'][nextState] += 1
    postSynaptic['AQR'][nextState] += 2
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['AVKR'][nextState] += 2
    postSynaptic['BAGR'][nextState] += 2
    postSynaptic['DVC'][nextState] += 1
    postSynaptic['OLLL'][nextState] += 1
    postSynaptic['OLQDL'][nextState] += 1
    postSynaptic['OLQVL'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 2
    postSynaptic['RIGR'][nextState] += 3
    postSynaptic['RIR'][nextState] += 2
    postSynaptic['RMEL'][nextState] += 2
    postSynaptic['RMHR'][nextState] += 3
    postSynaptic['URYDL'][nextState] += 1
    postSynaptic['URYVL'][nextState] += 1
    postSynaptic['VB2'][nextState] += 1
    postSynaptic['VD1'][nextState] += 2


def RIGR():
    postSynaptic['AIBL'][nextState] += 3
    postSynaptic['ALNR'][nextState] += 1
    postSynaptic['AQR'][nextState] += 1
    postSynaptic['AVER'][nextState] += 2
    postSynaptic['AVKL'][nextState] += 4
    postSynaptic['AVKR'][nextState] += 2
    postSynaptic['BAGL'][nextState] += 1
    postSynaptic['OLLR'][nextState] += 1
    postSynaptic['OLQDR'][nextState] += 1
    postSynaptic['OLQVR'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 2
    postSynaptic['RIGL'][nextState] += 3
    postSynaptic['RIR'][nextState] += 1
    postSynaptic['RMHL'][nextState] += 4
    postSynaptic['URYDR'][nextState] += 1
    postSynaptic['URYVR'][nextState] += 1


def RIH():
    postSynaptic['ADFR'][nextState] += 1
    postSynaptic['AIZL'][nextState] += 4
    postSynaptic['AIZR'][nextState] += 4
    postSynaptic['AUAR'][nextState] += 1
    postSynaptic['BAGR'][nextState] += 1
    postSynaptic['CEPDL'][nextState] += 2
    postSynaptic['CEPDR'][nextState] += 2
    postSynaptic['CEPVL'][nextState] += 2
    postSynaptic['CEPVR'][nextState] += 2
    postSynaptic['FLPL'][nextState] += 1
    postSynaptic['IL2L'][nextState] += 2
    postSynaptic['IL2R'][nextState] += 1
    postSynaptic['OLQDL'][nextState] += 4
    postSynaptic['OLQDR'][nextState] += 2
    postSynaptic['OLQVL'][nextState] += 1
    postSynaptic['OLQVR'][nextState] += 6
    postSynaptic['RIAL'][nextState] += 10
    postSynaptic['RIAR'][nextState] += 8
    postSynaptic['RIBL'][nextState] += 5
    postSynaptic['RIBR'][nextState] += 4
    postSynaptic['RIPL'][nextState] += 4
    postSynaptic['RIPR'][nextState] += 6
    postSynaptic['RMER'][nextState] += 2
    postSynaptic['RMEV'][nextState] += 1
    postSynaptic['URYVR'][nextState] += 1


def RIML():
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['AIYL'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['AVBL'][nextState] += 2
    postSynaptic['AVBR'][nextState] += 3
    postSynaptic['AVEL'][nextState] += 2
    postSynaptic['AVER'][nextState] += 3
    postSynaptic['MDR05'][nextState] += 2
    postSynaptic['MVR05'][nextState] += 2
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIS'][nextState] += 1
    postSynaptic['RMDL'][nextState] += 1
    postSynaptic['RMDR'][nextState] += 1
    postSynaptic['RMFR'][nextState] += 1
    postSynaptic['SAADR'][nextState] += 1
    postSynaptic['SAAVL'][nextState] += 3
    postSynaptic['SAAVR'][nextState] += 2
    postSynaptic['SMDDR'][nextState] += 5
    postSynaptic['SMDVL'][nextState] += 1


def RIMR():
    postSynaptic['ADAR'][nextState] += 1
    postSynaptic['AIBL'][nextState] += 4
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['AIYR'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 5
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 2
    postSynaptic['AVBR'][nextState] += 5
    postSynaptic['AVEL'][nextState] += 3
    postSynaptic['AVER'][nextState] += 2
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['MDL05'][nextState] += 1
    postSynaptic['MDL07'][nextState] += 1
    postSynaptic['MVL05'][nextState] += 1
    postSynaptic['MVL07'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RIS'][nextState] += 2
    postSynaptic['RMDL'][nextState] += 1
    postSynaptic['RMDR'][nextState] += 1
    postSynaptic['RMFL'][nextState] += 1
    postSynaptic['RMFR'][nextState] += 1
    postSynaptic['SAAVL'][nextState] += 3
    postSynaptic['SAAVR'][nextState] += 3
    postSynaptic['SMDDL'][nextState] += 2
    postSynaptic['SMDDR'][nextState] += 4


def RIPL():
    postSynaptic['OLQDL'][nextState] += 1
    postSynaptic['OLQDR'][nextState] += 1
    postSynaptic['RMED'][nextState] += 1


def RIPR():
    postSynaptic['OLQDL'][nextState] += 1
    postSynaptic['OLQDR'][nextState] += 1
    postSynaptic['RMED'][nextState] += 1


def RIR():
    postSynaptic['AFDR'][nextState] += 1
    postSynaptic['AIZL'][nextState] += 3
    postSynaptic['AIZR'][nextState] += 5
    postSynaptic['AUAL'][nextState] += 1
    postSynaptic['AWBR'][nextState] += 1
    postSynaptic['BAGL'][nextState] += 1
    postSynaptic['BAGR'][nextState] += 2
    postSynaptic['DVA'][nextState] += 2
    postSynaptic['HSNL'][nextState] += 1
    postSynaptic['PVPL'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 5
    postSynaptic['RIAR'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['URXL'][nextState] += 5
    postSynaptic['URXR'][nextState] += 1


def RIS():
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 7
    postSynaptic['AVER'][nextState] += 7
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['AVKR'][nextState] += 4
    postSynaptic['AVL'][nextState] += 2
    postSynaptic['CEPDR'][nextState] += 1
    postSynaptic['CEPVL'][nextState] += 2
    postSynaptic['CEPVR'][nextState] += 1
    postSynaptic['DB1'][nextState] += 1
    postSynaptic['OLLR'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 3
    postSynaptic['RIBR'][nextState] += 5
    postSynaptic['RIML'][nextState] += 2
    postSynaptic['RIMR'][nextState] += 5
    postSynaptic['RMDDL'][nextState] += 1
    postSynaptic['RMDL'][nextState] += 2
    postSynaptic['RMDR'][nextState] += 4
    postSynaptic['SMDDL'][nextState] += 1
    postSynaptic['SMDDR'][nextState] += 3
    postSynaptic['SMDVL'][nextState] += 1
    postSynaptic['SMDVR'][nextState] += 1
    postSynaptic['URYVR'][nextState] += 1


def RIVL():
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['MVR05'][nextState] += -2
    postSynaptic['MVR06'][nextState] += -2
    postSynaptic['MVR08'][nextState] += -3
    postSynaptic['RIAL'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 1
    postSynaptic['RIVR'][nextState] += 2
    postSynaptic['RMDL'][nextState] += 2
    postSynaptic['SAADR'][nextState] += 3
    postSynaptic['SDQR'][nextState] += 2
    postSynaptic['SIAVR'][nextState] += 2
    postSynaptic['SMDDR'][nextState] += 1
    postSynaptic['SMDVL'][nextState] += 1


def RIVR():
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['MVL05'][nextState] += -2
    postSynaptic['MVL06'][nextState] += -2
    postSynaptic['MVL08'][nextState] += -2
    postSynaptic['MVR04'][nextState] += -2
    postSynaptic['MVR06'][nextState] += -2
    postSynaptic['RIAL'][nextState] += 2
    postSynaptic['RIAR'][nextState] += 1
    postSynaptic['RIVL'][nextState] += 2
    postSynaptic['RMDDL'][nextState] += 1
    postSynaptic['RMDR'][nextState] += 1
    postSynaptic['RMDVR'][nextState] += 1
    postSynaptic['RMEV'][nextState] += 1
    postSynaptic['SAADL'][nextState] += 2
    postSynaptic['SDQR'][nextState] += 2
    postSynaptic['SIAVL'][nextState] += 2
    postSynaptic['SMDDL'][nextState] += 2
    postSynaptic['SMDVR'][nextState] += 4


def RMDDL():
    postSynaptic['MDR01'][nextState] += 1
    postSynaptic['MDR02'][nextState] += 1
    postSynaptic['MDR03'][nextState] += 1
    postSynaptic['MDR04'][nextState] += 1
    postSynaptic['MDR08'][nextState] += 2
    postSynaptic['MVR01'][nextState] += 1
    postSynaptic['OLQVL'][nextState] += 1
    postSynaptic['RMDL'][nextState] += 1
    postSynaptic['RMDVL'][nextState] += 1
    postSynaptic['RMDVR'][nextState] += 7
    postSynaptic['SMDDL'][nextState] += 1


def RMDDR():
    postSynaptic['MDL01'][nextState] += 1
    postSynaptic['MDL02'][nextState] += 1
    postSynaptic['MDL03'][nextState] += 2
    postSynaptic['MDL04'][nextState] += 1
    postSynaptic['MDR04'][nextState] += 1
    postSynaptic['MVR01'][nextState] += 1
    postSynaptic['MVR02'][nextState] += 1
    postSynaptic['OLQVR'][nextState] += 1
    postSynaptic['RMDVL'][nextState] += 12
    postSynaptic['RMDVR'][nextState] += 1
    postSynaptic['SAADR'][nextState] += 1
    postSynaptic['SMDDR'][nextState] += 1
    postSynaptic['URYDL'][nextState] += 1


def RMDL():
    postSynaptic['MDL03'][nextState] += 1
    postSynaptic['MDL05'][nextState] += 2
    postSynaptic['MDR01'][nextState] += 1
    postSynaptic['MDR03'][nextState] += 1
    postSynaptic['MVL01'][nextState] += 1
    postSynaptic['MVR01'][nextState] += 1
    postSynaptic['MVR03'][nextState] += 1
    postSynaptic['MVR05'][nextState] += 2
    postSynaptic['MVR07'][nextState] += 1
    postSynaptic['OLLR'][nextState] += 2
    postSynaptic['RIAL'][nextState] += 4
    postSynaptic['RIAR'][nextState] += 3
    postSynaptic['RMDDL'][nextState] += 1
    postSynaptic['RMDDR'][nextState] += 1
    postSynaptic['RMDR'][nextState] += 3
    postSynaptic['RMDVL'][nextState] += 1
    postSynaptic['RMER'][nextState] += 1
    postSynaptic['RMFL'][nextState] += 1


def RMDR():
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['MDL03'][nextState] += 1
    postSynaptic['MDL05'][nextState] += 1
    postSynaptic['MDR05'][nextState] += 1
    postSynaptic['MVL03'][nextState] += 1
    postSynaptic['MVL05'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 3
    postSynaptic['RIAR'][nextState] += 7
    postSynaptic['RIMR'][nextState] += 2
    postSynaptic['RIS'][nextState] += 1
    postSynaptic['RMDDL'][nextState] += 1
    postSynaptic['RMDL'][nextState] += 1
    postSynaptic['RMDVR'][nextState] += 1


def RMDVL():
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['MDR01'][nextState] += 1
    postSynaptic['MVL04'][nextState] += 1
    postSynaptic['MVR01'][nextState] += 1
    postSynaptic['MVR02'][nextState] += 1
    postSynaptic['MVR03'][nextState] += 1
    postSynaptic['MVR04'][nextState] += 1
    postSynaptic['MVR05'][nextState] += 1
    postSynaptic['MVR06'][nextState] += 1
    postSynaptic['MVR08'][nextState] += 1
    postSynaptic['OLQDL'][nextState] += 1
    postSynaptic['RMDDL'][nextState] += 1
    postSynaptic['RMDDR'][nextState] += 6
    postSynaptic['RMDL'][nextState] += 1
    postSynaptic['RMDVR'][nextState] += 1
    postSynaptic['SAAVL'][nextState] += 1
    postSynaptic['SMDVL'][nextState] += 1


def RMDVR():
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['MDL01'][nextState] += 1
    postSynaptic['MVL01'][nextState] += 1
    postSynaptic['MVL02'][nextState] += 1
    postSynaptic['MVL03'][nextState] += 1
    postSynaptic['MVL04'][nextState] += 1
    postSynaptic['MVL05'][nextState] += 1
    postSynaptic['MVL06'][nextState] += 1
    postSynaptic['MVL08'][nextState] += 1
    postSynaptic['MVR04'][nextState] += 1
    postSynaptic['MVR06'][nextState] += 1
    postSynaptic['MVR08'][nextState] += 1
    postSynaptic['OLQDR'][nextState] += 1
    postSynaptic['RMDDL'][nextState] += 4
    postSynaptic['RMDDR'][nextState] += 1
    postSynaptic['RMDR'][nextState] += 1
    postSynaptic['RMDVL'][nextState] += 1
    postSynaptic['SAAVR'][nextState] += 1
    postSynaptic['SIBDR'][nextState] += 1
    postSynaptic['SIBVR'][nextState] += 1
    postSynaptic['SMDVR'][nextState] += 1


def RMED():
    postSynaptic['IL1VL'][nextState] += 1
    postSynaptic['MVL02'][nextState] += -4
    postSynaptic['MVL04'][nextState] += -4
    postSynaptic['MVL06'][nextState] += -4
    postSynaptic['MVR02'][nextState] += -4
    postSynaptic['MVR04'][nextState] += -4
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RIPL'][nextState] += 1
    postSynaptic['RIPR'][nextState] += 1
    postSynaptic['RMEV'][nextState] += 2


def RMEL():
    postSynaptic['MDR01'][nextState] += -5
    postSynaptic['MDR03'][nextState] += -5
    postSynaptic['MVR01'][nextState] += -5
    postSynaptic['MVR03'][nextState] += -5
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RMEV'][nextState] += 1


def RMER():
    postSynaptic['MDL01'][nextState] += -7
    postSynaptic['MDL03'][nextState] += -7
    postSynaptic['MVL01'][nextState] += -7
    postSynaptic['RMEV'][nextState] += 1


def RMEV():
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 1
    postSynaptic['IL1DL'][nextState] += 1
    postSynaptic['IL1DR'][nextState] += 1
    postSynaptic['MDL02'][nextState] += -3
    postSynaptic['MDL04'][nextState] += -3
    postSynaptic['MDL06'][nextState] += -3
    postSynaptic['MDR02'][nextState] += -3
    postSynaptic['MDR04'][nextState] += -3
    postSynaptic['RMED'][nextState] += 2
    postSynaptic['RMEL'][nextState] += 1
    postSynaptic['RMER'][nextState] += 1
    postSynaptic['SMDDR'][nextState] += 1


def RMFL():
    postSynaptic['AVKL'][nextState] += 4
    postSynaptic['AVKR'][nextState] += 4
    postSynaptic['MDR03'][nextState] += 1
    postSynaptic['MVR01'][nextState] += 1
    postSynaptic['MVR03'][nextState] += 1
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['RIGR'][nextState] += 1
    postSynaptic['RMDR'][nextState] += 3
    postSynaptic['RMGR'][nextState] += 1
    postSynaptic['URBR'][nextState] += 1


def RMFR():
    postSynaptic['AVKL'][nextState] += 3
    postSynaptic['AVKR'][nextState] += 3
    postSynaptic['RMDL'][nextState] += 2


def RMGL():
    postSynaptic['ADAL'][nextState] += 1
    postSynaptic['ADLL'][nextState] += 1
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['ALML'][nextState] += 1
    postSynaptic['ALNL'][nextState] += 1
    postSynaptic['ASHL'][nextState] += 2
    postSynaptic['ASKL'][nextState] += 2
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['AVEL'][nextState] += 2
    postSynaptic['AWBL'][nextState] += 1
    postSynaptic['CEPDL'][nextState] += 1
    postSynaptic['IL2L'][nextState] += 1
    postSynaptic['MDL05'][nextState] += 2
    postSynaptic['MVL05'][nextState] += 2
    postSynaptic['RID'][nextState] += 1
    postSynaptic['RMDL'][nextState] += 1
    postSynaptic['RMDR'][nextState] += 3
    postSynaptic['RMDVL'][nextState] += 3
    postSynaptic['RMHL'][nextState] += 3
    postSynaptic['RMHR'][nextState] += 1
    postSynaptic['SIAVL'][nextState] += 1
    postSynaptic['SIBVL'][nextState] += 3
    postSynaptic['SIBVR'][nextState] += 1
    postSynaptic['SMBVL'][nextState] += 1
    postSynaptic['URXL'][nextState] += 2


def RMGR():
    postSynaptic['ADAR'][nextState] += 1
    postSynaptic['AIMR'][nextState] += 1
    postSynaptic['ALNR'][nextState] += 1
    postSynaptic['ASHR'][nextState] += 2
    postSynaptic['ASKR'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 3
    postSynaptic['AVJL'][nextState] += 1
    postSynaptic['AWBR'][nextState] += 1
    postSynaptic['IL2R'][nextState] += 1
    postSynaptic['MDR05'][nextState] += 1
    postSynaptic['MVR05'][nextState] += 1
    postSynaptic['MVR07'][nextState] += 1
    postSynaptic['RIR'][nextState] += 1
    postSynaptic['RMDL'][nextState] += 4
    postSynaptic['RMDR'][nextState] += 2
    postSynaptic['RMDVR'][nextState] += 5
    postSynaptic['RMHR'][nextState] += 1
    postSynaptic['URXR'][nextState] += 2


def RMHL():
    postSynaptic['MDR01'][nextState] += 2
    postSynaptic['MDR03'][nextState] += 3
    postSynaptic['MVR01'][nextState] += 2
    postSynaptic['RMDR'][nextState] += 1
    postSynaptic['RMGL'][nextState] += 3
    postSynaptic['SIBVR'][nextState] += 1


def RMHR():
    postSynaptic['MDL01'][nextState] += 2
    postSynaptic['MDL03'][nextState] += 2
    postSynaptic['MDL05'][nextState] += 2
    postSynaptic['MVL01'][nextState] += 2
    postSynaptic['RMER'][nextState] += 1
    postSynaptic['RMGL'][nextState] += 1
    postSynaptic['RMGR'][nextState] += 1


def SAADL():
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 6
    postSynaptic['RIML'][nextState] += 3
    postSynaptic['RIMR'][nextState] += 6
    postSynaptic['RMGR'][nextState] += 1
    postSynaptic['SMBDL'][nextState] += 1


def SAADR():
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 3
    postSynaptic['OLLL'][nextState] += 1
    postSynaptic['RIML'][nextState] += 4
    postSynaptic['RIMR'][nextState] += 5
    postSynaptic['RMDDR'][nextState] += 1
    postSynaptic['RMFL'][nextState] += 1
    postSynaptic['RMGL'][nextState] += 1


def SAAVL():
    postSynaptic['AIBL'][nextState] += 1
    postSynaptic['ALNL'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 16
    postSynaptic['OLLR'][nextState] += 1
    postSynaptic['RIML'][nextState] += 2
    postSynaptic['RIMR'][nextState] += 12
    postSynaptic['RMDVL'][nextState] += 2
    postSynaptic['RMFR'][nextState] += 2
    postSynaptic['SMBVR'][nextState] += 3
    postSynaptic['SMDDR'][nextState] += 8


def SAAVR():
    postSynaptic['AVAR'][nextState] += 13
    postSynaptic['RIML'][nextState] += 5
    postSynaptic['RIMR'][nextState] += 2
    postSynaptic['RMDVR'][nextState] += 1
    postSynaptic['SMBVL'][nextState] += 2
    postSynaptic['SMDDL'][nextState] += 6


def SABD():
    postSynaptic['AVAL'][nextState] += 4
    postSynaptic['VA2'][nextState] += 4
    postSynaptic['VA3'][nextState] += 2
    postSynaptic['VA4'][nextState] += 1


def SABVL():
    postSynaptic['AVAR'][nextState] += 3
    postSynaptic['DA1'][nextState] += 2
    postSynaptic['DA2'][nextState] += 1


def SABVR():
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['DA1'][nextState] += 3


def SDQL():
    postSynaptic['ALML'][nextState] += 2
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 3
    postSynaptic['AVEL'][nextState] += 1
    postSynaptic['FLPL'][nextState] += 1
    postSynaptic['RICR'][nextState] += 1
    postSynaptic['RIS'][nextState] += 3
    postSynaptic['RMFL'][nextState] += 1
    postSynaptic['SDQR'][nextState] += 1


def SDQR():
    postSynaptic['ADLL'][nextState] += 1
    postSynaptic['AIBL'][nextState] += 2
    postSynaptic['AVAL'][nextState] += 3
    postSynaptic['AVBL'][nextState] += 7
    postSynaptic['AVBR'][nextState] += 4
    postSynaptic['DVA'][nextState] += 3
    postSynaptic['RICR'][nextState] += 1
    postSynaptic['RIVL'][nextState] += 2
    postSynaptic['RIVR'][nextState] += 2
    postSynaptic['RMHL'][nextState] += 2
    postSynaptic['RMHR'][nextState] += 1
    postSynaptic['SDQL'][nextState] += 1
    postSynaptic['SIBVL'][nextState] += 1


def SIADL():
    postSynaptic['RIBL'][nextState] += 1


def SIADR():
    postSynaptic['RIBR'][nextState] += 1


def SIAVL():
    postSynaptic['RIBL'][nextState] += 1


def SIAVR():
    postSynaptic['RIBR'][nextState] += 1


def SIBDL():
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['SIBVL'][nextState] += 1


def SIBDR():
    postSynaptic['AIML'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['SIBVR'][nextState] += 1


def SIBVL():
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['SDQR'][nextState] += 1
    postSynaptic['SIBDL'][nextState] += 1


def SIBVR():
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RMHL'][nextState] += 1
    postSynaptic['SIBDR'][nextState] += 1


def SMBDL():
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['AVKR'][nextState] += 1
    postSynaptic['MDR01'][nextState] += 2
    postSynaptic['MDR02'][nextState] += 2
    postSynaptic['MDR03'][nextState] += 2
    postSynaptic['MDR04'][nextState] += 2
    postSynaptic['MDR06'][nextState] += 3
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RMED'][nextState] += 3
    postSynaptic['SAADL'][nextState] += 1
    postSynaptic['SAAVR'][nextState] += 1


def SMBDR():
    postSynaptic['ALNL'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['AVKR'][nextState] += 2
    postSynaptic['MDL02'][nextState] += 1
    postSynaptic['MDL03'][nextState] += 1
    postSynaptic['MDL04'][nextState] += 1
    postSynaptic['MDL06'][nextState] += 2
    postSynaptic['MDR04'][nextState] += 1
    postSynaptic['MDR08'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RMED'][nextState] += 4
    postSynaptic['SAAVL'][nextState] += 3


def SMBVL():
    postSynaptic['MVL01'][nextState] += 1
    postSynaptic['MVL02'][nextState] += 1
    postSynaptic['MVL03'][nextState] += 1
    postSynaptic['MVL04'][nextState] += 1
    postSynaptic['MVL05'][nextState] += 1
    postSynaptic['MVL06'][nextState] += 1
    postSynaptic['MVL08'][nextState] += 1
    postSynaptic['PLNL'][nextState] += 1
    postSynaptic['RMEV'][nextState] += 5
    postSynaptic['SAADL'][nextState] += 3
    postSynaptic['SAAVR'][nextState] += 2


def SMBVR():
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['AVKR'][nextState] += 1
    postSynaptic['MVR01'][nextState] += 1
    postSynaptic['MVR02'][nextState] += 1
    postSynaptic['MVR03'][nextState] += 1
    postSynaptic['MVR04'][nextState] += 1
    postSynaptic['MVR06'][nextState] += 1
    postSynaptic['MVR07'][nextState] += 1
    postSynaptic['RMEV'][nextState] += 3
    postSynaptic['SAADR'][nextState] += 4
    postSynaptic['SAAVL'][nextState] += 3


def SMDDL():
    postSynaptic['MDL04'][nextState] += 1
    postSynaptic['MDL06'][nextState] += 1
    postSynaptic['MDL08'][nextState] += 1
    postSynaptic['MDR02'][nextState] += 1
    postSynaptic['MDR03'][nextState] += 1
    postSynaptic['MDR04'][nextState] += 1
    postSynaptic['MDR05'][nextState] += 1
    postSynaptic['MDR06'][nextState] += 1
    postSynaptic['MDR07'][nextState] += 1
    postSynaptic['MVL02'][nextState] += 1
    postSynaptic['MVL04'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RIS'][nextState] += 1
    postSynaptic['RMDDL'][nextState] += 1
    postSynaptic['SMDVR'][nextState] += 2


def SMDDR():
    postSynaptic['MDL04'][nextState] += 1
    postSynaptic['MDL05'][nextState] += 1
    postSynaptic['MDL06'][nextState] += 1
    postSynaptic['MDL08'][nextState] += 1
    postSynaptic['MDR04'][nextState] += 1
    postSynaptic['MDR06'][nextState] += 1
    postSynaptic['MVR02'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 2
    postSynaptic['RIAR'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RIS'][nextState] += 1
    postSynaptic['RMDDR'][nextState] += 1
    postSynaptic['VD1'][nextState] += 1


def SMDVL():
    postSynaptic['MVL03'][nextState] += 1
    postSynaptic['MVL06'][nextState] += 1
    postSynaptic['MVR02'][nextState] += 1
    postSynaptic['MVR03'][nextState] += 1
    postSynaptic['MVR04'][nextState] += 1
    postSynaptic['MVR06'][nextState] += 1
    postSynaptic['PVR'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 3
    postSynaptic['RIAR'][nextState] += 8
    postSynaptic['RIBR'][nextState] += 2
    postSynaptic['RIS'][nextState] += 1
    postSynaptic['RIVL'][nextState] += 2
    postSynaptic['RMDDR'][nextState] += 1
    postSynaptic['RMDVL'][nextState] += 1
    postSynaptic['SMDDR'][nextState] += 4
    postSynaptic['SMDVR'][nextState] += 1


def SMDVR():
    postSynaptic['MVL02'][nextState] += 1
    postSynaptic['MVL03'][nextState] += 1
    postSynaptic['MVL04'][nextState] += 1
    postSynaptic['MVR07'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 7
    postSynaptic['RIAR'][nextState] += 5
    postSynaptic['RIBL'][nextState] += 2
    postSynaptic['RIVR'][nextState] += 1
    postSynaptic['RIVR'][nextState] += 2
    postSynaptic['RMDDL'][nextState] += 1
    postSynaptic['RMDVR'][nextState] += 1
    postSynaptic['SMDDL'][nextState] += 2
    postSynaptic['SMDVL'][nextState] += 1
    postSynaptic['VB1'][nextState] += 1


def URADL():
    postSynaptic['IL1DL'][nextState] += 2
    postSynaptic['MDL02'][nextState] += 2
    postSynaptic['MDL03'][nextState] += 2
    postSynaptic['MDL04'][nextState] += 2
    postSynaptic['RIPL'][nextState] += 3
    postSynaptic['RMEL'][nextState] += 1


def URADR():
    postSynaptic['IL1DR'][nextState] += 1
    postSynaptic['MDR01'][nextState] += 3
    postSynaptic['MDR02'][nextState] += 2
    postSynaptic['MDR03'][nextState] += 3
    postSynaptic['RIPR'][nextState] += 3
    postSynaptic['RMDVR'][nextState] += 1
    postSynaptic['RMED'][nextState] += 1
    postSynaptic['RMER'][nextState] += 1
    postSynaptic['URYDR'][nextState] += 1


def URAVL():
    postSynaptic['MVL01'][nextState] += 2
    postSynaptic['MVL02'][nextState] += 2
    postSynaptic['MVL03'][nextState] += 3
    postSynaptic['MVL04'][nextState] += 2
    postSynaptic['RIPL'][nextState] += 3
    postSynaptic['RMEL'][nextState] += 1
    postSynaptic['RMER'][nextState] += 1
    postSynaptic['RMEV'][nextState] += 2


def URAVR():
    postSynaptic['IL1R'][nextState] += 1
    postSynaptic['MVR01'][nextState] += 2
    postSynaptic['MVR02'][nextState] += 2
    postSynaptic['MVR03'][nextState] += 2
    postSynaptic['MVR04'][nextState] += 2
    postSynaptic['RIPR'][nextState] += 3
    postSynaptic['RMDVL'][nextState] += 1
    postSynaptic['RMER'][nextState] += 2
    postSynaptic['RMEV'][nextState] += 2


def URBL():
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['CEPDL'][nextState] += 1
    postSynaptic['IL1L'][nextState] += 1
    postSynaptic['OLQDL'][nextState] += 1
    postSynaptic['OLQVL'][nextState] += 1
    postSynaptic['RICR'][nextState] += 1
    postSynaptic['RMDDR'][nextState] += 1
    postSynaptic['SIAVL'][nextState] += 1
    postSynaptic['SMBDR'][nextState] += 1
    postSynaptic['URXL'][nextState] += 2


def URBR():
    postSynaptic['ADAR'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['CEPDR'][nextState] += 1
    postSynaptic['IL1R'][nextState] += 3
    postSynaptic['IL2R'][nextState] += 1
    postSynaptic['OLQDR'][nextState] += 1
    postSynaptic['OLQVR'][nextState] += 1
    postSynaptic['RICR'][nextState] += 1
    postSynaptic['RMDL'][nextState] += 1
    postSynaptic['RMDR'][nextState] += 1
    postSynaptic['RMFL'][nextState] += 1
    postSynaptic['SIAVR'][nextState] += 2
    postSynaptic['SMBDL'][nextState] += 1
    postSynaptic['URXR'][nextState] += 4


def URXL():
    postSynaptic['ASHL'][nextState] += 1
    postSynaptic['AUAL'][nextState] += 5
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 4
    postSynaptic['AVJR'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 8
    postSynaptic['RICL'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 3
    postSynaptic['RMGL'][nextState] += 2
    postSynaptic['RMGL'][nextState] += 1


def URXR():
    postSynaptic['AUAR'][nextState] += 4
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['AVER'][nextState] += 2
    postSynaptic['IL2R'][nextState] += 1
    postSynaptic['OLQVR'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 3
    postSynaptic['RIGR'][nextState] += 2
    postSynaptic['RIPR'][nextState] += 3
    postSynaptic['RMDR'][nextState] += 1
    postSynaptic['RMGR'][nextState] += 2
    postSynaptic['SIAVR'][nextState] += 1


def URYDL():
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVER'][nextState] += 2
    postSynaptic['RIBL'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RMDDR'][nextState] += 4
    postSynaptic['RMDVL'][nextState] += 6
    postSynaptic['SMDDL'][nextState] += 1
    postSynaptic['SMDDR'][nextState] += 1


def URYDR():
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVEL'][nextState] += 2
    postSynaptic['AVER'][nextState] += 2
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RIGR'][nextState] += 1
    postSynaptic['RMDDL'][nextState] += 3
    postSynaptic['RMDVR'][nextState] += 5
    postSynaptic['SMDDL'][nextState] += 4


def URYVL():
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['AVER'][nextState] += 5
    postSynaptic['IL1VL'][nextState] += 1
    postSynaptic['RIAL'][nextState] += 1
    postSynaptic['RIBL'][nextState] += 2
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['RIH'][nextState] += 1
    postSynaptic['RIS'][nextState] += 1
    postSynaptic['RMDDL'][nextState] += 4
    postSynaptic['RMDVR'][nextState] += 2
    postSynaptic['SIBVR'][nextState] += 1
    postSynaptic['SMDVR'][nextState] += 4


def URYVR():
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVEL'][nextState] += 6
    postSynaptic['IL1VR'][nextState] += 1
    postSynaptic['RIAR'][nextState] += 1
    postSynaptic['RIBR'][nextState] += 1
    postSynaptic['RIGR'][nextState] += 1
    postSynaptic['RMDDR'][nextState] += 6
    postSynaptic['RMDVL'][nextState] += 4
    postSynaptic['SIBDR'][nextState] += 1
    postSynaptic['SIBVL'][nextState] += 1
    postSynaptic['SMDVL'][nextState] += 3


def VA1():
    postSynaptic['AVAL'][nextState] += 3
    postSynaptic['DA2'][nextState] += 2
    postSynaptic['DD1'][nextState] += 9
    postSynaptic['MVL07'][nextState] += 3
    postSynaptic['MVL08'][nextState] += 3
    postSynaptic['MVR07'][nextState] += 3
    postSynaptic['MVR08'][nextState] += 3
    postSynaptic['VD1'][nextState] += 2


def VA2():
    postSynaptic['AVAL'][nextState] += 5
    postSynaptic['DD1'][nextState] += 13
    postSynaptic['MVL07'][nextState] += 5
    postSynaptic['MVL10'][nextState] += 5
    postSynaptic['MVR07'][nextState] += 5
    postSynaptic['MVR10'][nextState] += 5
    postSynaptic['SABD'][nextState] += 3
    postSynaptic['VA3'][nextState] += 2
    postSynaptic['VB1'][nextState] += 2
    postSynaptic['VD1'][nextState] += 2
    postSynaptic['VD1'][nextState] += 1
    postSynaptic['VD2'][nextState] += 11


def VA3():
    postSynaptic['AS1'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['DD1'][nextState] += 18
    postSynaptic['DD2'][nextState] += 11
    postSynaptic['MVL09'][nextState] += 5
    postSynaptic['MVL10'][nextState] += 5
    postSynaptic['MVL12'][nextState] += 5
    postSynaptic['MVR09'][nextState] += 5
    postSynaptic['MVR10'][nextState] += 5
    postSynaptic['MVR12'][nextState] += 5
    postSynaptic['SABD'][nextState] += 2
    postSynaptic['VA4'][nextState] += 1
    postSynaptic['VD2'][nextState] += 3
    postSynaptic['VD3'][nextState] += 3


def VA4():
    postSynaptic['AS2'][nextState] += 2
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['AVDL'][nextState] += 1
    postSynaptic['DA5'][nextState] += 1
    postSynaptic['DD2'][nextState] += 21
    postSynaptic['MVL11'][nextState] += 6
    postSynaptic['MVL12'][nextState] += 6
    postSynaptic['MVR11'][nextState] += 6
    postSynaptic['MVR12'][nextState] += 6
    postSynaptic['SABD'][nextState] += 1
    postSynaptic['VB3'][nextState] += 2
    postSynaptic['VD4'][nextState] += 3


def VA5():
    postSynaptic['AS3'][nextState] += 2
    postSynaptic['AVAL'][nextState] += 5
    postSynaptic['AVAR'][nextState] += 3
    postSynaptic['DA5'][nextState] += 2
    postSynaptic['DD2'][nextState] += 5
    postSynaptic['DD3'][nextState] += 13
    postSynaptic['MVL11'][nextState] += 5
    postSynaptic['MVL14'][nextState] += 5
    postSynaptic['MVR11'][nextState] += 5
    postSynaptic['MVR14'][nextState] += 5
    postSynaptic['VD5'][nextState] += 2


def VA6():
    postSynaptic['AVAL'][nextState] += 6
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['DD3'][nextState] += 24
    postSynaptic['MVL13'][nextState] += 5
    postSynaptic['MVL14'][nextState] += 5
    postSynaptic['MVR13'][nextState] += 5
    postSynaptic['MVR14'][nextState] += 5
    postSynaptic['VB5'][nextState] += 2
    postSynaptic['VD5'][nextState] += 1
    postSynaptic['VD6'][nextState] += 2


def VA7():
    postSynaptic['AS5'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 2
    postSynaptic['AVAR'][nextState] += 4
    postSynaptic['DD3'][nextState] += 3
    postSynaptic['DD4'][nextState] += 12
    postSynaptic['MVL13'][nextState] += 4
    postSynaptic['MVL15'][nextState] += 4
    postSynaptic['MVL16'][nextState] += 4
    postSynaptic['MVR13'][nextState] += 4
    postSynaptic['MVR15'][nextState] += 4
    postSynaptic['MVR16'][nextState] += 4
    postSynaptic['MVULVA'][nextState] += 4
    postSynaptic['VB3'][nextState] += 1
    postSynaptic['VD7'][nextState] += 9


def VA8():
    postSynaptic['AS6'][nextState] += 1
    postSynaptic['AVAL'][nextState] += 10
    postSynaptic['AVAR'][nextState] += 4
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['DD4'][nextState] += 21
    postSynaptic['MVL15'][nextState] += 6
    postSynaptic['MVL16'][nextState] += 6
    postSynaptic['MVR15'][nextState] += 6
    postSynaptic['MVR16'][nextState] += 6
    postSynaptic['PDER'][nextState] += 1
    postSynaptic['PVCR'][nextState] += 2
    postSynaptic['VA8'][nextState] += 1
    postSynaptic['VA9'][nextState] += 1
    postSynaptic['VB6'][nextState] += 1
    postSynaptic['VB8'][nextState] += 1
    postSynaptic['VB8'][nextState] += 3
    postSynaptic['VB9'][nextState] += 3
    postSynaptic['VD7'][nextState] += 5
    postSynaptic['VD8'][nextState] += 5
    postSynaptic['VD8'][nextState] += 1


def VA9():
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['DD4'][nextState] += 3
    postSynaptic['DD5'][nextState] += 15
    postSynaptic['DVB'][nextState] += 1
    postSynaptic['DVC'][nextState] += 1
    postSynaptic['MVL15'][nextState] += 5
    postSynaptic['MVL18'][nextState] += 5
    postSynaptic['MVR15'][nextState] += 5
    postSynaptic['MVR18'][nextState] += 5
    postSynaptic['PVCR'][nextState] += 1
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['VB8'][nextState] += 6
    postSynaptic['VB8'][nextState] += 1
    postSynaptic['VB9'][nextState] += 4
    postSynaptic['VD7'][nextState] += 1
    postSynaptic['VD9'][nextState] += 10


def VA10():
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['MVL17'][nextState] += 5
    postSynaptic['MVL18'][nextState] += 5
    postSynaptic['MVR17'][nextState] += 5
    postSynaptic['MVR18'][nextState] += 5


def VA11():
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['AVAR'][nextState] += 7
    postSynaptic['DD6'][nextState] += 10
    postSynaptic['MVL19'][nextState] += 5
    postSynaptic['MVL20'][nextState] += 5
    postSynaptic['MVR19'][nextState] += 5
    postSynaptic['MVR20'][nextState] += 5
    postSynaptic['PVNR'][nextState] += 2
    postSynaptic['VB10'][nextState] += 1
    postSynaptic['VD12'][nextState] += 4


def VA12():
    postSynaptic['AS11'][nextState] += 2
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['DA8'][nextState] += 3
    postSynaptic['DA9'][nextState] += 5
    postSynaptic['DB7'][nextState] += 4
    postSynaptic['DD6'][nextState] += 2
    postSynaptic['LUAL'][nextState] += 2
    postSynaptic['MVL21'][nextState] += 5
    postSynaptic['MVL22'][nextState] += 5
    postSynaptic['MVL23'][nextState] += 5
    postSynaptic['MVR21'][nextState] += 5
    postSynaptic['MVR22'][nextState] += 5
    postSynaptic['MVR23'][nextState] += 5
    postSynaptic['PHCL'][nextState] += 1
    postSynaptic['PHCR'][nextState] += 1
    postSynaptic['PVCL'][nextState] += 2
    postSynaptic['PVCR'][nextState] += 3
    postSynaptic['VA11'][nextState] += 1
    postSynaptic['VB11'][nextState] += 1
    postSynaptic['VD12'][nextState] += 3
    postSynaptic['VD13'][nextState] += 11


def VB1():
    postSynaptic['AIBR'][nextState] += 1
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVKL'][nextState] += 4
    postSynaptic['DB2'][nextState] += 2
    postSynaptic['DD1'][nextState] += 1
    postSynaptic['DVA'][nextState] += 1
    postSynaptic['MVL07'][nextState] += 1
    postSynaptic['MVL08'][nextState] += 1
    postSynaptic['MVR07'][nextState] += 1
    postSynaptic['MVR08'][nextState] += 1
    postSynaptic['RIML'][nextState] += 2
    postSynaptic['RMFL'][nextState] += 2
    postSynaptic['SAADL'][nextState] += 9
    postSynaptic['SAADR'][nextState] += 2
    postSynaptic['SABD'][nextState] += 1
    postSynaptic['SMDVR'][nextState] += 1
    postSynaptic['VA1'][nextState] += 3
    postSynaptic['VA3'][nextState] += 1
    postSynaptic['VB2'][nextState] += 4
    postSynaptic['VD1'][nextState] += 3
    postSynaptic['VD2'][nextState] += 1


def VB2():
    postSynaptic['AVBL'][nextState] += 3
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['DB4'][nextState] += 1
    postSynaptic['DD1'][nextState] += 20
    postSynaptic['DD2'][nextState] += 1
    postSynaptic['MVL07'][nextState] += 4
    postSynaptic['MVL09'][nextState] += 4
    postSynaptic['MVL10'][nextState] += 4
    postSynaptic['MVL12'][nextState] += 4
    postSynaptic['MVR07'][nextState] += 4
    postSynaptic['MVR09'][nextState] += 4
    postSynaptic['MVR10'][nextState] += 4
    postSynaptic['MVR12'][nextState] += 4
    postSynaptic['RIGL'][nextState] += 1
    postSynaptic['VA2'][nextState] += 1
    postSynaptic['VB1'][nextState] += 4
    postSynaptic['VB3'][nextState] += 1
    postSynaptic['VB5'][nextState] += 1
    postSynaptic['VB7'][nextState] += 2
    postSynaptic['VC2'][nextState] += 1
    postSynaptic['VD2'][nextState] += 9
    postSynaptic['VD3'][nextState] += 3


def VB3():
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['DB1'][nextState] += 1
    postSynaptic['DD2'][nextState] += 37
    postSynaptic['MVL11'][nextState] += 6
    postSynaptic['MVL12'][nextState] += 6
    postSynaptic['MVL14'][nextState] += 6
    postSynaptic['MVR11'][nextState] += 6
    postSynaptic['MVR12'][nextState] += 6
    postSynaptic['MVR14'][nextState] += 6
    postSynaptic['VA4'][nextState] += 1
    postSynaptic['VA7'][nextState] += 1
    postSynaptic['VB2'][nextState] += 1


def VB4():
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['DB1'][nextState] += 1
    postSynaptic['DB4'][nextState] += 1
    postSynaptic['DD2'][nextState] += 6
    postSynaptic['DD3'][nextState] += 16
    postSynaptic['MVL11'][nextState] += 5
    postSynaptic['MVL14'][nextState] += 5
    postSynaptic['MVR11'][nextState] += 5
    postSynaptic['MVR14'][nextState] += 5
    postSynaptic['VB5'][nextState] += 1


def VB5():
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['DD3'][nextState] += 27
    postSynaptic['MVL13'][nextState] += 6
    postSynaptic['MVL14'][nextState] += 6
    postSynaptic['MVR13'][nextState] += 6
    postSynaptic['MVR14'][nextState] += 6
    postSynaptic['VB2'][nextState] += 1
    postSynaptic['VB4'][nextState] += 1
    postSynaptic['VB6'][nextState] += 8


def VB6():
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['DA4'][nextState] += 1
    postSynaptic['DD4'][nextState] += 30
    postSynaptic['MVL15'][nextState] += 6
    postSynaptic['MVL16'][nextState] += 6
    postSynaptic['MVR15'][nextState] += 6
    postSynaptic['MVR16'][nextState] += 6
    postSynaptic['MVULVA'][nextState] += 6
    postSynaptic['VA8'][nextState] += 1
    postSynaptic['VB5'][nextState] += 1
    postSynaptic['VB7'][nextState] += 1
    postSynaptic['VD6'][nextState] += 1
    postSynaptic['VD7'][nextState] += 8


def VB7():
    postSynaptic['AVBL'][nextState] += 2
    postSynaptic['AVBR'][nextState] += 2
    postSynaptic['DD4'][nextState] += 2
    postSynaptic['MVL15'][nextState] += 5
    postSynaptic['MVR15'][nextState] += 5
    postSynaptic['VB2'][nextState] += 2


def VB8():
    postSynaptic['AVBL'][nextState] += 7
    postSynaptic['AVBR'][nextState] += 3
    postSynaptic['DD5'][nextState] += 30
    postSynaptic['MVL17'][nextState] += 5
    postSynaptic['MVL18'][nextState] += 5
    postSynaptic['MVL20'][nextState] += 5
    postSynaptic['MVR17'][nextState] += 5
    postSynaptic['MVR18'][nextState] += 5
    postSynaptic['MVR20'][nextState] += 5
    postSynaptic['VA8'][nextState] += 3
    postSynaptic['VA9'][nextState] += 9
    postSynaptic['VA9'][nextState] += 1
    postSynaptic['VB9'][nextState] += 6
    postSynaptic['VD10'][nextState] += 1
    postSynaptic['VD9'][nextState] += 10


def VB9():
    postSynaptic['AVAL'][nextState] += 5
    postSynaptic['AVAR'][nextState] += 4
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVBR'][nextState] += 6
    postSynaptic['DD5'][nextState] += 8
    postSynaptic['DVB'][nextState] += 1
    postSynaptic['MVL17'][nextState] += 6
    postSynaptic['MVL20'][nextState] += 6
    postSynaptic['MVR17'][nextState] += 6
    postSynaptic['MVR20'][nextState] += 6
    postSynaptic['PVCL'][nextState] += 2
    postSynaptic['VA8'][nextState] += 3
    postSynaptic['VA9'][nextState] += 4
    postSynaptic['VB8'][nextState] += 1
    postSynaptic['VB8'][nextState] += 3
    postSynaptic['VD10'][nextState] += 5


def VB10():
    postSynaptic['AVBL'][nextState] += 2
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['AVKL'][nextState] += 1
    postSynaptic['DD6'][nextState] += 9
    postSynaptic['MVL19'][nextState] += 5
    postSynaptic['MVL20'][nextState] += 5
    postSynaptic['MVR19'][nextState] += 5
    postSynaptic['MVR20'][nextState] += 5
    postSynaptic['PVCL'][nextState] += 1
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['VD11'][nextState] += 1
    postSynaptic['VD12'][nextState] += 2


def VB11():
    postSynaptic['AVBL'][nextState] += 2
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['DD6'][nextState] += 7
    postSynaptic['MVL21'][nextState] += 5
    postSynaptic['MVL22'][nextState] += 5
    postSynaptic['MVL23'][nextState] += 5
    postSynaptic['MVR21'][nextState] += 5
    postSynaptic['MVR22'][nextState] += 5
    postSynaptic['MVR23'][nextState] += 5
    postSynaptic['PVCR'][nextState] += 1
    postSynaptic['VA12'][nextState] += 2


def VC1():
    postSynaptic['AVL'][nextState] += 2
    postSynaptic['DD1'][nextState] += 7
    postSynaptic['DD2'][nextState] += 6
    postSynaptic['DD3'][nextState] += 6
    postSynaptic['DVC'][nextState] += 1
    postSynaptic['MVULVA'][nextState] += 6
    postSynaptic['PVT'][nextState] += 2
    postSynaptic['VC2'][nextState] += 9
    postSynaptic['VC3'][nextState] += 3
    postSynaptic['VD1'][nextState] += 5
    postSynaptic['VD2'][nextState] += 1
    postSynaptic['VD3'][nextState] += 1
    postSynaptic['VD4'][nextState] += 2
    postSynaptic['VD5'][nextState] += 5
    postSynaptic['VD6'][nextState] += 1


def VC2():
    postSynaptic['DB4'][nextState] += 1
    postSynaptic['DD1'][nextState] += 6
    postSynaptic['DD2'][nextState] += 4
    postSynaptic['DD3'][nextState] += 9
    postSynaptic['DVC'][nextState] += 1
    postSynaptic['MVULVA'][nextState] += 10
    postSynaptic['PVCR'][nextState] += 1
    postSynaptic['PVQR'][nextState] += 1
    postSynaptic['PVT'][nextState] += 2
    postSynaptic['VC1'][nextState] += 10
    postSynaptic['VC3'][nextState] += 6
    postSynaptic['VD1'][nextState] += 2
    postSynaptic['VD2'][nextState] += 2
    postSynaptic['VD4'][nextState] += 5
    postSynaptic['VD5'][nextState] += 5
    postSynaptic['VD6'][nextState] += 1


def VC3():
    postSynaptic['AVL'][nextState] += 1
    postSynaptic['DD1'][nextState] += 2
    postSynaptic['DD2'][nextState] += 4
    postSynaptic['DD3'][nextState] += 5
    postSynaptic['DD4'][nextState] += 13
    postSynaptic['DVC'][nextState] += 1
    postSynaptic['HSNR'][nextState] += 1
    postSynaptic['MVULVA'][nextState] += 11
    postSynaptic['PVNR'][nextState] += 1
    postSynaptic['PVPR'][nextState] += 1
    postSynaptic['PVQR'][nextState] += 4
    postSynaptic['VC1'][nextState] += 4
    postSynaptic['VC2'][nextState] += 3
    postSynaptic['VC4'][nextState] += 1
    postSynaptic['VC5'][nextState] += 2
    postSynaptic['VD1'][nextState] += 1
    postSynaptic['VD2'][nextState] += 1
    postSynaptic['VD3'][nextState] += 1
    postSynaptic['VD4'][nextState] += 2
    postSynaptic['VD5'][nextState] += 4
    postSynaptic['VD6'][nextState] += 4
    postSynaptic['VD7'][nextState] += 5


def VC4():
    postSynaptic['AVBL'][nextState] += 1
    postSynaptic['AVFR'][nextState] += 1
    postSynaptic['AVHR'][nextState] += 1
    postSynaptic['MVULVA'][nextState] += 7
    postSynaptic['VC1'][nextState] += 1
    postSynaptic['VC3'][nextState] += 5
    postSynaptic['VC5'][nextState] += 2


def VC5():
    postSynaptic['AVFL'][nextState] += 1
    postSynaptic['AVFR'][nextState] += 1
    postSynaptic['DVC'][nextState] += 2
    postSynaptic['HSNL'][nextState] += 1
    postSynaptic['MVULVA'][nextState] += 2
    postSynaptic['OLLR'][nextState] += 1
    postSynaptic['PVT'][nextState] += 1
    postSynaptic['URBL'][nextState] += 3
    postSynaptic['VC3'][nextState] += 3
    postSynaptic['VC4'][nextState] += 2


def VC6():
    postSynaptic['MVULVA'][nextState] += 1


def VD1():
    postSynaptic['DD1'][nextState] += 5
    postSynaptic['DVC'][nextState] += 5
    postSynaptic['MVL05'][nextState] += -5
    postSynaptic['MVL08'][nextState] += -5
    postSynaptic['MVR05'][nextState] += -5
    postSynaptic['MVR08'][nextState] += -5
    postSynaptic['RIFL'][nextState] += 1
    postSynaptic['RIGL'][nextState] += 2
    postSynaptic['SMDDR'][nextState] += 1
    postSynaptic['VA1'][nextState] += 2
    postSynaptic['VA2'][nextState] += 1
    postSynaptic['VC1'][nextState] += 1
    postSynaptic['VD2'][nextState] += 7


def VD2():
    postSynaptic['AS1'][nextState] += 1
    postSynaptic['DD1'][nextState] += 3
    postSynaptic['MVL07'][nextState] += -7
    postSynaptic['MVL10'][nextState] += -7
    postSynaptic['MVR07'][nextState] += -7
    postSynaptic['MVR10'][nextState] += -7
    postSynaptic['VA2'][nextState] += 9
    postSynaptic['VB2'][nextState] += 3
    postSynaptic['VD1'][nextState] += 7
    postSynaptic['VD3'][nextState] += 2


def VD3():
    postSynaptic['MVL09'][nextState] += -7
    postSynaptic['MVL12'][nextState] += -9
    postSynaptic['MVR09'][nextState] += -7
    postSynaptic['MVR12'][nextState] += -7
    postSynaptic['PVPL'][nextState] += 1
    postSynaptic['VA3'][nextState] += 2
    postSynaptic['VB2'][nextState] += 2
    postSynaptic['VD2'][nextState] += 2
    postSynaptic['VD4'][nextState] += 1


def VD4():
    postSynaptic['DD2'][nextState] += 2
    postSynaptic['MVL11'][nextState] += -9
    postSynaptic['MVL12'][nextState] += -9
    postSynaptic['MVR11'][nextState] += -9
    postSynaptic['MVR12'][nextState] += -9
    postSynaptic['PVPR'][nextState] += 1
    postSynaptic['VD3'][nextState] += 1
    postSynaptic['VD5'][nextState] += 1


def VD5():
    postSynaptic['AVAR'][nextState] += 1
    postSynaptic['MVL14'][nextState] += -17
    postSynaptic['MVR14'][nextState] += -17
    postSynaptic['PVPR'][nextState] += 1
    postSynaptic['VA5'][nextState] += 2
    postSynaptic['VB4'][nextState] += 2
    postSynaptic['VD4'][nextState] += 1
    postSynaptic['VD6'][nextState] += 2


def VD6():
    postSynaptic['AVAL'][nextState] += 1
    postSynaptic['MVL13'][nextState] += -7
    postSynaptic['MVL14'][nextState] += -7
    postSynaptic['MVL16'][nextState] += -7
    postSynaptic['MVR13'][nextState] += -7
    postSynaptic['MVR14'][nextState] += -7
    postSynaptic['MVR16'][nextState] += -7
    postSynaptic['VA6'][nextState] += 1
    postSynaptic['VB5'][nextState] += 2
    postSynaptic['VD5'][nextState] += 2
    postSynaptic['VD7'][nextState] += 1


def VD7():
    postSynaptic['MVL15'][nextState] += -7
    postSynaptic['MVL16'][nextState] += -7
    postSynaptic['MVR15'][nextState] += -7
    postSynaptic['MVR16'][nextState] += -7
    postSynaptic['MVULVA'][nextState] += -15
    postSynaptic['VA9'][nextState] += 1
    postSynaptic['VD6'][nextState] += 1


def VD8():
    postSynaptic['DD4'][nextState] += 2
    postSynaptic['MVL15'][nextState] += -18
    postSynaptic['MVR15'][nextState] += -18
    postSynaptic['VA8'][nextState] += 5


def VD9():
    postSynaptic['MVL17'][nextState] += -10
    postSynaptic['MVL18'][nextState] += -10
    postSynaptic['MVR17'][nextState] += -10
    postSynaptic['MVR18'][nextState] += -10
    postSynaptic['PDER'][nextState] += 1
    postSynaptic['VD10'][nextState] += 5


def VD10():
    postSynaptic['AVBR'][nextState] += 1
    postSynaptic['DD5'][nextState] += 2
    postSynaptic['DVC'][nextState] += 4
    postSynaptic['MVL17'][nextState] += -9
    postSynaptic['MVL20'][nextState] += -9
    postSynaptic['MVR17'][nextState] += -9
    postSynaptic['MVR20'][nextState] += -9
    postSynaptic['VB9'][nextState] += 2
    postSynaptic['VD9'][nextState] += 5


def VD11():
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['MVL19'][nextState] += -9
    postSynaptic['MVL20'][nextState] += -9
    postSynaptic['MVR19'][nextState] += -9
    postSynaptic['MVR20'][nextState] += -9
    postSynaptic['VA11'][nextState] += 1
    postSynaptic['VB10'][nextState] += 1


def VD12():
    postSynaptic['MVL19'][nextState] += -5
    postSynaptic['MVL21'][nextState] += -5
    postSynaptic['MVR19'][nextState] += -5
    postSynaptic['MVR22'][nextState] += -5
    postSynaptic['VA11'][nextState] += 3
    postSynaptic['VA12'][nextState] += 2
    postSynaptic['VB10'][nextState] += 1
    postSynaptic['VB11'][nextState] += 1


def VD13():
    postSynaptic['AVAR'][nextState] += 2
    postSynaptic['MVL21'][nextState] += -9
    postSynaptic['MVL22'][nextState] += -9
    postSynaptic['MVL23'][nextState] += -9
    postSynaptic['MVR21'][nextState] += -9
    postSynaptic['MVR22'][nextState] += -9
    postSynaptic['MVR23'][nextState] += -9
    postSynaptic['PVCL'][nextState] += 1
    postSynaptic['PVCR'][nextState] += 1
    postSynaptic['PVPL'][nextState] += 2
    postSynaptic['VA12'][nextState] += 1
