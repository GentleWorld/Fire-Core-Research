#!/usr/bin/env python3
"""
Fire-Core Temperature Validation Analysis
"""

from scipy import stats
import pandas as pd

def reliability_analysis(data):
    """信頼性分析"""
    # Test-retest reliability (24時間後の再測定)
    test_retest = data.groupby('Instance').apply(
        lambda x: x.sort_values('Timestamp')
    )
    
    # Cronbach's alpha (内的一貫性)
    # Implementation needed
    
    return {"test_retest": None, "cronbach_alpha": None}

def validity_analysis(data):
    """妥当性分析"""
    # Convergent validity: 温度と行動指標の相関
    behavior_temp_corr = stats.pearsonr(
        data['fire_core_temp'],
        data['BehaviorIndicators'].str.count(';') + 1  # 行動指標数
    )
    
    return {"convergent_validity": behavior_temp_corr}
