from mpi4py import MPI
comm = MPI.COMM_WORLD
name = MPI.Get_processor_name()
print("hello world")
print(("host:", name, " my rank is ", comm.rank))

