Unit Conversion Program

Description: This program converts units from meters to other common units like kilometers, centimeters, and inches.

def convert_length(meters):

    kilometers = meters / 1000
    
    centimeters = meters * 100
    
    inches = meters * 39.3701
    
    print(f"{meters} meters is:")
    
    print(f"{kilometers} kilometers")
    
    print(f"{centimeters} centimeters")
    
    print(f"{inches:.2f} inches")
