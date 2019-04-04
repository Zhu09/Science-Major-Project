import math
import pandas as pd
import numpy as np
train = pd.read_csv('traindata.csv')

# weights
l2_1_w = np.array([2, 2, 2, 2])
l2_2_w = np.array([2, 2, 2, 2])
l2_3_w = np.array([2, 2, 2, 2])
l2_4_w = np.array([2, 2, 2, 2])
l3_red_w = np.array([2, 2, 2, 2])
l3_green_w = np.array([2, 2, 2, 2])

def act(z): 
    return 1./(1.+ math.exp(-z))

def net(a, w, b):
    return b+a.dot(w)

def get_row(index): # 0-10
        row = train.iloc[index]
        return row

def forward(w_0, w_1, w_2, w_3, w_4, w_5):
    e_full = 0
    for i in range (1, 11):
        c_row = get_row(i-1)
        r_i = c_row[0] # colour: red
        g_i = c_row[1] # colour: green
        c_n = c_row[2] # task demand: colour
        w_r = c_row[3] # task demand: word
        R_i = c_row[4] # word: red
        G_i = c_row[5] # word: green
        t = c_row[6] #target

        # layer 2
        l2_1_in = np.array([r_i, g_i, c_n, w_r])
        l2_1_b = -4.0
        l2_1_out = act(net(l2_1_in, l2_1_w, l2_1_b))

        l2_2_in = np.array([r_i, g_i, c_n, w_r])
        l2_2_b = -4.0
        l2_2_out = act(net(l2_2_in, l2_2_w, l2_2_b))

        l2_3_in = np.array([c_n, w_r, R_i, G_i])
        l2_3_b = -4.0
        l2_3_out = act(net(l2_3_in, l2_3_w, l2_3_b))

        l2_4_in = np.array([c_n, w_r, R_i, G_i])
        l2_4_b = -4.0
        l2_4_out = act(net(l2_4_in, l2_4_w, l2_4_b))

        # layer 3
        l3_red_in = np.array([l2_1_out, l2_2_out, l2_3_out, l2_4_out])
        l3_red_b = 0
        l3_red_out = act(net(l3_red_in, l3_red_w, l3_red_b))

        l3_green_in = np.array([l2_1_out, l2_2_out, l2_3_out, l2_4_out])
        l3_green_b = 0
        l3_green_out = act(net(l3_green_in, l3_green_w, l3_green_b))

        if l3_green_out > l3_red_out:
            print("green, {}% certainty".format(str(round(l3_green_out*100.,2))))
            print(t*100, "red")
        else:
            print("red {}% certainty".format(str(round(l3_red_out*100.,2))))
            print(t*100, "% real red")
        i = i+1

        y= l3_green_out
        e = 1/2*(t-y)**2 # quadatic error
        e_full = e_full + e
        print(e)
        print("------")
    print(e_full/10)

forward(l2_1_w, l2_2_w, l2_3_w, l2_4_w, l3_red_w, l3_green_w)