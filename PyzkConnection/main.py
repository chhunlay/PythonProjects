from zk import ZK, const
from tabulate import tabulate  # pip install tabulate

conn = None

# Include comkey=8989
zk = ZK('124.248.191.146', port=8080, timeout=120, password=8989)

try:
    print('🔌 Connecting to device ...')
    conn = zk.connect()
    print('✅ Connected!')

    print('⛔ Disabling device ...')
    conn.disable_device()

    print(f'💾 Firmware Version: {conn.get_firmware_version()}')

    # 🔹 Get all users
    users = conn.get_users()
    if users:
        table_users = []
        for u in users:
            privilege = 'Admin' if u.privilege == const.USER_ADMIN else 'User'
            table_users.append([
                u.uid,
                u.user_id,
                u.name,
                privilege
            ])

        print(f"\n👥 Total Users: {len(users)}")
        # print(tabulate(
        #     table_users,
        #     headers=["UID", "User ID", "Name", "Privilege"],
        #     tablefmt="grid"
        # ))
    else:
        print("⚠️ No users found on the device.")

    # Create a lookup for user names
    user_map = {u.user_id: u.name for u in users}

    # 🔹 Get all attendance logs
    attendances = conn.get_attendance()
    print(f"\n🕒 Total attendance records: {len(attendances)}")

    if attendances:
        # Sort by timestamp (newest first)
        attendances.sort(key=lambda a: a.timestamp, reverse=True)

        # Filter only the latest 10
        latest_attendances = attendances[:10]

        table_att = []
        for att in latest_attendances:
            name = user_map.get(att.user_id, "Unknown")
            status = getattr(att, "status", "-")
            punch = getattr(att, "punch", "-")
            workcode = getattr(att, "workcode", "-")

            table_att.append([
                att.uid,
                att.user_id,
                name,
                att.timestamp,
                status,
                punch,
                workcode
            ])

        print("\n📆 Latest 10 Attendance Records:")
        print(tabulate(
            table_att,
            headers=["UID", "User ID", "Name", "Timestamp", "Status", "Punch", "Workcode"],
            tablefmt="grid"
        ))
    else:
        print("⚠️ No attendance records found.")

    print("\n🔊 Voice Test ...")
    conn.test_voice()

    print('\n✅ Re-enabling device ...')
    conn.enable_device()

except Exception as e:
    print("❌ Process terminated:", e)

finally:
    if conn:
        conn.disconnect()
        print("🔌 Device disconnected.")
