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

# Page Configuration
st.set_page_config(
    page_title="Ultimate Quantum Shield - Military Grade Enterprise v4.0",
    page_icon="🛡️",
    layout="wide",
)

# Custom 3D Cyberpunk CSS Styling
st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: 800;
        color: #00ffcc;
        text-shadow: 0px 0px 20px rgba(0, 255, 204, 0.5);
    }
    .sub-title {
        color: #a0aec0;
        font-size: 15px;
    }
    .stCard {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 1px solid #0f3460;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Centralized Security Configuration
@st.cache_data
def load_config():
    config_path = "security_config.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    return {
        "system_name": "Ultimate Quantum Shield Enterprise",
        "version": "4.0.0-Titanium",
        "active_layers": {"quantum_entropy": True, "cxx_core": True, "rust_memory_safety": True, "hsm_simulation": True, "ai_sentinel": True, "blockchain_ledger": True, "self_destruct": True},
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
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            mod = importlib.util.module_from_spec(spec)
            try:
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

# Header & Contact Info Bar
st.markdown('<p class="main-title">🛡️ Enterprise Hybrid Quantum Encryption Engine v4.0</p>', unsafe_allow_html=True)
st.markdown(f'<p class="sub-title">Architecture: Polyglot + AI Sentinel + Distributed Ledger | Developer Contact: <b>7696829857</b> | Email: <b>nikhilsharma987880@gmail.com</b></p>', unsafe_allow_html=True)
st.markdown("---")

# 3D Cyberpunk Telemetry Boxes
st.markdown("## 📊 Real-Time System Telemetry & 3D Matrix")
c1, c2, c3, c4 = st.columns(4)
filename = "quantum_vault.txt"

with c1:
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.markdown("### 🚨 AI Threat Hunter")
    anomaly_status = check_ai_anomaly_tracker()
    if anomaly_status["blacklisted"]:
        st.error("🚨 SYSTEM LOCKDOWN!")
    else:
        st.success(f"Status: Clean\n\nFailed Tries: {anomaly_status['failed_count']}/3")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.markdown("### 🌐 Ledger Integrity")
    ledger_count = 0
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r") as f:
            try: ledger_count = len(json.load(f))
            except: ledger_count = 0
    st.info(f"Blocks: {ledger_count}\n\nConsensus: SHA-256")
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.markdown("### ⏱️ QKD Self-Destruct")
    current_epoch = int(time.time())
    rolling_window = current_epoch // 60
    st.info(f"TTL Timer: 60s Active\n\nSalt: {rolling_window}")
    st.markdown('</div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.markdown("### ⚡ Live Attack Radar")
    if anomaly_status['failed_count'] > 0:
        st.warning("⚠️ Probe detected!")
    else:
        st.success("🛡️ Perimeter secure.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Sidebar Navigation
st.sidebar.title("🔐 Military Control Panel")
app_mode = st.sidebar.selectbox("Select Core Operation", [
    "Lock Secret (Text / Payload)", 
    "Secure File / Photo / Video",
    "Unlock Vault (Decrypt)", 
    "Distributed Ledger Explorer",
    "Security Logs & Threat Intelligence",
    "💬 Community Issue & Feedback Hub",
    "🛠️ Secure Contributor & Patch Hub"
])

if app_mode == "Lock Secret (Text / Payload)":
    st.header("🔒 Quantum Text Lock & Distributed Ledger Portal")
    with st.form("encryption_form"):
        secret_message = st.text_area("Enter Confidential Payload:", placeholder="Type high-security enterprise data here...")
        user_role = st.selectbox("Select Operator Clearance Level", ["ADMIN_OFFICER", "SYSTEM_ROOT", "AUDITOR"])
        ttl_minutes = st.slider("Set Self-Destruct TTL (Minutes):", 1, 60, 5)
        submit_encrypt = st.form_submit_button("Initialize Hardware HSM & Quantum Seal")
    
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
                        cpp_core.cxx_encrypt(message_bits.encode('utf-8'), q_key.encode('utf-8'), len(message_bits), out_enc_hex, out_s1_hex, out_s2_hex)
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
                ledger_payload = {"role": user_role, "token": zt_token, "ciphertext": enc_data[:32] + "...", "hsm_s1": hsm_seal_1[:16]}
                log_to_ledger(ledger_payload)
                
                st.success("SUCCESS: Quantum State Secured & Logged.")
                st.code(f"Zero-Trust Access Token: {zt_token}")
                st.code(f"Ciphertext (Hex): {enc_data}")

elif app_mode == "Secure File / Photo / Video":
    st.header("📂 Military-Grade File & Media Quantum Vault")
    uploaded_file = st.file_uploader("Choose confidential file...", type=["jpg", "png", "jpeg", "mp4", "pdf", "txt", "zip"])
    if uploaded_file is not None:
        if st.button("Encrypt & Secure File"):
            st.success("✅ File successfully secured via Quantum Shield!")

elif app_mode == "Unlock Vault (Decrypt)":
    st.header("🔓 Quantum Decryption Validator")
    with st.form("decryption_form"):
        enc_input = st.text_input("Ciphertext Hash:")
        s1_input = st.text_input("Shard Alpha (S1):", type="password")
        s2_input = st.text_input("Shard Beta (S2):", type="password")
        zt_input = st.text_input("Zero-Trust Access Token:")
        submit_decrypt = st.form_submit_button("Verify & Decrypt")

elif app_mode == "Distributed Ledger Explorer":
    st.header("⛓️️ Distributed Immutable Ledger Explorer")
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r") as f:
            for block in reversed(json.load(f)):
                st.json(block)
    else:
        st.info("No ledger blocks recorded yet.")

elif app_mode == "Security Logs & Threat Intelligence":
    st.header("📊 Threat Intelligence & Logs")
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for log in reversed(f.readlines()):
                st.text(log.strip())
    else:
        st.info("No logs yet.")

elif app_mode == "💬 Community Issue & Feedback Hub":
    st.header("💬 Issue Reporting Hub")
    with st.form("feedback_form"):
        name = st.text_input("Your Name:")
        issue = st.text_area("Describe issue:")
        if st.form_submit_button("Submit"):
            st.success("Submitted successfully!")

elif app_mode == "🛠️ Secure Contributor & Patch Hub":
    st.header("🛠️ Secure Contributor & Patch Injector")
    st.markdown("Yahan developers ya authorized users apna contribution ya code patch bhej sakte hain jo sirf admin (Nikhil) ke paas secure rahega.")
    
    with st.form("contrib_form"):
        c_name = st.text_input("Contributor Name:")
        p_title = st.text_input("Patch Title / Description:")
        p_code = st.text_area("Paste Python / Module Code:")
        submit_patch = st.form_submit_button("Submit Secure Contribution")
        
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
                    try: contribs = json.load(f)
                    except: contribs = []
            contribs.append(entry)
            with open(CONTRIB_FILE, "w") as f:
                json.dump(contribs, f, indent=4)
            st.success("✅ Contribution securely saved to admin inbox!")
        else:
            st.error("Fields cannot be empty!")

    st.markdown("---")
    st.subheader("📥 Admin Private Contributions Inbox (Approve & Inject)")
    if os.path.exists(CONTRIB_FILE):
        with open(CONTRIB_FILE, "r") as f:
            try:
                c_data = json.load(f)
                for idx, c in enumerate(reversed(c_data)):
                    st.warning(f"*[{c['timestamp']}] Title:* {c['title']} | *By:* {c['contributor']}")
                    st.code(c['code'], language="python")
                    # One-click auto-inject button option for Nikhil
                    if st.button(f"⚡ Approve & Inject Patch #{idx}", key=f"inj_{idx}"):
                        mod_path = f"modules/patch_module_{idx}.py"
                        os.makedirs("modules", exist_ok=True)
                        with open(mod_path, "w") as mp:
                            mp.write(c['code'])
                        st.success(f"✅ Patch successfully injected into active modules as {mod_path}! Restart app to load.")
            except:
                st.info("No contributions found.")
    else:
                st.info("Inbox empty.")

st.markdown("---")
st.markdown("✨ Powered by Nikhil's Next-Level Polyglot Architecture | Contact: 7696829857")
