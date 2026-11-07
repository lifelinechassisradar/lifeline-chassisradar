import streamlit as st

st.set_page_config(
    page_title="Lifeline ChassisRadar v98",
    page_icon="💾",
    layout="centered"
)

# Classic Retro Style Injection Matrix
st.markdown("""
    <style>
        .stApp { background-color: #008080 !important; color: #000000 !important; font-family: "MS Sans Serif", Tahoma, Arial, sans-serif !important; }
        .win98-window { background-color: #c0c0c0; border-top: 2px solid #fff; border-left: 2px solid #fff; border-right: 2px solid #808080; border-bottom: 2px solid #808080; box-shadow: 1px 1px 0 0 #000; padding: 4px; margin-bottom: 20px; }
        .win98-inner-inset { background-color: #c0c0c0; border-top: 2px solid #808080; border-left: 2px solid #808080; border-right: 2px solid #fff; border-bottom: 2px solid #fff; padding: 12px; margin-top: 4px; }
        .win98-titlebar { background: linear-gradient(90deg, #000080, #1084d0); color: #ffffff; padding: 4px 6px; font-weight: bold; font-size: 0.95rem; }
        .win98-readout { background-color: #ffffff; color: #000000; border-top: 2px solid #808080; border-left: 2px solid #808080; border-right: 2px solid #fff; border-bottom: 2px solid #fff; padding: 10px; font-family: monospace; font-size: 0.95rem; }
        label, p, h3, h4, span { color: #000000 !important; font-weight: bold !important; }
        .fit-ok { color: #008000 !important; font-weight: bold; }
        .fit-warn { color: #A52A2A !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# COMPREHENSIVE MULTI-SIZE ENTHUSIAST DATABASE DICTIONARY
# ---------------------------------------------------------
VEHICLE_DATABASE = {
    "Subaru Legacy GT-B (BH5 Chassis / KKC)": {
        "confirmed": "Subaru Legacy GT-B E-Tune II (BH5 Chassis)",
        "pcd": "5x100mm", "bore": "56.1mm", "oem_w": 7.0, "oem_et": 55, "oem_dia": 17, "oem_txt": "17x7.0\" ET+55 | 215/45R17",
        "sizes": {
            "16\" Sizing Strategy": {"wheel": "16x7.5\" ET+48", "tire": "205/55R16 Thick Track Cushion", "note": "Perfect downsized winter setup. Safe internal suspension tower clearance."},
            "17\" Sizing Strategy": {"wheel": "17x8.0\" ET+45", "tire": "215/45R17 Square Performance", "note": "Moves rim face out 16mm. Keeps original rolling radius while aligning lips with fender edge tracks."},
            "18\" Sizing Strategy": {"wheel": "18x9.0\" ET+35", "tire": "225/40R18 Low Stretched Profile", "note": "Aggressive upsize setup. Stretched sloped sidewalls required to keep tyre tread clear of metal seam lines."}
        }
    },
    "Mazda RX-7 (FD3S Chassis)": {
        "confirmed": "Mazda RX-7 Twin Turbo (FD3S Fourth Generation)",
        "pcd": "5x114.3mm", "bore": "67.1mm", "oem_w": 8.0, "oem_et": 50, "oem_dia": 16, "oem_txt": "16x8.0\" ET+50 | 225/50R16",
        "sizes": {
            "16\" Sizing Strategy": {"wheel": "16x8.0\" ET+38", "tire": "225/50R16 OEM Replacement Track", "note": "Period-correct style. Moves the face out 12mm closer to the guard lines while maintaining stock comfort levels."},
            "17\" Sizing Strategy": {"wheel": "17x9.0\" ET+40 Square Setup", "tire": "255/40R17 Thick Performance Radial", "note": "The legendary square motorsport configuration. Perfect balance of maximum traction footprint without front fender scrub."},
            "18\" Sizing Strategy": {"wheel": "18x9.5\" ET+22 F / 18x10.0\" ET+20 R", "tire": "225/40R18 & 235/40R18 Stretched Stance", "note": "Extreme deep-dish concavity profile. Tire carcass stretched narrow to clear internal chassis framework. Rear arch rolling highly advised."}
        }
    },
    "Honda Civic Type R (EK9 Chassis)": {
        "confirmed": "JDM Honda Civic Type R (EK9 Track Platform)",
        "pcd": "5x114.3mm", "bore": "64.1mm", "oem_w": 6.0, "oem_et": 50, "oem_dia": 15, "oem_txt": "15x6.0\" ET+50 | 195/55R15",
        "sizes": {
            "15\" Sizing Strategy": {"wheel": "15x7.0\" ET+42", "tire": "195/55R15 Classic Track Spec", "note": "Keeps signature lightweight wheel response. Widens rim track by 1\" to sit perfectly inline with racing guards."},
            "16\" Sizing Strategy": {"wheel": "16x7.5\" ET+40", "tire": "205/45R16 Flush Performance Upgrade", "note": "The ultimate upgrade diameter. Delivers razor-sharp steering feedback with perfect arch filling clearances."},
            "17\" Sizing Strategy": {"wheel": "17x8.0\" ET+35", "tire": "205/40R17 Low Profile Stretch", "note": "Maximum wheel face visual presence. Thin tire footprint curves shoulders away from inner plastic engine liners."}
        }
    },
    "Dodge Neon SRT-4 (Turbo Generation)": {
        "confirmed": "Dodge Neon SRT-4 Turbo (PL Platform)",
        "pcd": "5x100mm", "bore": "57.1mm", "oem_w": 6.0, "oem_et": 45, "oem_dia": 17, "oem_txt": "17x6.0\" ET+45 | 205/50R17",
        "sizes": {
            "17\" Sizing Strategy": {"wheel": "17x7.0\" ET+38 Street Setup", "tire": "215/45R17 High-Response Performance", "note": "Safely widens the incredibly narrow factory track width. Keeps plenty of room away from the large front strut springs."},
            "18\" Sizing Strategy": {"wheel": "18x8.0\" ET+35 Flush Track", "tire": "225/40R18 Normal Comfort Layout", "note": "Fills the tall body arches cleanly. Moves the face out 22.7mm. Sits completely level with the sheet metal."},
            "18\" Aggressive Stance": {"wheel": "18x8.5\" ET+30 Low Drop", "tire": "215/40R18 Angled Sidewall Stretch", "note": "Warning: Very tight layout fitment. Requires tire stretching to avoid parsing the rear fender quarter-panel lip under full compression."}
        }
    },
    "BMW 3-Series / M3 (E30 Generation)": {
        "confirmed": "BMW E30 Platform (Standard 4-Lug vs M3 5-Lug)",
        "pcd": "4x100mm (Standard) / 5x120mm (True E30 M3)", "bore": "57.1mm (Std) / 72.6mm (M3)", "oem_w": 7.0, "oem_et": 30, "oem_dia": 15, "oem_txt": "15x7.0\" ET+30 Basketweave | 205/55R15",
        "sizes": {
            "15\" Euro Strategy": {"wheel": "15x8.0\" ET+20 Square Track", "tire": "205/50R15 Classic Track Radial", "note": "The legendary retro race look for standard 4-lug models. Fills out stock arches cleanly with zero modification needed."},
            "16\" Sizing Strategy": {"wheel": "16x8.0\" ET+15 Period Correct", "tire": "215/45R16 High Response Layout", "note": "Perfect intermediate balance. Pushes wheel lines out 27.7mm outward for an aggressive stance on classic body contours."},
            "17\" Aggressive Stance": {"wheel": "17x8.5\" ET+20 Front / Rear", "tire": "215/40R17 Stretched Stance Fitment", "note": "Fills wheel wells completely. Tire stretch slants the shoulder tread to clear inner metal fender arches on lowered coilovers."}
        }
    },
    "Dodge Challenger/Charger (Modern LX/LA Widebody)": {
        "confirmed": "Modern Dodge Challenger & Charger (Scat Pack / Hellcat Widebody)",
        "pcd": "5x115mm (Heavy Duty Muscle Hub)", "bore": "71.5mm", "oem_w": 11.0, "oem_et": -2.5, "oem_dia": 20, "oem_txt": "20x11.0\" ET-2.5 Widebody Forged | 305/35ZR20",
        "sizes": {
            "20\" Factory Widebody": {"wheel": "20x11.0\" ET-2.5 Square Setup", "tire": "305/35R20 High Traction Muscle Radial", "note": "Massive factory square track alignment. Sits completely flush with plastic widebody flare lips."},
            "20\" Aggressive Deep Lip": {"wheel": "20x11.0\" ET-15 Front / 20x12.0\" ET-20 Rear", "tire": "305/35R20 & 315/35R20 Thick Compound", "note": "Pushes rear lip out another 35.1mm closer to the edge. Demands immense barrel concavity for a muscular track presence."},
            "21\" Custom Cruiser": {"wheel": "21x11.0\" ET-5 Front / Rear", "tire": "295/30R21 Low-Profile Thin Setup", "note": "Upsizes diameter for max car-show presence. Thin aspect rubber keeps body lines clean without inner liner rub."}
        }
    },
    "Toyota Corolla (AE86 Hachi-Roku)": {
        "confirmed": "Toyota Corolla Levin / Sprinter Trueno (AE86 GT-V/GT-Apex)",
        "pcd": "4x114.3mm", "bore": "60.1mm", "oem_w": 5.5, "oem_et": 27, "oem_dia": 14, "oem_txt": "14x5.5\" ET+27 | 185/60R14",
        "sizes": {
            "14\" Old School Custom": {"wheel": "14x7.0\" ET+0 Period Correct", "tire": "185/60R14 Throwback Vintage Radial", "note": "The classic, authentic drift era layout. Widens footprint by 1.5\" and aligns faces directly with standard metal panels."},
            "15\" Sizing Strategy": {"wheel": "15x7.5\" ET+10 Performance Track", "tire": "195/50R15 Modern Sticky Compound", "note": "Optimal modern sizing standard. Maximizes grip threshold boundaries while maintaining clean layout compression clearances."},
            "15\" Deep Lip Stance": {"wheel": "15x8.5\" ET-8 Deep Dish Dish", "tire": "195/45R15 Heavy Angled Shoulder Stretch", "note": "Creates huge visual lip concavity. Wheel face pokes 73mm outward past stock. Rear quarter panel lip rolling is 100% non-negotiable."}
        }
    },
    "Honda Odyssey (RL5 Chassis)": {
        "confirmed": "Honda Odyssey Van (RL5 Fourth Gen Platform)",
        "pcd": "5x120mm", "bore": "64.1mm", "oem_w": 7.0, "oem_et": 50, "oem_dia": 17, "oem_txt": "17x7.0\" ET+50 | 235/65R17",
        "sizes": {
            "17\" Sizing Strategy": {"wheel": "17x8.0\" ET+40 Comfort Track", "tire": "235/65R17 Stock Comfort Baseline", "note": "Maintains standard plush luxury cushion depths while tracking wheels 16mm wider to fill structural voids."},
            "19\" Sizing Strategy": {"wheel": "19x8.5\" ET+35 VIP Touring", "tire": "245/45R19 Premium VIP Touring Layout", "note": "Fills out large panel gaps perfectly. Sits cleanly flush with factory side panels without sliding door interference gaps."},
            "20\" Sizing Strategy": {"wheel": "20x10.0\" ET+25 Slammed Style", "tire": "245/35R20 Extreme Sloped Stretch", "note": "Slammed cruiser stance profile. Lip edge extends 63mm outward. Heavy inner fender line modification highly advised."}
        }
    }
}
