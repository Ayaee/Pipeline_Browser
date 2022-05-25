from pipeline import conf
import maya.cmds as cmds
import pymel.core as pm
import os

'''
#### UTILITAIRE TOUT PUBLISH ####
'''


def clean():
    panel = pm.ls("|*")

    for element in panel:
        print(element)
        if element in conf.grp_valid:
            pass
        else:
            print(element)
            pm.delete(element)


def importe():
    pm.FileReference(namespace="modeling").importContents(removeNamespace=True)


def save_publish():
    wip_path = cmds.file(sceneName=True, q=True)
    print(wip_path)
    publish_path = wip_path.replace("WIP", "PUBLISH").replace(".ma", ".mb")
    if os.path.exists(publish_path):
        raise Exception("This publish already exists.")
    print(publish_path)
    folder_path = os.path.dirname(publish_path)
    print(folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    pm.saveAs(publish_path)
