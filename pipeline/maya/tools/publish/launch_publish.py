from pipeline.maya.tools.publish import surfacing_publish
from pipeline.maya.tools.publish import modeling_publish
from pipeline.maya.tools.publish import rigging_publish
import maya.cmds as cmds

def run_publish():
    #verifie le chemin si le chemin a MODELING faire :
    #si le chemin a SUFACING :
    #sinon

    current_path = cmds.file(sceneName=True, q=True)
    current_path = current_path.split("/")

    if "MODELING" in current_path:
        modeling_publish.publish()
    elif "SURFACING" in current_path:
        surfacing_publish.publish()
    else:
        rigging_publish.publish()

if __name__ == '__main__':
    print(run_publish())