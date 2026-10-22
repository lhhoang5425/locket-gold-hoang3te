import tidevice
import time
import sys

d = tidevice.Device()
print(f"[*] Dang ket noi truc tiep voi iPhone: {d.name} (iOS {d.product_version})")

s = d.start_service("com.apple.syslog_relay")
print("[*] Bat dau lang nghe nhat ky he thong trong 12 giay...")
print("[*] Vui long MO APP LOCKET tren dien thoai ngay bay gio...")

start_time = time.time()
matching_lines = []
all_locket_lines = []

while time.time() - start_time < 12:
    try:
        raw = s.psock.recv().decode('utf-8', errors='ignore')
        if not raw:
            continue
        for line in raw.split('\n'):
            line_str = line.strip()
            if not line_str:
                continue
            lower = line_str.lower()
            if 'locket' in lower:
                all_locket_lines.append(line_str)
            if any(k in lower for k in ['revenuecat', 'firebase', 'remoteconfig', 'shadowrocket', 'mitm', 'script', 'ssl error', 'handshake']):
                matching_lines.append(line_str)
    except Exception as e:
        print("Loi doc stream:", e)
        break

print(f"\n================ KET QUA QUET LOG ================")
print(f"Tong so log lien quan den Locket: {len(all_locket_lines)}")
print(f"Tong so log lien quan den Mang / Shadowrocket / RevenueCat / Firebase: {len(matching_lines)}")

if matching_lines:
    print("\n--- Cac log mang quan trong nhat: ---")
    for l in matching_lines[:30]:
        print(l)
elif all_locket_lines:
    print("\n--- Cac log Locket ghi nhan duoc: ---")
    for l in all_locket_lines[:30]:
        print(l)
else:
    print("\n[!] Khong thay Locket phat sinh log mang trong 12 giay vua qua. Vui long dam bao ban da mo app Locket trong luc chay.")
