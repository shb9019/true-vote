# How to setup Backend

- cd to /backend, and create a new python virtual environment, with the command.

  ```bash
   python3 -m venv venv
  ```

- Activate the virtual environment by running the command

  ```bash
    activate venv/bin/activate
  ```

  > You will see (venv) in your terminal after you run this command

- Install the all the dependencies from requirements.txt by running the command

  ```bash
    pip install -r requirements.txt
  ```

- If you install a new package, add the package to requirements.txt by running the command

  ```bash
    pip freeze > requirements.txt
  ```

- To exit the virtual environment by entering the command, `deactivate`
