import matplotlib.pyplot as plt

def getLineGraph(length_lists, duration_lists, sorting_algorithm):
    # Plot the line graph
    for i, (length_list, duration_list) in enumerate(zip(length_lists, duration_lists)):
        label = f"scenario - {i+1}"
        plt.plot(length_list, duration_list, label=label)

    # Add labels and title
    plt.xlabel('Length')
    plt.ylabel('Time')

    plt.title('Size of input Vs Time Taken for ' + sorting_algorithm)
    
    # Add a legend
    plt.legend()

    path = 'output/'+sorting_algorithm+'.png'
    plt.savefig(path)
    
    # Show the plot
    plt.show()