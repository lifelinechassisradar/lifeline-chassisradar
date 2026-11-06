import streamlit as st
import json
import httpx

# ---------------------------------------------------------
# 1. FIXED CONNECTIVITY CREDENTIALS
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

# Classic Windows 98 Design Matrix Injection 
st.markdown("""
    <style>
        .stApp { background-color: #008080 !important; color: #000000 !important; font-family: "MS Sans Serif", Tahoma, Arial, sans-serif !important; }
        .win98-window { background-color: #c0c0c0; border-top: 2px solid #fff; border-left: 2px solid #fff; border-right: 2px solid #808080; border-bottom: 2px solid #808080; box-shadow: 1px 1px 0 0 #000; padding: 4px; margin-bottom: 20px; }
        .win98-inner-inset { background-color: #c0c0c0; border-top: 2px solid #808080; border-left: 20px solid #808080; border-right: 2px solid #fff; border-bottom: 2px solid #fff; padding: 12px; margin-top: 4px; }
        .win98-titlebar { background: linear-gradient(90deg, #000080, #1084d0); color: #ffffff; padding: 4px 6px; font-weight: bold; font-size: 0.95rem; }
        .win98-readout { background-color: #ffffff; color: #000000; border-top: 2px solid #808080; border-left: 2px solid #808080; border-right: 2px solid #fff; border-bottom: 2px solid #fff; padding: 10px; font-family: monospace; font-size: 0.95rem; }
        label, p, h3, h4 { color: #000000 !important; font-weight: bold !important; }
    </style>
""", unsafe_allow_html=True)

if not ANTHROPIC_API_KEY:
    st.error("🔑 API Key Required inside Streamlit Secrets panel.")
    st.stop()

# ---------------------------------------------------------
# 2. THE MASTER SEARCH PARSING ENGINE
# ---------------------------------------------------------
@st.cache_data(show_spinner=False)
def scan_global_chassis_archive(user_input):
    if not user_input.strip():
        return None
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
# 3. INTERACTIVE CONSOLE INTERFACE
# ---------------------------------------------------------
st.markdown('<div class="win98-window"><div class="win98-titlebar"><span>Lifeline_Radar.exe - Console</span></div></div>', unsafe_allow_html=True)
chassis_query = st.text_input("Type Chassis Code or Vehicle Title (Then Press Enter):", placeholder="e.g., 'RL5', 'BH5'").strip()

if chassis_query:
    with st.spinner("Decoding registers..."):
        active_specs = scan_global_chassis_archive(chassis_query)
    if active_specs:
        st.markdown('<div class="win98-window"><div class="win98-titlebar"><span>Chassis_Data_Readout.sys</span></div></div>', unsafe_allow_html=True)
        st.write("TARGET PLATFORM RESOLVED:")
        st.write(active_specs['chassis_confirmed'])
        st.write("HUB PITCH PCD:", active_specs['bolt_pattern'])
        st.write("CENTER BORE MAG:", active_specs['center_bore'])
        st.write("OEM TIRES:", str(active_specs['stock_tire_width']) + "/" + str(active_specs['stock_tire_aspect']) + "R" + str(active_specs['stock_rim_diameter']))
        st.write("OEM WHEELS:", str(active_specs['stock_rim_diameter']) + "x" + str(active_specs['stock_width']) + " ET+" + str(active_specs['stock_offset']) + "mm")
    else:
        st.error("Chassis signature unreadable. Please check text entry format parameters.")
else:
    st.info("💻 Standing By... Type a chassis code above and hit Enter to pull up the fitment map matrix.")
