'''Tests if module is downloaded'''

try:
    import matplotlib
except Exception as e:
    print("Module is not installed!", e)
else:
    print("You have this module")
    print("matplotlib version:", matplotlib.__version__ )
