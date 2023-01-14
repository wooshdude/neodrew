# neodrew

The official discord bot of Artism(Surreal) (https://artism.place).
This repository is open source. Feel free to contribute or fork it.

## Dependencies
If you intend to use these dependencies, or wish to add your own, I recommend that you a virtual environment. I'll leave a quick tutorial for linux users [here](#how-to-use-a-python-virtual-environment).

#### Discord.py V2.0  
`pip install -U git+https://github.com/Rapptz/discord.py`

#### MongoDB via pymongo  
`pip install pymongo`

#### Flask  
`pip install flask`

## How to use a Python Virtual Environment
A Python Virtual Environment is the best way to keep track of your pip libraries. I'll go over how to create one for specificly this project, but the steps will be the same for most other projects.

Before you've cloned this repoo, create a base directory somewhere. This is where you'll create your virtual environment.

#### Install Python Venv  
`pip install python3-venv`

#### Create the virtual environment  
`python3 -m venv ./`  

#### Activate the virtual environment  
`source bin/activate`  

You should see the name of the project directory on the left in parentheses. That means you've successfully created the virtual environment. You can freely use `pip install` and libraries you install won't be added to your PATH. If you want to leave the virtual environment you can use `deactivate` in any directory.

Feel free to clone the repository inside this directory or somewhere else.  
`git clone https://github.com/wooshdude/neodrew`