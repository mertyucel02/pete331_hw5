def density_overburden(density, x, depth):
        tot = 0
        for i in range(len(density)):
            tot += x[i] * density[i]
        density_ob = tot / depth
        return density_ob

def poisson_ratio(eps_l, eps_s):
    the_ratio = eps_s/eps_l
    return the_ratio

student_id = [2, 5, 1, 5, 4, 0, 1]

res_depth = 6500 + student_id[4] + 100 #ft

eps_long = .005
eps_teansverse = .00125
Poissons_Ratio = poisson_ratio(eps_long, eps_teansverse)

Biots_Constant = .7

tensile_strength = 1000 #psi

p_pore_gradient = .43 #psi/ft

density_layer_a = 140 + student_id[2] #lbm/cuft
density_layer_b = 150 + student_id[3] #lbm/cuft
density_layer_c = 160 + student_id[4] #lbm/cuft

x_layer_a = .3 * res_depth #ft
x_layer_b = .35 * res_depth #ft
x_layer_c = .35 * res_depth #ft

values_density = [density_layer_a, density_layer_b,
                  density_layer_c] #lbm/cuft
values_x = [x_layer_a, x_layer_b, x_layer_c] #ft

overburden_density = density_overburden(values_density,
                                        values_x, res_depth) #lbm/cuft

tectonic_stress = 1800 + student_id[6] * 20 #psi

viscosity = 14 #cP

SG = 1.17

tubing_id = 2.441 #in

injection_rate = 6.4 #bpm

overburden_stress = (overburden_density * res_depth) / 144 #psi

p_pore = p_pore_gradient * res_depth #psi

eff_vertical_stress = overburden_stress - Biots_Constant \
                      * p_pore #psi

eff_horizontal_stress = (Poissons_Ratio / (1 - Poissons_Ratio)) \
                        * eff_vertical_stress #psi

tot_horizontal_stress = eff_horizontal_stress \
                        + Biots_Constant * p_pore #psi

min_horizontal_stress = tot_horizontal_stress #psi

max_horizontal_stress = min_horizontal_stress + tectonic_stress #psi

p_bd = 3 * min_horizontal_stress - max_horizontal_stress \
       + tensile_strength - p_pore #psi

delta_p_h = .433 * SG * res_depth #psi

def SG_to_density_SI(specific_gravity):
    density_water = 1.000 #g/cm^3
    density = (specific_gravity * density_water) #g/cm^3
    return density

density_o = SG_to_density_SI(SG) #g/cm^3

delta_p_f = (518 * (SG_to_density_SI(SG) ** .79) * (injection_rate ** 1.79) *
             (viscosity ** .207) * res_depth) \
            / (1000 * (tubing_id ** 4.79))  #psi

p_si = p_bd - delta_p_h + delta_p_f #psi

HHP = (injection_rate * p_si) / 40.8 #HP


