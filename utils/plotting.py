"""
Plotting utilities for RL visualizations.

Functions for visualizing:
- Training curves (episode returns, losses)
- Value functions and Q-values
- Policies (discrete and continuous)
- Environment trajectories
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import List, Optional, Tuple


def plot_training_curve(
    episodes: List[int],
    returns: List[float],
    window_size: int = 100,
    title: str = "Training Curve",
    xlabel: str = "Episode",
    ylabel: str = "Return",
) -> None:
    """
    Plot training curve with moving average.

    Args:
        episodes: List of episode numbers
        returns: List of episode returns
        window_size: Window size for moving average
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
    """
    plt.figure(figsize=(10, 6))
    plt.plot(episodes, returns, alpha=0.3, label="Raw Returns")

    if len(returns) >= window_size:
        moving_avg = np.convolve(returns, np.ones(window_size) / window_size, mode='valid')
        plt.plot(episodes[window_size-1:], moving_avg, label=f"Moving Average ({window_size})")

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_value_function(
    values: np.ndarray,
    title: str = "Value Function",
    cmap: str = "viridis",
) -> None:
    """
    Plot 2D value function as heatmap.

    Args:
        values: 2D array of state values
        title: Plot title
        cmap: Colormap for heatmap
    """
    plt.figure(figsize=(8, 6))
    plt.imshow(values, cmap=cmap, interpolation='nearest')
    plt.colorbar(label="Value")
    plt.title(title)
    plt.xlabel("State Dimension 1")
    plt.ylabel("State Dimension 2")
    plt.tight_layout()
    plt.show()


# TODO: Add more plotting utilities as needed
# - plot_policy()
# - plot_trajectory()
# - plot_q_values()
# - plot_loss_curves()
