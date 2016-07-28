
import sys
import os

saved_path = sys.path.copy()

path = os.path.join(os.path.dirname(__file__), 'cast_upgrade_1_5_0.zip')
sys.path.append(path)

from lib_cast_upgrade_1_5_0.internal.upgrader import apply_patch #@UnresolvedImport

apply_patch('1.5.0')

    
    