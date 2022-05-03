a = [3, 1, 6, 3, 2, 11, 5, 1, 10]
b = len(a)
c= []
for i in range(len(a)):
    if a[i] >= (a[i-1]*2) or a[i] >= (a[i-2]*2) or a[i] >= (a[i+1]*2) or a[i] >= (a[i+1]*2):
        c.append(a[i])
        print(i)

print(c)

#
# There are 4 prisoners in a prison. The warden has decided to set the prisoners free if they can solve his puzzle.
#
# There is an interrogation room that contains 5 lights (all turned on) numbered 1 to 5. Once a day the warden will allow a prisoner chosen at random to enter the room and that prisoner must change one light switch. The prisoner to be chosen is entirely random, but after some time every prisoner will be chosen at least once.
#
# The prisoners are allowed to meet once before the process starts, and will then have no contact with each other.
#
# Once every prisoner has visited the room at least once, they must tell the warden that everyone has visited the room and they will all be set free. If in fact another prisoner has not entered the room, the prisoners will be locked up forever.
# What strategy should the prisoners follow in order to get out of jail as early as possible?
#
#
# AA00AV91D7
#
# Universal404!