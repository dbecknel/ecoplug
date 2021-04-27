import logging

from homeassistant.const import (DEVICE_DEFAULT_NAME, ATTR_HIDDEN, EVENT_TIME_CHANGED, EVENT_HOMEASSISTANT_STOP)
from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.entity import ToggleEntity
from homeassistant.helpers.event import track_time_change

DEFAULT_INVERT_LOGIC = False

DOMAIN = 'ecoplug'
REQUIREMENTS = ['pyecoplug==0.0.5']
_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = 5


class EcoPlugSwitch(SwitchEntity):
    def __init__(self, plug):
        self._plug = plug
        self._name = plug.name
        self._unique_id = "switch." + self._plug.plug_data[2].decode('utf-8')
        self._state = self._plug.is_on()

    @property
    def should_poll(self):
        return True

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        self.update()
        return self._state
        
    @property
    def state(self):
        if self._state:
            return "on"
        return "off"
        
    @property
    def unique_id(self):
        """Return a unique ID."""
        return self._unique_id
    
    @property
    def device_state_attributes(self):
        """Return the device state attributes."""
        attrs = {
            "brand": "Eco Plug",
            "friendly_name": self._name,
        }

        return attrs

    def turn_on(self):
        self._plug.turn_on()
        self.update()

    def turn_off(self):
        self._plug.turn_off()
        self.update()

    def update(self):
        _LOGGER.info('update')
        self._state = self._plug.is_on()

    

def setup_platform(hass, config, add_entities, discovery_info=None):
    from pyecoplug import EcoDiscovery

    discovered = {}
    def add(plug):
        if not plug.name in discovered:
            add_entities([EcoPlugSwitch(plug)], True)
            discovered[plug.name] = plug

    def remove(plug):
        # Is there a way to remove devices??
        pass

    disco = EcoDiscovery(add, remove)
    disco.start()

    def stop_disco(event):
        disco.stop()

    hass.bus.listen_once(EVENT_HOMEASSISTANT_STOP, stop_disco)

