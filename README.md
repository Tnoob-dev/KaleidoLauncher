# Kaleido Launcher

<div align="center">

**A modern Terminal User Interface (TUI) launcher for Minecraft profiles**

[![Python Version](https://img.shields.io/badge/python-3.10--3.14-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.0.5-orange.svg)](https://github.com/Tnoob-dev/KaleidoLauncher)

</div>

---

## 📋 Overview

Kaleido is a beautiful and intuitive Terminal User Interface (TUI) application for managing and launching Minecraft profiles. Built with [Textual](https://github.com/Textualize/textual), it provides a modern, keyboard-driven experience for Minecraft enthusiasts who prefer working in the terminal.

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Install from PyPI

```bash
pip install kaleido-launcher
```

```bash
pipx install kaleido-launcher
```

### Install from Source

```bash
# Clone the repository
git clone https://github.com/Tnoob-dev/KaleidoLauncher.git
cd kaleido

# Install in development mode
pip install -e .
```

---

## 🎯 Usage

Launch Kaleido from your terminal:

```bash
kaleido
```

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `q` or `Ctrl+C` | Quit the application |
| `1` | Switch to Minecraft theme |
| `2` | Switch to Nether theme |
| `3` | Switch to End theme |

---

## 🛠️ Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/Tnoob-dev/KaleidoLauncher.git
cd KaleidoLauncher

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e .
```

### Dependencies

Kaleido is built with these amazing libraries:

- **[Textual](https://github.com/Textualize/textual)** - Modern TUI framework
- **[minecraft-launcher-lib](https://minecraft-launcher-lib.readthedocs.io/)** - Minecraft launcher functionality
- **[SQLModel](https://sqlmodel.tiangolo.com/)** - SQL database management
- **[Pydantic](https://docs.pydantic.dev/)** - Data validation

## 🎨 Themes

Kaleido comes with three built-in themes inspired by Minecraft dimensions:

1. **Minecraft Theme** - Classic Overworld colors
2. **Nether Theme** - Dark reds and crimson tones
3. **End Theme** - Purple and dark cosmic colors

Switch themes on-the-fly using the number keys (1, 2, 3).

---

## 📝 Configuration

Kaleido stores its configuration and profiles in platform-specific directories:

- **Linux**: `~/kaleido/`
- **macOS**: `~/kaleido/`
- **Windows**: `C:\Users\<Username>\AppData\Roaming\kaleido\`
---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

[TitiLM10](https://t.me/TitiLM10)

- **Tnoob-dev**

- Email: cristiandeleonmonzon@gmail.com

---

## 💻 Follow the project

- [Discord](https://discord.gg/9qMVSfWs)
- [Telegram](https://t.me/KaleidoMC)


## 🙏 Acknowledgments

- [Textual](https://github.com/Textualize/textual) - For the amazing TUI framework
- [minecraft-launcher-lib](https://gitlab.com/JakobDev/minecraft-launcher-lib) - For Minecraft launcher functionality
- The Minecraft community - For inspiration

---

## 📊 Project Status

**Current Version**: 0.1.0

Kaleido is under active development. New features and improvements are being added regularly.

---

<div align="center">

Made with ❤️ by Tnoob-dev

</div>
