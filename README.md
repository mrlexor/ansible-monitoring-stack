# Monitoring stack

### Preparation

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

5. Decrypt `files/someadmin_id_rsa` and put this ssh private key outside the git repo, then encrypt again
   using `ansible-vaul`

> **_NOTE:_**  It's mandatory to use >= Python3.9 <= Python3.11 for working with ansible 5.10.0

### Installation

1. Execute the following command for installing `monitoring-stack`

```shell
ansible-playbook -i inventory playbooks/monitoring_stack.yaml -D
```

### Validation

At this moment only `alertmanager`, `grafana`, `loki` and `prometheus` roles are covered by `molecule`

1. Navigate to a role directory
2. Run `molecule create` for creating infrastructure and deploying dependencies there
3. Install a main service executing `molecule converge`
3. Execute `molecule verify` for running tests
4. Destroy all resources which were provisioned by molecule by executing `molecule destroy`
