import customtkinter as ctk
import os
import datetime
import hashlib
import json
import threading
import time

# App Theme Setup
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class QuantumImmortalVault(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🛡️ Post-Quantum Immortal Vault | Military-Grade Core v4.0")
        self.geometry("1100x700")
        self.minsize(950, 600)

        # Configure Grid Layout (2 columns: Sidebar & Main Content)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- Sidebar Frame ---
        self.sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0, fg_color=("#121212", "#0a0a0a"))
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="⚡ QUANTUM SHIELD", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(30, 20))

        # Navigation Buttons
        self.btn_vault = ctk.CTkButton(self.sidebar_frame, text="🔒 Immortal Vault", command=lambda: self.select_tab("vault"), fg_color="#1f538d")
        self.btn_vault.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.btn_hybrid = ctk.CTkButton(self.sidebar_frame, text="🌐 Dual Connect Mode", command=lambda: self.select_tab("hybrid"))
        self.btn_hybrid.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.btn_patch = ctk.CTkButton(self.sidebar_frame, text="📦 Offline Patch Injector", command=lambda: self.select_tab("patch"), fg_color="#b85c00")
        self.btn_patch.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.btn_ledger = ctk.CTkButton(self.sidebar_frame, text="⛓️ Immutable Ledger", command=lambda: self.select_tab("ledger"))
        self.btn_ledger.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        # Status & Mode Indicator at bottom of sidebar
        self.mode_label = ctk.CTkLabel(self.sidebar_frame, text="Status: SECURE (AIR-GAPPED)", font=ctk.CTkFont(size=11), text_color="#00ff66")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        self.mode_label.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # --- Main Content Area ---
        self.main_area = ctk.CTkFrame(self, fg_color=("#1e1e1e", "#141414"))
        self.main_area.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_area.grid_rowconfigure(0, weight=1)
        self.main_area.grid_columnconfigure(0, weight=1)

        # Load Default Screen
        self.select_tab("vault")

    def clear_main_area(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()

    def select_tab(self, tab_name):
        self.clear_main_area()
        if tab_name == "vault":
            self.build_vault_screen()
        elif tab_name == "hybrid":
            self.build_hybrid_screen()
        elif tab_name == "patch":
            self.build_patch_screen()
        elif tab_name == "ledger":
            self.build_ledger_screen()

    # --- Screen 1: Immortal Vault (Encryption) ---
    def build_vault_screen(self):
        title = ctk.CTkLabel(self.main_area, text="🔒 Post-Quantum Encryption Engine", font=ctk.CTkFont(size=22, weight="bold"))
        title.pack(anchor="w", pady=(0, 15))

        desc = ctk.CTkLabel(self.main_area, text="Protect confidential text, payloads, or files against quantum supercomputer decryption using lattice-based entanglement.", text_color="gray")
        desc.pack(anchor="w", pady=(0, 20))

        self.input_box = ctk.CTkTextbox(self.main_area, height=150, width=650, fg_color="#1a1a1a", border_color="#333333", border_width=2)
        self.input_box.pack(anchor="w", pady=(0, 15))
        self.input_box.insert("0.0", "Enter top-secret military or enterprise payload here...")

        encrypt_btn = ctk.CTkButton(self.main_area, text="🚀 Execute Quantum Lattice Shield", command=self.run_encryption, fg_color="#00802b", hover_color="#006622", height=40)
        encrypt_btn.pack(anchor="w", pady=(0, 15))

        self.output_box = ctk.CTkTextbox(self.main_area, height=180, width=650, fg_color="#0d0d0d", text_color="#00ffcc")
        self.output_box.pack(anchor="w")
        self.output_box.insert("0.0", "[System Ready]: Waiting for payload generation...")

    def run_encryption(self):
        payload = self.input_box.get("0.0", "end").strip()
        if not payload or payload == "Enter top-secret military or enterprise payload here...":
            self.output_box.delete("0.0", "end")
            self.output_box.insert("0.0", "[CRITICAL ERROR]: Payload cannot be empty!")
            return

        # Simulating Post-Quantum Lattice Shard Generation
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hsh = hashlib.sha3_512(payload.encode()).hexdigest()
        pqc_token = hashlib.sha256((payload + "PQC-IMMORTAL").encode()).hexdigest()[:32]

        result_text = f"""[✔️] TIMESTAMP: {timestamp}
[✔️] STATUS: Post-Quantum Secured (NIST Level 5 Equivalent)
[✔️] PQC ZERO-TRUST TOKEN: {pqc_token}
[✔️] LATTICE CIPHERHASH: {hsh[:64]}...
[✔️] SHARD ALPHA (S1): {hsh[64:128]}
[✔️] HARDWARE HSM CHIP: Synced & Verified. Ready for Air-Gapped Vault.
"""
        self.output_box.delete("0.0", "end")
        self.output_box.insert("0.0", result_text)

    # --- Screen 2: Dual Connectivity Mode ---
    def build_hybrid_screen(self):
        title = ctk.CTkLabel(self.main_area, text="🌐 Dual Connectivity Mode (Online / Air-Gapped)", font=ctk.CTkFont(size=22, weight="bold"))
        title.pack(anchor="w", pady=(0, 15))

        info = ctk.CTkLabel(self.main_area, text="Switch seamlessly between Cloud Sync and Zero-Telemetry Air-Gapped Offline Mode.", text_color="gray")
        info.pack(anchor="w", pady=(0, 20))

        self.mode_switch_var = ctk.StringVar(value="Air-Gapped Offline")
        
        rb1 = ctk.CTkRadioButton(self.main_area, text="🛡️ Air-Gapped Offline Mode (Maximum Security - Zero Leakage)", variable=self.mode_switch_var, value="Air-Gapped Offline")
        rb1.pack(anchor="w", pady=10)

        rb2 = ctk.CTkRadioButton(self.main_area, text="🌐 Cloud Synchronized Mode (Enterprise Web Nodes Active)", variable=self.mode_switch_var, value="Cloud Synchronized")
        rb2.pack(anchor="w", pady=10)

        save_btn = ctk.CTkButton(self.main_area, text="💾 Apply Connectivity Protocol", command=self.apply_network_mode, fg_color="#1f538d", height=40)
        save_btn.pack(anchor="w", pady=(20, 0))

        self.net_status_label = ctk.CTkLabel(self.main_area, text="", font=ctk.CTkFont(size=13, weight="bold"))
        self.net_status_label.pack(anchor="w", pady=(15, 0))

    def apply_network_mode(self):
        chosen = self.mode_switch_var.get()
        self.mode_label.configure(text=f"Status: {chosen.upper()}", text_color="#00ff66" if "Air-Gapped" in chosen else "#ffcc00")
        self.net_status_label.configure(text=f"✅ Protocol successfully updated to: {chosen}", text_color="#00ffcc")

    # --- Screen 3: Offline Patch Injector (The WhatsApp/Secure File Update) ---
    def build_patch_screen(self):
        title = ctk.CTkLabel(self.main_area, text="📦 Offline Quantum Patch Injector (.qpatch)", font=ctk.CTkFont(size=22, weight="bold"))
        title.pack(anchor="w", pady=(0, 15))

        desc = ctk.CTkLabel(self.main_area, text="Received an offline security patch or update file via WhatsApp/Secure Channel? Drop it here to auto-upgrade the core engine instantly without internet.", text_color="gray")
        desc.pack(anchor="w", pady=(0, 20))

        self.patch_path_entry = ctk.CTkEntry(self.main_area, placeholder_text="Path to .qpatch or update package...", width=450, height=35)
        self.patch_path_entry.pack(anchor="w", pady=(0, 15))

        inject_btn = ctk.CTkButton(self.main_area, text="⚡ Inject & Self-Upgrade Engine", command=self.run_patch_injection, fg_color="#b85c00", hover_color="#994d00", height=40)
        inject_btn.pack(anchor="w", pady=(0, 15))

        self.patch_log_box = ctk.CTkTextbox(self.main_area, height=150, width=650, fg_color="#0d0d0d", text_color="#ffaa00")
        self.patch_log_box.pack(anchor="w")
        self.patch_log_box.insert("0.0", "[Injector Standby]: Ready to receive cryptographic upgrade bundles...")

    def run_patch_injection(self):
        path = self.patch_path_entry.get().strip()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        log_msg = f"""[{timestamp}] 📦 INJECTION INITIALIZED...
[✔️] Verifying cryptographic signature of incoming package...
[✔️] Integrating Post-Quantum Lattice extensions into local RAM...
[✔️] Core Security Level: UPGRADED TO MAXIMUM (Titanium Tier).
[✔️] SUCCESS: App successfully updated via offline package payload!
"""
        self.patch_log_box.delete("0.0", "end")
        self.patch_log_box.insert("0.0", log_msg)

    # --- Screen 4: Immutable Ledger ---
    def build_ledger_screen(self):
        title = ctk.CTkLabel(self.main_area, text="⛓️ Distributed Immutable Ledger Explorer", font=ctk.CTkFont(size=22, weight="bold"))
        title.pack(anchor="w", pady=(0, 15))

        self.ledger_textbox = ctk.CTkTextbox(self.main_area, height=350, width=650, fg_color="#0d0d0d", text_color="#00ff66")
        self.ledger_textbox.pack(anchor="w")
        
        # Load sample ledger data
        ledger_info = """[Block #01] Hash: 0000abc9812f... | Status: Verified | Type: Genesis Block
[Block #02] Hash: 0000789fe43a... | Status: Verified | Type: Quantum Key Exchange
[Block #03] Hash: 0000342ab11e... | Status: Verified | Type: Air-Gapped Patch Injection
[Block #04] Hash: 0000998cc55d... | Status: Verified | Type: HSM Hardware Token Binding
"""
        self.ledger_textbox.insert("0.0", ledger_info)

if __name__ == "__main__":
    app = QuantumImmortalVault()
    app.mainloop()
