import requests

def scan_users(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            users = response.json()  # Kthehen të gjithë përdoruesit nga përgjigja JSON
            for user in users:
                print(user)
        else:
            print("Kodi i statusit:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Gabim gjatë kërkesës:", str(e))

def main():
    url = input("Shkruani URL-në e targetit: ")
    scan_users(url)

if __name__ == "__main__":
    main()
