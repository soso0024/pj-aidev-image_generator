import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Data from the first image
models = ["Claude 3.7 Sonnet", "Gemini 2.5 Pro Preview", "GPT-4.1"]
percentages = [8.6, 26.2, -12.8]  # Percentage changes vs base method

# Convert to relative costs for the bar chart (similar to second image)
# Assuming baseline is 100%
relative_costs = [100 + p for p in percentages]

# Colors
colors = ["#E74C3C", "#E74C3C", "#3498DB"]  # Red, Red, Blue

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the bars
bars = ax.bar(
    models,
    relative_costs,
    color=colors,
    width=0.6,
    alpha=0.8,
    edgecolor="black",
    linewidth=1.2,
)

# Add baseline at 100%
ax.axhline(y=100, color="navy", linestyle="--", label="Baseline (100%)")

# Add percentage labels on top of bars
for bar, percentage in zip(bars, relative_costs):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 3,
        f"{percentage:.1f}%",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold",
    )

# Customize the plot
ax.set_ylim(0, max(relative_costs) * 1.2)  # Add some space above the bars
ax.set_ylabel("Relative API Cost", fontsize=16, fontweight="bold")
ax.set_xlabel("Model", fontsize=16, fontweight="bold")
ax.set_title("API Cost Change (vs. Base Method)", fontsize=18, fontweight="bold")
ax.tick_params(axis="y", labelsize=14)
ax.set_xticklabels(models, fontsize=12, fontweight="bold")

# Add grid
ax.grid(axis="y", alpha=0.3, linestyle="--", linewidth=0.5)
ax.set_axisbelow(True)

# Remove top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.0)
ax.spines["bottom"].set_linewidth(1.0)

# Save the figure
plt.tight_layout()
plt.savefig(
    "imgs/api_cost_comparison_docstring_removal.png", dpi=300, bbox_inches="tight"
)
plt.show()
