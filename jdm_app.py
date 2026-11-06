import streamlit as st
import json
import httpx

# ---------------------------------------------------------
# 1. PREMIUM APPARATUS & BLACKOUT RADAR STYLING
# ---------------------------------------------------------
# Paste your sk-ant-... key right inside the quotes below!
ANTHROPIC_API_KEY = "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"

st.set_page_config(
    page_title="Lifeline ChassisRadar",
    page_icon="⚡",
    layout="centered"
)

# Custom CSS to mimic the premium mobile app theme exactly
st.markdown("""
    <style>
        /* Deep Matte Charcoal Blackout Base */
        .stApp { 
            background-color: #080A0E; 
            color: #E2E8F0; 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; 
        }
        
        /* Premium Card Container */
        .premium-card {
            background-color: #111520;
            border: 1px solid #1F283A;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 16px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }
        
        /* Electric Green High-Contrast Accents */
        .neon-accent {
            color: #39FF14;
            font-weight: bold;
            font-family: monospace;
        }
        
        /* Custom Styling for Results Header */
        .chassis-title {
            font-size: 1.3rem;
            font-weight: 800;
            color: #FFFFFF;
            margin-bottom: 2px;
        }
        
        /* Crisp Fitment Status Badges */
        .fit-ok {
            color: #39FF14;
            font-weight: bold;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .fit-warn {
            color: #FFEA00;
            font-weight: bold;
            font-size: 0.9rem;
            text-transform: uppercase;
        }
        
        /* Input Box Tuning */
        input {
            background-color: #111520 !important;
            color: #39FF14 !important;
            border: 2px solid #1F283A !important;
            border-radius: 10px !important;
            font-weight: bold !important;
        }
        input:focus {
            border-color: #39FF14 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. BRANDING LOGO COMPONENT
# ---------------------------------------------------------
# Once you upload your wagon graphic, we can replace this placeholder with your exact logo image file!
st.image("https://imgur.com", width=350, fallback="⚡ LIFELINE CHASSISRADAR")
st.write("---")

if ANTHROPIC_API_KEY == "PASTE_YOUR_KEY_HERE" or not ANTHROPIC_API_KEY.startswith("sk-ant"):
    st.error("🔑 API Key Required: Please paste your active Anthropic API key at the top of the file to connect the matrix.")
    st.stop()

# ---------------------------------------------------------
# 3. CONSOLE UNBLOCKABLE DISCOVERY BACKEND
# ---------------------------------------------------------
@st.cache_data(show_spinner=False)
def resolve_chassis_dna_matrix(user_input):
    if not user_input.strip():
        return None
        
    url = "https://anthropic.com"
    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    
    prompt = (
        f"Analyze this automotive user lookup input: '{user_input}'. "
        "Locate the correct factory original stock wheel and tire specs for this vehicle layout. "
        "You MUST return ONLY a valid raw JSON object string with zero conversational text, backticks, or markdown formatting wrappers. "
        "The JSON must map exactly to these specific structural keys: "
        '{"chassis_confirmed": "Vehicle Identity and Chassis Code", '
        '"bolt_pattern": "e.g. 5x120mm", '
        '"center_bore": "e.g. 72.6mm", '
        '"stock_width": 8.0, '
        '"stock_offset": 47, '
        '"stock_tire_width": 225, '
        '"stock_tire_aspect": 45, '
        '"stock_rim_diameter": 17}'
    )
    
    data = {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 300,
        "messages": [{"role": "user", "content": prompt}]
    }
    
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
# 4. CHASSIS RESOLVER FIELD (Type Code -> Press Enter)
# ---------------------------------------------------------
chassis_query = st.text_input("📡 ENTER VEHICLE CHASSIS DESIGNATION:", placeholder="e.g., 'E36 M3', 'RL5', 'BH5', 'Silvia S15', 'Ford GT'").strip()

if chassis_query:
    with st.spinner("Locking radar onto factory chassis blueprints..."):
        active_specs = resolve_chassis_dna_matrix(chassis_query)
        
    if active_specs:
        # ---------------------------------------------------------
        # 5. PREMIUM FACTORY WHEEL READOUT WINDOW
        # ---------------------------------------------------------
        st.markdown(f"""
            <div class="premium-card">
                <div class="chassis-title">{active_specs['chassis_confirmed']}</div>
                <div style="font-size:0.85rem; color:#64748B; margin-bottom:12px; font-weight:bold; letter-spacing:0.5px;">FACTORY WHEEL BASE DATA</div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 0.95rem; font-family: monospace;">
                    <div>Bolt Pattern: <span class="neon-accent">{active_specs['bolt_pattern']}</span></div>
                    <div>Center Bore: <span class="neon-accent">{active_specs['center_bore']}</span></div>
                    <div>Factory Tire: <span style="color:#FFF;">{active_specs['stock_tire_width']}/{active_specs['stock_tire_aspect']}R{active_specs['stock_rim_diameter']}</span></div>
                    <div>Factory Wheel: <span style="color:#FFF;">{active_specs['stock_rim_diameter']}x{active_specs['stock_width']}" ET{active_specs['stock_offset']}</span></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # ---------------------------------------------------------
        # 6. TRY YOUR OWN WHEEL (Interactive Sliders Workspace)
        # ---------------------------------------------------------
        st.write("### Try Your Own Wheel")
        st.write("Enter custom aftermarket wheel measurements below to simulate clearances instantly.")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            custom_diameter = st.slider("Diameter (Inches)", min_value=13, max_value=24, value=int(active_specs['stock_rim_diameter']))
        with c2:
            custom_width = st.slider("Width (Inches)", min_value=5.0, max_value=15.0, value=float(active_specs['stock_width'] + 1.0), step=0.5)
        with c3:
            custom_offset = st.slider("Offset (mm)", min_value=-40, max_value=70, value=int(active_specs['stock_offset'] - 12), step=1)

        st.write("#### Custom Tire Profile Sizing:")
        t1, t2 = st.columns(2)
        with t1:
            custom_tire_w = st.slider("Tire Width (mm)", min_value=155, max_value=355, value=int(active_specs['stock_tire_width']), step=10)
        with t2:
            custom_tire_a = st.slider("Aspect Ratio (%)", min_value=20, max_value=80, value=int(active_specs['stock_tire_aspect']), step=5)

        # ---------------------------------------------------------
        # 7. FITMENT STRATEGY GEOMETRY MATHEMATICS
        # ---------------------------------------------------------
        width_delta_mm = (custom_width - active_specs['stock_width']) * 25.4
        half_width_delta = width_delta_mm / 2
        offset_delta = active_specs['stock_offset'] - custom_offset
        
        total_outer_poke = half_width_delta + offset_delta
        total_inner_clearance = half_width_delta - offset_delta
        rim_barrel_mm = custom_width * 25.4
        tire_stretch_metric = rim_barrel_mm - custom_tire_w

        # PRESET CAR STRUCTURE VALUES LOGIC BASED ON APP SCREENSHOTS
        # 1. Popular Aftermarket Formula Simulation
        pop_width = active_specs['stock_width'] + 1.0
        pop_offset = active_specs['stock_offset'] - 7
        pop_poke = ((pop_width - active_specs['stock_width']) * 25.4 / 2) + (active_specs['stock_offset'] - pop_offset)
        
        # 2. Aggressive Aftermarket Formula Simulation
        agg_width = active_specs['stock_width'] + 1.5
        agg_offset = active_specs['stock_offset'] - 15
        agg_poke = ((agg_width - active_specs['stock_width']) * 25.4 / 2) + (active_specs['stock_offset'] - agg_offset)

        # ---------------------------------------------------------
        # 8. PREMIUM RENDER LABELS (SAFE / FLUSH / AGGRESSIVE PRESETS)
        # ---------------------------------------------------------
        st.write("---")
        st.write("### Calculated Fitment Strategies Output")

        # Preset Block 1: Popular Aftermarket
        st.markdown(f"""
            <div class="premium-card" style="border-left: 5px solid #1F283A;">
                <div style="font-size:0.75rem; color:#64748B; font-weight:bold; text-transform:uppercase; letter-spacing:0.5px;">SAVED SETUP</div>
                <div style="font-size:1.1rem; font-weight:bold; color:#FFF; margin-bottom:4px;">Popular Aftermarket Setup Blueprint</div>
                <div style="font-family:monospace; font-size:1rem; margin-bottom:6px; color:#FFFFFF;">{int(active_specs['stock_rim_diameter'])}x{pop_width} ET{int(pop_offset)}</div>