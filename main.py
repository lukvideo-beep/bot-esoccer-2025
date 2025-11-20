import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

print("BOT IMPECÁVEL v12 - 24H GRÁTIS ETERNO NA RENDER.COM")
print("Atualização automática + mais rápido do mundo - 20/11/2025")

OVER_KINGS = ["JAB", "CARNAGE", "MEXICAN", "YAKUZA", "PABLO", "GANGER_29", "DMITRIY", "WINSTRIKE", "SATO", "GROOT", "ALBACK", "CYPHER", "KANE", "FIDEL", "TORRES"]

while True:
    try:
        r = requests.get("https://esoccerbet.org/fifa-8-minutes/", timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        for row in soup.select('tr'):
            text = row.text
            if 'vs' not in text or '(' not in text: continue
            
            try:
                teams = row.select_one('.team-name, .teams, td')
                if not teams: continue
                full = teams.text
                home, away = full.split('vs')
                hp = home.split('(')[-1].replace(')', '').strip().upper()
                ap = away.split('(')[-1].replace(')', '').strip().upper() if '(' in away else ""
                
                odd = row.select_one('.odd, .over-odd')
                if not odd: continue
                odd_text = odd.text.strip().replace('@', '').replace(' ', '')
                if not odd_text.replace('.', '').isdigit(): continue
                over35 = float(odd_text)
                
                if (hp in OVER_KINGS or ap in OVER_KINGS) and over35 >= 2.00:
                    print("\n" + "█" * 90)
                    print(f" GREEN IMPECÁVEL → {home.strip()} vs {away.strip()}")
                    print(f" Players → {hp} × {ap} | Over 3.5 @ {over35:.2f}")
                    print(f" {datetime.now().strftime('%H:%M:%S')} → METE NA BETANO JÁ!!!")
                    print("█" * 90 + "\n")
            except:
                continue
                
        time.sleep(15)
        
    except Exception as e:
        print(f"Erro ignorado: {e}")
        time.sleep(15)
