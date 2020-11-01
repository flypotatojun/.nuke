import nuke
from element_browser import *
from cacheFile import *

m = nuke.menu('Nuke')
m.addCommand('ThedgeVFX/Element Browser', "runElementBrowser()")
m.addCommand('ThedgeVFX/Cache File', "runCachePanel()")


from nukescripts import panels
pane = nuke.getPaneFor('Properties.1')
panels.registerWidgetAsPanel('ElementBrowser', 'Element Browser', 'uk.co.thefoundry.ElementBrowser', True).addToPane(pane)

