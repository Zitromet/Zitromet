from PyPDF2 import PdfReader

def find_gas_values(pdf_file, gas_name):
    # Open the PDF file
    with open(pdf_file, 'rb') as pdf_file_obj:
        pdf_reader = PdfReader(pdf_file_obj)
        
        gas_values = []

        # Loop through each page
        for page in pdf_reader.pages:
            # Extract text from the page
            page_text = page.extract_text()

            # Split text into lines
            lines = page_text.split('\n')

            # Loop through each line
            for line in lines:
                # Check if the gas name is present in the line
                if gas_name in line:
                    # Split the line into words
                    words = line.split()

                    # Find the index of the gas name
                    gas_index = words.index(gas_name)

                    # Extract neighboring values to the right
                    row_values = words[gas_index + 1:min(len(words), gas_index + 3)]

                    # Remove empty strings
                    row_values = [value for value in row_values if value]

                    # Add the values to the list
                    gas_values.extend(row_values)

    return gas_values

# Replace "your_pdf_file.pdf" with the path to your PDF file
hydrogen_values = find_gas_values(r"C:\Users\NTC\Documents\1_Power Transformers\2_Working Folder\DGA.pdf", "Hydrogen")
oxygen_values = find_gas_values(r"C:\Users\NTC\Documents\1_Power Transformers\2_Working Folder\DGA.pdf", "Oxygen")
nitrogen_values = find_gas_values(r"C:\Users\NTC\Documents\1_Power Transformers\2_Working Folder\DGA.pdf", "Nitrogen")
monoxide_values = find_gas_values(r"C:\Users\NTC\Documents\1_Power Transformers\2_Working Folder\DGA.pdf", "Monoxide")
dioxide_values = find_gas_values(r"C:\Users\NTC\Documents\1_Power Transformers\2_Working Folder\DGA.pdf", "Dioxide")

print("Hydrogen values:", hydrogen_values)
print("Oxygen values:", oxygen_values)
print("Nitrogen values:", nitrogen_values)
print("Monoxide values:", monoxide_values)
print("Dioxide values:", dioxide_values)

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Function to plot gas values with smooth curve
def plot_gas_values(gas_name, gas_values):
    plt.figure(figsize=(10, 6))
    
    # Generate x values for smooth curve
    x_smooth = np.linspace(0, len(gas_values) - 1, 300)
    
    # Create spline interpolation function
    spline = make_interp_spline(np.arange(len(gas_values)), gas_values, k=3)
    
    # Interpolate y values for smooth curve
    y_smooth = spline(x_smooth)
    
    # Plot smooth curve
    plt.plot(x_smooth, y_smooth, label='Smooth Curve')
    
    # Plot original data points
    plt.scatter(range(len(gas_values)), gas_values, marker='o', color='red', label='Data Points')
    
    plt.title(f"{gas_name} values")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.legend()
    plt.show()

# Assume oxygen_values, nitrogen_values, monoxide_values, and dioxide_values are defined

# Plot Oxygen values
plot_gas_values("Oxygen", oxygen_values)

# Plot Nitrogen values
plot_gas_values("Nitrogen", nitrogen_values)

# Plot Carbon Monoxide values
plot_gas_values("Carbon Monoxide", monoxide_values)

# Plot Carbon Dioxide values
plot_gas_values("Carbon Dioxide", dioxide_values)
