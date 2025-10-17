try:
    import matplotlib
    print(f"Matplotlib is installed. Version: {matplotlib.__version__}")
except ImportError:
    print("Matplotlib is not installed.")