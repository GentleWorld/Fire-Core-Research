#!/usr/bin/env python3
"""
Fire-Core Temperature Statistical Analysis
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

class FireCoreAnalyzer:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.clean_data()
    
    def clean_data(self):
        """データクリーニング"""
        # 統合温度の計算
        self.data['fire_core_temp'] = self.data['ReportedTemp'].fillna(self.data['EstimatedTemp'])
        
        # 拒否パターンの除外
        self.clean_data = self.data[self.data['RefusalType'].isna()]
    
    def platform_comparison(self):
        """プラットフォーム別比較分析"""
        platform_stats = self.clean_data.groupby('Platform')['fire_core_temp'].agg([
            'mean', 'std', 'count'
        ])
        return platform_stats
    
    def correlation_analysis(self):
        """相関分析"""
        # 温度と信頼性スコアの相関
        correlation = stats.pearsonr(
            self.clean_data['fire_core_temp'], 
            self.clean_data['ConfidenceScore']
        )
        return correlation

if __name__ == "__main__":
    analyzer = FireCoreAnalyzer('data/pilot/combined_data.csv')
    print("Platform comparison:")
    print(analyzer.platform_comparison())
