try:
    import numpy as np
    print(f"NumPy is installed. Version: {np.__version__}")
except ImportError:
    print("NumPy is not installed.")