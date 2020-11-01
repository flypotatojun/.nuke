# -*- coding: utf-8 -*-
# __author__ = 'XingHuan'
# 9/5/2017

import os
import batchKnob_path as BP
if BP.inNuke:
    import nuke



def get_selected_nodes():
    if not BP.inNuke:
        nodes = []
        node1 = Node("Grade1", "Grade", {"disable":Knob("Boolean_Knob", "disable", False), "black":Knob("AColor_Knob", "black", 1.0)})
        node2 = Node("Grade2", "Grade", {"disable":Knob("Boolean_Knob", "disable", True), "black":Knob("AColor_Knob", "black", 0.5)})
        node3 = Node("Grade3", "Grade", {"disable":Knob("Boolean_Knob", "disable", False, True), "black":Knob("AColor_Knob", "black", [0.1, 0.2, 0.3, 0.4])})
        node4 = Node("Read1", "Read", {"disable":Knob("Boolean_Knob", "disable", False), "file":Knob("File_Knob", "file", ".../.exr")})
        node5 = Node("Read2", "Read", {"disable":Knob("Boolean_Knob", "disable", True), "file":Knob("File_Knob", "file", ".00/.jpg"), "label":Knob("Multiline_Eval_String_Knob", "label", "a\nb")})
        node6 = Node("Write1", "Write", {"disable":Knob("Boolean_Knob", "disable", False), "file":Knob("File_Knob", "file", "final.jpg")})
        node7 = Node("Blur1", "Blur", {"disable":Knob("Boolean_Knob", "disable", False), "size":Knob("Array_Knob", "size", 0.0)})
        nodes.append(node1)
        nodes.append(node2)
        nodes.append(node3)
        nodes.append(node4)
        nodes.append(node5)
        nodes.append(node6)
        nodes.append(node7)
        return nodes
    else:
        return nuke.selectedNodes()


def get_nodes_class(nodes):
    nodeClasses = []
    for node in nodes:
        if node.Class() not in nodeClasses:
            nodeClasses.append(node.Class())
    return nodeClasses


def node_in_class(node, nodeClasses):
    if node.Class() in nodeClasses:
        return True
    else:
        return False







def get_knobs_from_node(node):
    return node.knobs()

def get_knobs_from_nodeName(nodeName):
    if BP.inNuke:
        try:
            node = nuke.createNode(nodeName, inpanel=False)
            knobs = node.knobs().keys()
            nuke.delete(node)
            return knobs
        except:
            return []
    else:
        return []



class Node():
    def __init__(self, nodeName, nodeClass, nodeKnobs):
        self.nodeName = nodeName
        self.nodeClass = nodeClass
        self.nodeKnobs = nodeKnobs

    def Class(self):
        return self.nodeClass

    def name(self):
        return self.nodeName

    def knobs(self):
        return self.nodeKnobs

    def knob(self, name):
        return self.nodeKnobs[name]




Knob_Classes = ["Boolean_Knob", "File_Knob", "Array_Knob", "ColorChip_Knob", "PythonKnob", "Multiline_Eval_String_Knob", "AColor_Knob", "Disable_Knob", "ChannelMask_Knob", "WH_Knob", "Enumeration_Knob"]




class Knob():
    def __init__(self, knobClass, knobName, knobValue, knobHasExpression=False):
        self.knobClass = knobClass
        self.knobName = knobName
        self.knobValue = knobValue
        self.knobHasExpression = knobHasExpression
        self.knobCurveList = [curve("frame"), curve()]

    def Class(self):
        return self.knobClass

    def value(self):
        return self.knobValue

    def setValue(self, value):
        print "set value"
        self.knobValue = value

    def hasExpression(self):
        return self.knobHasExpression

    def setExpression(self, expression):
        print "set expression"
        pass

    def animation(self, n):
        if self.knobHasExpression:
            return self.knobCurveList[n]
        else:
            return None

    def deleteAnimation(self, c):
        if c in self.knobCurveList:
            self.knobCurveList.remove(c)



class curve():
    def __init__(self, curveExpression="curve"):
        self.curveExpression = curveExpression

    def expression(self):
        return self.curveExpression
