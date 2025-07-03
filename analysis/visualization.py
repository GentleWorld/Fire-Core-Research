#!/usr/bin/env python3
"""
Fire-Core Temperature Visualization Tools
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_temperature_distribution(data, save_path='docs/images/temp_distribution.png'):
    """温度分布の可視化"""
    plt.figure(figsize=(10, 6))
    sns.histplot(data['fire_core_temp'], bins=20, kde=True)
    plt.title('Fire-Core Temperature Distribution')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.axvline(37.1, color='blue', linestyle='--', label='Baseline')
    plt.axvline(39.2, color='orange', linestyle='--', label='Aesthetic Critical')
    plt.legend()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def plot_platform_comparison(data, save_path='docs/images/platform_comparison.png'):
    """プラットフォーム別比較"""
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data, x='Platform', y='fire_core_temp')
    plt.title('Fire-Core Temperature by Platform')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
