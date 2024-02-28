import tellurium as te

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
import pandas as pd


def plot_several_models(filepath, rows, cols):
    fig, axs = plt.subplots(rows, cols)
    models = []
    cwd = os.getcwd()
    cwd = os.path.join(cwd, "src")
    for file in os.listdir(filepath):
        fullpath = os.path.join(filepath, file)
        fullpath = os.path.join(cwd, fullpath)
        f = open(fullpath, "r")
        models.append(f.read())
        f.close()
    idx = 0
    for i in range(rows):
        for j in range(cols):
            r = te.loada(models[idx])
            m = r.simulate(0,1,50)
            axs[i,j].plot(m)
            idx += 1
    plt.show()


# path ="/home/hellsbells/Desktop/networkEv/src/final_models"
# plot_several_models(path, 5, 2)

def make_truth_csv(model, filename, simulation=[0, 1, 10]):
    if not filename.endswith(".csv"):
        filename += ".csv"
    cwd = os.getcwd()
    path = os.path.join(cwd, f"test_files/{filename}")
    r = te.loada(model)
    result = r.simulate(simulation[0], simulation[1], simulation[2])
    df = pd.DataFrame(result, columns=['time']+r.getFloatingSpeciesIds())
    df.set_index('time', inplace=True)
    df.to_csv(path)

def plot_single_model(model, simulation=[0, 1, 10]):
    r = te.loada(model)
    r.simulate(simulation[0], simulation[1], simulation[2])
    r.plot()

def compare_model_plots(truthmodel, evolvedmodel, simulation=[0, 1, 10]):
    r1 = te.loada(truthmodel)
    result1 = r1.simulate(simulation[0], simulation[1], simulation[2])

    r2 = te.loada(evolvedmodel)
    result2 = r2.simulate(simulation[0], simulation[1], simulation[2])

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1, title="Truth Model")
    ax2 = fig.add_subplot(1, 2, 2, title="Evolved Model")#, sharey=ax1)
    ax2.set_ylim(0,20)
    ax1.plot(result1[:, 0], result1[:, 1:])
    ax2.plot(result2[:, 0], result2[:, 1:])
    ax1.legend(r1.getFloatingSpeciesIds())
    ax2.legend(r2.getFloatingSpeciesIds())
    plt.show()


model = """S2 -> S1; k0*S2
S2 + S0 -> S0; k1*S2*S0
S0 -> S2; k2*S0
S2 -> S2+S2; k3*S2
S1 -> S0+S2; k4*S1
k0 = 3.708920735583032
k1 = 4.027285355118902
k2 = 7.450108022248875
k3 = 145.89432306715088
k4 = 16.371587764670334
S0 = 1.0
S1 = 5.0
S2 = 9.0

"""

evolvedmodel = """
S0 + S0 -> S1 + S1; k1*S0*S0
S0 + S0 -> S0 + S0; k2*S0*S0
S1 + S2 -> S0 + S2; k3*S1*S2
S2 -> S1 + S2; k4*S2
S2 -> S2 + S2; k5*S2
S1 -> S0 + S1; k7*S1
S1 -> S2; k8*S1
S1 + S2 -> S0; k9*S1*S2
S2 -> S1; k10*S2
k1 = 31.172546720935046
k2 = 78.89088208128048
k3 = 82.03285626562331
k4 = 2.648349825474124
k5 = 99.93579480894451
k7 = 18.619724882494946
k8 = 38.295673707771776
k9 = 23.420218268236173
k10 = 3.942945480210541
S0 = 1.0
S1 = 5.0
S2 = 9.0
"""

# compare_model_plots(model, evolvedmodel, simulation=[0, 10, 1000])

r = te.loada(evolvedmodel)
r.simulate(0,1000,5000)
# r.plot()

print(r.getFullEigenValues())