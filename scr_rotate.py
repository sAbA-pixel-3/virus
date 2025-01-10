# import win32api
# import win32con
# import pywintypes

# # Constants for rotation
# DEGREES = {
#     0: 0,
#     90: 1,
#     180: 2,
#     270: 3,
# }

# def rotate_screen(degrees):
#     if degrees not in DEGREES:
#         raise ValueError("Degrees must be one of 0, 90, 180, 270.")
    
#     try:
#         # Get the display device
#         device = win32api.EnumDisplayDevices(None, 0)
#         devmode = win32api.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
        
#         # Update orientation
#         devmode.DisplayOrientation = DEGREES[degrees]
#         # Adjust width and height if orientation is 90 or 270
#         if degrees in [90, 270]:
#             devmode.PelsWidth, devmode.PelsHeight = devmode.PelsHeight, devmode.PelsWidth
        
#         # Apply settings
#         result = win32api.ChangeDisplaySettings(devmode, 0)
#         if result != win32con.DISP_CHANGE_SUCCESSFUL:
#             print("Failed to change display orientation. Error code:", result)
#     except pywintypes.error as e:
#         print(f"An error occurred: {e}")

# # Rotate the screen 90 degrees
# rotate_screen(90) 

# DO NOT TRY THIS AT HOME



import time , rotatescreen as rs
pd = rs.get_primary_display()
angel_list = [90,90,90,90] 
for i in range(5):
    for x in angel_list:
        pd.rotate_to(x)
        time.sleep(0.5) 
pd.rotate_to(0) 