student_id = [2, 5, 1, 5, 4, 0, 1]

formaion_depth = 11500 + student_id[4] * 100 #ft

density_layer_a = 140 + student_id[2] #lbm/cuft
density_layer_b = 150 + student_id[3] #lbm/cuft
density_layer_c = 160 + student_id[4] #lbm/cuft
density_layer_d = 170 + student_id[5] #lbm/cuft

x_layer_a = .3 * formaion_depth #ft
x_layer_b = .2 * formaion_depth #ft
x_layer_c = .2 * formaion_depth #ft
x_layer_d = .3 * formaion_depth #ft

values_density = [density_layer_a, density_layer_b, density_layer_c, density_layer_d] #lbm/cuft
values_x = [x_layer_a, x_layer_b, x_layer_c, x_layer_d] #ft

def density_overburden(density, x, depth):
        tot = 0
        for i in range(len(density)):
            tot += x[i] * density[i]
        density_ob = tot / depth
        return density_ob

overburden_density = density_overburden(values_density,
                                        values_x,
                                        formaion_depth) #lbm/cuft

p_res = 6500 + student_id[6] * 100 #psi

def poisson_ratio(eps_l, eps_s):
    the_ratio = eps_s/eps_l
    return the_ratio

epsilon_long = .006
epsilon_transverse = .0015

Poissons_Ratio = poisson_ratio(epsilon_long, epsilon_transverse)

Biots_Constant = .72

p_drawdown = 1500 + student_id[6] * 100 #psi

overburden_stress = (density_overburden(values_density,
                                        values_x, formaion_depth)
                     * formaion_depth) / 144 #psi

eff_vertical_stress_at_initial = overburden_stress - \
                                 Biots_Constant * p_res #psi

eff_horizontal_stress_at_initial = (Poissons_Ratio /
                                    (1 - Poissons_Ratio)) \
                                   * eff_vertical_stress_at_initial #psi



p_pore_under_drawdown = p_res - p_drawdown #psi

eff_vertical_stress = overburden_stress - Biots_Constant \
                      * p_pore_under_drawdown #psi

eff_horizontal_stress = (Poissons_Ratio / (1 - Poissons_Ratio)) \
                        * eff_vertical_stress #psi


