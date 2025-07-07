from import_libs import *
def get_steam_id_from_local():
    local_app_data_path = os.path.expandvars(r"%localappdata%\Pal\Saved\SaveGames")
    if os.path.exists(local_app_data_path):
        subdirs = [d for d in os.listdir(local_app_data_path) if os.path.isdir(os.path.join(local_app_data_path, d))]
        return subdirs[0] if subdirs else None
    return None
steam_id_from_local = get_steam_id_from_local()
if steam_id_from_local:
    try:
        steam_id = int(steam_id_from_local)
        palworld_uid = steamIdToPlayerUid(steam_id)
        nosteam_uid = PlayerUid2NoSteam(int.from_bytes(toUUID(palworld_uid).raw_bytes[0:4], byteorder='little')) + "-0000-0000-0000-000000000000"
        print(f"Your SteamID: {steam_id_from_local}")
        print(f"Palworld UID: {str(palworld_uid).upper()}")
        print(f"NoSteam UID: {nosteam_uid.upper()}")
    except ValueError:
        print("Invalid Steam ID found locally.")
steam_input = input("Enter Steam ID (with or without 'steam_' or full URL): ")
if not steam_input: sys.exit()
if "steamcommunity.com/profiles/" in steam_input:
    steam_input = steam_input.split("steamcommunity.com/profiles/")[1].split("/")[0]
elif steam_input.startswith("steam_"):
    steam_input = steam_input[6:]
try:
    steam_id = int(steam_input)
    palworld_uid = steamIdToPlayerUid(steam_id)
    nosteam_uid = PlayerUid2NoSteam(int.from_bytes(toUUID(palworld_uid).raw_bytes[0:4], byteorder='little')) + "-0000-0000-0000-000000000000"
    print("Palworld UID:", str(palworld_uid).upper())
    print("NoSteam UID:", nosteam_uid.upper())
except ValueError:
    print("Invalid Steam ID entered. Please provide a valid number.")