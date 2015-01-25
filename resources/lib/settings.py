import json
import uuid
import xbmc
import xbmcaddon

settings = {}

def getGUI(name):
    response = xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Settings.GetSettingValue", "params": {"setting": "' + name + '" }, "id": 1 }')
    return json.loads(response)['result']['value']

print getGUI('services.devicename')

addon = xbmcaddon.Addon()
plexbmc = xbmcaddon.Addon('plugin.video.plexbmc')
settings['debug'] = addon.getSetting('debug') == "true"
settings['gdm_debug'] = int(addon.getSetting('gdm_debug'))
if addon.getSetting('use_xbmc_name') == "true":
    settings['client_name'] = getGUI('services.devicename')
else:
    settings['client_name'] = addon.getSetting('c_name')
settings['uuid'] = str(addon.getSetting('uuid')) or str(uuid.uuid4())
addon.setSetting('uuid', settings['uuid'])
settings['version'] = addon.getAddonInfo('version')
settings['myplex_user'] = plexbmc.getSetting('myplex_user')
settings['serverList'] = []
settings['myport'] = 3005
