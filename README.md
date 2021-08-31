# Jobsity QA Challenge

## Requeriments

You'll need to install Python on your computer. Here I'll leave the link to Python [page](https://www.python.org) so you latest version.

**Note**: Python version 3.8 or later is required.

## How to install?

After you install Python you have to install a Python library called pipenv. This library will help you to setup the project on a virtual environment.

To install it just run the script `pip3 install pipenv` on a Terminal or Command Prompt.

After you successfully install pipenv proceed to execute the command `pipenv install` on the project directory using a Terminal or Command Prompt. You will note that all dependencies such as Selenium and Pytest will start to download and install.

When everything is done proceed to execute `pipen shell` on the project main directory to enter the virtual environment created by pipenv. The next step depends on the Operating Systems you're using. If you're using macOS you'll have to copy and paste the browser drivers on certain path of your device. In advance I already added the drivers on the drivers directory, so you just have to copy and paste the drivers for macOS on the path `/usr/local/bin`.

**IMPORTANT**: remember to rename the files, removing the sufix __mac_ from them. For example, I have a MacBook with Intel chip, so I would use the drivers chromerdriver_mac and geckodriver_mac, copy and paste the files on the above directory and rename them to remove the sufix __mac_. If you have a MacBook with M1 chip than use the corresponding ones for that case.

If you use Windows, it's even easier. You just have to run the command `pytest` while being in the pipenv virtual environment to execute the test cases.

### How you know you're already inside the virtual environment?

While being on the Terminal or Command Prompt, and after executing the command `pipenv shell` you will note that the path suddenly change and starts with the name of the project as a prefix.

## How to run the project?

The first thing to note is that the project counts with a config file where you have to specify the operating system where you would want to run it. By default, the config file contains macOS as operating system, but if that's not your OS than replace it with a supported one, in this case we're talking about Windows.