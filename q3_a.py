import cv2
import math

student_id = [2, 5, 1, 5, 4, 0, 1]

s = 4 + .75 * student_id[6]

k = 3 + .3 * student_id[4] #md

d_well = .4 + .05 * student_id[5] #ft

r_w = d_well / 2 #ft

drainage_area = 61 + 2 * student_id[5] #acres

k_f = 240000 + student_id[6] * 5000 #md

w = .15 #in

x_f = 850 #ft

def in_to_ft(L_in):
    L_ft = .0833333 * L_in #ft
    return L_ft

w_ft = in_to_ft(w) #ft

F_CD = (k_f * w_ft) / (k * x_f)



the_graph = cv2.imread("Relation between fracture conductivity and equivalent skin factor.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Relation between fracture conductivity and equivalent skin factor", the_graph)

assumption = 1.62

s_f = assumption - math.log(x_f/r_w)



def acre_to_sqft(acre):
    sqft = 43560 * acre
    return sqft

A_sqft = acre_to_sqft(drainage_area) #ft^2

r_e = math.sqrt(A_sqft / math.pi)

J_over_J_o = (math.log(r_e / r_w) + s) / (math.log(r_e / r_w) + s_f)



cv2.waitKey(0)
cv2.destroyAllWindows()
