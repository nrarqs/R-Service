DATABASE = {
    "BMW E60 (2003-2010)": {
        "Diesel": {
            "520d": {"2005-2007": "M47D20 (163 HP)", "2007-2010": "N47D20 (177 HP)"},
            "525d": {"2004-2007": "M57D25 (177 HP)", "2007-2010": "M57D30 (197 HP)"},
            "530d": {"2003-2007": "M57D30 (218/231 HP)", "2007-2010": "M57D30 (235 HP)"},
            "535d": {"2004-2007": "M57D30 (272 HP)", "2007-2010": "M57D30 (286 HP)"}
        },
        "Petrol": {
            "520i": {"2003-2005": "M54B22 (170 HP)", "2005-2007": "N46B20 (156 HP)", "2007-2010": "N43B20 (170 HP)"},
            "523i": {"2005-2007": "N52B25 (177 HP)", "2007-2010": "N53B25 (190 HP)"},
            "525i": {"2003-2005": "M54B25 (192 HP)", "2005-2007": "N52B25 (218 HP)", "2007-2010": "N53B30 (218 HP)"},
            "530i": {"2003-2005": "M54B30 (231 HP)", "2005-2007": "N52B30 (258 HP)", "2007-2010": "N53B30 (272 HP)"},
            "545i": {"2003-2005": "N62B44 (333 HP)"},
            "550i": {"2005-2010": "N62B48 (367 HP)"},
            "M5": {"2005-2010": "S85B50 (507 HP)"}
        }
    },
    "Audi A6 C6 (2004-2011)": {
        "Diesel": {
            "2.0 TDI": {"2004-2008": "BLB/BRE (140 HP)", "2008-2011": "CAGB/CAHA (136/170 HP)"},
            "2.7 TDI": {"2004-2008": "BPP (180 HP)", "2008-2011": "CANA/CANB (190 HP)"},
            "3.0 TDI": {"2004-2008": "BMK/ASB (225/233 HP)", "2008-2011": "CDYA/CDYC (240 HP)"}
        },
        "Petrol": {
            "2.0 TFSI": {"2005-2011": "BPJ (170 HP)"},
            "2.4 V6": {"2004-2008": "BDW (177 HP)"},
            "2.8 FSI": {"2007-2011": "BDX/CCDA (190/210/220 HP)"},
            "3.0 TFSI": {"2008-2011": "CAJA (290 HP)"},
            "3.2 FSI": {"2004-2008": "AUK (256 HP)"},
            "4.2 V8": {"2004-2011": "BAT/BVJ (335/350 HP)"},
            "RS6": {"2008-2010": "BUH (580 HP)"}
        }
    },
    "Mercedes E-Class W211 (2002-2009)": {
        "Diesel": {
            "E200 CDI": {"2002-2006": "OM646 (122 HP)", "2006-2009": "OM646 (136 HP)"},
            "E220 CDI": {"2002-2006": "OM646 (150 HP)", "2006-2009": "OM646 (170 HP)"},
            "E270 CDI": {"2002-2005": "OM647 (177 HP)"},
            "E280 CDI": {"2004-2005": "OM648 (177 HP)", "2005-2009": "OM642 V6 (190 HP)"},
            "E320 CDI": {"2002-2005": "OM648 (204 HP)", "2005-2009": "OM642 V6 (224 HP)"},
            "E400/420 CDI": {"2003-2009": "OM628/629 V8 (260/314 HP)"}
        },
        "Petrol": {
            "E200 Kompressor": {"2002-2006": "M271 (163 HP)", "2006-2009": "M271 (184 HP)"},
            "E240/E280": {"2002-2005": "M112 (177 HP)", "2005-2009": "M272 (231 HP)"},
            "E320/E350": {"2002-2005": "M112 (224 HP)", "2005-2009": "M272 (272 HP)"},
            "E500": {"2002-2006": "M113 (306 HP)", "2006-2009": "M273 (388 HP)"},
            "E55 AMG": {"2002-2006": "M113 (476 HP)"},
            "E63 AMG": {"2006-2009": "M156 (514 HP)"}
        }
    }
}

DIAGNOSTIC_DATABASE = {
    # --- BMW E60 ---
    "N47D20": [ # 2.0d Facelift (177 HP)
        {"keywords": ["noise", "rattle", "chain", "metallic"], "issue": "Timing Chain", "solution": "Critical N47 failure. Chain is at the back. If rattling, replace immediately."},
        {"keywords": ["jerk", "hesitation", "egr", "carbon"], "issue": "Intake Carbon Buildup", "solution": "Check EGR and intake manifold for soot. Common on N47."}
    ],
    "M57D30": [ # 3.0d (218/231/235/286 HP)
        {"keywords": ["smoke", "oil", "breather", "turbo"], "issue": "PCV / Turbo Seals", "solution": "Check the crankcase breather. If clogged, it kills the turbo."},
        {"keywords": ["glow", "start", "module", "cold"], "issue": "Glow Plug Module", "solution": "Common Beru module failure. Causes rough cold starts."}
    ],
    "N52B25": [ # 2.5i Petrol (218 HP)
        {"keywords": ["oil", "consumption", "smoke"], "issue": "Valve Stem Seals", "solution": "N52 consumes oil due to CCV or valve seals. Expensive to fix."},
        {"keywords": ["tick", "lifter", "hydraulic"], "issue": "Hydraulic Lifters", "solution": "Known 'ticking' sound. Usually harmless but annoying; requires specific oil."}
    ],

    # --- AUDI A6 C6 ---
    "2.0 TDI": [ # BLB / BRE / CAHA
        {"keywords": ["oil pressure", "balance shaft", "red oil light"], "issue": "Oil Pump Drive", "solution": "The hex drive 'creion' wears out. Loss of oil pressure kills the engine instantly."},
        {"keywords": ["vibration", "clutch", "flywheel", "shaking"], "issue": "Dual Mass Flywheel", "solution": "Common on manual 2.0 TDI. If shaking at idle, replace clutch kit."}
    ],
    "3.0 TDI": [ # ASB / BMK / CDYA
        {"keywords": ["rattle", "start", "chain", "tensioner"], "issue": "Timing Chain Tensioners", "solution": "Upper tensioners fail. 1-2 sec rattle on start is the warning sign."},
        {"keywords": ["injector", "smoke", "haze", "idle"], "issue": "Piezo Injectors", "solution": "Early 3.0 TDI (BMK/ASB) had leaky injectors. Can melt pistons if not replaced."}
    ],
    "2.4 V6": [ # BDW (Petrol)
        {"keywords": ["cylinder", "bore", "scoring", "oil"], "issue": "Nikasil Bore Scoring", "solution": "Known issue for 2.4/3.2 FSI. If consuming massive oil, check cylinders with a camera."},
        {"keywords": ["chain", "misfire", "timing"], "issue": "Timing Chain Stretch", "solution": "Rear-mounted chains. Very expensive labor."}
    ],

    # --- MERCEDES W211 ---
    "OM646": [ # E220 CDI (150/170 HP)
        {"keywords": ["black death", "injector", "leak", "tar"], "issue": "Injector Copper Seals", "solution": "Fuel leaks around injectors and turns into hard carbon ('Black Death'). Clean and reseal."},
        {"keywords": ["thermostat", "temp", "cold"], "issue": "Thermostat Failure", "solution": "Engine won't reach 90C. Common on OM646, affects fuel economy."}
    ],
    "OM642": [ # E280/E320 CDI V6
        {"keywords": ["oil leak", "purple", "cooler", "v-shape"], "issue": "Oil Cooler Seals", "solution": "The seals in the 'V' leak oil onto the starter. 10-15h of labor to replace 10€ seals."},
        {"keywords": ["swirl", "m55", "limp", "actuator"], "issue": "Swirl Flap Motor", "solution": "Oil drips from the intake onto the M55 motor, shorting it out."}
    ],
    "M272": [ # E280/E350 Petrol
        {"keywords": ["balance shaft", "gear", "check engine", "timing"], "issue": "Balance Shaft Gear", "solution": "Premature wear of the gear teeth. Requires engine removal to fix."},
        {"keywords": ["manifold", "lever", "plastic", "tumble"], "issue": "Intake Manifold Lever", "solution": "Plastic lever breaks. Use an aluminum repair kit instead of a new manifold."}
    ]
}


NON_ENGINE_DATABASE = {
    "AUDI": [
        {"keywords": ["suspension", "arm", "multilink", "bolt", "stuck"], "issue": "Seized Upper Control Arm Bolt", "solution": "The 'Pinch Bolt' is notorious. Most shops refuse it. Requires heat, a press, or drilling. Don't touch unless you have a replacement bolt ready."},
        {"keywords": ["mmi", "screen", "black", "audio"], "issue": "MMI Fiber Optic Break", "solution": "If one module (Nav, CD, Amp) fails, the whole loop breaks. Use a bypass loop to find the culprit."}
    ],
    "BMW": [
        {"keywords": ["steering", "active", "angle", "heavy"], "issue": "Active Steering / SZL", "solution": "Optical sensor in the steering column gets dirty. Clean it before replacing the expensive rack."},
        {"keywords": ["water", "trunk", "sunroof", "drain"], "issue": "Sunroof Drains / MPM Module", "solution": "Drains clog, water floods the trunk and kills the Micro Power Module (MPM). Relocate modules higher!"}
    ],
    "MERCEDES": [
        {"keywords": ["sbc", "brake", "red", "pedal"], "issue": "SBC Brake Pump", "solution": "Sensotronic Brake Control has a cycle limit. If the red warning appears, the pump is at the end of its life. Check for Bosch warranty/recall."},
        {"keywords": ["airmatic", "low", "compressor", "bag"], "issue": "Airmatic Leaks", "solution": "If the car sits low in the morning, a strut or the valve block is leaking. Running it like this kills the compressor."}
    ]
}