"""Lecture Demonstration: Proving that summary statistics lie by plotting Anscombe's Quartet."""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_anscombe():
    # Load the famous Anscombe's Quartet dataset built into Seaborn
    df = sns.load_dataset("anscombe")
    
    # Show the statistical summary (they will look nearly identical)
    print("Summary Statistics Grouped by Dataset:")
    print(df.groupby("dataset").agg(["mean", "var"]).round(2))
    
    # Create a 2x2 grid of subplots using Object-Oriented Matplotlib
    fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=True)
    fig.suptitle("Anscombe's Quartet: Why We Visualize", fontsize=16)

    datasets = ['I', 'II', 'III', 'IV']
    
    # Plot each dataset on its respective axes
    for ax, ds in zip(axes.flatten(), datasets):
        subset = df[df['dataset'] == ds]
        ax.scatter(subset['x'], subset['y'], color='darkred', s=50)
        ax.set_title(f"Dataset {ds}")
        
        # Add a simple trendline (Linear Regression)
        sns.regplot(x='x', y='y', data=subset, ax=ax, scatter=False, color='blue')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_anscombe()
