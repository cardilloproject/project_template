# project_template

This is a basic file structure for a project that uses cardillo. The folder `cardillo_add_ons` will contain your cardillo building blocks, e.g., own implementations of solvers, bodies or constraints. The `example` folder contains your simulation project that invokes cardillo together with your own add-ons. In order to use your add-ons, this template provides a `setup.py` that allows you to install the add-ons. It is recommended to install the add-ons in *editable* mode, such that the add-ons can be modified while working on the simulation project.

If you are experienced with Python and have an own workflow, go to [Installation](#installation). If you are a newbie or if you are interested in the workflow we are using, go to [Our Workflow](#our-workflow).

## Installation
To install the project in editable mode (option `-e`), clone or download the current repository, open a console, navigate to the root folder of the project and run `pip install -e .`.

```bash
git clone https://github.com/cardilloproject/project_template.git
pip install -e .
```

The latest version of [cardillo](https://github.com/cardilloproject/cardillo) will automatically be installed as a dependency.

### Test the installation

You can test the installation by running the example simulation
```bash
python example/woodpecker_toy_sim.py
```

## Our workflow

We use Visual Studio Code (VS Code) as development environment. The following installation instructions will guide you through the installation of Python, VS Code and the present template and show you how to set up a virtual Python environment for your project. Simply put, the following will set you up for your amazing cardillo-based project from scratch. 

### Python

Download and install Python from https://www.python.org/downloads/. Alternatively you can use a package manager to install Python (recommended on Mac/Linux). On Windows, make sure that Python is on your system's path.

Check that Python is properly installed by typing `python` in a terminal, which should start the Python application. Note, depending on the installation, e.g.\ on Mac, the Python command is `python3`. 

### VS Code

Download and install VS Code from https://code.visualstudio.com. Then, start VS Code and install the Python extension called "Python" (provided by Microsoft). For help, consult https://code.visualstudio.com/docs/languages/python.

### Virtual envirionment and project template

Clone (or download) the template
```bash
git clone https://github.com/cardilloproject/project_template.git
```

Open the downloaded folder in VS Code. Either manually within VS Code (File $\to$ Open Folder ...) or type `code project_template` in your terminal.

Start a new terminal in VS Code (Terminal $\to$ New Terminal). The path should point to the downloaded folder now. Otherwise, navigate to the downloaded folder using the `cd` command.

It is favorable to work within a [virtual environment](https://docs.python.org/3/library/venv.html) for every project, such that installed packages do not interfere between different projects. To create a virtual environment named *myvenv*, execute
```bash
python -m venv myvenv
```
You might have to replace the `python` command by `python3`.

To activate the created virtual environment run the activation script `myvenv/bin/activate` (on Windows: `myvenv/Scripts/activate`) from your terminal. You should notice a change in your terminal and the name *myvenv* should typically appear somewhere. Now, the terminal commands `python` and `pip` point to the executables in your virtual environment and we are ready to install the project template in the virtual environment by
```bash
pip install -e .
```
where option `-e` is used to install the project template in editable mode. This will enable you to modify your cardillo add-ons on the fly while working on your project. The latest version of [cardillo](https://github.com/cardilloproject/cardillo) will automatically be installed as a dependency.

You are now set up to run your first simulation. For that, either run
```bash
python example/woodpecker_toy_sim.py
```
in your terminal or open the file `example/woodpecker_toy_sim.py` in VS Code and click "Run Python File" (typically a green triangle in the top right of your VS Code window.) Alternatively, right-click and "Run Python $\to$ Run Python File in Terminal".

Everything is set up now. Have fun modifying the simulation, coding new simulations or extending cardillo with own add-ons!

