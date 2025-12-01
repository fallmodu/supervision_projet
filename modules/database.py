import sqlite3

DB_NAME = "supervision.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Table des appareils SNMP
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS snmp_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device TEXT,
            cpu REAL,
            ram REAL,
            throughput REAL,
            uptime TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Table Nagios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nagios_status (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            host TEXT,
            service TEXT,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Table Wireshark
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS packets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            src_ip TEXT,
            dst_ip TEXT,
            protocol TEXT,
            info TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Table des devices
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT UNIQUE,
            hostname TEXT,
            type TEXT,
            last_seen DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    conn.close()


# Fonctions d’insertion
def save_snmp(cpu, ram, device):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO snmp_data (device, cpu, ram) VALUES (?, ?, ?)", 
                   (device, cpu, ram))
    conn.commit()
    conn.close()


def save_nagios_status(host, service, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO nagios_status (host, service, status) VALUES (?, ?, ?)",
                   (host, service, status))
    conn.commit()
    conn.close()


def save_packet_info(src, dst, protocol, info):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO packets (src_ip, dst_ip, protocol, info) VALUES (?, ?, ?, ?)",
                   (src, dst, protocol, info))
    conn.commit()
    conn.close()
