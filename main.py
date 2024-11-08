import requests
import cx_Oracle
import pandas as pd

# Oracle DB connection setup
def connect_to_oracle():
    #dsn_tns = cx_Oracle.makedsn('adb.us-ashburn-1.oraclecloud.com', '1522', service_name='gf63e059c3dfcbd_ax9cd7nk6hac0um4_high.adb.oraclecloud.com')
    connection = cx_Oracle.connect(user='ADMIN', password='Oracleclash2024', dsn='gf63e059c3dfcbd_ax9cd7nk6hac0um4_high')
    print("Connection successful")
    return connection

# API call with bearer token
def fetch_player_data(api_url, bearer_token):
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Extract essential data from the API response
def extract_essential_data(player_json):
    return {
        'tag': player_json.get('tag', None),
        'name': player_json.get('name', None),
        'role': player_json.get('role', 'unknown'),  # Default value if 'role' is missing
        'townHallLevel': player_json.get('townHallLevel', None),
        'expLevel': player_json.get('expLevel', None),
        'leagueName': player_json.get('league', {}).get('name', None),
        'trophies': player_json.get('trophies', None),
        'clanRank': player_json.get('clanRank', None),
        'donations': player_json.get('donations', None),
        'donationsReceived': player_json.get('donationsReceived', None)
    }

# Insert data into Oracle ATP
def insert_data_to_oracle(connection, data):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO PLAYERSTATS (tag, name, role, townHallLevel, expLevel, leagueName, trophies, clanRank, donations, donationsReceived)
    VALUES (:tag, :name, :role, :townHallLevel, :expLevel, :leagueName, :trophies, :clanRank, :donations, :donationsReceived)
    """
    cursor.execute(insert_query, data)
    connection.commit()

def check_left([],[]):

# Check if player already exits in the table
def check_player(connection, data):
    tag_json = data['tag']
    cursor = connection.cursor()
    check_query = "select count(*) from PLAYERSTATS where tag = :tag"
    cursor.execute(check_query, {'tag': tag_json})
    count = cursor.fetchone()[0]
    if count > 0:
        return True
    else:
        flag_query = "update playerstats set exit = 1 where tag = :tag"
        cursor.execute(flag_query, {'tag': tag_json})
        connection.commit()
        return False
    
# update the new donation value
def update_player(connection, data):
    tag_json = data['tag']
    new_donation = data['donations']
    cursor = connection.cursor()
    update_query = """
        update PLAYERSTATS 
        set old_donation = case when exit = 1 then donations ELSE null END,
        donations = case when exit is null then :new_donation else old_donation + :new_donation end,
        where tag = :tag
        """
    cursor.execute(update_query, {'tag': tag_json, 'new_donation': new_donation})
    connection.commit()


# Main logic
def main():
    api_url = "https://api.clashofclans.com/v1/clans/%232UJJ0VYG"
    bearer_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjA4MjliOTc0LTNmMGEtNDNkNC05NTkzLWFjMDhmNTIxZDg5MyIsImlhdCI6MTcyNjU0MjA1MCwic3ViIjoiZGV2ZWxvcGVyLzBlMzE5ZDQ3LTBhOGMtNWQxZC1kZGE1LTk3NGFmODhiZDBkMSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM1LjIyMy4xNTIuMTkxIiwiMC4wLjAuMCIsIjcxLjE3Mi4xMzguMTQ5Il0sInR5cGUiOiJjbGllbnQifV19.h1RrJNmoRGwGDxqknORas8v2Oe-X1GAK1solPjvqyM6hRt_mY6KJsftqzK2sHPCNpD6dfucjYYEOibigweB0gQ"  # Replace with your actual token
    
    player_data = fetch_player_data(api_url, bearer_token)
    if player_data:
        members = player_data.get('memberList', [])
        connection = connect_to_oracle()
        
        for player in members:
            essential_data = extract_essential_data(player)
            player_exits = check_player(connection, essential_data)
            if player_exits:
                update_player(connection, essential_data)
            else:
                insert_data_to_oracle(connection, essential_data)
        connection.close()

if __name__ == "__main__":
    main()

