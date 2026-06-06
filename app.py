import streamlit as st

# ==========================
# KONFIGURASI HALAMAN
# ==========================
st.set_page_config(
    page_title="Cyber Security Chatbot",
    page_icon="🔐",
    layout="centered"
)

# ==========================
# JUDUL
# ==========================
st.title("🔐 Cyber Security Chatbot")
st.subheader("Implementasi Finite State Automata (FSA)")
st.write(
    "Chatbot edukasi keamanan siber yang mengenali beberapa topik keamanan digital."
)

# ==========================
# STATE AUTOMATA
# ==========================
states = {

    "phishing": {
        "state": "STATE_PHISHING",
        "response": """
Phishing adalah teknik penipuan untuk mencuri informasi pribadi
seperti username, password, atau data kartu kredit melalui email
atau website palsu.
"""
    },

    "malware": {
        "state": "STATE_MALWARE",
        "response": """
Malware adalah perangkat lunak berbahaya yang dirancang untuk
merusak, mencuri, atau mengganggu sistem komputer.
"""
    },

    "ransomware": {
        "state": "STATE_RANSOMWARE",
        "response": """
Ransomware adalah malware yang mengenkripsi data korban dan
meminta tebusan agar data dapat dipulihkan.
"""
    },

    "virus": {
        "state": "STATE_VIRUS",
        "response": """
Virus komputer adalah program berbahaya yang dapat menyebar
dan merusak file atau sistem komputer.
"""
    },

    "password": {
        "state": "STATE_PASSWORD",
        "response": """
Tips password aman:
- Minimal 8 karakter
- Gunakan huruf besar dan kecil
- Gunakan angka
- Gunakan simbol
- Jangan gunakan tanggal lahir
"""
    },

    "firewall": {
        "state": "STATE_FIREWALL",
        "response": """
Firewall berfungsi menyaring lalu lintas jaringan dan mencegah
akses tidak sah ke sistem komputer.
"""
    },

    "vpn": {
        "state": "STATE_VPN",
        "response": """
VPN (Virtual Private Network) digunakan untuk mengenkripsi
koneksi internet dan meningkatkan privasi pengguna.
"""
    },

    "antivirus": {
        "state": "STATE_ANTIVIRUS",
        "response": """
Antivirus adalah perangkat lunak yang digunakan untuk
mendeteksi, mencegah, dan menghapus malware.
"""
    },

    "2fa": {
        "state": "STATE_2FA",
        "response": """
2FA (Two Factor Authentication) adalah metode keamanan
yang membutuhkan dua langkah verifikasi sebelum login.
"""
    },

    "sql injection": {
        "state": "STATE_SQL_INJECTION",
        "response": """
SQL Injection adalah serangan yang memanfaatkan celah
pada input aplikasi untuk menjalankan perintah SQL berbahaya.
"""
    },

    "social engineering": {
        "state": "STATE_SOCIAL_ENGINEERING",
        "response": """
Social Engineering adalah teknik manipulasi psikologis
untuk memperoleh informasi rahasia dari korban.
"""
    },

    "data breach": {
        "state": "STATE_DATA_BREACH",
        "response": """
Data Breach adalah kebocoran data sensitif akibat akses
yang tidak sah terhadap sistem.
"""
    },

    "wifi": {
        "state": "STATE_WIFI_SECURITY",
        "response": """
Untuk mengamankan WiFi:
- Gunakan WPA2 atau WPA3
- Ganti password default
- Matikan WPS
- Perbarui firmware router
"""
    },

    "cyberbullying": {
        "state": "STATE_CYBERBULLYING",
        "response": """
Cyberbullying adalah tindakan perundungan yang dilakukan
melalui media digital seperti media sosial atau chat.
"""
    }
}

# ==========================
# INPUT USER
# ==========================
user_input = st.text_input(
    "Masukkan pertanyaan:",
    placeholder="Contoh: Apa itu phishing?"
)

# ==========================
# PROSES INPUT
# ==========================
if user_input:

    text = user_input.lower()

    ditemukan = False

    for keyword in states:

        if keyword in text:

            st.success(
                f"State Aktif : {states[keyword]['state']}"
            )

            st.info(
                states[keyword]["response"]
            )

            ditemukan = True
            break

    if not ditemukan:

        st.warning("""
Maaf, pertanyaan belum dikenali.

Silakan tanyakan tentang:
- phishing
- malware
- ransomware
- virus
- password
- firewall
- vpn
- antivirus
- 2fa
- sql injection
- social engineering
- data breach
- wifi
- cyberbullying
""")

# ==========================
# DAFTAR TOPIK
# ==========================
st.divider()

st.subheader("📚 Topik yang Didukung")

st.markdown("""
1. Phishing
2. Malware
3. Ransomware
4. Virus
5. Password
6. Firewall
7. VPN
8. Antivirus
9. 2FA
10. SQL Injection
11. Social Engineering
12. Data Breach
13. WiFi Security
14. Cyberbullying
""")

st.divider()

st.caption(
    "Project Teori Bahasa dan Otomata - Cyber Security Chatbot"
)