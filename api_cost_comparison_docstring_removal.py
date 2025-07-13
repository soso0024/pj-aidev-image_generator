import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import matplotlib.patches as patches

# Data from the first image
models = ["Claude 3.7 Sonnet", "Gemini 2.5 Pro Preview", "GPT-4.1"]
percentages = [8.6, 26.2, -12.8]  # Percentage changes vs base method

# Convert to relative costs for the bar chart (similar to second image)
# Assuming baseline is 100%
relative_costs = [100 + p for p in percentages]

# Colors
colors = ["#E74C3C", "#E74C3C", "#3498DB"]  # Red, Red, Blue

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create the bars
bars = ax.bar(
    models,
    relative_costs,
    color=colors,
    width=0.6,
    alpha=0.8,
    edgecolor="black",
    linewidth=1.5,
)

# Add baseline at 100%
ax.axhline(y=100, color="navy", linestyle="--", linewidth=2, label="Baseline (100%)")

# Add percentage labels on top of bars
for bar, percentage in zip(bars, relative_costs):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 3,
        f"{percentage:.1f}%",
        ha="center",
        va="bottom",
        fontsize=22,
        fontweight="bold",
    )

# Customize the plot
ax.set_ylim(0, max(relative_costs) * 1.2)  # Add some space above the bars
ax.set_ylabel("Relative API Cost", fontsize=24, fontweight="bold")
ax.set_xlabel("Model", fontsize=24, fontweight="bold")

# Set title with larger font
title = ax.set_title(
    "API Cost Change (vs. Base Method)", fontsize=28, fontweight="bold", pad=36
)

# Add a box around the title
title_bbox = title.get_window_extent(fig.canvas.get_renderer())
title_bbox = title_bbox.transformed(fig.transFigure.inverted())
rect = patches.Rectangle(
    (title_bbox.x0 - 0.05, title_bbox.y0 - 0.02),
    title_bbox.width + 0.15,
    title_bbox.height + 0.04,
    linewidth=2,
    edgecolor="black",
    facecolor="none",
    transform=fig.transFigure,
)
fig.patches.append(rect)

# Increase tick label size
ax.tick_params(axis="y", labelsize=20)
ax.tick_params(axis="x", labelsize=20)

# Add grid
ax.grid(axis="y", alpha=0.3, linestyle="--", linewidth=1)
ax.set_axisbelow(True)

# Remove top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(1.5)
ax.spines["bottom"].set_linewidth(1.5)

# Save the figure
plt.tight_layout()
plt.savefig(
    "imgs/api_cost_comparison_docstring_removal.png", dpi=300, bbox_inches="tight"
)
plt.show()
