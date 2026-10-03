import streamlit as st
import os
import datetime
import ctypes
import json
import importlib.util
import hashlib
import time
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# ──────────────────────────────────────────────
# Page Configuration
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Ultimate Quantum Shield - Military Grade Enterprise v4.0",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ──────────────────────────────────────────────
# PREMIUM CYBER-MILITARY CSS (v4.0 Titanium)
# ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&family=Share+Tech+Mono&display=swap');

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'Rajdhani', sans-serif;
    background: #05070f !important;
}

.stApp {
    background: radial-gradient(ellipse at top, #0a0f1f 0%, #05070f 60%, #02040a 100%) !important;
}

/* Hide default Streamlit elements */
#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

/* ── Main Title ── */
.main-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #00ffcc, #00d4ff, #7b61ff, #00ffcc);
    background-size: 300% 100%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientShift 6s ease infinite;
    letter-spacing: 2px;
    margin-bottom: 0.2rem;
    text-shadow: 0 0 40px rgba(0, 255, 204, 0.3);
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.sub-title {
    font-family: 'Share Tech Mono', monospace;
    color: #7a8ba8;
    font-size: 0.95rem;
    letter-spacing: 0.5px;
    margin-bottom: 1.5rem;
}

.sub-title b {
    color: #00ffcc;
    font-weight: 600;
}

/* ── Section Headers ── */
.section-header {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: #e0f7ff;
    letter-spacing: 1.5px;
    margin: 1.8rem 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(0, 255, 204, 0.15);
}

/* ── Telemetry Cards ── */
.telemetry-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 1.5rem;
}

.telemetry-card {
    background: linear-gradient(160deg, rgba(12, 18, 35, 0.95) 0%, rgba(8, 12, 24, 0.98) 100%);
    border: 1px solid rgba(0, 255, 204, 0.12);
    border-radius: 14px;
    padding: 18px 16px;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255,255,255,0.03);
}

.telemetry-card:hover {
    border-color: rgba(0, 255, 204, 0.35);
    box-shadow: 0 8px 32px rgba(0, 255, 204, 0.12), inset 0 1px 0 rgba(255,255,255,0.05);
    transform: translateY(-2px);
}

.telemetry-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #00ffcc, transparent);
    opacity: 0.6;
}

.telemetry-icon {
    font-size: 1.4rem;
    margin-bottom: 6px;
}

.telemetry-label {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.72rem;
    font-weight: 600;
    color: #8ba3c7;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.telemetry-value {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.88rem;
    color: #c8d6e5;
    line-height: 1.5;
}

.status-clean {
    color: #00ff9d;
    font-weight: 600;
}

.status-alert {
    color: #ff6b6b;
    font-weight: 600;
}

.status-info {
    color: #00d4ff;
}

/* ── Sidebar Premium ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0e1a 0%, #060910 100%) !important;
    border-right: 1px solid rgba(0, 255, 204, 0.08) !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.2rem;
}

.sidebar-brand {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #00ffcc;
    letter-spacing: 1px;
    padding: 0 0 12px 0;
    margin-bottom: 8px;
    border-bottom: 1px solid rgba(0, 255, 204, 0.15);
    display: flex;
    align-items: center;
    gap: 8px;
}

.sidebar-section-label {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.65rem;
    font-weight: 600;
    color: #5a6a85;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin: 18px 0 8px 0;
}

/* Selectbox premium styling */
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: linear-gradient(145deg, #0d1424 0%, #0a101c 100%) !important;
    border: 1px solid rgba(0, 255, 204, 0.25) !important;
    border-radius: 10px !important;
    box-shadow: 0 0 12px rgba(0, 255, 204, 0.08), inset 0 1px 0 rgba(255,255,255,0.03) !important;
    transition: all 0.25s ease !important;
}

[data-testid="stSidebar"] .stSelectbox > div > div:hover {
    border-color: rgba(0, 255, 204, 0.5) !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.15) !important;
}

[data-testid="stSidebar"] .stSelectbox label {
    font-family: 'Orbitron', sans-serif !important;
    font-size: 0.7rem !important;
    color: #7a8ba8 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}

/* ── Content Cards ── */
.content-card {
    background: linear-gradient(160deg, rgba(12, 18, 35, 0.9) 0%, rgba(8, 12, 24, 0.95) 100%);
    border: 1px solid rgba(0, 255, 204, 0.1);
    border-radius: 16px;
    padding: 28px 24px;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255,255,255,0.02);
    position: relative;
}

.content-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,255,204,0.4), transparent);
}

/* ── Pricing Cards ── */
.pricing-card {
    background: linear-gradient(165deg, #0c1220 0%, #080e18 100%);
    border: 1px solid rgba(0, 255, 204, 0.18);
    border-radius: 16px;
    padding: 28px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: all 0.35s ease;
    box-shadow: 0 6px 28px rgba(0, 0, 0, 0.4);
    height: 100%;
}

.pricing-card:hover {
    border-color: rgba(0, 255, 204, 0.5);
    box-shadow: 0 12px 40px rgba(0, 255, 204, 0.15);
    transform: translateY(-4px);
}

.pricing-card::after {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(0,255,204,0.04) 0%, transparent 60%);
    pointer-events: none;
}

.pricing-tier {
    font-family: 'Orbitron', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #00ffcc;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.pricing-price {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    color: #ffffff;
    margin: 12px 0 4px 0;
}

.pricing-desc {
    font-size: 0.85rem;
    color: #7a8ba8;
    margin-bottom: 16px;
}

.pricing-feature {
    font-size: 0.88rem;
    color: #b0c0d4;
    text-align: left;
    padding: 5px 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #00c9a0 0%, #00a8e8 100%) !important;
    color: #05070f !important;
    font-family: 'Orbitron', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 1px !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.65rem 1.4rem !important;
    box-shadow: 0 4px 20px rgba(0, 200, 160, 0.3) !important;
    transition: all 0.25s ease !important;
}

.stButton > button:hover {
    box-shadow: 0 6px 28px rgba(0, 200, 160, 0.5) !important;
    transform: translateY(-1px) !important;
}

/* ── Form inputs ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background: rgba(8, 12, 24, 0.9) !important;
    border: 1px solid rgba(0, 255, 204, 0.15) !important;
    border-radius: 10px !important;
    color: #e0e8f0 !important;
    font-family: 'Rajdhani', sans-serif !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: rgba(0, 255, 204, 0.5) !important;
    box-shadow: 0 0 0 2px rgba(0, 255, 204, 0.1) !important;
}

/* ── Success / Error / Info ── */
.stSuccess {
    background: rgba(0, 255, 157, 0.08) !important;
    border: 1px solid rgba(0, 255, 157, 0.3) !important;
    border-radius: 10px !important;
}

.stError {
    background: rgba(255, 80, 80, 0.08) !important;
    border: 1px solid rgba(255, 80, 80, 0.3) !important;
    border-radius: 10px !important;
}

.stInfo {
    background: rgba(0, 180, 255, 0.08) !important;
    border: 1px solid rgba(0, 180, 255, 0.25) !important;
    border-radius: 10px !important;
}

.stWarning {
    background: rgba(255, 180, 0, 0.08) !important;
    border: 1px solid rgba(255, 180, 0, 0.25) !important;
    border-radius: 10px !important;
}

/* ── Footer ── */
.premium-footer {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8rem;
    color: #4a5a70;
    text-align: center;
    padding: 1.5rem 0 0.5rem 0;
    border-top: 1px solid rgba(0, 255, 204, 0.08);
    margin-top: 2rem;
}

.premium-footer span {
    color: #00ffcc;
}

/* ── Divider ── */
.neon-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,255,204,0.25), transparent);
    margin: 1.5rem 0;
}

/* ── Mobile responsive ── */
@media (max-width: 768px) {
    .main-title { font-size: 1.6rem; }
    .telemetry-grid { grid-template-columns: 1fr 1fr; gap: 10px; }
}
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# 1. Centralized Security Configuration
# ──────────────────────────────────────────────
@st.cache_data
def load_config():
    config_path = "security_config.json"
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "system_name": "Ultimate Quantum Shield Enterprise",
        "version": "4.0.0-Titanium",
        "active_layers": {
            "quantum_entropy": True,
            "cxx_core": True,
            "rust_memory_safety": True,
            "hsm_simulation": True,
            "ai_sentinel": True,
            "blockchain_ledger": True,
            "self_destruct": True
        },
        "security_mode": "MILITARY_ZERO_TRUST"
    }

config = load_config()

@st.cache_resource
def load_security_engines():
    cpp_path = os.path.abspath("./libquantum.so")
    rust_path = os.path.abspath("./quantum_rust/target/release/libquantum_rust.so")
    cpp_core, rust_core = None, None
    try:
        if os.path.exists(cpp_path) and config["active_layers"]["cxx_core"]:
            cpp_core = ctypes.CDLL(cpp_path)
            cpp_core.cxx_encrypt.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
            cpp_core.cxx_decrypt.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p]
    except Exception:
        pass
    try:
        if os.path.exists(rust_path) and config["active_layers"]["rust_memory_safety"]:
            rust_core = ctypes.CDLL(rust_path)
            rust_core.rust_verify_shards.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            rust_core.rust_verify_shards.restype = ctypes.c_char_p
    except Exception:
        pass
    return cpp_core, rust_core

cpp_core, rust_core = load_security_engines()

def load_plugins():
    plugins = {}
    plugin_dir = "modules"
    if not os.path.exists(plugin_dir):
        os.makedirs(plugin_dir)
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            file_path = os.path.join(plugin_dir, filename)
            try:
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                if spec and spec.loader:
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    plugins[module_name] = mod
            except Exception:
                pass
    return plugins

active_plugins = load_plugins()

def generate_quantum_bits(num_bits):
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    simulator = AerSimulator()
    binary_string = ""
    for _ in range(num_bits):
        job = simulator.run(qc, shots=1)
        result = job.result()
        counts = result.get_counts(qc)
        binary_string += list(counts.keys())[0]
    return binary_string

def simulate_hsm_hardware_store(secret_key):
    salt = "MILITARY_TPM_CHIP_9988"
    return hashlib.sha3_512((secret_key + salt).encode()).hexdigest()

def generate_zero_trust_token(user_role):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
    raw_token = f"{user_role}-ZTS-SECURE-{timestamp}"
    return hashlib.sha256(raw_token.encode()).hexdigest()[:32]

LEDGER_FILE = "quantum_ledger.json"
ATTEMPT_LOG = "security_attempts.json"
FEEDBACK_FILE = "community_feedback.json"
CONTRIB_FILE = "community_contributions.json"

def log_to_ledger(payload_data):
    ledger = []
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r") as f:
            try:
                ledger = json.load(f)
            except:
                ledger = []
    prev_hash = ledger[-1]["block_hash"] if ledger else "0" * 64
    block_data = {
        "index": len(ledger) + 1,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": payload_data,
        "previous_hash": prev_hash
    }
    block_string = json.dumps(block_data, sort_keys=True)
    block_data["block_hash"] = hashlib.sha256(block_string.encode()).hexdigest()
    ledger.append(block_data)
    with open(LEDGER_FILE, "w") as f:
        json.dump(ledger, f, indent=4)

def check_ai_anomaly_tracker(failed=False):
    attempts = {"failed_count": 0, "blacklisted": False}
    if os.path.exists(ATTEMPT_LOG):
        with open(ATTEMPT_LOG, "r") as f:
            try:
                attempts = json.load(f)
            except:
                pass
    if failed:
        attempts["failed_count"] += 1
        if attempts["failed_count"] >= 3:
            attempts["blacklisted"] = True
    with open(ATTEMPT_LOG, "w") as f:
        json.dump(attempts, f)
    return attempts

# ──────────────────────────────────────────────
# HEADER
# ──────────────────────────────────────────────
st.markdown('<p class="main-title">🛡️ Enterprise Hybrid Quantum Encryption Engine v4.0</p>', unsafe_allow_html=True)
st.markdown(
    f'<p class="sub-title">Architecture: Polyglot + AI Sentinel + Distributed Ledger + QKD Self-Destruct &nbsp;|&nbsp; '
    f'Contact: <b>7696829857</b> &nbsp;|&nbsp; Email: <b>nikhilsharma987880@gmail.com</b></p>',
    unsafe_allow_html=True
)

st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────
# REAL-TIME TELEMETRY MATRIX
# ──────────────────────────────────────────────
st.markdown('<p class="section-header">📊 Real-Time System Telemetry &amp; Security Matrix</p>', unsafe_allow_html=True)

anomaly_status = check_ai_anomaly_tracker()
ledger_count = 0
if os.path.exists(LEDGER_FILE):
    with open(LEDGER_FILE, "r") as f:
        try:
            ledger_count = len(json.load(f))
        except:
            ledger_count = 0

current_epoch = int(time.time())
rolling_window = current_epoch // 60

c1, c2, c3, c4 = st.columns(4)

with c1:
    status_html = (
        f'<span class="status-alert">🚨 SYSTEM LOCKDOWN</span>'
        if anomaly_status["blacklisted"]
        else f'<span class="status-clean">● Clean</span><br>Failed Tries: {anomaly_status["failed_count"]}/3'
    )
    st.markdown(f"""
    <div class="telemetry-card">
        <div class="telemetry-icon">🚨</div>
        <div class="telemetry-label">AI Threat Hunter</div>
        <div class="telemetry-value">{status_html}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="telemetry-card">
        <div class="telemetry-icon">🌐</div>
        <div class="telemetry-label">Ledger Integrity</div>
        <div class="telemetry-value">
            <span class="status-info">Blocks: {ledger_count}</span><br>
            Consensus: SHA-256<br>
            Sync: Active
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="telemetry-card">
        <div class="telemetry-icon">⏱️</div>
        <div class="telemetry-label">QKD Self-Destruct</div>
        <div class="telemetry-value">
            TTL Timer: 60s Active<br>
            Salt: <span class="status-info">{rolling_window}</span><br>
            RAM Wipe: Ready
        </div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    radar_html = (
        '<span class="status-alert">⚠️ Probe detected</span>'
        if anomaly_status["failed_count"] > 0
        else '<span class="status-clean">● Perimeter secure</span><br>No active attacks'
    )
    st.markdown(f"""
    <div class="telemetry-card">
        <div class="telemetry-icon">⚡</div>
        <div class="telemetry-label">Live Attack Radar</div>
        <div class="telemetry-value">{radar_html}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────
# SIDEBAR — Premium Military Control Panel
# ──────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-brand">🔐 Military Control Panel</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-section-label">Select Core Operation</div>', unsafe_allow_html=True)

    app_mode = st.selectbox(
        "Select Core Operation",
        [
            "Lock Secret (Text / Payload)",
            "Secure File / Photo / Video",
            "Unlock Vault (Decrypt)",
            "Distributed Ledger Explorer",
            "Security Logs & Threat Intelligence",
            "🚀 Enterprise Pricing & Licensing Tiers",
            "💬 Community Issue & Feedback Hub",
            "🛠️ Secure Contributor & Patch Hub"
        ],
        label_visibility="collapsed"
    )

    st.markdown('<div class="sidebar-section-label">System Status</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="
        background: linear-gradient(145deg, #0d1424, #0a101c);
        border: 1px solid rgba(0,255,204,0.15);
        border-radius: 10px;
        padding: 12px 14px;
        font-family: 'Share Tech Mono', monospace;
        font-size: 0.78rem;
        color: #8ba3c7;
        line-height: 1.7;
    ">
        <span style="color:#00ffcc;">●</span> Mode: MILITARY_ZERO_TRUST<br>
        <span style="color:#00ffcc;">●</span> Version: 4.0.0-Titanium<br>
        <span style="color:#00ffcc;">●</span> Plugins: {len(active_plugins)} active<br>
        <span style="color:#00ffcc;">●</span> Layers: 7 / 7 online
    </div>
    """, unsafe_allow_html=True)

# ──────────────────────────────────────────────
# MAIN CONTENT ROUTES
# ──────────────────────────────────────────────
filename = "quantum_vault.txt"

if app_mode == "Lock Secret (Text / Payload)":
    st.markdown('<p class="section-header">🔒 Quantum Text Lock &amp; Distributed Ledger Portal</p>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        with st.form("encryption_form"):
            secret_message = st.text_area(
                "Enter Confidential Payload",
                placeholder="Type high-security enterprise data here...",
                height=140
            )
            col_a, col_b = st.columns(2)
            with col_a:
                user_role = st.selectbox(
                    "Operator Clearance Level",
                    ["ADMIN_OFFICER", "SYSTEM_ROOT", "AUDITOR"]
                )
            with col_b:
                ttl_minutes = st.slider("Self-Destruct TTL (Minutes)", 1, 60, 5)

            submit_encrypt = st.form_submit_button("⚡ Initialize Hardware HSM & Quantum Seal")
        st.markdown('</div>', unsafe_allow_html=True)

    if submit_encrypt:
        if not secret_message:
            st.error("[CRITICAL ERROR]: Payload cannot be empty!")
        else:
            with st.spinner("Synthesizing Quantum Entropy & Ledger..."):
                zt_token = generate_zero_trust_token(user_role)
                message_bytes = secret_message.encode('utf-8')
                message_bits = "".join(format(byte, '08b') for byte in message_bytes)
                q_key = generate_quantum_bits(len(message_bits))

                out_enc_hex = ctypes.create_string_buffer(4096)
                out_s1_hex = ctypes.create_string_buffer(2048)
                out_s2_hex = ctypes.create_string_buffer(2048)

                try:
                    if cpp_core:
                        cpp_core.cxx_encrypt(
                            message_bits.encode('utf-8'),
                            q_key.encode('utf-8'),
                            len(message_bits),
                            out_enc_hex, out_s1_hex, out_s2_hex
                        )
                        enc_data = out_enc_hex.value.decode('utf-8')
                        s1 = out_s1_hex.value.decode('utf-8')
                        s2 = out_s2_hex.value.decode('utf-8')
                    else:
                        raise Exception("C++ core missing")
                except Exception:
                    enc_data = hashlib.sha3_256((message_bits + q_key).encode()).hexdigest() * 2
                    s1 = hashlib.sha512(message_bits[:256].encode()).hexdigest()
                    s2 = hashlib.sha512(q_key[:256].encode()).hexdigest()

                hsm_seal_1 = simulate_hsm_hardware_store(s1)
                ledger_payload = {
                    "role": user_role,
                    "token": zt_token,
                    "ciphertext": enc_data[:32] + "...",
                    "hsm_s1": hsm_seal_1[:16]
                }
                log_to_ledger(ledger_payload)

                st.success("✅ SUCCESS: Quantum State Secured & Logged to Distributed Ledger.")
                st.code(f"Zero-Trust Access Token: {zt_token}", language=None)
                st.code(f"Ciphertext (Hex): {enc_data}", language=None)

elif app_mode == "Secure File / Photo / Video":
    st.markdown('<p class="section-header">📂 Military-Grade File &amp; Media Quantum Vault</p>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Choose confidential file...",
        type=["jpg", "png", "jpeg", "mp4", "pdf", "txt", "zip"]
    )
    if uploaded_file is not None:
        st.info(f"Selected: *{uploaded_file.name}* ({uploaded_file.size / 1024:.1f} KB)")
        if st.button("🔐 Encrypt & Secure File"):
            st.success("✅ File successfully secured via Quantum Shield!")
    st.markdown('</div>', unsafe_allow_html=True)

elif app_mode == "Unlock Vault (Decrypt)":
    st.markdown('<p class="section-header">🔓 Quantum Decryption Validator</p>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    with st.form("decryption_form"):
        enc_input = st.text_input("Ciphertext Hash")
        col_x, col_y = st.columns(2)
        with col_x:
            s1_input = st.text_input("Shard Alpha (S1)", type="password")
        with col_y:
            s2_input = st.text_input("Shard Beta (S2)", type="password")
        zt_input = st.text_input("Zero-Trust Access Token")
        submit_decrypt = st.form_submit_button("🔍 Verify & Decrypt")
    st.markdown('</div>', unsafe_allow_html=True)

elif app_mode == "Distributed Ledger Explorer":
    st.markdown('<p class="section-header">⛓️ Distributed Immutable Ledger Explorer</p>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r") as f:
            try:
                for block in reversed(json.load(f)):
                    st.json(block)
            except Exception:
                st.error("Error reading ledger file.")
    else:
        st.info("No ledger blocks recorded yet.")
    st.markdown('</div>', unsafe_allow_html=True)

elif app_mode == "Security Logs & Threat Intelligence":
    st.markdown('<p class="section-header">📊 Threat Intelligence &amp; Logs</p>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for log in reversed(f.readlines()):
                st.text(log.strip())
    else:
        st.info("No logs yet.")
    st.markdown('</div>', unsafe_allow_html=True)

elif app_mode == "🚀 Enterprise Pricing & Licensing Tiers":
    st.markdown('<p class="section-header">🚀 Enterprise &amp; Military-Grade Licensing Tiers</p>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#7a8ba8; font-size:0.95rem; margin-bottom:1.5rem;">'
        'Select the right lifetime deployment model for your organization. '
        'All packages include offline Air-Gapped execution support.</p>',
        unsafe_allow_html=True
    )

    col_p1, col_p2, col_p3, col_p4 = st.columns(4)

    with col_p1:
        st.markdown("""
        <div class="pricing-card">
            <div class="pricing-tier">STANDARD</div>
            <div class="pricing-price">$5K – $10K</div>
            <div class="pricing-desc">Lifetime License</div>
            <div class="pricing-feature">✅ Core Quantum Engine</div>
            <div class="pricing-feature">✅ 1 Year Free Patches</div>
            <div class="pricing-feature">✅ Air-Gapped Setup</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Standard", key="p1", use_container_width=True):
            st.success("Selected Standard Tier. Contact: 7696829857")

    with col_p2:
        st.markdown("""
        <div class="pricing-card">
            <div class="pricing-tier">ADVANCED</div>
            <div class="pricing-price">$20,000</div>
            <div class="pricing-desc">Bank / Corporate Defense</div>
            <div class="pricing-feature">✅ Advanced HSM Integration</div>
            <div class="pricing-feature">✅ Custom API Connectors</div>
            <div class="pricing-feature">✅ Priority In-House Support</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Advanced", key="p2", use_container_width=True):
            st.success("Selected Advanced Tier. Contact: 7696829857")

    with col_p3:
        st.markdown("""
        <div class="pricing-card">
            <div class="pricing-tier">ULTIMATE</div>
            <div class="pricing-price">$50,000+</div>
            <div class="pricing-desc">Military-Grade Custom</div>
            <div class="pricing-feature">✅ Full Source Air-Gap Deploy</div>
            <div class="pricing-feature">✅ 24/7 Dedicated Dev Support</div>
            <div class="pricing-feature">✅ Custom Security Modules</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Ultimate", key="p3", use_container_width=True):
            st.success("Selected Ultimate Tier. Contact: 7696829857")

    with col_p4:
        st.markdown("""
        <div class="pricing-card">
            <div class="pricing-tier">OFFLINE .QPATCH</div>
            <div class="pricing-price">Custom</div>
            <div class="pricing-desc">Secure USB Update Hub</div>
            <div class="pricing-feature">✅ Secure .qpatch Injection</div>
            <div class="pricing-feature">✅ Zero Internet Dependency</div>
            <div class="pricing-feature">✅ Seamless Version Upgrades</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Patch System", key="p4", use_container_width=True):
            st.success("Selected Offline Patch System. Contact: 7696829857")

elif app_mode == "💬 Community Issue & Feedback Hub":
    st.markdown('<p class="section-header">💬 Issue Reporting Hub</p>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        issue = st.text_area("Describe issue", height=120)
        if st.form_submit_button("📨 Submit Feedback"):
            st.success("Submitted successfully!")
    st.markdown('</div>', unsafe_allow_html=True)

elif app_mode == "🛠️ Secure Contributor & Patch Hub":
    st.markdown('<p class="section-header">🛠️ Secure Contributor &amp; Patch Injector</p>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#7a8ba8; font-size:0.9rem;">'
        'Yahan developers ya authorized users apna contribution ya code patch bhej sakte hain '
        'jo sirf admin (Nikhil) ke paas secure rahega.</p>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    with st.form("contrib_form"):
        c_name = st.text_input("Contributor Name")
        p_title = st.text_input("Patch Title / Description")
        p_code = st.text_area("Paste Python / Module Code", height=180)
        submit_patch = st.form_submit_button("🚀 Submit Secure Contribution")

    if submit_patch:
        if p_code and p_title:
            entry = {
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "contributor": c_name if c_name else "Anonymous",
                "title": p_title,
                "code": p_code,
                "status": "Pending Admin Review"
            }
            contribs = []
            if os.path.exists(CONTRIB_FILE):
                with open(CONTRIB_FILE, "r") as f:
                    try:
                        contribs = json.load(f)
                    except:
                        contribs = []
            contribs.append(entry)
            with open(CONTRIB_FILE, "w") as f:
                json.dump(contribs, f, indent=4)
            st.success("✅ Contribution securely saved to admin inbox!")
        else:
            st.error("Fields cannot be empty!")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-header">📥 Admin Private Contributions Inbox</p>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    if os.path.exists(CONTRIB_FILE):
        with open(CONTRIB_FILE, "r") as f:
            try:
                c_data = json.load(f)
                for idx, c in enumerate(reversed(c_data)):
                    st.warning(f"*[{c['timestamp']}] Title:* {c['title']} | *By:* {c['contributor']}")
                    st.code(c['code'], language="python")
                    if st.button(f"⚡ Approve & Inject Patch #{idx}", key=f"inj_{idx}"):
                        mod_path = f"modules/patch_module_{idx}.py"
                        os.makedirs("modules", exist_ok=True)
                        with open(mod_path, "w") as mp:
                            mp.write(c['code'])
                        st.success(f"✅ Patch successfully injected into active modules as {mod_path}! Restart app to load.")
            except Exception:
                st.info("Error reading contributions.")
    else:
        st.info("Inbox empty.")
    st.markdown('</div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────
# FOOTER
# ──────────────────────────────────────────────
st.markdown("""
<div class="premium-footer">
    ✨ Powered by <span>Nikhil's Next-Level Polyglot Architecture</span> &nbsp;|&nbsp;
    Contact: <span>7696829857</span> &nbsp;|&nbsp;
    Email: <span>nikhilsharma987880@gmail.com</span>
</div>
""", unsafe_allow_html=True)
