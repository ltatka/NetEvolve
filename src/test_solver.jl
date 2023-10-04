using Plots
using CSV
using DataFrames
include("ode_solver.jl")
include("evo_utils.jl")
include("settings.jl")



# #### TEST
settings = UserSettings(["S1", "S2", "S3"], [1.0, 2.0, 2.0], "/home/hellsbells/Desktop/testtimeseries.csv", ["S2"])

objfunct = get_objectivefunction(settings)

# rn = NetworkGenerator(["S1", "S2", "S3"], [1.0, 2.0, 2.0], 5, ReactionProbabilities(.25, 0.25, 0.25, 0.25), [0.1, 2.0])
# network = get_random_network(rn)



# df = DataFrame(CSV.File(settings.objectivedatapath))

# time = df[!, "time"]
# objective = df[!, ["S2", "S1"]]
# print(typeof(objective))



# tspan = (0.0, 1)

# u0 = network.initialcondition
# ode_prob = ODEProblem(ode_funct!, u0, tspan, network)
# sol = solve(ode_prob, CVODE_BDF(), saveat=1.0/9)
# # plot(sol)
# # savefig("/home/hellsbells/Desktop/plot1.png")

# display(sol)
# display(sol.u)

# Get fitness
# fitness = 0.0
# for (j, row) in enumerate(sol.u)
#     global fitness
#     diff = abs(objective[j] - row[2])
#     fitness += diff
    
# end
# display(fitness)




println("Success")

