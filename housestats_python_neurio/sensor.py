import logging
import neurio

from housestats.metric import Metric
from housestats.sensor.base import BaseSensor

LOG = logging.getLogger(__name__)


class NeurioSensor(BaseSensor):
    sensor_type = 'neurio'

    def __init__(self, config):
        super().__init__(config)

        LOG.info('authenticating to neurio api')
        LOG.debug('key = {client_id}, secret = {client_secret}'.format(
            **(self.config)))

        tp = neurio.TokenProvider(key=self.config['client_id'],
                                  secret=self.config['client_secret'])
        self.nc = neurio.Client(token_provider=tp)

    def sample(self):
        data = self.nc.get_samples_live_last(self.config['id'])
        del data['timestamp']
        return data

    def fetch(self):
        return [Metric.load(dict(
            sensor_type=self.sensor_type,
            sensor_id=str(self.config.get('id', 0)),
            tags=self.config.get('tags', {}),
            fields=self.sample(),
        ))]
