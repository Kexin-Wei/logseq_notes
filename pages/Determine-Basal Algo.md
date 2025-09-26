# Refer
- https://openaps.readthedocs.io/en/latest/docs/While%20You%20Wait%20For%20Gear/Understand-determine-basal.html
  
  ```python
  [
  "autosens_max", # autosens calculates a 'ratio'  
  "autosens_min", # see above  
  "basalprofile", # not sure  
  "battery_indicates_battery_change", # irrelevant  
  "bg_targets", #target BG i suppose  
  "carb_ratio", # one single frac  
  "carb_ratios", #not quite sure whaat the stuff inside means  
  "current_basal", #  
  "current_basal_safety_multiplier", # there are some explanations in the docs about the safety  
  "curve", # probably used for prediction  
  
  
  
  
  "dia", # no idea  
  "enableSMB_after_carbs", # smb is supermicrobolus and is explained in the reference design doc  
  "enableSMB_with_COB", # same  
  "enableSMB_with_bolus", # same  
  "enableSMB_with_temptarget", #same  
  "enableUAM", #not sure  
  "insulinPeakTime", #not sure  
  "isfProfile",  
  "maxCOB", # cob is carbs on board i think  
  "maxSMBBasalMinutes",  
  "max_basal", # safety feature is suppose  
  "max_bg", # probably safety feature to use max bg for calc  
  "max_daily_basal", # same as above  
  "max_daily_safety_multiplier", # same as above  
  "max_iob", # same as above  
  "min_5m_carbimpact", # not sure  
  "min_bg", # same as above but min  
  "out_units", # units  
  "prime_indicates_pump_site_change", # probably irrelevant  
  "remainingCarbsCap", # probably like max COB  
  "rewind_indicates_cartridge_change", # probably irrelevant  
  "sens", # insulin sensitivity i assume  
  "useCustomPeakTime" # not sure  
  ]
  ```
  
  in the autosens.json, there's only a ratio, basal profile i suppose has the  history of basal injections
  pumphistory records different pump event types, which i'm not sure what they mean
  
  ```
  [  {    "timestamp": "2018-06-02T00:05:00-07:00",    "_type": "Bolus",    "amount": 0.4,    "duration": 0  },  {    "timestamp": "2018-06-02T00:00:00-07:00",    "_type": "TempBasalDuration",    "duration (min)": 14400  },  {    "timestamp": "2018-06-02T00:00:00-07:00",    "_type": "TempBasal",    "temp": "absolute",    "rate": 0  }] 
  ```
- # list of parameters
  ```json
  {
  "carb_ratio": 10,
  "sens": 50,
  "dia": 6,
  "max_bg": 120,
  "min_bg": 120,
  "max_basal": 4.0,
  "current_basal": 1.0,
  "max_iob": 6.0,
  "maxCOB": 100,
  "max_daily_safety_multiplier": 4,
  "current_basal_safety_multiplier": 5,
  "autosens_max": 2,
  "autosens_min": 0.5,
  "autosens": False,
  "enableSMB_with_bolus": True,
  "enableSMB_with_COB": True,
  "curve": "rapid-acting",
  "insulinPeakTime": 75,
  "basalprofile": [
  {"minutes": 0, "rate": 1.0, "start": "00:00:00", "i": 0},
  {"minutes": 360, "rate": 0.8, "start": "06:00:00", "i": 1},
  {"minutes": 720, "rate": 1.2, "start": "12:00:00", "i": 2},
  {"minutes": 1080, "rate": 0.9, "start": "18:00:00", "i": 3},
  ],
  "isfProfile": {
  "first": 1,
  "sensitivities": [
  	{"endOffset": 1440, "offset": 0, "x": 0, "sensitivity": 50, "start": "00:00:00", "i": 0}
  ],
  "user_preferred_units": "mg/dL",
  "units": "mg/dL",
  },
  }
  ```
- # determin-basal-test.js
  ```json
  {
  "max_iob":2.5,
  "dia":3,
  "type":"current",
  "current_basal":0.9,
  "max_daily_basal":1.3,
  "max_basal":3.5,
  "max_bg":120,
  "min_bg":110,
  "sens":40,
  "carb_ratio":10
  }
  ```
- # following [openaps document](https://openaps.readthedocs.io/en/latest/docs/While%20You%20Wait%20For%20Gear/preferences-and-safety-settings.html)
  no exercise mode, only oref0 (oref1 excluded)
- You should have run oref0 (basic OpenAPS looping) for more than two weeks, and be very aware of all the types of situations in which your rig might fail, before you enable oref1-related features.
  ```json
  { 
  // commonly adjusted
  "max_iob": 0,
  "max_daily_safety_multiplier": 3,
  "current_basal_safety_multiplier": 4,
  "autosens_max": 1.2,
  "autosens_min": 0.7,
  "rewind_resets_autosens": true,
  "unsuspend_if_no_temp": true, // change to false
  "curve": "rapid-acting",
  // no need to adjust
  "adv_target_adjustments": true,
  // oref1, false by default
  "enableSMB_after_carbs": false, 
  "enableSMB_with_COB": false,
  "enableSMB_with_temptarget": false,
  "enableUAM": false,
  }
  ```
  
  | Variable                          | Instruction                                                                                                                                 |
  | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
  | max_iob                           | 0, A good rule of thumb to start out with is for `max_iob` to be no more than 3 times your highest basal rate PLUS your typical meal bolus. |
  | max_daily_safety_multiplier       | 3                                                                                                                                           |
  | current_basal_safety_multiplier   | 4                                                                                                                                           |
  | autosens_max                      | 20% =>1.2                                                                                                                                   |
  | autosens_min                      | ? (0.7)                                                                                                                                     |
  | rewind_resets_autosens            | true                                                                                                                                        |
  | unsuspend_if_no_temp              | false                                                                                                                                       |
  | carbsReqThreshold                 | 1                                                                                                                                           |
  | curve                             | “rapid-acting”                                                                                                                              |
  | useCustomPeakTime                 | false                                                                                                                                       |
  | insulinPeakTime                   | 75 for rapid acting                                                                                                                         |
  |                                   |                                                                                                                                             |
  | Pushover                          |                                                                                                                                             |
  | pushover_snooze                   | 15                                                                                                                                          |
  | pushover_only                     | "carb"                                                                                                                                      |
  | pushover_sound                    | "none"                                                                                                                                      |
  | pushover_priority                 | 0                                                                                                                                           |
  | pushover_retry                    | 60                                                                                                                                          |
  | pushover_expire                   | 600                                                                                                                                         |
  |                                   |                                                                                                                                             |
  | No needed to adjust               |                                                                                                                                             |
  | autosens_adjust_targets           |                                                                                                                                             |
  | adv_target_adjustments            |                                                                                                                                             |
  | skip_neutral_temps                |                                                                                                                                             |
  | bolussnooze_dia_divisor           |                                                                                                                                             |
  | min_5m_carbimpact                 |                                                                                                                                             |
  | carbratio_adjustmentratio         |                                                                                                                                             |
  | maxCOB                            |                                                                                                                                             |
  | remainingCarbsCap                 |                                                                                                                                             |
  | remainingCarbsFraction            |                                                                                                                                             |
  | autotune_isf_adjustmentFraction   |                                                                                                                                             |
  | offline_hotspot                   |                                                                                                                                             |
  | wide_bg_target_range              |                                                                                                                                             |
  | A52_risk_enable                   |                                                                                                                                             |
  | rewind_indicates_cartridge_change |                                                                                                                                             |
  | prime_indicates_pump_site_change  |                                                                                                                                             |
  | battery_indicates_battery_change  |                                                                                                                                             |
  |                                   |                                                                                                                                             |
  | oref1-related                     |                                                                                                                                             |
  | enableSMB_with_COB                |                                                                                                                                             |
  | enableSMB_with_temptarget         |                                                                                                                                             |
  | enableUAM                         |                                                                                                                                             |
  | enableSMB_always                  |                                                                                                                                             |
  | enableSMB_after_carbs             |                                                                                                                                             |
  | allowSMB_with_high_temptarget<br> |                                                                                                                                             |
  | maxSMBBasalMinutes                |                                                                                                                                             |
  | maxUAMSMBBasalMinutes             |                                                                                                                                             |
  
  ![[Pasted image 20250724172443.png]]
- # in \profile\index.js
  ```javascript
  function defaults ( ) {
  return /* profile */ {
    max_iob: 0 // if max_iob is not provided, will default to zero 
    , max_daily_safety_multiplier: 3
    , current_basal_safety_multiplier: 4
    , autosens_max: 1.2
    , autosens_min: 0.7
    , rewind_resets_autosens: true // reset autosensitivity to neutral for awhile after each pump rewind
    // , autosens_adjust_targets: false // when autosens detects sensitivity/resistance, also adjust BG target accordingly
    , high_temptarget_raises_sensitivity: false // raise sensitivity for temptargets >= 101.  synonym for exercise_mode
    , low_temptarget_lowers_sensitivity: false // lower sensitivity for temptargets <= 99.
    , sensitivity_raises_target: true // raise BG target when autosens detects sensitivity
    , resistance_lowers_target: false // lower BG target when autosens detects resistance
    , exercise_mode: false // when true, > 100 mg/dL high temp target adjusts sensitivityRatio for exercise_mode. This majorly changes the behavior of high temp targets from before. synonmym for high_temptarget_raises_sensitivity
    , half_basal_exercise_target: 160 // when temptarget is 160 mg/dL *and* exercise_mode=true, run 50% basal at this level (120 = 75%; 140 = 60%)
    // create maxCOB and default it to 120 because that's the most a typical body can absorb over 4 hours.
    // (If someone enters more carbs or stacks more; OpenAPS will just truncate dosing based on 120.
    // Essentially, this just limits AMA/SMB as a safety cap against excessive COB entry)
    , maxCOB: 120
    , skip_neutral_temps: false // if true, don't set neutral temps
    , unsuspend_if_no_temp: false // if true, pump will un-suspend after a zero temp finishes
    , bolussnooze_dia_divisor: 2 // bolus snooze decays after 1/2 of DIA
    , min_5m_carbimpact: 8 // mg/dL per 5m (8 mg/dL/5m corresponds to 24g/hr at a CSF of 4 mg/dL/g (x/5*60/4))
    , autotune_isf_adjustmentFraction: 1.0 // keep autotune ISF closer to pump ISF via a weighted average of fullNewISF and pumpISF.  1.0 allows full adjustment, 0 is no adjustment from pump ISF.
    , remainingCarbsFraction: 1.0 // fraction of carbs we'll assume will absorb over 4h if we don't yet see carb absorption
    , remainingCarbsCap: 90 // max carbs we'll assume will absorb over 4h if we don't yet see carb absorption
    // WARNING: use SMB with caution: it can and will automatically bolus up to max_iob worth of extra insulin
    , enableUAM: true // enable detection of unannounced meal carb absorption
    , A52_risk_enable: false
    , enableSMB_with_COB: false // enable supermicrobolus while COB is positive
    , enableSMB_with_temptarget: false // enable supermicrobolus for eating soon temp targets
    // *** WARNING *** DO NOT USE enableSMB_always or enableSMB_after_carbs with Libre or similar
    // LimiTTer, etc. do not properly filter out high-noise SGVs.  xDrip+ builds greater than or equal to
    // version number d8e-7097-2018-01-22 provide proper noise values, so that oref0 can ignore high noise
    // readings, and can temporarily raise the BG target when sensor readings have medium noise,
    // resulting in appropriate SMB behaviour.  Older versions of xDrip+ should not be used with enableSMB_always.
    // Using SMB overnight with such data sources risks causing a dangerous overdose of insulin
    // if the CGM sensor reads falsely high and doesn't come down as actual BG does
    , enableSMB_always: false // always enable supermicrobolus (unless disabled by high temptarget)
    , enableSMB_after_carbs: false // enable supermicrobolus for 6h after carbs, even with 0 COB
    , enableSMB_high_bg: false // enable SMBs when a high BG is detected, based on the high BG target (adjusted or profile)
    , enableSMB_high_bg_target: 110 // set the value enableSMB_high_bg will compare against to enable SMB. If BG > than this value, SMBs should enable.
    // *** WARNING *** DO NOT USE enableSMB_always or enableSMB_after_carbs with Libre or similar.
    , allowSMB_with_high_temptarget: false // allow supermicrobolus (if otherwise enabled) even with high temp targets
    , maxSMBBasalMinutes: 30 // maximum minutes of basal that can be delivered as a single SMB with uncovered COB
    , maxUAMSMBBasalMinutes: 30 // maximum minutes of basal that can be delivered as a single SMB when IOB exceeds COB
    , SMBInterval: 3 // minimum interval between SMBs, in minutes.
    , bolus_increment: 0.1 // minimum bolus that can be delivered as an SMB
    , maxDelta_bg_threshold: 0.2 // maximum change in bg to use SMB, above that will disable SMB
    , curve: "rapid-acting" // change this to "ultra-rapid" for Fiasp, or "bilinear" for old curve
    , useCustomPeakTime: false // allows changing insulinPeakTime
    , insulinPeakTime: 75 // number of minutes after a bolus activity peaks.  defaults to 55m for Fiasp if useCustomPeakTime: false
    , carbsReqThreshold: 1 // grams of carbsReq to trigger a pushover
    , offline_hotspot: false // enabled an offline-only local wifi hotspot if no Internet available
    , noisyCGMTargetMultiplier: 1.3 // increase target by this amount when looping off raw/noisy CGM data
    , suspend_zeros_iob: true // recognize pump suspends as non insulin delivery events
    // send the glucose data to the pump emulating an enlite sensor. This allows to setup high / low warnings when offline and see trend.
    // To enable this feature, enable the sensor, set a sensor with id 0000000, go to start sensor and press find lost sensor.
    , enableEnliteBgproxy: false
    // TODO: make maxRaw a preference here usable by oref0-raw in myopenaps-cgm-loop
    //, maxRaw: 200 // highest raw/noisy CGM value considered safe to use for looping
    , calc_glucose_noise: false
    , target_bg: false // set to an integer value in mg/dL to override pump min_bg
    , edison_battery_shutdown_voltage: 3050
    , pi_battery_shutdown_percent: 2
  }
  }
  ```