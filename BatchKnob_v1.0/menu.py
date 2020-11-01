import nuke
import batchKnob

tool_menu = nuke.menu("Nuke").addMenu("Extra")
tool_menu.addCommand("batchKnob", batchKnob.main, "", icon="")
