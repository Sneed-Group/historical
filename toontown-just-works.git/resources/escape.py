from sys import argv
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
base.disableMouse()
 
legsAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand-start.bam', 'firehose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_firehose.bam', 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateL-putt.bam', 'slip-forward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-forward.bam', 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eatnrun.bam', 'tickle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_tickle.bam', 'water-gun': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_water-gun.bam', 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverNeutral.bam', 'swim': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swim.bam', 'catch-run': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gamerun.bam', 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sad-neutral.bam', 'pet-loop': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petloop.bam', 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zstart.bam', 'wave': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_wave.bam', 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelneutral.bam', 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_poleneutral.bam', 'bank': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_jellybeanJar.bam', 'scientistGame': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistGame.bam', 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand.bam', 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_lookloop-putt.bam', 'victory': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_victory-dance.bam', 'lose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_lose.bam', 'cringe': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_cringe.bam', 'right': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_right.bam', 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_headdown-putt.bam', 'conked': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_conked.bam', 'jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump.bam', 'into-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_into-putt.bam', 'fish-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishEND.bam', 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zend.bam', 'shrug': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_shrug.bam', 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_sprinkle-dust.bam', 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-bottle.bam', 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_takePhone.bam', 'melt': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_melt.bam', 'pet-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petin.bam', 'look-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_look-putt.bam', 'loop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_loop-putt.bam', 'good-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_good-putt.bam', 'juggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_juggle.bam', 'run': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_run.bam', 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_press-button.bam', 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-back-right.bam', 'water': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_water.bam', 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point-start.bam', 'bad-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_bad-putt.bam', 'struggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_struggle.bam', 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_running-jump.bam', 'callPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_callPet.bam', 'throw': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_pie-throw.bam', 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eat_neutral.bam', 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_tug-o-war.bam', 'bow': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bow.bam', 'swing': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swing.bam', 'climb': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_climb.bam', 'scientistWork': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistWork.bam', 'think': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_think.bam', 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameThrow.bam', 'walk': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_walk.bam', 'down': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_down.bam', 'pole': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_pole.bam', 'periscope': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_periscope.bam', 'duck': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_duck.bam', 'curtsy': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_curtsy.bam', 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zend.bam', 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_loop_dig.bam', 'angry': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_angry.bam', 'bored': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bored.bam', 'swing-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_swing-putt.bam', 'pet-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petend.bam', 'spit': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_spit.bam', 'right-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point.bam', 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_into_dig.bam', 'castlong': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_castlong.bam', 'confused': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_confused.bam', 'neutral': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral.bam', 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zhang.bam', 'reel': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reel.bam', 'slip-backward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-backward.bam', 'sound': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_shout.bam', 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_sidestep-left.bam', 'up': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_up.bam', 'fish-again': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishAGAIN.bam', 'cast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_cast.bam', 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneBack.bam', 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneNeutral.bam', 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistJealous.bam', 'battlecast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fish.bam', 'sit-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_intoSit.bam', 'toss': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_toss.bam', 'happy-dance': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_happy-dance.bam', 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zstart.bam', 'teleport': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_teleport.bam', 'sit': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sit.bam', 'sad-walk': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_losewalk.bam', 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props-start.bam', 'book': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_book.bam', 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zhang.bam', 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistEmcee.bam', 'leverPull': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverPull.bam', 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_tutorial-neutral.bam', 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_badloop-putt.bam', 'give-props': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props.bam', 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-magnet.bam', 'hypnotize': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hypnotize.bam', 'left-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_left-point.bam', 'leverReach': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverReach.bam', 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_feedPet.bam', 'reel-H': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelH.bam', 'applause': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_applause.bam', 'smooch': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_smooch.bam', 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateR-putt.bam', 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishneutral.bam', 'push': 'phase_9/models/char/tt_a_chr_dgs_shorts_legs_push.bam', 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameneutral.bam', 'left': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_left.bam'}
 
torsoAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-hand-start.bam', 'firehose': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_firehose.bam', 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_rotateL-putt.bam', 'slip-forward': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_slip-forward.bam', 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_eatnrun.bam', 'tickle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_tickle.bam', 'water-gun': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_water-gun.bam', 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverNeutral.bam', 'swim': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_swim.bam', 'catch-run': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gamerun.bam', 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sad-neutral.bam', 'pet-loop': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petloop.bam', 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zstart.bam', 'wave': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_wave.bam', 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reelneutral.bam', 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_poleneutral.bam', 'bank': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_jellybeanJar.bam', 'scientistGame': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistGame.bam', 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-hand.bam', 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_lookloop-putt.bam', 'victory': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_victory-dance.bam', 'lose': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_lose.bam', 'cringe': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_cringe.bam', 'right': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_right.bam', 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_headdown-putt.bam', 'conked': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_conked.bam', 'jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump.bam', 'into-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_into-putt.bam', 'fish-end': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishEND.bam', 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zend.bam', 'shrug': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_shrug.bam', 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_sprinkle-dust.bam', 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hold-bottle.bam', 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_takePhone.bam', 'melt': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_melt.bam', 'pet-start': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petin.bam', 'look-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_look-putt.bam', 'loop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_loop-putt.bam', 'good-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_good-putt.bam', 'juggle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_juggle.bam', 'run': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_run.bam', 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_press-button.bam', 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-back-right.bam', 'water': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_water.bam', 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-point-start.bam', 'bad-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_bad-putt.bam', 'struggle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_struggle.bam', 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_running-jump.bam', 'callPet': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_callPet.bam', 'throw': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_pie-throw.bam', 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_eat_neutral.bam', 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_tug-o-war.bam', 'bow': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_bow.bam', 'swing': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_swing.bam', 'climb': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_climb.bam', 'scientistWork': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistWork.bam', 'think': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_think.bam', 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gameThrow.bam', 'walk': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_walk.bam', 'down': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_down.bam', 'pole': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_pole.bam', 'periscope': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_periscope.bam', 'duck': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_duck.bam', 'curtsy': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_curtsy.bam', 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zend.bam', 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_loop_dig.bam', 'angry': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_angry.bam', 'bored': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_bored.bam', 'swing-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_swing-putt.bam', 'pet-end': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petend.bam', 'spit': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_spit.bam', 'right-point': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-point.bam', 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_into_dig.bam', 'castlong': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_castlong.bam', 'confused': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_confused.bam', 'neutral': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral.bam', 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zhang.bam', 'reel': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reel.bam', 'slip-backward': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_slip-backward.bam', 'sound': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_shout.bam', 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_sidestep-left.bam', 'up': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_up.bam', 'fish-again': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishAGAIN.bam', 'cast': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_cast.bam', 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_phoneBack.bam', 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_phoneNeutral.bam', 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistJealous.bam', 'battlecast': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fish.bam', 'sit-start': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_intoSit.bam', 'toss': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_toss.bam', 'happy-dance': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_happy-dance.bam', 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zstart.bam', 'teleport': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_teleport.bam', 'sit': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sit.bam', 'sad-walk': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_losewalk.bam', 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_give-props-start.bam', 'book': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_book.bam', 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zhang.bam', 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistEmcee.bam', 'leverPull': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverPull.bam', 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_tutorial-neutral.bam', 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_badloop-putt.bam', 'give-props': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_give-props.bam', 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hold-magnet.bam', 'hypnotize': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hypnotize.bam', 'left-point': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_left-point.bam', 'leverReach': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverReach.bam', 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_feedPet.bam', 'reel-H': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reelH.bam', 'applause': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_applause.bam', 'smooch': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_smooch.bam', 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_rotateR-putt.bam', 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishneutral.bam', 'push': 'phase_9/models/char/tt_a_chr_dgl_shorts_torso_push.bam', 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gameneutral.bam', 'left': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_left.bam'}
 
duckHead = loader.loadModel('phase_3/models/char/duck-heads-1000.bam')
otherParts = duckHead.findAllMatches('**/*long*')
for partNum in range(0, otherParts.getNumPaths()):
    otherParts.getPath(partNum).removeNode()
ntrlMuzzle = duckHead.find('**/*muzzle*neutral')
otherParts = duckHead.findAllMatches('**/*muzzle*')
for partNum in range(0, otherParts.getNumPaths()):
    part = otherParts.getPath(partNum)
    if part != ntrlMuzzle:
        otherParts.getPath(partNum).removeNode()
duckTorso = loader.loadModel('phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam')
duckLegs  = loader.loadModel('phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam')
otherParts = duckLegs.findAllMatches('**/boots*')+duckLegs.findAllMatches('**/shoes')
for partNum in range(0, otherParts.getNumPaths()):
    otherParts.getPath(partNum).removeNode()
 
duckBody = Actor({'head':duckHead, 'torso':duckTorso, 'legs':duckLegs},
                {'torso':torsoAnimDict, 'legs':legsAnimDict})
duckBody.attach('head', 'torso', 'def_head')
duckBody.attach('torso', 'legs', 'joint_hips')
 
gloves = duckBody.findAllMatches('**/hands')
ears = duckBody.findAllMatches('**/*ears*')
head = duckBody.findAllMatches('**/head-*')
sleeves = duckBody.findAllMatches('**/sleeves')
shirt = duckBody.findAllMatches('**/torso-top')
shorts = duckBody.findAllMatches('**/torso-bot')
neck = duckBody.findAllMatches('**/neck')
arms = duckBody.findAllMatches('**/arms')
legs = duckBody.findAllMatches('**/legs')
feet = duckBody.findAllMatches('**/feet')
 
bodyNodes = []
bodyNodes += [gloves]
bodyNodes += [head, ears]
bodyNodes += [sleeves, shirt, shorts]
bodyNodes += [neck, arms, legs, feet]
bodyNodes[0].setColor(1, 1, 1, 1)
bodyNodes[1].setColor(0.884, 0.248, 0.268, 1)
bodyNodes[2].setColor(0.884, 0.248, 0.268, 1)
bodyNodes[3].setColor(0.264, 0.308, 0.676, 1)
bodyNodes[4].setColor(0.264, 0.308, 0.676, 1)
bodyNodes[5].setColor(1, 1, 1, 1)
bodyNodes[6].setColor(0.264, 0.308, 0.676, 1)
bodyNodes[7].setColor(0.264, 0.308, 0.676, 1)
bodyNodes[8].setColor(0.276, 0.872, 0.36, 1)
bodyNodes[9].setColor(0.276, 0.872, 0.36, 1)
 
topTex = loader.loadTexture('phase_3/maps/desat_shirt_5.jpg')
botTex = loader.loadTexture('phase_4/maps/CowboyShorts1.jpg')
sleeveTex = loader.loadTexture('phase_3/maps/desat_sleeve_5.jpg')
 
bodyNodes[3].setTexture(sleeveTex, 1)
bodyNodes[4].setTexture(topTex, 1)
bodyNodes[5].setTexture(botTex, 1)
 
duckBody.reparentTo(render)
 
geom = duckBody.getGeomNode()
geom.getChild(0).setSx(0.730000019073)
geom.getChild(0).setSz(0.730000019073)
 
offset = 3.2375
 
base.camera.reparentTo(duckBody)
base.camera.setPos(0, -10.0 - offset, offset)
wallBitmask = BitMask32(1)
floorBitmask = BitMask32(2)
base.cTrav = CollisionTraverser()
def getAirborneHeight():
    return offset + 0.025000000000000001
walkControls = GravityWalker(legacyLifter=True)
walkControls.setWallBitMask(wallBitmask)
walkControls.setFloorBitMask(floorBitmask)
walkControls.setWalkSpeed(16.0, 24.0, 8.0, 80.0)
walkControls.initializeCollisions(base.cTrav, duckBody, floorOffset=0.025, reach=4.0)
walkControls.setAirborneHeightFunc(getAirborneHeight)
walkControls.enableAvatarControls()
duckBody.physControls = walkControls
 
def setWatchKey(key, input, keyMapName):
    def watchKey(active=True):
        if active == True:
            inputState.set(input, True)
            keyMap[keyMapName] = 1
        else:
            inputState.set(input, False)
            keyMap[keyMapName] = 0
    base.accept(key, watchKey, [True])
    base.accept(key+'-up', watchKey, [False])
 
keyMap = {'left':0, 'right':0, 'forward':0, 'backward':0, 'control':0}
 
setWatchKey('arrow_up', 'forward', 'forward')
setWatchKey('control-arrow_up', 'forward', 'forward')
setWatchKey('alt-arrow_up', 'forward', 'forward')
setWatchKey('shift-arrow_up', 'forward', 'forward')
setWatchKey('arrow_down', 'reverse', 'backward')
setWatchKey('control-arrow_down', 'reverse', 'backward')
setWatchKey('alt-arrow_down', 'reverse', 'backward')
setWatchKey('shift-arrow_down', 'reverse', 'backward')
setWatchKey('arrow_left', 'turnLeft', 'left')
setWatchKey('control-arrow_left', 'turnLeft', 'left')
setWatchKey('alt-arrow_left', 'turnLeft', 'left')
setWatchKey('shift-arrow_left', 'turnLeft', 'left')
setWatchKey('arrow_right', 'turnRight', 'right')
setWatchKey('control-arrow_right', 'turnRight', 'right')
setWatchKey('alt-arrow_right', 'turnRight', 'right')
setWatchKey('shift-arrow_right', 'turnRight', 'right')
setWatchKey('control', 'jump', 'control')
 
movingNeutral, movingForward = (False, False)
movingRotation, movingBackward = (False, False)
movingJumping = False
 
def setMovementAnimation(loopName, playRate=1.0):
    global movingNeutral
    global movingForward
    global movingRotation
    global movingBackward
    global movingJumping
    if 'jump' in loopName:
        movingJumping = True
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'run':
        movingJumping = False
        movingForward = True
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'walk':
        movingJumping = False
        movingForward = False
        movingNeutral = False
        if playRate == -1.0:
            movingBackward = True
            movingRotation = False
        else:
            movingBackward = False
            movingRotation = True
    elif loopName == 'neutral':
        movingJumping = False
        movingForward = False
        movingNeutral = True
        movingRotation = False
        movingBackward = False
    else:
        movingJumping = False
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    ActorInterval(duckBody, loopName, playRate=playRate).loop()
 
def handleMovement(task):
    global movingNeutral, movingForward
    global movingRotation, movingBackward, movingJumping
    if keyMap['control'] == 1:
        if keyMap['forward'] or keyMap['backward'] or keyMap['left'] or keyMap['right']:
            if movingJumping == False:
                if duckBody.physControls.isAirborne:
                    setMovementAnimation('running-jump-idle')
                else:
                    if keyMap['forward']:
                        if movingForward == False:
                            setMovementAnimation('run')
                    elif keyMap['backward']:
                        if movingBackward == False:
                            setMovementAnimation('walk', playRate=-1.0)
                    elif keyMap['left'] or keyMap['right']:
                        if movingRotation == False:
                            setMovementAnimation('walk')
            else:
                if not duckBody.physControls.isAirborne:
                    if keyMap['forward']:
                        if movingForward == False:
                            setMovementAnimation('run')
                    elif keyMap['backward']:
                        if movingBackward == False:
                            setMovementAnimation('walk', playRate=-1.0)
                    elif keyMap['left'] or keyMap['right']:
                        if movingRotation == False:
                            setMovementAnimation('walk')
        else:
            if movingJumping == False:
                if duckBody.physControls.isAirborne:
                    setMovementAnimation('jump-idle')
                else:
                    if movingNeutral == False:
                        setMovementAnimation('neutral')
            else:
                if not duckBody.physControls.isAirborne:
                    if movingNeutral == False:
                        setMovementAnimation('neutral')
    elif keyMap['forward'] == 1:
        if movingForward == False:
            if not duckBody.physControls.isAirborne:
                setMovementAnimation('run')
    elif keyMap['backward'] == 1:
        if movingBackward == False:
            if not duckBody.physControls.isAirborne:
                setMovementAnimation('walk', playRate=-1.0)
    elif keyMap['left'] or keyMap['right']:
        if movingRotation == False:
            if not duckBody.physControls.isAirborne:
                setMovementAnimation('walk')
    else:
        if not duckBody.physControls.isAirborne:
            if movingNeutral == False:
                setMovementAnimation('neutral')
    return Task.cont
 
base.taskMgr.add(handleMovement, 'controlManager')
 
def collisionsOn():
    duckBody.physControls.setCollisionsActive(True)
    duckBody.physControls.isAirborne = True
def collisionsOff():
    duckBody.physControls.setCollisionsActive(False)
    duckBody.physControls.isAirborne = True
def toggleCollisions():
    if duckBody.physControls.getCollisionsActive():
        duckBody.physControls.setCollisionsActive(False)
        duckBody.physControls.isAirborne = True
    else:
        duckBody.physControls.setCollisionsActive(True)
        duckBody.physControls.isAirborne = True
base.accept('f1', toggleCollisions)
duckBody.collisionsOn = collisionsOn
duckBody.collisionsOff = collisionsOff
duckBody.toggleCollisions = toggleCollisions
 
localAvatar = duckBody
base.localAvatar = localAvatar
 
loadCogishAscent = True
if len(argv) > 1:
    filepath = argv[1]
    if '.' in filepath:
        try:
            execfile(filepath)
            loadCogishAscent = False
        except Exception, e:
            loadCogishAscent = False
            print e
    else:
        loadCogishAscent = True
 
if loadCogishAscent == True:
 
    onScreenDebug.add('Loaded Minigame', 'Escape from Castle Cogenstien')
 
    environ = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    environ.reparentTo(render)
    environ.setPos(25,-150,0)
    environ.setHpr(0,0,0)
    environ.setScale(1)
    environ = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    environ.reparentTo(render)
    environ.setPos(10,-135,0)
    environ.setHpr(0,0,0)
    environ.setScale(1)
    environ = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    environ.reparentTo(render)
    environ.setPos(-5,-120,0)
    environ.setHpr(0,0,0)
    environ.setScale(1)
    environ = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    environ.reparentTo(render)
    environ.setPos(-10,-80,-10)
    environ.setHpr(0,0,0)
    environ.setScale(10)
    environ = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    environ.reparentTo(render)
    environ.setPos(50,-80,-10)
    environ.setHpr(0,0,0)
    environ.setScale(10)
    environ = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    environ.reparentTo(render)
    environ.setPos(-40,-140,-10)
    environ.setHpr(0,0,0)
    environ.setScale(10)
    e = loader.loadModel("phase_9/models/cogHQ/Elevator.bam")
    e.reparentTo(render)
    e.setHpr(0,0,0)
    e.setPos(-5,-120,0)
    pandaPosInterval22 = e.posInterval(13,Point3(-5,-120,0),
    startPos=Point3(-5,-120,50))
    pandaPosInterval33 = e.posInterval(13,Point3(-5,-120,50),
    startPos=Point3(-5,-120,0))
    pandaHprInterval11 = e.hprInterval(3,Point3(0,0,0),
    startHpr=Point3(0, 0, 0))
    pandaHprInterval22 = e.hprInterval(3,Point3(0, 0, 0),
    startHpr=Point3(0, 0, 0))
    pandaPace = Sequence(pandaPosInterval22,
    pandaHprInterval11,
    pandaPosInterval33,
    pandaHprInterval22,
    name="pandaPace")
    pandaPace.loop()
    e.find('**/wall_back').removeNode()
    e.find('**/wall_front').removeNode()
    sell1 = loader.loadModel('phase_9/models/cogHQ/SelbotLegFactory.bam')
    sell1.reparentTo(render)
    sell1.setPos(-15,0,80)
    sell1.setHpr(90,0,0)
    sell1.setScale(1)
    sell1.setColor(0,0,3)
    environ = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    environ.reparentTo(render)
    environ.setPos(-10,20,30)
    environ.setHpr(0,45,0)
    environ.setScale(10)
    environ = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    environ.reparentTo(render)
    environ.setPos(-10,-30,50)
    environ.setHpr(0,0,0)
    environ.setScale(3)
    ceo = Actor({"head":"phase_12/models/char/bossbotBoss-head-zero.bam", \
    "torso":"phase_12/models/char/bossbotBoss-torso-zero.bam", \
    "legs":"phase_9/models/char/bossCog-legs-zero.bam"}, \
    {"head":{"walk":"phase_9/models/char/bossCog-head-Bb_neutral.bam", \
    "run":"phase_9/models/char/bossCog-head-Bb_neutral.bam"}, \
    "torso":{"walk":"phase_9/models/char/bossCog-torso-Bb_neutral.bam", \
    "run":"phase_9/models/char/bossCog-torso-Bb_neutral.bam"}, \
    "legs":{"walk":"phase_9/models/char/bossCog-legs-Bb_neutral.bam", \
    "run":"phase_9/models/char/bossCog-legs-Bb_neutral.bam"} \
    })
    ceo.attach("head", "torso", "joint34")
    ceo.attach("torso", "legs", "joint_legs")
    ceo.reparentTo(render)
    tread3 = loader.loadModel("phase_9/models/char/bossCog-treads.bam")
    rear4 = ceo.find('**/joint_axle')
    tread3.reparentTo(rear4)
    ceo.setPos(-180,21,83.5)
    ceo.loop("walk")
    ceo.setHpr(90,0,0)
    environ = loader.loadModel("phase_4/models/minigames/toonblitz_game_arrow.bam")
    environ.reparentTo(render)
    environ.setPos(-125,21,84)
    environ.setHpr(90,0,0)
    environ.setScale(3)
    environ = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    environ.reparentTo(render)
    environ.setPos(-267,10,83.5)
    environ.setHpr(0,0,0)
    environ.setScale(3)
    crate1 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate1.reparentTo(render)
    crate1.setPos(-390,155,98)
    crate1.setHpr(0,0,0)
    crate1.setScale(3)
    crate2 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate2.reparentTo(render)
    crate2.setPos(-350,220,99)
    crate2.setHpr(0,0,0)
    crate2.setScale(0.5)
    crate3 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate3.reparentTo(render)
    crate3.setPos(-350,230,100)
    crate3.setHpr(0,0,0)
    crate3.setScale(0.4)
    crate4 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate4.reparentTo(render)
    crate4.setPos(-340,240,101)
    crate4.setHpr(0,0,0)
    crate4.setScale(0.3)
    paint1 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint1.reparentTo(render)
    paint1.setPos(-340,260,101)
    paint1.setHpr(0,0,0)
    paint1.setScale(2.5)
    paint2 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint2.reparentTo(render)
    paint2.setPos(-345,330,102)
    paint2.setHpr(0,0,0)
    paint2.setScale(0.5)
    paint3 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint3.reparentTo(render)
    paint3.setPos(-345,325,105)
    paint3.setHpr(0,0,0)
    paint3.setScale(0.5)
    paint4 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint4.reparentTo(render)
    paint4.setPos(-345,320,108)
    paint4.setHpr(0,0,0)
    paint4.setScale(0.5)
    paint5 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint5.reparentTo(render)
    paint5.setPos(-345,315,111)
    paint5.setHpr(0,0,0)
    paint5.setScale(0.5)
    paint6 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint6.reparentTo(render)
    paint6.setPos(-345,310,114)
    paint6.setHpr(0,0,0)
    paint6.setScale(0.5)
    paint7 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint7.reparentTo(render)
    paint7.setPos(-345,305,117)
    paint7.setHpr(0,0,0)
    paint7.setScale(0.5)
    paint8 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint8.reparentTo(render)
    paint8.setPos(-345,300,120)
    paint8.setHpr(0,0,0)
    paint8.setScale(0.5)
    paint9 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint9.reparentTo(render)
    paint9.setPos(-345,290,125)
    paint9.setHpr(0,0,0)
    paint9.setScale(1)
    paint10 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint10.reparentTo(render)
    paint10.setPos(-345,280,130)
    paint10.setHpr(0,0,0)
    paint10.setScale(1)
    paint11 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint11.reparentTo(render)
    paint11.setPos(-345,270,135)
    paint11.setHpr(0,0,0)
    paint11.setScale(1)
    paint12 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint12.reparentTo(render)
    paint12.setPos(-345,260,140)
    paint12.setHpr(0,0,0)
    paint12.setScale(1)
    paint13 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint13.reparentTo(render)
    paint13.setPos(-345,250,145)
    paint13.setHpr(0,0,0)
    paint13.setScale(1)
    paint14 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint14.reparentTo(render)
    paint14.setPos(-350,260,145)
    paint14.setHpr(0,0,0)
    paint14.setScale(1)
    paint15 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint15.reparentTo(render)
    paint15.setPos(-345,240,145)
    paint15.setHpr(0,0,0)
    paint15.setScale(1)
    paint16 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint16.reparentTo(render)
    paint16.setPos(-345,230,145)
    paint16.setHpr(0,0,0)
    paint16.setScale(1)
    paint17 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint17.reparentTo(render)
    paint17.setPos(-345,220,145)
    paint17.setHpr(0,0,0)
    paint17.setScale(1)
    paint18 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint18.reparentTo(render)
    paint18.setPos(-345,210,145)
    paint18.setHpr(0,0,0)
    paint18.setScale(1)
    paint19 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint19.reparentTo(render)
    paint19.setPos(-345,200,145)
    paint19.setHpr(0,0,0)
    paint19.setScale(1)
    paint20 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint20.reparentTo(render)
    paint20.setPos(-345,190,145)
    paint20.setHpr(0,0,0)
    paint20.setScale(1)
    paint21 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint21.reparentTo(render)
    paint21.setPos(-345,180,145)
    paint21.setHpr(0,0,0)
    paint21.setScale(1)
    paint22 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint22.reparentTo(render)
    paint22.setPos(-345,170,145)
    paint22.setHpr(0,0,0)
    paint22.setScale(1)
    paint23 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint23.reparentTo(render)
    paint23.setPos(-355,160,145)
    paint23.setHpr(0,0,0)
    paint23.setScale(1)
    paint24 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint24.reparentTo(render)
    paint24.setPos(-365,150,145)
    paint24.setHpr(0,0,0)
    paint24.setScale(1)
    crate5 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate5.reparentTo(render)
    crate5.setPos(-365,120,120)
    crate5.setHpr(0,0,0)
    crate5.setScale(10)
    sign1 = loader.loadModel("phase_4/models/minigames/toonblitz_game_arrow.bam")
    sign1.reparentTo(render)
    sign1.setPos(-365,150,145)
    sign1.setHpr(0,0,0)
    sign1.setScale(1)
    crate6 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate6.reparentTo(render)
    crate6.setPos(-500,0,90)
    crate6.setHpr(0,0,0)
    crate6.setScale(5)
    crate7 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate7.reparentTo(render)
    crate7.setPos(-467,0,90)
    crate7.setHpr(0,0,0)
    crate7.setScale(5)
    crate8 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate8.reparentTo(render)
    crate8.setPos(-467,-130,90)
    crate8.setHpr(0,0,0)
    crate8.setScale(5)
    crate9 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate9.reparentTo(render)
    crate9.setPos(-570,-500,80)
    crate9.setHpr(0,0,0)
    crate9.setScale(5)
    paint25 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint25.reparentTo(render)
    paint25.setPos(-610,-600,91)
    paint25.setHpr(0,0,0)
    paint25.setScale(0.05)
    paint26 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint26.reparentTo(render)
    paint26.setPos(-610,-650,93)
    paint26.setHpr(0,0,0)
    paint26.setScale(0.5)
    paint27 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint27.reparentTo(render)
    paint27.setPos(-610,-640,98)
    paint27.setHpr(0,0,0)
    paint27.setScale(0.5)
    paint28 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint28.reparentTo(render)
    paint28.setPos(-610,-630,103)
    paint28.setHpr(0,0,0)
    paint28.setScale(0.5)
    paint29 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint29.reparentTo(render)
    paint29.setPos(-610,-620,108)
    paint29.setHpr(0,0,0)
    paint29.setScale(0.5)
    crate10 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate10.reparentTo(render)
    crate10.setPos(-540,-600,80)
    crate10.setHpr(0,0,0)
    crate10.setScale(10)
    crate11 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate11.reparentTo(render)
    crate11.setPos(-267,5,80)
    crate11.setHpr(0,45,0)
    crate11.setScale(3)
    crate12 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate12.reparentTo(render)
    crate12.setPos(-273,20,75)
    crate12.setHpr(0,0,0)
    crate12.setScale(3)
    mgr = loader.loadModel("phase_10/models/cogHQ/CBMetalCrate2.bam")
    mgr.reparentTo(render)
    mgr.setPos(-270,150,87)
    mgr.setHpr(0,0,0)
    mgr.setScale(5)
    mgr.setColor(3,0,0)
    pandaHprInterval1 = mgr.hprInterval(3,Point3(0,0,0),
    startHpr=Point3(359, 359, 359))
    pandaHprInterval2 = mgr.hprInterval(3,Point3(359, 359, 359),
    startHpr=Point3(0, 0, 0))
    maryspin = Sequence(pandaHprInterval1,
    name="maryspin")
    maryspin.loop()
    mail1 = Actor("phase_5/models/char/tt_r_ara_ttc_mailbox.bam",
    {"cheer":"phase_5/models/char/tt_a_ara_ttc_mailbox_fightCheer.bam"})
    mail1.reparentTo(render)
    mail1.loop("cheer")
    mail1.setPos(-510,-250,145)
    mail1.setHpr(180,0,180)
    mail1.setScale(5)
    hydrant1 = Actor("phase_5/models/char/tt_r_ara_ttc_hydrant.bam",{"cheer":"phase_5/models/char/tt_a_ara_ttc_hydrant_fightCheer.bam"})
    hydrant1.reparentTo(render)
    hydrant1.loop("cheer")
    hydrant1.setPos(-510,-320,101.5)
    hydrant1.setHpr(0,0,0)
    hydrant1.setScale(10)
    crate13 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate13.reparentTo(render)
    crate13.setPos(-267,10,83.5)
    crate13.setHpr(0,0,0)
    crate13.setScale(3)
    paint30 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint30.reparentTo(render)
    paint30.setPos(-280,30,87)
    paint30.setHpr(0,0,0)
    paint30.setScale(1)
    paint31 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint31.reparentTo(render)
    paint31.setPos(-420,-20,142)
    paint31.setHpr(0,0,0)
    paint31.setScale(1)
    paint32 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint32.reparentTo(render)
    paint32.setPos(-420,-5,147)
    paint32.setHpr(0,0,0)
    paint32.setScale(1)
    paint33 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint33.reparentTo(render)
    paint33.setPos(-420,10,152)
    paint33.setHpr(0,0,0)
    paint33.setScale(1)
    paint34 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint34.reparentTo(render)
    paint34.setPos(-420,25,157)
    paint34.setHpr(0,0,0)
    paint34.setScale(1)
    paint35 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint35.reparentTo(render)
    paint35.setPos(-420,27,162)
    paint35.setHpr(0,0,0)
    paint35.setScale(1)
    paint36 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint36.reparentTo(render)
    paint36.setPos(-417,5,162)
    paint36.setHpr(0,315,0)
    paint36.setScale(0.5)
    paint37 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint37.reparentTo(render)
    paint37.setPos(-417,0,167)
    paint37.setHpr(0,315,0)
    paint37.setScale(0.5)
    paint38 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint38.reparentTo(render)
    paint38.setPos(-750,0,293)
    paint38.setHpr(0,0,0)
    paint38.setScale(1)
    paint39 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint39.reparentTo(render)
    paint39.setPos(-752,0,299)
    paint39.setHpr(0,0,0)
    paint39.setScale(1)
    paint40 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint40.reparentTo(render)
    paint40.setPos(-754,0,305)
    paint40.setHpr(0,0,0)
    paint40.setScale(1)
    paint41 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint41.reparentTo(render)
    paint41.setPos(-756,0,311)
    paint41.setHpr(0,0,0)
    paint41.setScale(1)
    paint42 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint42.reparentTo(render)
    paint42.setPos(-758,0,317)
    paint42.setHpr(0,0,0)
    paint42.setScale(1)
    paint43 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint43.reparentTo(render)
    paint43.setPos(-760,0,323)
    paint43.setHpr(0,0,0)
    paint43.setScale(1)
    paint44 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint44.reparentTo(render)
    paint44.setPos(-762,0,329)
    paint44.setHpr(0,0,0)
    paint44.setScale(1)
    cash1 = loader.loadModel('phase_10/models/cashbotHQ/ZONE31a.bam')
    cash1.reparentTo(render)
    cash1.setPos(-762,0,329)
    cash1.setHpr(0,0,0)
    cash1.setScale(1)
    cash2 = loader.loadModel('phase_10/models/cashbotHQ/connector_7cubeL2.bam')
    cash2.reparentTo(render)
    cash2.setPos(-762,-30,329)
    cash2.setHpr(0,0,0)
    cash2.setScale(1)
    cash3 = loader.loadModel('phase_10/models/cashbotHQ/ZONE15a.bam')
    cash3.reparentTo(render)
    cash3.setPos(-747.5,-112,324)
    cash3.setHpr(90,0,0)
    cash3.setScale(1)
    train1 = loader.loadModel('phase_10/models/cogHQ/CashBotTankCar.bam')
    train1.reparentTo(render)
    train1.setPos(-770.5,-120,344)
    train1.setHpr(10,190,10)
    train1.setScale(0.5)
    paint45 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint45.reparentTo(render)
    paint45.setPos(-765,-105,330)
    paint45.setHpr(0,0,80)
    paint45.setScale(1)
    cash4 = loader.loadModel('phase_10/models/cashbotHQ/ZONE08a.bam')
    cash4.reparentTo(render)
    cash4.setPos(-755,-223,324)
    cash4.setHpr(90,60,0)
    cash4.setScale(1)
    law1 = loader.loadModel('phase_11/models/lawbotHQ/LawbotCourtroom3.bam')
    law1.reparentTo(render)
    law1.setPos(-755,-223,330)
    law1.setHpr(0,0,0)
    law1.setScale(1)
    paint46 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint46.reparentTo(render)
    paint46.setPos(-780,-129,410)
    paint46.setHpr(0,0,280)
    paint46.setScale(2)
    paint47 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint47.reparentTo(render)
    paint47.setPos(-720,-150,425)
    paint47.setHpr(0,0,0)
    paint47.setScale(3,3,0.001)
    paint47.setColor(3,0,0)
    paint48 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint48.reparentTo(render)
    paint48.setPos(-720,-240,420)
    paint48.setHpr(0,0,90)
    paint48.setScale(1,1,0.001)
    paint48.setColor(0,3,0)
    paint49 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint49.reparentTo(render)
    paint49.setPos(-710,-240,415)
    paint49.setHpr(0,0,0)
    paint49.setScale(1,10,1)
    ceo2 = Actor({"head":"phase_12/models/char/bossbotBoss-head-zero.bam", \
    "torso":"phase_12/models/char/bossbotBoss-torso-zero.bam", \
    "legs":"phase_9/models/char/bossCog-legs-zero.bam"}, \
    {"head":{"walk":"phase_9/models/char/bossCog-head-Bb_neutral.bam", \
    "run":"phase_9/models/char/bossCog-head-Bb_neutral.bam"}, \
    "torso":{"walk":"phase_9/models/char/bossCog-torso-Bb_neutral.bam", \
    "run":"phase_9/models/char/bossCog-torso-Bb_neutral.bam"}, \
    "legs":{"walk":"phase_9/models/char/bossCog-legs-Bb_neutral.bam", \
    "run":"phase_9/models/char/bossCog-legs-Bb_neutral.bam"} \
    })
    ceo2.attach("head", "torso", "joint34")
    ceo2.attach("torso", "legs", "joint_legs")
    ceo2.reparentTo(render)
    tread3 = loader.loadModel("phase_9/models/char/bossCog-treads.bam")
    rear4 = ceo2.find('**/joint_axle')
    tread3.reparentTo(rear4)
    ceo2.setPos(-760,-280,402)
    ceo2.loop("walk")
    ceo2.setHpr(180,0,0)
    ceo2.setScale(2.5,2.5,2.5)
    ceo2.setColor(3,0,0)
    crate14 = loader.loadModel('phase_10/models/cogHQ/CBMetalCrate2.bam')
    crate14.reparentTo(render)
    crate14.setPos(-760,-330,400)
    crate14.setHpr(0,0,0)
    crate14.setScale(10,0.1,10)
    law2 = loader.loadModel('phase_11/models/lawbotHQ/LB_DA_Lobby.bam')
    law2.reparentTo(render)
    law2.setPos(-760,-300,365)
    law2.setHpr(180,0,0)
    law2.setScale(1)
    metal1 = loader.loadModel('phase_11/models/lawbotHQ/LB_metal_crate.bam')
    metal1.reparentTo(render)
    metal1.setPos(-855,-380,412)
    metal1.setHpr(180,0,0)
    metal1.setScale(3,3,2)
    metal2 = loader.loadModel('phase_11/models/lawbotHQ/LB_metal_crate.bam')
    metal2.reparentTo(render)
    metal2.setPos(-897,-385,412)
    metal2.setHpr(180,0,0)
    metal2.setScale(3,1,2)
    metal3 = loader.loadModel('phase_11/models/lawbotHQ/LB_metal_crate.bam')
    metal3.reparentTo(render)
    metal3.setPos(-939,-375,412)
    metal3.setHpr(180,0,0)
    metal3.setScale(3,5,2)
    metal4 = loader.loadModel('phase_11/models/lawbotHQ/LB_metal_crate.bam')
    metal4.reparentTo(render)
    metal4.setPos(-855,-390,410)
    metal4.setHpr(180,0,0)
    metal4.setScale(3,1,2)
    paint50 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint50.reparentTo(render)
    paint50.setPos(-875,-380,430)
    paint50.setHpr(0,280,0)
    paint50.setScale(1)
    paint50.setColor(3,0,3)
    metal5 = loader.loadModel('phase_11/models/lawbotHQ/LB_metal_crate.bam')
    metal5.reparentTo(render)
    metal5.setPos(-916,-395,412)
    metal5.setHpr(180,0,0)
    metal5.setScale(7,2,2)
    paint51 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam')
    paint51.reparentTo(render)
    paint51.setPos(-950,-380,490)
    paint51.setHpr(0,279,0)
    paint51.setScale(1,10,1)
    paint51.setColor(3,3,0)
    boss1 = loader.loadModel('phase_12/models/bossbotHQ/CogGolfHub.bam')
    boss1.reparentTo(render)
    boss1.setPos(-1020,-550,550)
    boss1.setHpr(180,0,0)
    boss1.setScale(1)
 
else:
 
    onScreenDebug.add('Loaded Land', argv[1])
 
localAvatar.physControls.placeOnFloor()
 
onScreenDebug.enabled = True
 
def updateOnScreenDebug(task):
 
    onScreenDebug.add('Avatar Position', localAvatar.getPos())
    onScreenDebug.add('Avatar Angle', localAvatar.getHpr())
 
    return Task.cont
 
base.taskMgr.add(updateOnScreenDebug, 'UpdateOSD')
 
run()
