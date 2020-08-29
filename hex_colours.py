"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
HEX_TO_NAME = {"ALICEBLUE": "#f0f8ff", "BLACK": "#000000", "BLUEVIOLET": "#8a2be2", "DEEPSKYBLUE": "#00bfff",
                "GHOSTWHITE": "	#f8f8ff", "FORESTGREEN": "#228b22", "GREEN": "#00ff00"}
print(HEX_TO_NAME)

hex_code = input("Enter Colour: ")
while hex_code != "":
    if hex_code.upper() in HEX_TO_NAME:
        print(hex_code, "is", HEX_TO_NAME[hex_code.upper()])
    else:
        print("Invalid short state")
    hex_code = input("Enter short state: ")