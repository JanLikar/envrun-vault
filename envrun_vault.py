from envrun.interfaces import Backend

import hvac


class Vault(Backend):
    """Only KV2 is currently supported, token auth only."""

    _client = None

    config_defaults = {
        'vault_url': 'http://localhost:8200',
    }

    def __init__(self, name: str, backend_config: dict, *args, **kwargs):
        self.name = name

        config = {**self.config_defaults, **backend_config}

        self.url = config['vault_url']
        self.token = config['vault_token']
        self.path = config['vault_path']

    def _get_client(self):
        if self._client is None:
            self._client = hvac.Client(url=self.url, token=self.token)

        return self._client

    def __getitem__(self, key):
        client = self._get_client()

        secret = client.secrets.kv.read_secret_version(path=self.path)

        return secret['data']['data'][key]
