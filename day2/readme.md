Ohm's Law Calculator

This program calculates voltage, current, or resistance based on the other two values using Ohm's Law: 𝑉=𝐼×𝑅

def ohms_law(voltage=None, current=None, resistance=None):

    # Calculate voltage if current and resistance are provided
    
    voltage = current * resistance
    
    # Calculate current if voltage and resistance are provided
    
    current = voltage / resistance
    
    # Calculate resistance if voltage and current are provided
    
    resistance = voltage / current
    
    # If all three values or fewer than two values are provided, show an error
    
    return "Please provide exactly two values."
Example usage
ohms_law(voltage=10, resistance=5) ohms_law(current=2, resistance=5)
