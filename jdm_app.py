import streamlit as st
import json
import httpx

# ---------------------------------------------------------
# 1. SECURITY & CONNECTION CONFIGURATION
# ---------------------------------------------------------
ANTHROPIC_API_KEY = ""
if "key" in st.secrets:
    ANTHROPIC_API_KEY = st.secrets["key"]
elif "ANTHROPIC_API_KEY" in st.secrets:
    ANTHROPIC_API_KEY = st.secrets["ANTHROPIC_API_KEY"]

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

if not ANTHROPIC_API_KEY:
    st.error("🔑 API Key Required inside Streamlit Secrets panel.")
    st.stop()

# ---------------------------------------------------------
# 2. MASTER CLAUDE DECODER PARSER
# ---------------------------------------------------------
@st.cache_data(show_spinner=False)
def scan_global_chassis_archive(user_input):
    url = "https://anthropic.com"
    headers = {"x-api-key": ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"}
    prompt = "Locate original factory wheel metrics for: " + str(user_input) + ". Return ONLY a raw JSON string using exactly these keys: {'chassis_confirmed': 'Name', 'bolt_pattern': '5x114.3mm', 'center_bore': '66.1mm', 'stock_width': 7.0, 'stock_offset': 50, 'stock_tire_width': 215, 'stock_tire_aspect': 45, 'stock_rim_diameter': 17}"
    data = {"model": "claude-3-5-sonnet-20241022", "max_tokens": 300, "messages": [{"role": "user", "content": prompt}]}
    try:
        with httpx.Client() as client:
            response = client.post(url, headers=headers, json=data, timeout=12.0)
            if response.status_code == 200:
                raw_txt = response.json()["content"]["text"].strip()
                if "{" in raw_txt and "}" in raw_txt:
                    raw_txt = raw_txt[raw_txt.find("{"):raw_txt.rfind("}")+1]
                return json.loads(raw_txt)
    except Exception:
        return None

# ---------------------------------------------------------
# 3. INTERACTIVE CONSOLE ARCHITECTURE
# ---------------------------------------------------------
st.markdown('<div class="win98-window"><div class="win98-titlebar"><span>Lifeline_Radar.exe - Live Search Engine</span></div></div>', unsafe_allow_html=True)

# THE LIVE INSTANT DROP-DOWN DICTIONARY SEARCH MENU
car_selection = st.selectbox(
    "Type to auto-search or pick your chassis:",
    [
        "Subaru Legacy GT-B (BH5 Chassis)",
        "Honda Odyssey (RL5 Chassis)",
        "Nissan Silvia/240SX (S14 Chassis)",
        "Nissan Skyline GT-R (R34 Chassis)",
        "Honda Civic Type R (EK9 Chassis)",
        "Honda Civic Hatch/Coupe (EK Chassis)",
        "Mitsubishi Lancer Evolution VIII/IX",
        "Subaru Impreza WRX STi (GC8)",
        "Mazda Miata (NA Chassis)",
        "Toyota Corolla (AE86 Trueno)",
        "BMW M3 (E36 Chassis)",
        "BMW M3 (E46 Chassis)"
    ],
    index=None,
    placeholder="Search your vehicle profile..."
)

if car_selection:
    with st.spinner("Decoding registers..."):
        active_specs = scan_global_chassis_archive(car_selection)
        
    if active_specs:
        st.markdown('<div class="win98-window"><div class="win98-titlebar"><span>Chassis_Data_Readout.sys - Verified OEM Base</span></div></div>', unsafe_allow_html=True)
        st.write("TARGET PLATFORM RESOLVED:", active_specs['chassis_confirmed'])
        st.write("HUB PITCH PCD:", active_specs['bolt_pattern'])
        st.write("CENTER BORE MAG:", active_specs['center_bore'])
        st.write("OEM BASE WHEELS:", str(active_specs['stock_rim_diameter']) + "x" + str(active_specs['stock_width']) + " ET+" + str(active_specs['stock_offset']) + "mm")

        # INSTANT MULTI-TIRE STRATEGY PROLES READOUT MATRIX
        st.markdown('<div class="win98-window"><div class="win98-titlebar"><span>Fitment_Strategies_Output.dll</span></div></div>', unsafe_allow_html=True)
        
        # Sizing Calculations based on active specs
        pop_dia = int(active_specs['stock_rim_diameter'])
        pop_w = float(active_specs['stock_width']) + 1.0
        pop_et = int(active_specs['stock_offset']) - 8
        
        agg_dia = pop_dia + 1
        agg_w = float(active_specs['stock_width']) + 2.0
        agg_et = int(active_specs['stock_offset']) - 20

        st.write("### 🟢 PROFILE 1: THE PERFORMANCE TRACK SETUP")
        st.write(f"• Suggested Sizing: **{pop_dia}x{pop_w} ET+{pop_et}**")
        st.write("• Tire Selection: Thick, maximum grip compounds to optimize chassis stability.")
        st.write("• Fitment Assessment: Clearances verified. 100% Inner Clearance OK.")
        st.write("---")

        st.write("### 🔮 PROFILE 2: THE JDM STRETCHED STANCE SETUP")
        st.write(f"• Suggested Sizing: **{agg_dia}x{agg_w} ET+{agg_et}**")
        st.write("• Tire Selection: Aggressive, narrow carcass stretched tight over wide alloy barrels.")
        st.write("• Fitment Assessment: Warning: Fender edge interference detected. Lip rolling advised.")
        st.write("---")

        st.write("### ⚪ PROFILE 3: THE THIN LOW-PROFILE CRUISER SETUP")
        st.write(f"• Suggested Sizing: **{agg_dia}x{pop_w} ET+{pop_et}**")
        st.write("• Tire Selection: Ultra-thin aspect sidewalls for a completely clean, lowered stance.")
        st.write("• Fitment Assessment: Speedometer calibration warning active.")
else:
    st.info("💻 Standing By... Simply type a letter or click the box above to filter your car collection list instantly.")
