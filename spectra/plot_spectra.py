import matplotlib.pyplot as plt

def wavelength_to_rgb(wavelength, gamma=0.8):
    wavelength = float(wavelength)

    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    # R *= 255
    # G *= 255
    # B *= 255
    return R, G, B

def main():
    plt.figure(figsize=(8, 2), dpi=144)
    for wl in range(380, 750):
        color = wavelength_to_rgb(wl)
        plt.vlines(wl, 0, 1, color=color)

    absorbance = {
        "FAM": 494,
        "NED": 546,
        "VIC": 538,
        "PET": 558,
        "LIZ": 638
    }

    for dye, wl in absorbance.items():
        color = wavelength_to_rgb(wl)
        plt.arrow(wl, 1.1, 0, -0.1, color=color, head_length=0.05, head_width=4, length_includes_head=True, label=dye)

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

