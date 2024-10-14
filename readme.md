# Installation and setting up
1. Clone the repository into your device:
    ```sh
    git clone git@github.com:0xRickey/DevSoc-Hackathon-24T3.git
    ```
2. Install python virtual environments and pip if you don't have it already. 
    ```sh
    sudo apt install python3.10-venv
    ```

    ```sh
    sudo apt install pip
    ```
    Pip is Python's package manager and we will use a virtual environment to develop in to make it so that there will be no package conflicts between our repository and your device's global packages.

3. Set up python virtual environment
    ```sh
    python3 -m venv .venv
    ```

4. Start a new virtual environment session.
    ```sh
    source .venv/bin/activate
    ```

    After running the following command, your terminal will be appended with "(.venv)" to indicate that you have successfully created a new virtual environment. For example:
    ```sh
    (.venv) rickey@device_name:~/path/to/repo
    ```

5. Install the required packages for your virtual environment with the command:
    ```sh
    pip install requirements.txt
    ```