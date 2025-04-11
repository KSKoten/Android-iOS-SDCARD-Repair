import subprocess

def detect_sdcard():
    # Menjalankan perintah untuk mengetahui perangkat>
    command = "lsblk -o NAME,TYPE,MOUNTPOINT | grep ->
    result = subprocess.run(command, shell=True, stdo>

    # Memeriksa output dari perintah lsblk
    if result.returncode == 0:
        output = result.stdout.strip()
        lines = output.split('\n')
        sdcard_devices = [line.split()[0] for line in>
        return sdcard_devices[0] if sdcard_devices el>
    else:
        print("Gagal mendeteksi perangkat kartu memor>
        return None

def repair_sdcard(device_path):
    # Menjalankan perintah untuk memperbaiki kartu me>
    command = f"fsck -y {device_path}"
    result = subprocess.run(command, shell=True, stdo>

    # Memeriksa hasil dari perintah fsck
    if result.returncode == 0:
        print("Kartu memori telah diperbaiki.")
    else:
        print("Gagal memperbaiki kartu memori.")

if __name__ == '__main__':
    sdcard_path = detect_sdcard()
    if sdcard_path:
        print(f"Kartu memori terdeteksi: {sdcard_path>
        repair_sdcard(sdcard_path)
    else:
        print("Kartu memori tidak ditemukan.")