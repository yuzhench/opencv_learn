import screeninfo

# Get the monitor information
monitors = screeninfo.get_monitors()

# Iterate over each monitor and print the size
for monitor in monitors:
    width = monitor.width
    height = monitor.height
    print(f"Monitor Size: {width}x{height}")
