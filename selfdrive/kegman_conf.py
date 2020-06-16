import json
import os

class kegman_conf():
  def __init__(self, CP=None):
    self.conf = self.read_config()
    if CP is not None:
      self.init_config(CP)

  def init_config(self, CP):
    write_conf = False
    if self.conf['tuneGernby'] != "1":
      self.conf['tuneGernby'] = str(1)
      write_conf = True
	
    # only fetch Kp, Ki, Kf sR and sRC from interface.py if it's a PID controlled car
    if CP.lateralTuning.which() == 'indi':
      if self.conf['outerLG'] == "-1":
        self.conf['outerLG'] = str(round(CP.lateralTuning.indi.outerLoopGain,2))
        write_conf = True
      if self.conf['innerLG'] == "-1":
        self.conf['innerLG'] = str(round(CP.lateralTuning.indi.innerLoopGain,2))
        write_conf = True
      if self.conf['timeConst'] == "-1":
        self.conf['timeConst'] = str(round(CP.lateralTuning.indi.timeConstant,2))
        write_conf = True
      if self.conf['actEffect'] == "-1":
        self.conf['actEffect'] = str(round(CP.lateralTuning.indi.actuatorEffectiveness,2))
        write_conf = True
    
    if self.conf['steerRatio'] == "-1":
      self.conf['steerRatio'] = str(round(CP.steerRatio,3))
      write_conf = True
    
    if self.conf['steerRateCost'] == "-1":
      self.conf['steerRateCost'] = str(round(CP.steerRateCost,3))
      write_conf = True

    if write_conf:
      self.write_config(self.config)

  def read_config(self):
    self.element_updated = False

    if os.path.isfile('/data/kegman.json'):
      with open('/data/kegman.json', 'r') as f:
        self.config = json.load(f)

      if "cameraOffset" not in self.config:
        self.config.update({"cameraOffset":"0.06"})
        self.element_updated = True

      if "battPercOff" not in self.config:
        self.config.update({"battPercOff":"100"})
        self.config.update({"carVoltageMinEonShutdown":"11800"})
        self.config.update({"brakeStoppingTarget":"0.25"})
        self.element_updated = True

      if "tuneGernby" not in self.config:
        self.config.update({"tuneGernby":"1"})
        self.element_updated = True

      if "outerLG" not in self.config:
        self.config.update({"outerLG":"-1"})
        self.config.update({"innerLG":"-1"})
        self.config.update({"timeConst":"-1"})
        self.config.update({"actEffect":"-1"})
        self.element_updated = True

      if "liveParams" not in self.config:
        self.config.update({"liveParams":"1"})
        self.element_updated = True
	
      if "steerRatio" not in self.config:
        self.config.update({"steerRatio":"-1"})
        self.config.update({"steerRateCost":"-1"})
        self.element_updated = True

      if "steerMax" not in self.config:
        self.config.update({"steerMax":"300"})
        self.element_updated = True

      if "deltaUp" not in self.config:
        self.config.update({"deltaUp":"3"})
        self.element_updated = True

      if "deltaDown" not in self.config:
        self.config.update({"deltaDown":"3"})
        self.element_updated = True
	
      if "leadDistance" not in self.config:
        self.config.update({"leadDistance":"5"})
        self.element_updated = True
	
      if "1barBP0" not in self.config:
        self.config.update({"1barBP0":"-0.1"})
        self.config.update({"1barBP1":"2.25"})
        self.config.update({"2barBP0":"-0.1"})
        self.config.update({"2barBP1":"2.5"})
        self.config.update({"3barBP0":"0.0"})
        self.config.update({"3barBP1":"3.0"})
        self.element_updated = True

      if "1barMax" not in self.config:
        self.config.update({"1barMax":"2.1"})
        self.config.update({"2barMax":"2.1"})
        self.config.update({"3barMax":"2.1"})
        self.element_updated = True
	
      if "1barHwy" not in self.config:
        self.config.update({"1barHwy":"0.4"})
        self.config.update({"2barHwy":"0.3"})
        self.config.update({"3barHwy":"0.1"})
        self.element_updated = True
	
      if "slowOnCurves" not in self.config:
        self.config.update({"slowOnCurves":"0"})
        self.element_updated = True
	
      if "sR_boost" not in self.config:
        self.config.update({"sR_boost":"0"})
        self.config.update({"sR_BP0":"0"})
        self.config.update({"sR_BP1":"0"})
        self.config.update({"sR_time":"0.2"})
        self.element_updated = True

      if "ALCnudgeLess" not in self.config:
        self.config.update({"ALCnudgeLess":"1"})
        self.config.update({"ALCminSpeed":"16.666667"})
        self.element_updated = True

      if "ALCtimer" not in self.config:
        self.config.update({"ALCtimer":"1.0"})
        self.element_updated = True

      if "CruiseDelta" not in self.config:
        self.config.update({"CruiseDelta":"8"})
        self.element_updated = True

      if "CruiseEnableMin" not in self.config:
        self.config.update({"CruiseEnableMin":"0"})
        self.element_updated = True

      if self.element_updated:
        print("updated")
        self.write_config(self.config)

    else:
      self.config = {"cameraOffset":"0.06", "lastTrMode":"1", "battChargeMin":"60", "battChargeMax":"70", \
                     "wheelTouchSeconds":"30000", "battPercOff":"100", "carVoltageMinEonShutdown":"11800", \
                     "brakeStoppingTarget":"0.25", "tuneGernby":"1", \
                     "outerLG":"-1", "innerLG":"-1", "timeConst":"-1", "actEffect":"-1", \
                     "liveParams":"1", "leadDistance":"5", "steerMax":"300", "deltaUp":"3", "deltaDown":"3", \
                     "1barBP0":"-0.1", "1barBP1":"2.25", "2barBP0":"-0.1", "2barBP1":"2.5", "3barBP0":"0.0", \
                     "3barBP1":"3.0", "1barMax":"2.1", "2barMax":"2.1", "3barMax":"2.1", \
                     "1barHwy":"0.4", "2barHwy":"0.3", "3barHwy":"0.1", \
                     "steerRatio":"-1", "steerRateCost":"-1", "slowOnCurves":"0", \
                     "sR_boost":"0", "sR_BP0":"0", "sR_BP1":"0", "sR_time":"0.2", \
                     "ALCnudgeLess":"1", "ALCminSpeed":"16.666667", "ALCtimer":"1.0", "CruiseDelta":"8", \
                     "CruiseEnableMin":"0"}


      self.write_config(self.config)
    return self.config

  def write_config(self, config):
    try:
      with open('/data/kegman.json', 'w') as f:
        json.dump(self.config, f, indent=2, sort_keys=True)
        os.chmod("/data/kegman.json", 0o764)
    except IOError:
      os.mkdir('/data')
      with open('/data/kegman.json', 'w') as f:
        json.dump(self.config, f, indent=2, sort_keys=True)
        os.chmod("/data/kegman.json", 0o764)
