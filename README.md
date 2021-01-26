# envrun-vault

[envrun](https://github.com/janlikar/envrun) is a CLI tool that runs a command with dynamically-sourced env variables.

This package provides a [Vault](https://www.vaultproject.io/) backend for `envrun`.

Only Vault KV version 2 API is currently implemented.

[PyPi](https://pypi.org/project/envrun-vault/)

This tool is still under heavy development and its API might change at any time. Use with caution.


## Installation
(not yet published on PyPi)

To install using pip, run:

    pip install envrun_vault

### Example .envrun.toml file

    [vars.vault]
        AWS_API_KEY = "aws-api-key"

    [backends.vault] 
        type = "vault"
        vault_url = "http://localhost:8200"
        vault_token = "myroot"
        vault_path = "app-secrets"
