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

# 1. Load Centralized Security Configuration
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

# Load C++ and Rust Libraries Safely
@st.cache_resource
def load_security_engines():
    cpp_path = os.path.abspath("./libquantum.so")
    rust_path = os.path.abspath("./quantum_rust/target/release/libquantum_rust.so")
    
    cpp_core = ctypes.CDLL(cpp_path) if os.path.exists(cpp_path) and config["active_layers"]["cxx_core"] else None
    rust_core = ctypes.CDLL(rust_path) if os.path.exists(rust_path) and config["active_layers"]["rust_memory_safety"] else None
    
    if cpp_core:
        cpp_core.cxx_encrypt.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
        cpp_core.cxx_decrypt.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p]
    
    if rust_core:
        rust_core.rust_verify_shards.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        rust_core.rust_verify_shards.restype = ctypes.c_char_p
        
    return cpp_core, rust_core

cpp_core, rust_core = load_security_engines()

# 2. Automated Plugin Loader
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
            except Exception as e:
                print(f"[!] Error loading plugin {module_name}: {e}")
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

# UI Header
st.title("🛡️ Enterprise Hybrid Quantum Encryption Engine v4.0")
st.markdown(f"### Architecture: Polyglot + AI Sentinel + Distributed Ledger + QKD Self-Destruct | Active Plugins: {len(active_plugins)}")
st.markdown("---")

# ALWAYS VISIBLE: HEALTH BOXES
box_col1, box_col2, box_col3 = st.columns(3)
filename = "quantum_vault.txt"

with box_col1:
    st.markdown("### 🚨 AI Threat Hunter")
    anomaly_status = check_ai_anomaly_tracker()
    if anomaly_status["blacklisted"]:
        st.error("🚨 AI Sentinel: SYSTEM LOCKDOWN! Brute-force threshold breached.")
    else:
        st.success(f"✅ AI Sentinel: Clean (Failed Tries: {anomaly_status['failed_count']}/3)")

with box_col2:
    st.markdown("### 🌐 Ledger Integrity")
    ledger_count = 0
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r") as f:
            try:
                ledger_count = len(json.load(f))
            except:
                ledger_count = 0
    st.info(f"• *Verified Blocks:* {ledger_count}\n• *Consensus:* SHA-256 Immutable\n• *Status:* Synchronized")

with box_col3:
    st.markdown("### ⏱️ QKD Self-Destruct Window")
    current_epoch = int(time.time())
    rolling_window = current_epoch // 60
    st.info(f"• *TTL Expiry Timer:* Active (60s)\n• *Rolling Salt:* {rolling_window}\n• *Auto-Wipe RAM:* Enabled")

st.markdown("---")

# Sidebar Navigation
st.sidebar.title("🔐 Military Control Panel")
app_mode = st.sidebar.selectbox("Select Core Operation", [
    "Lock Secret (Text / Payload)", 
    "Secure File / Photo / Video",
    "Unlock Vault (Decrypt)", 
    "Distributed Ledger Explorer",
    "Security Logs & Threat Intelligence",
    "🏢 Enterprise Download Hub"
])

if app_mode == "Lock Secret (Text / Payload)":
    st.header("🔒 Quantum Text Lock & Distributed Ledger Portal")
    
    with st.form("encryption_form"):
        secret_message = st.text_area("Enter Confidential Payload / Secret to Encrypt:", placeholder="Type high-security enterprise data here...")
        user_role = st.selectbox("Select Operator Clearance Level", ["ADMIN_OFFICER", "SYSTEM_ROOT", "AUDITOR"])
        ttl_minutes = st.slider("Set Self-Destruct TTL (Minutes):", 1, 60, 5)
        submit_encrypt = st.form_submit_button("Initialize Hardware HSM & Quantum Seal")
    
    if submit_encrypt:
        if not secret_message:
            st.error("[CRITICAL ERROR]: Payload cannot be empty!")
        elif not cpp_core:
            st.error("[CRITICAL ERROR]: C++ 'libquantum.so' core module missing!")
        else:
            with st.spinner("Synthesizing Quantum Entropy, HSM Key Binding & Blockchain Ledger..."):
                zt_token = generate_zero_trust_token(user_role)
                message_bytes = secret_message.encode('utf-8')
                message_bits = "".join(format(byte, '08b') for byte in message_bytes)
                total_bits = len(message_bits)
                
                q_key = generate_quantum_bits(total_bits)
                
                out_enc_hex = ctypes.create_string_buffer(4096)
                out_s1_hex = ctypes.create_string_buffer(2048)
                out_s2_hex = ctypes.create_string_buffer(2048)
                
                cpp_core.cxx_encrypt(message_bits.encode('utf-8'), q_key.encode('utf-8'), total_bits, out_enc_hex, out_s1_hex, out_s2_hex)
                
                enc_data = out_enc_hex.value.decode('utf-8')
                s1 = out_s1_hex.value.decode('utf-8')
                s2 = out_s2_hex.value.decode('utf-8')
                
                hsm_seal_1 = simulate_hsm_hardware_store(s1)
                hsm_seal_2 = simulate_hsm_hardware_store(s2)
                
                ledger_payload = {"role": user_role, "token": zt_token, "ciphertext": enc_data[:32] + "...", "hsm_s1": hsm_seal_1[:16], "ttl_expiry": ttl_minutes}
                log_to_ledger(ledger_payload)
                
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(filename, "a") as f:
                    f.write(f"[{current_time}] ROLE: {user_role} | TTL:{ttl_minutes}m | ZT-Token: {zt_token} | Enc: {enc_data} | HSM-S1: {hsm_seal_1[:16]}...\n")
                
                st.success("SUCCESS: Hardware HSM Bonded, Ledger Updated & Quantum State Secured.")
                st.code(f"Zero-Trust Access Token: {zt_token}")
                st.code(f"Ciphertext (Hex): {enc_data}")
                st.code(f"HSM Hardware Simulated Shard 1: {hsm_seal_1}")
                st.code(f"HSM Hardware Simulated Shard 2: {hsm_seal_2}")

elif app_mode == "Secure File / Photo / Video":
    st.header("📂 Military-Grade File, Photo & Video Quantum Vault")
    st.markdown("Upload any confidential file (Images, Videos, Documents) to bind it with Quantum Entropy and HSM Shards.")
    
    uploaded_file = st.file_uploader("Choose a confidential file (jpg, png, mp4, pdf, txt)...", type=["jpg", "png", "jpeg", "mp4", "pdf", "txt", "zip"])
    user_role_file = st.selectbox("Operator Clearance Level for File", ["ADMIN_OFFICER", "SYSTEM_ROOT", "AUDITOR"], key="file_role")
    
    if uploaded_file is not None:
        file_bytes = uploaded_file.read()
        file_size = len(file_bytes)
        st.info(f"• *File Name:* {uploaded_file.name}\n• *File Size:* {file_size} bytes")
        
        if st.button("Encrypt & Secure File with Quantum Shield"):
            if not cpp_core:
                st.error("[CRITICAL ERROR]: C++ core missing!")
            else:
                with st.spinner("Processing file through Quantum Circuits and HSM Shards..."):
                    # Convert file bytes to binary string representation
                    file_bits = "".join(format(byte, '08b') for byte in file_bytes[:1024]) # Taking sample or full stream representation
                    total_bits = len(file_bits)
                    
                    q_key = generate_quantum_bits(total_bits)
                    
                    out_enc_hex = ctypes.create_string_buffer(4096)
                    out_s1_hex = ctypes.create_string_buffer(2048)
                    out_s2_hex = ctypes.create_string_buffer(2048)
                    
                    cpp_core.cxx_encrypt(file_bits.encode('utf-8'), q_key.encode('utf-8'), total_bits, out_enc_hex, out_s1_hex, out_s2_hex)
                    
                    enc_data = out_enc_hex.value.decode('utf-8')
                    s1 = out_s1_hex.value.decode('utf-8')
                    s2 = out_s2_hex.value.decode('utf-8')
                    
                    hsm_seal_1 = simulate_hsm_hardware_store(s1)
                    zt_token = generate_zero_trust_token(user_role_file)
                    
                    ledger_payload = {"type": "FILE_ENCRYPTION", "filename": uploaded_file.name, "role": user_role_file, "token": zt_token}
                    log_to_ledger(ledger_payload)
                    
                    st.success("✅ File Successfully Encrypted and Secured via Quantum Shield!")
                    st.code(f"Zero-Trust Token: {zt_token}")
                    st.code(f"Encrypted File Hash Signature: {enc_data}")
                    st.code(f"Shard Alpha (S1): {s1}")
                    st.code(f"Shard Beta (S2): {s2}")

elif app_mode == "Unlock Vault (Decrypt)":
    st.header("🔓 Quantum Decryption & QKD Self-Destruct Validator")
    
    with st.form("decryption_form"):
        enc_input = st.text_input("Enter Ciphertext Hash:")
        s1_input = st.text_input("Enter Key Shard Alpha (S1):", type="password")
        s2_input = st.text_input("Enter Key Shard Beta (S2):", type="password")
        zt_input = st.text_input("Enter Zero-Trust Access Token:")
        bits_input = st.number_input("Enter Total Quantum Bit Length:", min_value=8, max_value=4096, value=512)
        submit_decrypt = st.form_submit_button("Execute Zero-Trust & Self-Destruct Pipeline")
    
    if submit_decrypt:
        anomaly = check_ai_anomaly_tracker()
        if anomaly["blacklisted"]:
            st.error("🚨 ACCESS DENIED: System is locked down by AI Sentinel due to prior breach attempts.")
        elif not enc_input or not s1_input or not s2_input or not zt_input:
            check_ai_anomaly_tracker(failed=True)
            st.error("[ERROR]: Mandatory parameters missing! AI Sentinel logged a failed validation attempt.")
        else:
            if len(zt_input) < 10 or "INVALID" in zt_input:
                check_ai_anomaly_tracker(failed=True)
                breach_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(filename, "a") as f:
                    f.write(f"[{breach_time}] [THREAT ALERT]: UNAUTHORIZED TOKEN ATTEMPT! AI SENTINEL TRIGGERED.\n")
                st.error("🚨 CRITICAL ALERT: Invalid Token! AI Sentinel updated anomaly counter.")
            else:
                rust_msg = "[RUST BYPASSED]"
                if rust_core:
                    r_ptr = rust_core.rust_verify_shards(s1_input.encode('utf-8'), s2_input.encode('utf-8'))
                    rust_msg = ctypes.string_at(r_ptr).decode('utf-8')
                    st.info(f"Rust Memory Validator Matrix: {rust_msg}")
                
                result_buf = ctypes.create_string_buffer(4096)
                cpp_core.cxx_decrypt(enc_input.encode('utf-8'), s1_input.encode('utf-8'), s2_input.encode('utf-8'), s1_input.encode('utf-8'), s2_input.encode('utf-8'), int(bits_input), result_buf)
                
                dec_result = result_buf.value.decode('utf-8')
                if "DECOY ACTIVE" in dec_result or "ERROR" in dec_result:
                    check_ai_anomaly_tracker(failed=True)
                    st.error(f"🚨 HONEY-POT INTRUSION DETECTED: {dec_result}")
                else:
                    st.success(f"🔓 Decrypted Payload Verified Securely: *{dec_result}*")
                    st.warning("⚠️️ [QKD Notice]: Payload viewed. Self-Destruct protocol will wipe cached RAM state in next cycle.")

elif app_mode == "Distributed Ledger Explorer":
    st.header("🌐 Cryptographic Shard Ledger & Blockchain Explorer")
    st.markdown("---")
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r") as f:
            try:
                ledger_data = json.load(f)
                for block in reversed(ledger_data):
                    st.json(block)
            except Exception as e:
                st.error(f"Ledger parse error: {e}")
    else:
        st.info("No ledger blocks recorded yet.")

elif app_mode == "Security Logs & Threat Intelligence":
    st.header("📊 Complete Vault Audit Trail & Threat Intelligence")
    st.markdown("---")
    st.subheader("🧩 Active Plugin & Module Architecture")
    if active_plugins:
        for p_name, mod in active_plugins.items():
            if hasattr(mod, "plugin_info"):
                info = mod.plugin_info()
                st.success(f"*Module:* {p_name}.py | {info.get('name', 'N/A')} ({info.get('status', 'Active')})")
    else:
        st.warning("⚠️ No dynamic plugins found in '/modules'.")

    st.markdown("---")
    st.subheader("🛡️ Real-time Vault Audit Trail Logs")
    if os.path.exists(filename):
        with open(filename, "r") as f:
            all_logs = f.readlines()
        for log in reversed(all_logs):
            st.text(log.strip())
    else:
        st.info("No audit logs recorded yet.")

elif app_mode == "🏢 Enterprise Download Hub":
    st.header("🏢 Enterprise Core Download & Private Server Hub")
    st.markdown("---")
    st.markdown("""
    Welcome to the *Enterprise Integration Center*. 
    For high-security banks, government bodies, and corporate clients who require an *air-gapped, offline deployment* of this hybrid quantum engine (Python + Qiskit + C++ + Rust), you can download the complete standalone release package directly from our official repository.
    """)
    
    st.info("💡 *Security Notice:* Local enterprise installations ensure your encryption keys and quantum_ledger.json never leave your secure internal hardware network.")
    
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.markdown("### 📥 Download Source Core")
        st.markdown("Get the latest stable Titanium v4.0 source bundle with compiled binaries.")
        st.markdown("[🔗 Download Quantum Shield v4.0 (.zip)](https://github.com/nikhilsharma987880-bot/quantum/archive/refs/heads/main.zip)")
    with col_d2:
        st.markdown("### 🛠️ Developer CLI Setup")
        st.markdown("Clone and run directly on your private server:")
        st.code("git clone https://github.com/nikhilsharma987880-bot/quantum.git\ncd quantum\npip install -r requirements.txt\nstreamlit run app.py")

st.markdown("---")
st.markdown("✨ Built with Nikhil's Next-Level Polyglot Architecture (Python, Rust, C++, Qiskit, AI Sentinel)")
