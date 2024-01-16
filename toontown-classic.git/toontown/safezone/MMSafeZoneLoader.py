from panda3d.core import *
import SafeZoneLoader
import MMPlayground
import thread
from toontown.toonbase import ToontownGlobals
import toontown.toonbase.WaitAsync as WaitAsync
#"I added modern merrygorounds!" --Sparksammy

class MMSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = MMPlayground.MMPlayground
        self.musicFile = 'phase_6/audio/bgm/MM_nbrhood.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/MM_SZ_activity.ogg'
        self.dnaFile = 'phase_6/dna/minnies_melody_land_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_MM_sz.dna'

    def load(self):
        print 'loading MM safezone'
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.piano = self.geom.find('**/center_icon')
        if self.piano.isEmpty():
            self.notify.error('Piano not found')
        else:
            hq = self.geom.find('**/*toon_landmark_hqMM_DNARoot')
            hq.wrtReparentTo(self.piano)
        self.mgra = loader.loadModel("phase_13/models/parties/partyMerryGoRound.bam")
        self.mgra.setPos(21,-45,-12)
        self.mgra.setHpr(666,0,0)
        self.mgrb = loader.loadModel("phase_13/models/parties/partyMerryGoRound.bam")
        self.mgrb.setPos(-28,-41,-12)
        self.mgrb.setHpr(666,0,0)
        self.mgra.reparentTo(render)
        self.mgrb.reparentTo(render)
        self.mgra.show()
        self.mgrb.show()
        
    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        dummyNode = render.attachNewNode("Dummy Node Name")
        self.mgra.hide()
        self.mgrb.hide()
        del self.piano
