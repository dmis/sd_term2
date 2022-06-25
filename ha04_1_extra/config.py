import yaml


class Config:
    def __init__(self):
        with open('settings.yaml', 'r') as f:
            self._config = yaml.load(f, Loader=yaml.FullLoader)
        # print(self._config['requests'][0]['method'])

    @property
    def config(self):
        return self._config

    def __call__(self, *args, **kwargs):
        return self._config

    @property
    def requests(self) -> list:
        return self._config['requests']

    @property
    def stages(self) -> list:
        return self._config['STAGES']
