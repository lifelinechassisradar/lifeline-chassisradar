import streamlit as st

st.set_page_config(
    page_title="Lifeline ChassisRadar v98",
    page_icon="💾",
    layout="centered"
)

# Classic Retro Style Injection
st.markdown("""
    <style>
        .stApp { background-color: #008080 !important; color: #000000 !important; font-family: "MS Sans Serif", Tahoma, Arial, sans-serif !important; }
        .win98-window { background-color: #c0c0c0; border-top: 2px solid #fff; border-left: 2px solid #fff; border-right: 2px solid #808080; border-bottom: 2px solid #808080; box-shadow: 1px 1px 0 0 #000; padding: 4px; margin-bottom: 20px; }
        .win98-inner-inset { background-color: #c0c0c0; border-top: 2px solid #808080; border-left: 2px solid #808080; border-right: 2px solid #fff; border-bottom: 2px solid #fff; padding: 12px; margin-top: 4px; }
        .win98-titlebar { background: linear-gradient(90deg, #000080, #1084d0); color: #ffffff; padding: 4px 6px; font-weight: bold; font-size: 0.95rem; }
        .win98-readout { background-color: #ffffff; color: #000000; border-top: 2px solid #808080; border-left: 2px solid #808080; border-right: 2px solid #fff; border-bottom: 2px solid #fff; padding: 10px; font-family: monospace; font-size: 0.95rem; }
        label, p, h3, h4 { color: #000000 !important; font-weight: bold !important; }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# VEHICLE MECHANICAL MATRIX DICTIONARY (YOUR CLAUDE DATA)
# ---------------------------------------------------------
VEHICLE_DATABASE = {
    "Subaru Legacy GT-B (BH5 Chassis / KKC)": {
        "confirmed": "Subaru Legacy GT-B E-Tune II (BH5 Chassis)",
        "pcd": "5x100mm", "bore": "56.1mm", "oem": "17x7.0\" ET+55 | 215/45R17",
        "perf_specs": "17x8.0\" or 18x8.0\" ET+45 to ET+42", "perf_tire": "215/45R17 or 225/40R18 Thick Compound", "perf_note": "Widens barrel by 1\", pushes wheel lip out 20mm closer to fender line. Perfect square track look without rubbing inner strut towers.",
        "stretch_specs": "18x9.0\" ET+35 to ET+30 (Aggressive Low Drop)", "stretch_tire": "215/40R18 Stretched Angled Sidewall", "stretch_note": "Angled tire tread ducks inside wheel arches. Fender lip rolling and negative camber adjustment required to protect metal.",
        "thin_specs": "18x7.5\" ET+48 (Low-Profile Cruiser)", "thin_tire": "215/35R18 Ultra-Thin Sidewall", "thin_note": "Gives an extreme slammed cruise height stance with minimal tire profile cushion. Watch out for potholes."
    },
    "Honda Civic Type R (EK9 Chassis)": {
        "confirmed": "JDM Honda Civic Type R (EK9 Track Platform)",
        "pcd": "5x114.3mm (Heavy-Duty Racing Hub)", "bore": "64.1mm", "oem": "15x6.0\" ET+50 | 195/55R15",
        "perf_specs": "16x7.0\" ET+40 or 16x7.5\" ET+42", "perf_tire": "205/45R16 Track / Performance Compound", "perf_note": "Moves the wheel lip perfectly flush with the classic factory EK9 type-R racing fenders. Maximum cornering response.",
        "stretch_specs": "16x8.0\" ET+35 (Aggressive Stance Offset)", "stretch_tire": "205/40R16 Stretched Carcass Setup", "stretch_note": "Curves tire wall inward to allow extra clearance over wide high-performance coilover setups.",
        "thin_specs": "17x7.0\" ET+45 (Thin Profile Cruiser)", "thin_tire": "205/35R17 Low Profile Tire Lines", "thin_note": "Upsizes to a larger wheel layout with flat, thin rubber lines. Fills out arches completely."
    },
    "Honda Civic Hatch/Coupe (EK Chassis)": {
        "confirmed": "Standard Honda Civic Coupe/Hatch (EK Base Platform)",
        "pcd": "4x100mm (Economy 4-Lug Commuter Hub)", "bore": "56.1mm", "oem": "14x5.5\" ET+45 | 185/65R14",
        "perf_specs": "15x7.0\" ET+35 or 16x7.0\" ET+40", "perf_tire": "195/50R15 High Response Compound", "perf_note": "Pushes the outer rim edge cleanly out to the fender border without rubbing inner plastic liners.",
        "stretch_specs": "16x8.0\" ET+25 (Stretched Stance Layout)", "stretch_tire": "195/40R16 Deep Stretch Profile", "stretch_note": "Requires rear quarter panel sheet metal manipulation or rolling to keep tire shoulders clean under compression.",
        "thin_specs": "16x7.0\" ET+42 (Clean Commuter Style)", "thin_tire": "195/40R16 Thin Footprint Setup", "thin_note": "Provides a clean, sharp cosmetic update with thin tire aesthetics and no speedometer variation anomalies."
    },
    "Nissan Silvia / 240SX (S14 Turbo Platforms)": {
        "confirmed": "Nissan Silvia / 240SX (S14 Base & Spec-R)",
        "pcd": "5x114.3mm (Turbo Multi-Lug Hub / Base 4-lug varies)", "bore": "66.1mm", "oem": "16x6.5\" ET+40 | 205/55R16",
        "perf_specs": "17x9.0\" ET+22 or 18x9.0\" ET+22 (Signature Fitment)", "perf_tire": "235/40R17 or 245/40R18 Performance Radial", "perf_note": "The absolute signature golden track footprint for an S-chassis. Sits perfectly flush with factory metal body lines.",
        "stretch_specs": "18x9.5\" ET+12 (Aggressive Wide Lip Stance)", "stretch_tire": "225/40R18 Stretched Low-Profile Tyre", "stretch_note": "Pokes 8mm past stock fender boundaries. Requires rolling inner sheet-metal lines to avoid carving up tire shoulders.",
        "thin_specs": "18x8.5\" ET+25 (Clean Daily Driver)", "thin_tire": "215/35R18 Ultra Thin Profile Style", "thin_note": "Maintains low structural body clearance while emphasizing massive wheel lip depth without fender modification."
    },
    "Nissan Skyline GT-R (R34 Chassis)": {
        "confirmed": "Nissan Skyline GT-R (R34 Forged Widebody Platform)",
        "pcd": "5x114.3mm (Heavy-Duty Track Pitch)", "bore": "66.1mm", "oem": "18x9.0\" ET+30 | 244/40ZR18 Forged Alloy",
        "perf_specs": "18x10.5\" ET+15 or ET+12 Muscular Setup", "perf_tire": "275/35R18 Track Spec Sticky Compounds", "perf_note": "Builds that legendary, beefy high-traction motorsport track presence. Sits tight to stock arch inner walls.",
        "flush_specs": "18x9.5\" ET+12 or 19x9.5\" ET+12 Optimized", "flush_tire": "255/35R19 Performance Track Profile Layout", "flush_note": "The R34 has massive factory flared quarters that look phenomenal with deep aggressive offset wheel hub placements.",
        "stretch_specs": "19x11.0\" ET+15 (Deep Dish Over-Stance)", "stretch_tire": "255/35R19 Heavy Stretched Sidewall", "stretch_note": "Maximizes wheel barrel depth and deep-dish concavity while letting the sloped tire tread clear structural body framework."
    },
    "Mitsubishi Lancer Evolution VIII / IX": {
        "confirmed": "Mitsubishi Lancer Evolution VIII / IX (CT9A Chassis)",
        "pcd": "5x114.3mm", "bore": "67.1mm", "oem": "17x8.0\" ET+38 Enkei Factory Base",
        "perf_specs": "18x9.0\" ET+29 or ET+30 Performance Tracking", "perf_tire": "245/40R18 High Adhesion Track Radial", "perf_note": "The ultimate setup for this chassis. Fills out factory blister arches perfectly with maximum rubber contact patch.",
        "stretch_specs": "18x9.5\" ET+22 (Aggressive Outer Edge Poke)", "stretch_tire": "235/40R18 Stretched Compound Setup", "stretch_note": "Pokes 5mm outward past factory metal lines. Requires rolling rear quarter panel inner tabs to eliminate tire rub.",
        "thin_specs": "19x8.5\" ET+35 (Large Diameter Show Setup)", "thin_tire": "235/30R19 Ultra Low-Profile Tyre Lines", "thin_note": "Accentuates massive brake caliper clearance and wheel spacing, keeping tyre sidewall visibility to a bare minimum."
    },
    "Subaru Impreza WRX STi (GC8 Chassis)": {
        "confirmed": "Subaru Impreza WRX STi (Classic GC8 Generation)",
        "pcd": "5x100mm Hub Interface", "bore": "56.1mm", "oem": "16x7.0\" ET+53 Base / 17x7.5\" ET+51 Trims",
        "perf_specs": "17x7.5\" ET+48 or 17x8.0\" ET+45 Balanced Setup", "perf_tire": "215/45R17 High-Performance Track Tire", "perf_note": "Classic Subarus have flat, narrow rear metal arches. Sizing up here maximizes grip boundaries without body rubs.",
        "stretch_specs": "18x8.5\" ET+35 (Aggressive Stance Stretched Line)", "stretch_tire": "215/40R18 Aggressive Angle Sidewall Stretch", "stretch_note": "Pokes 8mm past fender line. Requires heavy rolling and negative alignment camber adjustments to tuck tread clear of sheet-metal.",
        "thin_specs": "18x7.5\" ET+45 (Thin Low-Profile Stance)", "thin_tire": "205/35R18 Custom Low Profile Cushion", "thin_note": "Tucks wheel cleanly inside tight arches while maintaining a thin rubber baseline for an ultra-clean appearance."
    }
}

# ---------------------------------------------------------
# INTERACTIVE APPLICATION INTERFACE
# ---------------------------------------------------------
st.markdown('<div class="win98-window"><div class="win98-titlebar"><span>Lifeline_Radar.exe - Live Search Engine</span></div></div>', unsafe_allow_html=True)

# THE SEARCH DROP-DOWN DISPLAY
car_selection = st.selectbox(
    "Type to auto-search or pick your chassis:",
    list(VEHICLE_DATABASE.keys()),
    index=None,
    placeholder="Search your vehicle profile..."
)

if car_selection:
    specs = VEHICLE_DATABASE[car_selection]
    
    # 1. VERIFIED OEM BASE CARD WINDOW
    st.markdown('<div class="win98-window"><div class="win98-titlebar"><span>Chassis_Data_Readout.sys - Verified OEM Base</span></div></div>', unsafe_allow_html=True)
    st.write("TARGET PLATFORM RESOLVED: **" + specs['confirmed'] + "**")
    st.write("HUB PITCH PCD: **" + specs['pcd'] + "**")
    st.write("CENTER BORE MAG: **" + specs['bore'] + "**")
    st.write("OEM BASE LINE CONFIGURATION: **" + specs['oem'] + "**")

    # 2. THE CUSTOM CLAUDE STRATEGY RESULTS readouts
    st.markdown('<div class="win98-window"><div class="win98-titlebar"><span>Fitment_Strategies_Output.dll - Stance Presets</span></div></div>', unsafe_allow_html=True)
    
    st.write("### 🟢 PROFILE 1: THE PERFORMANCE TRACK SETUP")
    st.write("• **Wheel Blueprint:** " + specs['perf_specs'])
    st.write("• **Tire Fitment:** " + specs['perf_tire'])
    st.write("• **Mechanical Assessment:** " + specs['perf_note'])
    st.write("---")
