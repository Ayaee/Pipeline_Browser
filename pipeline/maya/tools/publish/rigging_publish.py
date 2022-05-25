from pipeline.maya.tools.publish import utils_publish as utils
import pymel.core as pm


def publish():
    utils.clean()
    utils.importe()
    utils.save_publish()


##### TEST #####
if __name__ == '__main__':
    pm.openFile("D:/ABYGAELLE_FABRE/WS_MicroFilm/MOVIE/ASSETS/CHAIR/RIGGING/WIP/CHAIR_RIGGING_V001.ma", force=True)
    publish()
