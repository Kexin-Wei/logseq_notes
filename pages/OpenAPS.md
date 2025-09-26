- Reference:
	- [OpenAPS](https://openaps.org/reference-design/)
- [oref0/lib at master · openaps/oref0](https://github.com/openaps/oref0/tree/master/lib)
- [Welcome to OpenAPS’s documentation! — OpenAPS 0.0.0 documentation](https://openaps.readthedocs.io/en/latest/index.html)
- ## Algorithm Types
- oref0 : basic
	- [[Determine-Basal Algo]]
- oref0 +  AMA (Advanced Meal Assist)
- oref1 = oref0 + AMA + SMB (supermicroboluses)
- ## Oref0 Algorithm
- ### Logic
- To safely dose insulin based on data from a CGM, OpenAPS does not place undue, excess reliance on any single glucose measurement.
- Because new CGM measurements are received every 5 minutes, OpenAPS can continually recalculate the insulin dosing adjustments required to bring BG back to the target range.
- Error handling
	- Case 1
		- If the CGM provides erroneous data, such as from a dying sensor or a compression event (where someone is lying directly on the sensor and restricting blood flow), OpenAPS will react conservatively by withholding or slightly increasing insulin dosing.
		- If 5, 10, or 15 minutes later the new data from the CGM indicates that the temporary basal rate currently running is no longer appropriate, OpenAPS can simply cancel the temporary basal and return to the normally scheduled basal rate, or make other dosing adjustments if necessary.
	- Case 2
		- In addition, OpenAPS is designed to simply and safely fall back to the patient’s pre-programmed basal therapy whenever it receives conflicting information about what the appropriate course of action is (or when required information is missing).
		- if BG is predicted to eventually go low but is actually rising at that moment, OpenAPS can cancel any temporary basals and wait to see whether BG continues rising or begins to fall, and only then begin issuing the appropriate temporary basal commands.
- Suspend
	- Additionally, OpenAPS further ensures safety by falling back to traditional “low glucose suspend” behavior when current BG is below a configured threshold and falling or not rising fast enough.
- Constraint
	- OpenAPS oref0 cannot issue insulin boluses
	- maximum allowed temporary basal rate
- #### SMB
  https://www.diabettech.com/artificial-pancreas/understanding-smb-and-oref1/?cn-reloaded=1
- ### Code
  refer to [LoopinSight1](https://github.com/hpeuscher/loopinsight1)
  the profile should be 
  ```python
  base_profile = {
            "current_basal": current_basal,  # Current basal rate in U/h
            "sens": 50,  # Insulin Sensitivity Factor (ISF)
            "dia": 6,  # Duration of Insulin Action in hours
            "carb_ratio": 10,  # Carb Ratio (g/U)
            "max_iob": 6,  # Maximum insulin on board allowed
            "max_basal": 3.5,  # Maximum temporary basal rate in U/h
            "max_daily_basal": 3.5,  # Maximum daily basal rate in units per day
            "max_bg": 120,  # Upper target
            "min_bg": 120,  # Lower target
            "maxCOB": 120,  # Maximum carbs on board
            "isfProfile": {"sensitivities": [{"offset": 0, "sensitivity": 50}]},
            "min_5m_carbimpact": 12.0,  # Minimum carb absorption rate
            "type": "current",  # Profile type
        }
  ```
  codes are at [simglucose](https://github.com/ImperialGlobalSingapore/simglucose/blob/kexin/simglucose/controller/oref_zero.py) and [oref0](https://github.com/ImperialGlobalSingapore/oref0/blob/master/server.js)
  a better oref0 controller is in [[Oref0 Controller]]
- ### Tuning Parameters
  References:
  1. ISF ranges: PMC8957904 - "Diurnal Variation of Real-Life Insulin Sensitivity Factor Among Children and Adolescents"
	- Children <6y: ISF 1:150 (70-228), 6-12y: ISF 1:90 (50-140), 12-18y: ISF 1:50 (40-80)
	  2. ICR ranges: PMC5478012 - "Bolus Calculator Settings in Well-Controlled Prepubertal Children"
	- Children 2-4y: ICR 30 (13-42), 5-7y: ICR 20 (17-33), 8-10y: ICR 16 (10-60)
	- Adults typically ICR 1:10-15
	  3. DIA: PMC5478012 & diabetesnet.com
	- Children: 2-3.5 hours, Adults: 4-4.5 hours
	  4. Basal rates: PMC8186333 - "Initial Basal and Bolus Rates During Pump Treatment"
	- Children <7y: 0.69 U/kg/day, Adolescents: 0.90-0.97 U/kg/day
	  5. COB/carbimpact: AndroidAPS documentation & OpenAPS guidelines
		- Default maxCOB: 120g, min_5m_carbimpact: 8 mg/dL/5min
		  so these are the ai generated suggestion for the range of the parameters
- # Reference
  
  OpenAPS Reference Design – OpenAPS.org
  
  🌐 https://openaps.org/reference-design/
  🔗 https://app.web-highlights.com/page/680ee59e0511170f720d1bf1
  
  **Highlights & Notes**
  
  > To safely dose insulin based on data from a CGM, OpenAPS does not place undue, excess reliance on any single glucose measurement.
  
  > Because new CGM measurements are received every 5 minutes, OpenAPS can continually recalculate the insulin dosing adjustments required to bring BG back to the target range.
  
  > If the CGM provides erroneous data, such as from a dying sensor or a compression event (where someone is lying directly on the sensor and restricting blood flow), OpenAPS will react conservatively by withholding or slightly increasing insulin dosing. If 5, 10, or 15 minutes later the new data from the CGM indicates that the temporary basal rate currently running is no longer appropriate, OpenAPS can simply cancel the temporary basal and return to the normally scheduled basal rate, or make other dosing adjustments if necessary.
  
  > By ensuring that all available information, including BG level and trend information and insulin dosing history, is used in determining all insulin dosing decisions, OpenAPS can safely mitigate high blood sugar levels while minimizing hypoglycemia risk.
  
  > In addition, OpenAPS is designed to simply and safely fall back to the patient’s pre-programmed basal therapy whenever it receives conflicting information about what the appropriate course of action is (or when required information is missing). For example, if BG is predicted to eventually go low but is actually rising at that moment, OpenAPS can cancel any temporary basals and wait to see whether BG continues rising or begins to fall, and only then begin issuing the appropriate temporary basal commands.
  
  > Additionally, OpenAPS further ensures safety by falling back to traditional “low glucose suspend” behavior when current BG is below a configured threshold and falling or not rising fast enough.
  
  > OpenAPS oref0 cannot issue insulin boluses
  
  > To completely avoid this issue, oref0 instead relies solely on temporary basal commands. Repeatedly reissuing the same temporary basal command does not change the rate at which the pump infuses insulin;
  
  > maximum allowed temporary basal rate
  
  > This means that oref0 cannot be used to substitute for mealtime insulin boluses,
  
  > oref0 makes an estimate of how long the (bolus-wizard inputted or assumed) meal is expected to take to digest (or how long the BG excursion is expected to continue, if it’s something other than a meal).
  
  > operate completely autonomously, without requiring any specific interaction from the patien
  
  > If no boluses have been administered recently (see “Bolus Snooze” below), OpenAPS can then use the current CGM glucose reading to calculate an eventual BG estimate using simple bolus calculator math: current BG – (ISF * IOB) = eventual BG.
  
  > If current BG is below a configured threshold (defaulting to 30mg/dL below the target range), OpenAPS enters low glucose suspend mode, and simply continues to issue 30-minute temp basals to zero as long as BG is not rising. Otherwise, OpenAPS determines whether the eventual BG is projected to be above or below the target range, and makes note of whether the CGM glucose readings are currently rising or falling more than expected. It then decides on the appropriate course of action as follows:
  
  > if BG is rising but eventual BG is below target, cancel any temp basals.
  else, if BG is falling but eventual BG is above target, cancel any temp basals.
  else, if eventual BG is above target:
  calculate 30m temp required to get eventual BG down to target
  if required temp is > existing basal, issue the new high temp basal
  else, if BG is below target:
  calculate 30m temp required to get projected BG up to target
  if required temp is < existing basal, issue the new low temp basal
  if >30m @ 0 required, extend zero temp to 30m
  
  > The maximum temp basal rate is set on the pump, but for safety purposes OpenAPS will set a lower maximum temp basal rate if necessary, as the minimum of:
  
  The pump’s maximum temp basal rate
  3x the maximum daily scheduled basal rate
  4x the current scheduled basal rate
  
  > BG Impact” or BGI, which is simply the current insulin activity (first derivative of IOB) * insulin sensitivity.
  
  > To calculate the deviation, OpenAPS does exactly this comparison, between the 15m average delta in CGM readings and the predicted BGI.
  
  > It then applies that deviation as an adjustment to the eventual BG prediction.
  
  > By adjusting for BG deviations as described above, OpenAPS can avoid issuing low temp basals when BG is rising or remaining high after a meal, even without being informed about the fact that a meal has been consumed, or being provided a carbohydrate count.
  
  > To accomplish this, OpenAPS applies a “bolus snooze”, which causes OpenAPS to effectively go “hands off” as soon as a user executes a bolus,
  
  > The bolus snooze is currently implemented in advanced OpenAPS implementations by tracking bolus IOB (with an accelerated decay based on half the user’s normal DIA) separately from net IOB, and re-adding the BG impact of the bolus IOB (plus a small multiple) when deciding whether to set a low temporary basal.
  
  > This is accomplished through a “maximum IOB” setting, which instructs OpenAPS to never set high temp basals that would allow the net IOB to exceed the bolus IOB by more than a user-configured amount.
  
  > Advanced Meal Assist
  
  > it still requires the user to count and enter their carbs, and administer a meal bolus when the meal is eaten.
  
  > Despite these limitations, AMA is apparently still the most advanced postprandial insulin dosing algorithm in widespread human use, so there has been a lot of interest in seeing whether it could be extended to further reduce the burden on patients using it, and more completely automate insulin dosing in all situations.
  
  > oref1 algorithms is that oref1 makes use of small “supermicroboluses” (SMB) of insulin at mealtimes to more quickly (but safely) administer the insulin required to respond to blood sugar rises due to carb absorption.
  
  > As with oref0, the oref1 algorithm continuously recalculates the insulin required every 5 minutes based on CGM data and previous dosing, which means that oref1 will continually issue new supermicroboluses every 5 minutes, increasing or reducing their size as needed as long as CGM data indicates that blood glucose levels are rising (or not falling) relative to what would be expected from insulin alone.
  
  > To verify that it knows about all recent insulin dosing and that no bolus is currently being administered, oref1 first checks the pump’s reservoir level, then performs a full query of the pump’s treatment history, calculates the required insulin dose (noting the reservoir level the pump should be at when the dose is administered) and then checks the pump’s bolusing status and reservoir level again immediately before dosing.
  
  > In addition, all SMBs are limited to 1/3 of the insulin known to be required based on current information, such that even in the race condition where two rigs nearly simultaneously issue boluses, no more than 2/3 of the required insulin is delivered, and future SMBs can be adjusted to ensure that oref1 never delivers more insulin than it can safely withhold via a zero temp basal.
  
  > In some situations, a lack of BG or intermittent pump communications can prevent SMBs from being delivered promptly.  In such cases, oref1 attempts to fall back to oref0 + AMA behavior and set an appropriate high temp basal.