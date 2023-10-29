# donut-animation

A Python project that showcases a mesmerizing rotating donut animation using object-oriented programming principles, inspired by Andy Sloane's original C implementation.
<br><br>

[![Video Preview](donut-animation.png)](https://drive.google.com/file/d/103gciOKSiq67wH-ZFcU8JBxo3aFAhN5O/view?usp=sharing)

Click the image above to play the video.
<br><br>

<div align="center">
<h1 align="center">

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/license/vaidyanathaniyer/donut-animation?style&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/vaidyanathaniyer/donut-animation?style&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/vaidyanathaniyer/donut-animation?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/vaidyanathaniyer/donut-animation?style&color=5D6D7E" alt="GitHub top language" />
</div>

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#-modules)
- [📚 Object-Oriented Programming Concepts](#-object-oriented-programming-concepts)
- [🍩 How Does donut-animation.py Work?](#-how-does-donut-animationpy-work)
- [🚀 Getting Started](#-getting-started)
  - [How to Install Python and Visual Studio Code on Windows or macOS](#how-to-install-python-and-visual-studio-code-on-windows-or-macos)
  - [How to Fork a GitHub Project and Open it in Visual Studio Code](#how-to-fork-a-github-project-and-open-it-in-visual-studio-code)
  - [Running the Python Script in Visual Studio Code](#running-the-python-script-in-visual-studio-code)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

VabAI is an all-in-one AI-powered web application built with a range of cutting-edge technologies and services. It offers an array of features designed to empower users with the latest AI capabilities:

1. GPT-3 Text Analyzer 🔍: Unleash the power of GPT-3 for supercharged text analysis. Extract key insights, discover the most positive words, and visualize named entity recognition for your text.

2. AMA AI (Ask Me Anything) 🤖: Meet your virtual buddy, AMA AI. Ask questions and receive smart responses in the blink of an eye.

3. Image Generation 🖼️: Watch the magic happen with Huggingface Diffusers, conjuring AI-powered images based on your text prompts.

VabAI is powered by OpenAI, Spacy, Bard, and Torch, and is designed for a seamless user experience. Navigate through the features via the sidebar and explore the limitless possibilities of AI.

## 📦 Features

### Adherence to Object-Oriented Principles 🧬

The project is designed with a clear adherence to object-oriented principles, ensuring modularity and maintainability. It utilizes classes and methods to encapsulate functionality, promoting code organization and reusability.

### Modular and Extensible 🧩

The project embraces a modular and extensible architecture, allowing for easy integration of new features and components. The use of classes and well-defined interfaces facilitates the addition of functionality without disrupting the existing codebase.

### Error Handling 🚧

The project includes robust error handling mechanisms to gracefully manage unexpected issues. It leverages Streamlit for error reporting and provides users with informative feedback in case of errors, ensuring a smooth and user-friendly experience.

### Configuration and Settings ⚙️

Configuration and settings management are central to this project. It follows best practices by using environment variables and a '.env' file for storing sensitive API keys and other configuration options. This approach ensures security and easy configuration changes.

### Customization 🎨

Customization is at the heart of the project, allowing users to tailor their interactions. It leverages the power of Streamlit, offering users the ability to personalize their inputs, prompts, and settings to meet their specific needs and preferences.

### Streamlit Integration 🚀

Streamlit is seamlessly integrated into the project, enhancing its capabilities in error handling and customization. Streamlit is utilized to provide a user-friendly interface for input and output, making it easy for users to interact with the project.

---

## 📂 Repository Structure

```sh
└── Vab-AI/
    ├── .gitattributes
    ├── LICENSE
    ├── README.md
    ├── app.py
    ├── requirements.txt
    └── wordcloud.png
```

---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                   | Summary          |
| ------------------------------------------------------------------------------------------------------ | ---------------- |
| [app.py](https://github.com/vaibhavkumawat-17/Vab-AI/blob/main/app.py) | Source Code File |

</details>

---

## 📚 Object-Oriented Programming Concepts

### Classes and Objects 🧩

The code defines multiple classes, each representing a distinct aspect of the program, including '`HomePage`', '`TextAnalyzer`', '`GPT3Analyzer`', '`AMA_AI`', and '`ImageGenerator`'. Objects of these classes are created and used within the Streamlit application.

### Encapsulation 🔒

Each class encapsulates its data and methods. For example, the '`TextAnalyzer`' class encapsulates the text data to be analyzed and provides methods like '`generate_wordcloud`', '`ner`', and others to manipulate and analyze the text. Encapsulation helps maintain data integrity and prevents unintended modifications from outside the class.

### Initialization and Constructors 🏗️

Each class has an `__init__` method, which serves as a constructor. It initializes the object's attributes. For instance, the '`TextAnalyzer`' class initializes the text attribute with the provided '`text`' for analysis.

### Methods 🧰

Each class has methods that encapsulate specific functionality. For example, the `generate_wordcloud` method in the '`TextAnalyzer`' class generates a word cloud based on the input text, and the `generate_image` method in the '`ImageGenerator`' class generates an image based on a text prompt.

### Attributes 📝

The classes define attributes that store data specific to their roles. For example, the `text` attribute in the '`TextAnalyzer`' class stores the input text for analysis, and the pipe attribute in the '`ImageGenerator`' class stores the Diffusion Pipeline for image generation.

### Modularity and Reusability 🔄

The use of classes and methods enhances modularity and code reusability. Each class encapsulates a specific set of functionalities, making it easy to reuse and maintain code.

### Separation of Concerns 🎯

The code separates different functionalities into distinct classes, following the Single Responsibility Principle (SRP) of OOP. For example, the '`TextAnalyzer`' class is responsible for text analysis, while the '`ImageGenerator`' class is responsible for image generation.

---

## 🍩 How Does donut-animation.py Work?

The "Donut" class represents the rotating donut and has attributes for controlling its horizontal and vertical movement. The "update" method updates these angles to create the rotating effect.

The "TerminalRenderer" class handles the rendering of the donut animation in the terminal. It maintains a character screen and a depth buffer for rendering characters. The "clear_screen" method clears the terminal screen, and the "render" method performs the rendering of the rotating donut based on its orientation.

To visualize the animation, the code performs calculations based on trigonometric functions to determine the position and shading of characters in the terminal, creating the illusion of a rotating donut. The `clear_screen` function is used to clear the screen before rendering each frame, and the loop in the main function continuously updates and displays frames to create the animation effect. The animation speed is controlled by the "FRAME_RATE" variable.

The rotation of the donut is controlled by the A and B attributes of the Donut object, which are incremented in the update method, causing the donut to rotate around the X and Y axes. The shape of the donut is created by manipulating the coordinates and using math functions to calculate depth and shading.

---

## 🚀 Getting Started

### How to Install Python and Visual Studio Code on Windows or macOS:

#### For Windows:

- 🌐 Go to the [Python official website](https://www.python.org/downloads/) and download the latest Python installer for Windows.
- 🏃‍♀️ Run the installer and make sure to check the box that says "Add Python to PATH" during the installation process.
- ✔️ Once the installation is complete, open Command Prompt to verify that Python is installed by running `python --version`.

#### For macOS:

- 🍏 Open the Terminal on your macOS.
- 🕵️‍♀️ Check if Python is already installed by running `python --version`. If it's not installed, you'll be prompted to install it.
- 💻 To install Python on macOS, it is recommended to use the Homebrew package manager. If you don't have Homebrew, you can install it by following the instructions at [brew.sh](https://brew.sh/).
- 🍺 After installing Homebrew, run the following command to install Python: `brew install python`.

### Installing Visual Studio Code:

- 🌐 Visit the [Visual Studio Code official website](https://code.visualstudio.com/).
- 📥 Download the installer for Windows or macOS.
- 🏁 Run the installer and follow the on-screen instructions to complete the installation.

### How to Fork a GitHub Project and Open It in Visual Studio Code:

- 🌐 Open your web browser and go to the GitHub repository you want to fork: [vaidyanathaniyer/donut-animation](https://github.com/vaidyanathaniyer/donut-animation).
- 🍴 Click the "Fork" button in the top right corner of the repository page. This will create a copy of the repository in your GitHub account.
- ✅ Once the forking process is complete, go to your GitHub profile, and you'll find the forked repository in your repositories list.
- 🔗 Click on the forked repository to open it.
- 🟢 Click the "Code" button and copy the URL of the repository (e.g., `https://github.com/your-username/donut-animation.git`).

### Using Visual Studio Code:

- 🚀 Open Visual Studio Code.
- 🧩 Click on the "Extensions" icon on the left sidebar (or press `Ctrl+Shift+X` on Windows/Linux or `Cmd+Shift+X` on macOS).
- 📦 Search for "GitHub Pull Requests and Issues" and "GitLens" extensions and install them. These extensions will help you work with GitHub repositories.
- 🔄 Click on the "Source Control" icon on the left sidebar (or press `Ctrl+Shift+G` on Windows/Linux or `Cmd+Shift+G` on macOS).
- 📂 Click the "Clone Repository" button.
- 📋 Paste the URL of your forked repository and choose a local directory where you want to clone the repository.
- 📂 Open the cloned repository in Visual Studio Code.

### Running the Python Script in Visual Studio Code:

- 💼 In Visual Studio Code, open the `donut-animation.py` file from the cloned repository.
- 🚀 Open a terminal in Visual Studio Code by clicking on "Terminal" in the top menu and selecting "New Terminal."
- 📂 In the terminal, navigate to the directory where the `donut-animation.py` script is located. You can use the `cd` command to change directories.
- ▶️ Run the Python script with the following command:

  `python donut-animation.py`

- 🎉 The script will execute, and you will see the rotating donut animation in the terminal.

🎉 That's it! You've successfully installed Python and Visual Studio Code, forked a GitHub repository, and run the Python script using Visual Studio Code's terminal. Enjoy the donut animation!

---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:

1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).

```sh
git checkout -b new-feature-branch
```

4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.

```sh
git commit -m 'Implemented new feature.'
```

6. Push your changes to your forked repository on GitHub using the following command

```sh
git push origin new-feature-branch
```

7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
   The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the **MIT License**. See the [MIT License](LICENSE) file for additional information.

---

## 👏 Acknowledgments

- ℹ️ https://www.youtube.com/watch?v=sW9npZVpiMI&t=151s
- ℹ️ https://www.a1k0n.net/2011/07/20/donut-math.html

[↑ Return](#Top)

---