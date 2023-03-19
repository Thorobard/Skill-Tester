import matplotlib.pyplot as plt
import numpy as np


def graph_main():
    data = open('data.txt', 'r') 

    reaction_time_data = [x for x in data if 'Count' in x ]
    reaction_time_list = [x.split() for x in reaction_time_data]

    y_input = [int(x[-1]) for x in reaction_time_list]
    x_input = [x for x in range(len(y_input))]
    
    sorted_reaction_time = sorted(y_input)
    
    median_reaction_time = sorted_reaction_time[int(len(sorted_reaction_time) / 2)]
    
    x = 0
    for i in sorted_reaction_time:
        x += i
    average_reaction_time = x / len(sorted_reaction_time)
    
    print(f"Average Reaction Time: {average_reaction_time}")
    print(f"Median Reaction Time: {median_reaction_time}")

    xpoints = np.array(x_input)
    ypoints = np.array(y_input)

    line_x = np.array([0, len(y_input)])
    median_y = np.array([median_reaction_time, median_reaction_time])
    average_y = np.array([average_reaction_time, average_reaction_time])
    plt.plot(line_x, average_y, color = 'b')
    plt.plot(line_x, median_y, color = 'g')
    plt.plot(xpoints, ypoints, color = 'r')

    plt.show()

if __name__ == '__main__':
    graph_main()



