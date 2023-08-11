# GNSS-SIMpy: A Multi-Frequency Multi-GNSS Signal Simulator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GNSS-SIMpy is a Python-based multi-frequency multi-GNSS signal simulator that allows you to generate simulated signals for various Global Navigation Satellite Systems (GNSS) at different frequencies. This tool is designed to aid researchers, engineers, and enthusiasts in testing and evaluating GNSS receiver algorithms, systems, and applications.

## Features

- **Multi-GNSS Support:** Generate simulated signals for multiple GNSS constellations, including GPS, GLONASS, Galileo, BeiDou, and more.

- **Multi-Frequency Simulation:** Simulate signals at different frequencies, accommodating various GNSS frequency bands.

- **Custom Signal Parameters:** Adjust signal parameters such as carrier frequency, signal strength, modulation schemes, and more.

- **Scenario Definition:** Define custom scenarios with multiple satellites in view, each with its own trajectory and signal characteristics.

- **Noise and Interference:** Introduce noise and interference models to simulate real-world conditions.

- **User-Friendly Interface:** Simple-to-use command-line interface (CLI) for configuring and generating simulations.

## Getting Started

These instructions will guide you on setting up and using GNSS-SIMpy on your local machine. 

### Prerequisites

- Python 3.7 or higher
- Additional dependencies listed in `requirements.txt`

### Installation

1. Clone the GNSS-SIMpy repository:
   ```shell
   git clone https://github.com/Imtiaz08/GNSS-SIMpy.git
   cd GNSS-SIMpy
   ```

2. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

### Usage

1. Configure your simulation parameters in the `config.yml` file.

2. Run the simulator using the following command:
   ```shell
   python simulator.py
   ```

3. Simulated signals will be generated and saved in the specified output directory.

## Contributing

Contributions to GNSS-SIMpy are welcome! Whether you want to report a bug, suggest a feature, or submit a pull request, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please create an issue on the [GitHub repository](https://github.com/Imtiaz08/GNSS-SIMpy/issues).

---
*Disclaimer: GNSS-SIMpy is a project developed by [Imtiaz08](https://github.com/Imtiaz08). This project is not affiliated with or endorsed by any official GNSS organization.*
```
