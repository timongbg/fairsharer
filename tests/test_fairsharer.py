import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from src.fair_sharer import fair_sharer

def test_fair_sharer():
    result1 = fair_sharer([0, 1000, 800, 0], 1)
    assert result1 == [100, 800, 900, 0]
    
    result2 = fair_sharer([0, 1000, 800, 0], 2)
    assert result2 == [100, 890, 720, 90]