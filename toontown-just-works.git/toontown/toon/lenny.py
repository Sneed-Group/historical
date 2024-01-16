from pandac.PandaModules import *
toon = base.localAvatar
head = base.localAvatar.getPart('head')

def makeCard(book=False):
    cardMaker = CardMaker('laughing-man-cm')
    cardMaker.setHasUvs(1)
    cardMaker.setFrame(-0.5, 0.5, -0.5, 0.5)

    nodePath = NodePath('laughing-man')
    nodePath.setBillboardPointEye()

    lmFace = nodePath.attachNewNode(cardMaker.generate())
    lmFace.setTexture(loader.loadTexture('phase_3/lenny.png'))
    lmFace.setY(-0.302)
    lmFace.setTransparency(True)

    return nodePath


def addHeadEffect(head, book=False):
    card = makeCard(book=book)
    card.setScale(1.45 if book else 2.5)
    card.setZ(0.05 if book else 0.5)
    for nodePath in head.getChildren():
        nodePath.removeNode()
    card.instanceTo(head)


def addToonEffect(toon):
    toon.getDialogueArray = lambda *args, **kwargs: []
for lod in base.localAvatar.getLODNames():
				addHeadEffect(base.localAvatar.getPart('head', lod))