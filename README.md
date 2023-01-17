# neodrew

The official discord bot of Artism(Surreal) (https://artism.place).
This repository is open source. Feel free to contribute or fork it.  

Need support? Check out our support server at https://discord.gg/uGS9wSjMys!

## Dependencies
 
#### Discord.py V2.0  
`pip install -U git+https://github.com/Rapptz/discord.py`

#### MongoDB via pymongo  
`pip install pymongo`

#### Flask  
`pip install flask`

#### Requests  
`pip install requests`  

> Note: If you intend to use these dependencies, or wish to add your own, I recommend that you a create a Python Virtual Environment. I'll leave a quick tutorial for linux users [here](#how-to-use-a-python-virtual-environment).


## ToDo
- Separate functionality into cogs.
- Create Flask webserver.
    - Allow users to generate a custom event embed.
- Save user data in MongoDB database.
    - Bot should be able to fetch how active users are in each server.


## How to use a Python Virtual Environment
A Python Virtual Environment is the best way to keep track of your pip libraries. I'll go over how to create one for specificly this project, but the steps will be the same for most other projects.

Before you've cloned this repo, create a new directory somewhere. This is where you'll make your virtual environment.

#### Install Python Venv  
`pip install python3-venv`

#### Create the virtual environment  
`python3 -m venv ./`  

#### Activate the virtual environment  
`source bin/activate`  

You should see the name of the project directory on the left in parentheses. That means you've successfully created the virtual environment. You can freely use `pip install` and libraries you install won't be added to your PATH. If you want to leave the virtual environment you can use `deactivate` in any directory.

Feel free to clone the repository inside this directory or somewhere else.  
`git clone https://github.com/wooshdude/neodrew`
