import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import numpy as np

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

def plot_results(results):
    # Create a color map for different algorithms
    color_map = mcolors.ListedColormap(['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown'])

    for i, (scenario, group) in enumerate(group_by_scenario(results)):
        lengths = [result["Length"] for result in group]

        # Separate values for each algorithm
        algorithm_values = {algorithm: np.array([result[algorithm] for result in group]) for algorithm in ["Quick Sort", "Heap Sort", "Merge Sort", "Radix Sort", "Bucket Sort", "Tim Sort"]}

        # Plot for each algorithm with a different color
        for j, (algorithm, values) in enumerate(algorithm_values.items()):
            plt.plot(lengths, values, label=f"{algorithm}", marker='o', markersize=5, color=color_map(j))

        # Add labels and title
        plt.xlabel('Length')
        plt.ylabel('Time (s)')

        plt.title(f'Size of Input vs Time Taken for Sorting Algorithms - {scenario}')

        # Add a legend
        plt.legend()

        # Save the plot to a file
        plt.savefig(f'output/sorting_algorithms_line_{scenario}.png')

        # Show the plot
        plt.show()

def group_by_scenario(results):
    results.sort(key=lambda x: (x["Scenario"], x["Length"]))

    current_scenario = None
    current_group = []

    for result in results:
        if result["Scenario"] != current_scenario:
            if current_group:
                yield current_scenario, current_group
            current_scenario = result["Scenario"]
            current_group = []
        current_group.append(result)

    if current_group:
        yield current_scenario, current_group