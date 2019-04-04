# import math
# import numpy as np

# def act(z): 
#     return 1./(1.+ math.exp(-z))

# def net(a, w, b):
#     return b+a.dot(w)

# #L1 
# r_i = 0. # colour: red
# g_i = 1. # colour: green
# c_n = 1. # task demand: colour
# w_r = 0. # task demand: word
# R_i = 1. # word: red
# G_i = 0. # word: green

# #L2 LHS
# l2_1_w = np.array([2.2, -2.2, 4.0])
# l2_1_in = np.array([r_i, g_i, c_n])
# l2_1_b = -4.0
# l2_1_out = act(net(l2_1_in, l2_1_w, l2_1_b))
# print(l2_1_out)

# l2_2_w = np.array([-2.2, 2.2, 4.0])
# l2_2_in = np.array([r_i, g_i, c_n])
# l2_2_b = -4.0
# l2_2_out = act(net(l2_2_in, l2_2_w, l2_2_b))
# print(l2_2_out)

# #L2 RHS
# l2_3_w = np.array([4.0, 2.6, -2.6])
# l2_3_in = np.array([w_r, R_i, G_i])
# l2_3_b = -4.0
# l2_3_out = act(net(l2_3_in, l2_3_w, l2_3_b))
# print(l2_3_out)

# l2_4_w = np.array([4.0, -2.6, 2.6])
# l2_4_in = np.array([w_r, R_i, G_i])
# l2_4_b = -4.0
# l2_4_out = act(net(l2_4_in, l2_4_w, l2_4_b))
# print(l2_3_out)

# # RESP 3
# l3_red_w = np.array([1.3, -1.3, 2.5, -2.5])
# l3_red_in = np.array([l2_1_out, l2_2_out, l2_3_out, l2_4_out])
# l3_red_b = 0
# l3_red_out = act(net(l3_red_in, l3_red_w, l3_red_b))
# print(l3_red_out)

# l3_green_w = np.array([-1.3, 1.3, -2.5, 2.5])
# l3_green_in = np.array([l2_1_out, l2_2_out, l2_3_out, l2_4_out])
# l3_green_b = 0
# l3_green_out = act(net(l3_green_in, l3_green_w, l3_green_b))
# print(l3_green_out)

# if l3_green_out > l3_red_out:
#     print("green, {}% certainty".format(str(round(l3_green_out*100.,2))))
# else:
#     print("red, {}% certainty".format(str(round(l3_red_out*100.,2))))
