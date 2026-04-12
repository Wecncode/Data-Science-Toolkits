import matplotlib.pyplot as plt

def plot_misleading_and_honest_charts():
    """
    Plots the same exact revenue data in two different ways to 
    demonstrate how axes manipulation changes the narrative.
    """
    # Simulated Company Revenue over 6 months (Very stable, slight dip)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    revenue = [105000, 106000, 105500, 104000, 103500, 103000]

    # Create a figure with two side-by-side subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("The Power of Axes: Same Data, Different Story", fontsize=16, fontweight='bold')

    # --- PLOT 1: The "Disaster" Chart (Misleading) ---
    # By zooming in on the y-axis, a 2% drop looks like the company is failing
    ax1.plot(months, revenue, marker='o', color='red', linewidth=3)
    ax1.set_title("Marketing's View: 'REVENUE PLUMMETS!'", color='red')
    ax1.set_ylabel("Revenue ($)")
    ax1.grid(True, linestyle='--', alpha=0.5)
    
    # THE TRICK: Setting the Y-axis limits extremely close to the min/max data points
    ax1.set_ylim(102500, 106500) 

    # --- PLOT 2: The "Stable" Chart (Honest Context) ---
    # By starting the y-axis at 0, we see the true relative scale of the change
    ax2.plot(months, revenue, marker='o', color='green', linewidth=3)
    ax2.set_title("Data Team's View: 'Revenue Remains Stable'", color='green')
    ax2.set_ylabel("Revenue ($)")
    ax2.grid(True, linestyle='--', alpha=0.5)
    
    # THE CORRECTION: Setting the Y-axis to start at 0
    ax2.set_ylim(0, 120000) 

    # Add data labels to the honest chart to show the actual numbers
    for i, v in enumerate(revenue):
        ax2.text(i, v + 2000, f"${v:,}", ha='center', fontsize=9)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_misleading_and_honest_charts()
