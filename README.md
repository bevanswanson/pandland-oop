# Pandland

Welcome to the High Street Discount Data Consultancy _Pandland_!  We are growing rapidly, and need to provide some BI metrics to measure how we've been doing.  Unfortunately, our homemade Data Science library, `oaklandas` is broken!  Can _you_ fix it before the board meeting tomorrow?!

## Setting Up the Suite

It works best in either Codespaces or a code editor with notebook support (PyCharm or VSCode with Jupyter).  I don't understand Conda or JupyterLabs so you're on your own with that one.  If you are running this on your own machine, set up a virtual environment by running `python3 -m venv venv` then `source ./venv/bin/activate` in unix or `.\venv\Scripts\activate` in smelly old Windows. Then 
install all the dependencies with `pip3 install -r requirements.txt` and you should be ready to go!

If you are running this in Codespaces, then it runs in an isolated Dev Container, so it runs fine.  Press the play icon in the `pandland.ipynb` and install all the suggested extensions, then 'run all' to get the jupyter experience.


## Fixing the Library

Make sure you are in the `tutorial` branch.  All the functions are broken!  If you run the notebook `pandland.ipynb` you can see what needs to happen - at the moment, each cell calls a function in `oaklandas/oaklandas.py` which is set to `raise` an error.  This should perform the expected ask - change the class methods to perform the required task.  You can check your work by running `pytest -xv`.  You might have to restart the IPython kernel for libary changes to be reflected in the notebook.
