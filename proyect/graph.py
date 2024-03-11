import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.62607015e-34  # Planck's constant (m^2 kg / s)
c = 299792458  # Speed of light in vacuum (m/s)
k = 1.380649e-23  # Boltzmann's constant (m^2 kg s^-2 K^-1)
T = 5778  # Temperature of the Sun (K)

# Wavelength range (m)
wavelengths = np.linspace(100, 1400, 1000)  # 1 nm to 3000 nm

# Planck's law equation
def planck_law(wavelength, T):
    return (2 * h * c**2) / ((wavelength*1e-9)**5 * (np.exp((h * c) / ((wavelength*1e-9) * k * T)) - 1)) *1e-13

# Calculate spectral radiance
spectral_radiance = planck_law(wavelengths, T)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(wavelengths , spectral_radiance, color='red')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Spectral Radiance (W·m⁻²·sr⁻¹·m⁻¹)')
plt.title('Solar Radiation Spectrum')
plt.grid(True)
plt.show()

def gaussian(Amplitude=1,mu=700,sigma=20):
    return lambda x: Amplitude * np.exp(-((x - mu)** 2) / (2 * sigma ** 2)) 

#plot gaussian 
x = np.linspace(600, 800, 1000)
y = gaussian(1,700,20)(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('Gaussian Function')

plt.grid(True)
plt.show()
