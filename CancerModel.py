# From the insights from the analysis on haberman's dataset, we could get a insight that node and age played a vital in patients surivial.
#Hence from the insights we have got we have created a model using Nodes and Ages

def CancerModel(age,nodes):
    if nodes in range(0,3):
        print('Survival rate is 85% approx.')

    elif nodes in range(3,6):
        if age in range(45,71):
            print('Survival rate is 47%.')

        else:# From the insights from the analysis on haberman's dataset, we could get a insight that node and age played a vital in patients surivial.
#Hence from the insights we have got we have created a model using Nodes and Ages

def CancerModel(age,nodes):
    if nodes in range(0,3):
        print('Survival rate is 85% approx.')

    elif nodes in range(3,6):
        if age in range(45,71):
            print('Survival rate is 47%.')

        else:
            print('Survival rate is 70% approx.')

    elif nodes in range(6,10):
        if age in range(44,59):
            print('Survival rate is 39%.')

        else:
            print('Survival rate 80% approx.')

    elif nodes >=10:
        if age in range(44,59):
            print('Survival rate is 33%.')

        else:
            print('Survival rate is 50% approx.')

    else:
        print('Input parameter doesnt come in range')


while True:
    Age = int(input("Whats the ages of the patient?"))
    Nodes = int(input("How many nodes does the patient have?"))
    CancerModel(Age,Nodes)

            print('Survival rate is 70% approx.')

    elif nodes in range(6,10):
        if age in range(44,59):
            print('Survival rate is 39%.')

        else:
            print('Survival rate 80% approx.')

    elif nodes >=10:
        if age in range(44,59):
            print('Survival rate is 33%.')

        else:
            print('Survival rate is 50% approx.')

    else:
        print('Input parameter doesnt come in range')


while True:
    Age = int(input("Whats the ages of the patient?"))
    Nodes = int(input("How many nodes does the patient have?"))
    CancerModel(Age,Nodes)
