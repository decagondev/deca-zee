# Deca-Zee: Z-Machine Simulator for Zork 1

## Overview
Deca-Zee is a Python-based Z-Machine simulator designed to run Zork 1, a classic text adventure game by Infocom. The simulator interprets Z-Machine version 3 (`.z3`) story files, emulating the virtual machine's memory model, instruction set, and input/output systems to provide a playable experience. This project is under active development and currently supports basic functionality, with plans for full Zork 1 gameplay support.

For detailed project requirements, see the [Product Requirements Document (PRD)](docs/PRD.md).

## Features
- Loads and validates Zork 1 `.z3` story files.
- Supports basic Z-Machine opcodes (`print`, `je`, `ret_true`).
- Decodes ZSCII text for console output.
- Modular design for future extensions (e.g., additional opcodes, input parsing).

## Requirements
- **Python**: 3.8 or higher
- **Zork 1 Story File**: A legally obtained `.z3` file (not included in this repository).
- **No external dependencies** required for core functionality.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/decagondev/deca-zee.git
   cd deca-zee
   ```
2. Ensure Python 3.8+ is installed:
   ```bash
   python --version
   ```
3. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage
1. Obtain a Zork 1 `.z3` file (e.g., `zork1.z3`) and place it in the project directory.
2. Run the simulator:
   ```bash
   python zmachine_simulator.py zork1.z3
   ```
3. The simulator will load the story file and display initial game text. Note: The current version supports limited opcodes and is not fully playable.

## Project Structure
```
deca-zee/
├── docs/
│   └── PRD.md              # Product Requirements Document
├── zmachine_simulator.py   # Main Z-Machine simulator code
├── README.md               # This file
└── LICENSE                 # License file (to be added)
```

## Development Status
The project is in **Phase 1** (see [PRD](docs/PRD.md)):
- Implemented: Story file loading, memory management, basic opcode execution (`print`, `je`, `ret_true`), and ZSCII text decoding.
- Next Steps: Add support for object system, input parsing, and additional opcodes for full Zork 1 gameplay.

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

See the [PRD](docs/PRD.md) for planned features and technical details.

## License
To be determined. A license file will be added to the repository.

## References
- [Z-Machine Standards Document (v1.0)](https://www.inform-fiction.org/zmachine/standards/zmach06a.html)
- [PRD](docs/PRD.md) for detailed project requirements
