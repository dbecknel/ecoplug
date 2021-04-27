# ecoplug

-- Copied from https://github.com/gbealmer/pyecoplug

I updated the python to work with the latest releases of home assistant.  The manifest.json needed a version.  switch.py had a deprecated object SwitchDevice, so I switched to SwitchEntity and updated the call to setup_platform accordingly.  Also, I added a unique_id to get rid of the error screen.  Finally, I added logic for displaying on and off instead of true and false.

NOTE: works for the plug that I am using and quiets the logs down.

While evaluating Home Assistant, I ran across this repository. I was looking for support available for my existing devices to determine the viability of moving from openHAB. One type of device I have is Workchoice outlets (same as Woods/WiOn, KAB, etc.) that I use with openHAB, but no offical addon exists. I currently use the homebridge-ecoplug npm package to control them.

When a search revealed this repository, I found no mention of it in the Home Assistant Community. I did find some requests for support with little response. The primary method of use seemed to be firmware mods, not an option I was interested in. I decided to test this with my evaluation system. The author, philburr, had published the requirements on PyPi, so all I had to do was determine the (undocumented) installation steps and test. I was successful in installing, testing and operating my plugs, but I did have to fix errors in the homeassistant support module. Discovery detected all devices on my network, and as I add devices via the Eco Plug apk, they were discovered and included w/o addtional interaction. Once the plugs are setup, the Eco Plug apk is no longer required. Alexa/Google Assistant discovery and control using the homeassistant/hass.io skills work. Note: No support for the energy monitoring capability of selected outlets.

Home Assistant installation

Plugs must be setup on the same network as your homeassistant system via the Eco Plug apk.
Copy folder/files from "ecoplug" to "your homeassistant dir"/custom_components/ecoplug
Edit your configuration.yaml and add the following lines
   switch:
   - platform: ecoplug
     scan_interval: 10
Restart homeassistant. The requirements will be loaded successfully by homeassistant.
Plugs on the same network will be discovered and switches added in the ui.
