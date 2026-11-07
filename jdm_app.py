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
# COMPREHENSIVE MULTI-SIZE DIAMETER MATRIX DICTIONARY
# ---------------------------------------------------------
VEHICLE_DATABASE = {
    "Subaru Legacy GT-B (BH5 Chassis / KKC)": {
        "confirmed": "Subaru Legacy GT-B E-Tune II (BH5 Chassis)",
        "pcd": "5x100mm", "bore": "56.1mm", "oem_w": 7.0, "oem_et": 55, "oem_dia": 17, "oem_txt": "17x7.0\" ET+55 | 215/45R17",
        "sizes": {
            "16\" Sizing Strategy": {"wheel": "16x7.5\" ET+48", "tire": "205/55R16 Thick Winter Track", "note": "Perfect downsized layout for high-cushion rubber profiles. Safe internal suspension tower clearance."},
            "17\" Sizing Strategy": {"wheel": "17x8.0\" ET+45", "tire": "215/45R17 Square Performance", "note": "Moves rim face out 16mm. Keeps original rolling radius while aligning lips with fender edge tracks."},
            "18\" Sizing Strategy": {"wheel": "18x9.0\" ET+35", "tire": "225/40R18 Low Stretched Profile", "note": "Aggressive upsize setup. Stretched sloped sidewalls are required to keep tyre tread blocks clear of metal seam lines."}
        }
    },
    "Mazda RX-7 (FD3S Chassis)": {
        "confirmed": "Mazda RX-7 Twin Turbo (FD3S Fourth Generation)",
        "pcd": "5x114.3mm", "bore": "67.1mm", "oem_w": 8.0, "oem_et": 50, "oem_dia": 16, "oem_txt": "16x8.0\" ET+50 | 225/50R16",
        "sizes": {
            "16\" Sizing Strategy": {"wheel": "16x8.0\" ET+38", "tire": "225/50R16 OEM Replacement Track", "note": "Period-correct style. Moves the face out 12mm closer to the guard lines while maintaining stock comfort levels."},
            "17\" Sizing Strategy": {"wheel": "17x9.0\" ET+40 Front / Rear", "tire": "255/40R17 Thick Performance Radial", "note": "The legendary square motorsport configuration. Perfect balance of maximum traction footprint without front fender scrub."},
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
    "Honda Odyssey (RL5 Chassis)": {
        "confirmed": "Honda Odyssey Van (RL5 Fourth Gen Platform)",
        "pcd": "5x120mm", "bore": "64.1mm", "oem_w": 7.0, "oem_et": 50, "oem_dia": 17, "oem_txt": "17x7.0\" ET+50 | 235/65R17",
        "sizes": {
            "17\" Sizing Strategy": {"wheel": "17x8.0\" ET+40", "tire": "235/65R17 Stock Comfort Baseline", "note": "Maintains standard plush luxury cushion depths while tracking wheels 16mm wider to fill structural voids."},
            "19\" Sizing Strategy": {"wheel": "19x8.5\" ET+35", "tire": "245/45R19 Premium VIP Touring", "note": "Fills out large panel gaps perfectly. Sits cleanly flush with factory side panels without sliding door interference gaps."},
            "20\" Sizing Strategy": {"wheel": "20x10.0\" ET+25", "tire": "245/35R20 Extreme Sloped Stretch", "note": "Slammed cruiser stance profile. Lip edge extends 63mm outward. Heavy inner fender line modification highly advised."}
        }
    }
}

# ---------------------------------------------------------
# INTERACTIVE APPLICATION CONSOLE DESIGN
# ---------------------------------------------------------
st.markdown('<div class="win98-window"><div class="win98-titlebar"><span>Lifeline_Radar.exe - Live Search Engine</span></div></div>', unsafe_allow_html=True)

car_selection = st.selectbox(
    "Type to auto-search or pick your chassis:",
    list(VEHICLE_DATABASE.keys()),
    index=None,
    placeholder="Search your vehicle profile..."
)

if car_selection:
    specs = VEHICLE_DATABASE[car_selection]
    
    # PANEL 1: FACTORY OEM REFERENCE DATA CARD
    st.markdown('<div class="win98-window"><div class="win98-titlebar"><span>Chassis_Data_Readout.sys - Verified OEM Base</span></div></div>', unsafe_allow_html=True)
    st.write("TARGET PLATFORM RESOLVED: **" + specs['confirmed'] + "**")
    st.write("HUB PITCH PCD: **" + specs['pcd'] + "**")
    st.write("CENTER BORE DIA: **" + specs['bore'] + "**")
    st.write("FACTORY WHEEL BASELINE: **" + specs['oem_txt'] + "**")

    # PANEL 2: DIAMETER SIZE CHOICE SEGMENT (MATCHING YOUR SCREENSHOT)
    st.markdown('<div class="win98-window"><div class="win98-titlebar"><span>Diameter_Strategy_Selector.dll</span></div></div>', unsafe_allow_html=True)
    st.write("### 🎛️ Select Aftermarket Alloy Diameter Target:")
    
    # This automatically maps the available strategy buttons to your chosen vehicle options
    selected_size = st.radio(
        "Choose rim dimension layout:",
        list(specs['sizes'].keys()),
        horizontal=True
    )

    if selected_size:
        strategy = specs['sizes'][selected_size]
        st.markdown(f'<div class="win98-window"><div class="win98-titlebar"><span>Fitment_Specs_Active_Profile</span></div></div>', unsafe_allow_html=True)
        st.write(f"### 🟢 {selected_size} CONFIGURATION")
        st.write(f"• **Recommended Sizing Setup:** `{strategy['wheel']}`")
        st.write(f"• **Target Tire Configuration:** `{strategy['tire']}`")
        st.write(f"• **Clearance Blueprint Assessment:** {strategy['note']}")

    # PANEL 3: INTERACTIVE TUNER WORKSPACE ("TRY YOUR OWN WHEELS")
    st.markdown('<div class="win98-window"><div class="win98-titlebar"><span>Custom_Wheel_Override_Tuner.exe</span></div></div>', unsafe_allow_html=True)
    st.write("### 🛠️ Try Your Own Wheels & Tires")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        user_dia = st.slider("Diameter (Inches)", min_value=13, max_value=22, value=int(specs['oem_dia']))
    with col2:
        user_width = st.slider("Width (Inches)", min_value=5.0, max_value=12.0, value=float(specs['oem_w'] + 1.0), step=0.5)
    with col3:
        user_offset = st.slider("Offset (mm)", min_value=-20, max_value=65, value=int(specs['oem_et'] - 10), step=1)

    # MATHEMATICAL FITMENT CALCULATIONS
    width_diff_mm = (user_width - specs['oem_w']) * 25.4
    half_width_diff = width_diff_mm / 2
    offset_shift = specs['oem_et'] - user_offset
    calculated_poke = half_width_diff + offset_shift

    st.markdown("#### Live Clearance Diagnostic Output:")
    st.write(f"• **Fender Edge Poke Shift:** +{calculated_poke:.1f} mm outward past factory lines.")
    
    if calculated_poke > 35.0:
        st.markdown('⚠️ <span class="fit-warn">WARNING ASSESSMENT: Heavy Outer Face Poke. Fender manipulation required.</span>', unsafe_allow_html=True)
    else:
        st.markdown('✅ <span class="fit-ok">SYSTEM ASSESSMENT: Clearance values float safely inside standard tolerances.</span>', unsafe_allow_html=True)
else:
    st.info("💻 Standing By... Simply click or start typing above to open a chassis radar dashboard profile.")
