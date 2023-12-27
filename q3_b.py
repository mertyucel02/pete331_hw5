import math

student_id = [2, 5, 1, 5, 4, 0, 1]

s = 4 + .75 * student_id[6]

k = 3 + .3 * student_id[4]

d_well = .4 + .05 * student_id[5]

r_w = d_well / 2

drainage_area = 61 + 2 * student_id[5]

k_f = 240000 + student_id[6] * 5000

w = .15

x_f = 850

def in_to_ft(L_in):
    L_ft = .0833333 * L_in
    return L_ft

F_CD = (k_f * in_to_ft(w)) / (k * x_f)



def acre_to_sqft(acre):
    sqft = 43560 * acre
    return sqft

A_sqft = acre_to_sqft(drainage_area)

r_e = math.sqrt(A_sqft / math.pi)

u = math.log(F_CD)

correlation = (1.65 - .328 * u + .116 * u ** 2) / (1 + .18 * u
                                                   + .064 * u ** 2 +
                                                   .005 * u ** 3)


s_f = correlation - math.log(x_f / r_w)

J_over_J_o = (math.log(r_e / r_w) + s) / (math.log(r_e / r_w) + s_f)


