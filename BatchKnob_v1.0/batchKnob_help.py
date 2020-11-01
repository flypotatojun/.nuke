# -*- coding: utf-8 -*-
# __author__ = 'XingHuan'
# 9/5/2017

import os
import shutil
import json
import batchKnob_path as BP
import batchKnob_nuke as BN

Current_User = os.path.expanduser('~').replace('\\','/').split("/")[-1]
Default_Knob_Pref_Json = "%s/knob_default_pref.json" % BP.GLOBAL_Folder
Knob_Pref_Json = "%s/Pref/knob_pref.json" % BP.GLOBAL_Folder



def read_json(jsonFile):
    with open(jsonFile) as json_file:
        jsonData = json.load(json_file)
    return jsonData

def write_json(data, jsonFile):
    if not os.path.exists(os.path.dirname(jsonFile)):
        os.makedirs(os.path.dirname(jsonFile))
    jsonDic = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '), encoding="utf-8", ensure_ascii=False)
    with open(jsonFile, 'w') as json_file:
        json_file.write(jsonDic)



def convert_value(valueBefore, valueAfter=""):
    valueType = type(valueBefore)
    #print "value type: %s" % valueType
    if valueType != str:
        finalValue = eval(valueAfter)
    else:
        #print "str"
        finalValue = valueAfter
    #print "afterValue type: %s" % type(finalValue)
    return finalValue


#convert_value("123", "00")

def create_default_pref():
    if not os.path.exists(os.path.dirname(Knob_Pref_Json)):
        os.makedirs(os.path.dirname(Knob_Pref_Json))
    if not os.path.exists(Knob_Pref_Json):
        shutil.copy(Default_Knob_Pref_Json, Knob_Pref_Json)




#knobPref = {"All":["hide_input", "label", "note_font_size"], "Blur":["size"], "Grade":["white", "black"]}
#write_json(knobPref, Default_Knob_Pref_Json)

def get_pref_nodes():
    oldPref = read_json(Knob_Pref_Json)
    return oldPref.keys()

def get_pref_knobs_from_node(nodeName):
    oldPref = read_json(Knob_Pref_Json)
    if nodeName in oldPref.keys():
        return oldPref[nodeName]
    else:
        return []


def add_node(nodeName):
    oldPref = read_json(Knob_Pref_Json)
    oldPref[nodeName] = []
    write_json(oldPref, Knob_Pref_Json)

def del_nodes(nodeNames):
    oldPref = read_json(Knob_Pref_Json)
    for nodeName in nodeNames:
        if nodeName in oldPref:
            del oldPref[nodeName]
    write_json(oldPref, Knob_Pref_Json)

def add_knobs(nodeName, knobNames):
    oldPref = read_json(Knob_Pref_Json)
    for knobName in knobNames:
        if knobName not in oldPref[nodeName]:
            oldPref[nodeName].append(knobName)
    write_json(oldPref, Knob_Pref_Json)

def del_knobs(nodeName, knobNames):
    oldPref = read_json(Knob_Pref_Json)
    for knobName in knobNames:
        if knobName in oldPref[nodeName]:
            oldPref[nodeName].remove(knobName)
    write_json(oldPref, Knob_Pref_Json)


def up(oldList, upIndex):
    if not upIndex >= len(oldList):
        oldList1 = oldList[:upIndex]
        oldList2 = oldList[upIndex]
        oldList3 = oldList[upIndex+1:]
        newList = []
        oldList1.insert(-1, oldList2)
        newList = oldList1
        newList.extend(oldList3)
        return newList

def up_to_top(oldList, upIndex):
    if not upIndex >= len(oldList):
        oldList1 = oldList[:upIndex]
        oldList2 = oldList[upIndex]
        oldList3 = oldList[upIndex+1:]
        newList = []
        newList.append(oldList2)
        newList.extend(oldList1)
        newList.extend(oldList3)
        return newList

def down(oldList, upIndex):
    if not upIndex >= len(oldList):
        oldList1 = oldList[:upIndex]
        oldList2 = oldList[upIndex]
        oldList3 = oldList[upIndex+1:]
        newList = []
        oldList3.insert(1, oldList2)
        newList = oldList1
        newList.extend(oldList3)
        return newList

def down_to_bottom(oldList, upIndex):
    if not upIndex >= len(oldList):
        oldList1 = oldList[:upIndex]
        oldList2 = oldList[upIndex]
        oldList3 = oldList[upIndex+1:]
        newList = []
        newList.extend(oldList1)
        newList.extend(oldList3)
        newList.append(oldList2)
        return newList

def up_knob(nodeName, knobName):
    oldPref = read_json(Knob_Pref_Json)
    oldList = oldPref[nodeName]
    oldIndex = oldList.index(knobName)
    newList = up(oldList, oldIndex)
    oldPref[nodeName] = newList
    write_json(oldPref, Knob_Pref_Json)

def up_knob_to_top(nodeName, knobName):
    oldPref = read_json(Knob_Pref_Json)
    oldList = oldPref[nodeName]
    oldIndex = oldList.index(knobName)
    newList = up_to_top(oldList, oldIndex)
    oldPref[nodeName] = newList
    write_json(oldPref, Knob_Pref_Json)

def down_knob(nodeName, knobName):
    oldPref = read_json(Knob_Pref_Json)
    oldList = oldPref[nodeName]
    oldIndex = oldList.index(knobName)
    newList = down(oldList, oldIndex)
    oldPref[nodeName] = newList
    write_json(oldPref, Knob_Pref_Json)

def down_knob_to_bottom(nodeName, knobName):
    oldPref = read_json(Knob_Pref_Json)
    oldList = oldPref[nodeName]
    oldIndex = oldList.index(knobName)
    newList = down_to_bottom(oldList, oldIndex)
    oldPref[nodeName] = newList
    write_json(oldPref, Knob_Pref_Json)


#create_default_pref()
#add_node("Read")
#add_knobs("Read", ["file", "type"])
#del_knobs("Read", ["file"])





def sort_knobs(nodeName, allKnobList):
    overAllPrefList = get_pref_knobs_from_node("All")
    prefKnobsList = get_pref_knobs_from_node(nodeName)
    # print overAllPrefList
    # print prefKnobsList
    newKnobsList1 = {}
    newKnobsList2 = {}
    newKnobsList = []
    for knobName in allKnobList:
        if knobName in overAllPrefList:
            knobIndex = overAllPrefList.index(knobName)
            newKnobsList1[knobIndex] = knobName
            allKnobList.remove(knobName)
        elif knobName in prefKnobsList:
            knobIndex = prefKnobsList.index(knobName)
            newKnobsList2[knobIndex] = knobName
            allKnobList.remove(knobName)
    allKnobList.sort()
    # print newKnobsList1
    # print newKnobsList2
    # print allKnobList
    newKnobsList.extend(newKnobsList1.values())
    newKnobsList.extend(newKnobsList2.values())
    newKnobsList.extend(allKnobList)
    # print newKnobsList
    return newKnobsList







#aa = ['disable', 'black', "hide_input", "add", "white", "label"]
#bb = sort_knobs("De", aa)





