from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys
#from ch11soundutilities import play_sound

def update(frame_data):
    data, colors, swaps, comparisons = frame_data
    plt.cla() 

    bar_positions = np.arange(len(data))
    axes = sns.barplot(bar_positions, data, palette=colors) # new bars
    axes.set(xlabel=f'Comparisons: {comparisons}; Swaps: {swaps}',xticklabels=data)

def flash_bars(index1, index2, data, colors, swaps, comparisons):
    """Flash the bars about to be swapped and play their notes."""
    for x in range(0, 2):
        colors[index1], colors[index2] = 'white', 'white'
        yield (data, colors, swaps, comparisons)
        colors[index1], colors[index2] = 'purple', 'purple'
        yield (data, colors, swaps, comparisons)
        #play_sound(data[index1], seconds=0.05)
        #play_sound(data[index2], seconds=0.05)
        
def selection_sort(data):
    """Sort data using the selection sort algorithm and
    yields values that update uses to visualize the algorithm.""" 
    swaps = 0
    comparisons = 0
    colors = ['lightgray'] * len(data) # list of bar colors
    
    # display initial bars representing shuffled values
    yield (data, colors, swaps, comparisons)
    # loop over len(data) - 1 elements
    for index1 in range(0, len(data) - 1):
        smallest = index1
        # loop to find index of smallest element's index
        for index2 in range(index1 + 1, len(data)):
            comparisons += 1
            colors[smallest] = 'purple'
            colors[index2] = 'red'
            yield (data, colors, swaps, comparisons)
            #play_sound(data[index2], seconds=0.05)

            # compare elements at positions index and smallest
            if data[index2] < data[smallest]:
                colors[smallest] = 'lightgray'
                smallest = index2
                colors[smallest] = 'purple'
                yield (data, colors, swaps, comparisons)
            else:
                colors[index2] = 'lightgray'
                yield (data, colors, swaps, comparisons)

        # ensure that last bar is not purple
        colors[-1] = 'lightgray'

        # flash the bars about to be swapped
        yield from flash_bars(index1, smallest, data, colors,
           swaps, comparisons)

        swaps += 1
        data[smallest], data[index1] = data[index1], data[smallest]
    
        # flash the bars that were just swapped
        yield from flash_bars(index1, smallest, data, colors,
                          swaps, comparisons)
    
        # indicate that bar index1 is now in its final spot
        colors[index1] = 'lightgreen'
        yield (data, colors, swaps, comparisons)

    # indicate that last bar is now in its final spot
    colors[-1] = 'lightgreen'
    yield (data, colors, swaps, comparisons)
    #play_sound(data[-1], seconds=0.05)

    # play each bar's note once and color it darker green
    for index in range(len(data)):
        colors[index] = 'green'
        yield (data, colors, swaps, comparisons)
        #play_sound(data[index], seconds=0.05)
        
def main():
    number_of_values = int(sys.argv[1]) if len(sys.argv) == 2 else 10

    figure = plt.figure('Selection Sort') 
    numbers = np.arange(1, number_of_values + 1) 
    np.random.shuffle(numbers)
    print(numbers)
    anim = animation.FuncAnimation(figure, update, repeat=False, frames=selection_sort(numbers), interval=50)
    plt.show() 
    
if __name__ == '__main__':
    main()

