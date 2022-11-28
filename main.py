# Visualizing the position of slow dippers as found by 
# Boyajin 2016 and Schmidt 2021
# Marminge 

###########################################################
## IMPORTS

#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import os
import time
from Star import Star
from matplotlib.ticker import AutoLocator

###########################################################
## GLOBAL CONSTANTS

# meta usage
bar = "*****************************************************"

# lambda functions
clear = lambda: os.system('cls')

###########################################################
## STAR DATA

##############################
# clump data
clump_names = ["2913753", "3037513", "3093586", \
    "5334181", "5436225", "5482005", "7971210", \
    "8046240"]

x_clump = [210, 579, 313, 574, 262, 623, 580, 394]
y_clump = [56, 125, 101, -31, 16, -1, -182, -49]
z_clump = [39, -10, -55, 98, -3, -33, 130, 36]

##############################
# non-clump data

nclump_names = ["2958269", "8128754", "8233191"\
    "8491743", "8935719", "8942941", "8987978"]

x_nclump = [2180, 1507, 7658, 1025, 1154, 687, 829]
y_nclump = [836, -418, -876, 21, 507, 344, 757]
z_nclump = [332, -56, -1142, -508, -1444, -863, -1530]

##############################
# Boyajin's star data

x_boy = 415
y_boy = 77
z_boy = -137

##############################
# new candidates data

new_names = ["1933490", "2354429", "2506699",\
    "2560138", "3781455", "4111136", "4754014",\
    "4989822", "5190574", "6757658", "6804071",\
    "6814519", "7255468", "7575062", "7642696"]

x_new = [183, 228, 105, 461, 394, 314, 46, 144, 699, -226,\
    -398, -119, -265, 68, 72]
y_new = [650, 758, 321, 668, 711, 1527, 341, 143, 46, 749,\
    1902, 669, 651, 99, 25]
z_new = [-151, 299, 237, 650, -563, -314, 196, 278, 352,\
    -171, -225, -45, 349, 278, 137]

###########################################################
## FUNCTIONS

def print_clump(ax):
    ax.scatter(x_clump, y_clump, z_clump, color='black',\
        depthshade=False, marker='o', label="clustered slow dippers from paper 1")
    
def print_non_clump(ax):
    ax.scatter(x_nclump, y_nclump, z_nclump, color='black',\
        depthshade=False, marker='o', facecolor='none', label="non-clustered slow dippers from paper 1")
    
def print_boy(ax):
    ax.scatter(x_boy, y_boy, z_boy, color='red',\
        marker='o', label="Boyajin's star")

def print_sun(ax):
    ax.scatter(0, 0, 0, color='black', marker="${\odot}$",\
        sizes=[100], label="the sun")
    
def print_new(ax):
    ax.scatter(x_new, y_new, z_new, color='blue',\
        depthshade=False, marker='o', facecolor='none', label="new slow dippers from paper 2")  
    
def print_standard(ax):
    print_clump(ax)
    print_boy(ax)
    print_sun(ax)
    ax.scatter(72, 25, 137, color='blue',\
        marker='o', facecolor='none', label="clustered slow dipper from paper 2")
    
    ax.set_xticks(range(0,700,100))
    ax.set_yticks(range(-200,300,100))
    ax.set_zticks(range(-200,300,100))
    
    return "clustered slow dippers and sun"

def print_cluster(ax):
    print_clump(ax)
    print_boy(ax)
    ax.scatter(72, 25, 137, color='blue',\
        marker='o', facecolor='none', label="clustered slow dipper from paper 2")
    
    ax.set_xticks(range(100,700,100))
    ax.set_yticks(range(-200,300,100))
    ax.set_zticks(range(-200,300,100))
    
    return "clustered slow dippers"

def print_all(ax):
    print_clump(ax)
    print_non_clump(ax)
    print_boy(ax)
    print_sun(ax)
    print_new(ax)
    return "all slow dippers as of Schmidt 2021"
    
def print_box(ax):
    ax.plot([-50,700,700,-50,-50,-50,700,700,-50,-50],\
        [-200,-200,200,200,-200,-200,-200,200,200,-200],\
        [-200,-200,-200,-200,-200,200,200,200,200,200],\
        color="gray", label="standard view")
    ax.plot([-50,-50],[200,200],[-200,200],color="gray")
    ax.plot([700,700],[200,200],[-200,200],color="gray")
    ax.plot([700,700],[-200,-200],[-200,200],color="gray")
    
def print_all_plus(ax):
    print_all(ax)
    print_box(ax)

def select_menu(ax):
    choices = {"clu": print_clump, "non": print_non_clump,\
        "boy": print_boy, "sun": print_sun, "new": print_new,\
        "box": print_box}
    
    while True:
        title = "slow dippers of labels "
        latch = False
        clear()
        print("input determines what is printed")
        print("input: opt1opt2opt3\nor")
        print("input: opt1 opt2 opt3")
        print(bar)
        print("print clustered group: clu")
        print("print non-clustered group: non")
        print("print Boyajin\'s star: boy")
        print("print sun: sun")
        print("print new candidates: new")
        print("print box of standard view: box")
        print(bar)
        
        choice = input("input: ")
        
        for key in choices.keys():
            if key in choice:
                choices[key](ax)
                title += f"{key}, "
                latch = True
        
        if latch:
            return title[:-2]
        
        print("no choice selected")
        time.sleep(1)
        
def cluster_stars(addition):
    clump_stars = {}
    
    for name, x, y, z in zip(clump_names, x_clump,\
        y_clump, z_clump):
        clump_stars[name] = Star(name, x, y, z, "clu")
        
    clump_stars["Boyajin"] = Star("Boyajin", x_boy, y_boy,\
        z_boy, "boy")
    
    if addition == "w":
        clump_stars["7642696"] = Star("7642696", 72, 25, 137,\
            "new")
    
    dist = 0
    
    for star in clump_stars.values():
        temp_dist = 0
        for o_star in clump_stars.values():
            temp_dist += star.dist(o_star)
        temp_dist = temp_dist/(len(clump_stars.values())-1)
        dist += temp_dist
        
    return int(dist/len(clump_stars))
        
def info():
    clear()
    print("information about the cluster")
    print(bar)
    print(f"Average distance between stars in cluster (with paper 2 addition): {round(cluster_stars('w'),0)}pc")
    print(f"Average distance between stars in cluster (without paper 2 addition): {round(cluster_stars('wo'),0)}pc")
    print("press [Enter] to continue")
    input()
        
def menu():
    
    while True:
        fig = plt.figure()
        ax = plt.axes(projection='3d')

        clear()
        print("Visual presentation of the Schmidt 2021 data")
        print(bar)
        print("type standard to print the standard selection")
        print("type cluster to print the clustered stars")
        print("type select to select what to print")
        print("type all to print all stars")
        print("type all+ to print all stars and visualize standard view")
        print("type info to view some info about the cluster")
        print("type exit to exit")
        print(bar)
        choice = input("input: ")
        
        if choice == "exit":
            break
        elif choice == "info":
            info()
            continue
        elif choice == "standard":
            title = print_standard(ax)
        elif choice == "cluster":
            title = print_cluster(ax)
        elif choice == "all":
            title = print_all(ax)
        elif choice == "all+":
            title = print_all_plus(ax)
        elif choice == "select":
            title = select_menu(ax)
        else:
            print("unclear command")
            time.sleep(1)
            continue

        ax.set_xlabel('x-axis (pc)')
        ax.set_ylabel('y-axis (pc)')
        ax.set_zlabel('z-axis (pc)')
        ax.set_title(title)
        ax.legend()
        
        plt.show()
        
def main():
    menu()
    
    print("exiting...")
    time.sleep(1)

if __name__ == "__main__":
    main()