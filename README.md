# Monitoring stack

In order to work with this repo you have to perform the following step:

1. Setup `venv`:

```shell
python3 -m venv ./venv
```

2. Activate `venv`:

```shell
. venv/bin/activate
```

3. Install Python packages:

```shell
pip install -r requirements.txt
```

4. Create `.vault` directory and put the ansible vault key into `.vault/devops` file

> **_NOTE:_**  It's mandatory to use >= Python3.9 <= Python3.11 for working with ansible 5.10.0
