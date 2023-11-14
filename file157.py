from file87 import *


my_pi = Picontainer()
my_pi_2 = Picontainer()
try:
    pi_gen = foo(5)
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
    my_pi.mth(pi_gen.__next__())
except Exception as e:
    print('Error', e)
pIgEn3 = foo(194)
for the_variable_that_contains_next_approximations_of_pi_from_generator in range(23):
    my_pi_2.mth(next(pIgEn3))
my_pi_3 = Picontainer()
pi_gen = foo(6)
my_pi_3.mth([i for i in list(pi_gen)])
print('my first pi')
my_enumerate(my_pi)
print('my second pi')
my_enumerate(my_pi_2)

with open('some-file.txt', 'w') as new_file:
    new_file.write(f'my best pi: {my_pi_3.a[-2]}')
