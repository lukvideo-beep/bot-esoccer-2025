import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

print("BOT IMPECÁVEL v13 - RENDER.COM 24H GRÁTIS ETERNO - 20/11/2025")

OVER_KINGS = ["JAB","CARNAGE","MEXICAN","YAKUZA","PABLO","GANGER_29","DMITRIY","WINSTRIKE","SATO","GROOT","ALBACK","CYPHER","KANE","FIDEL","TORRES","RAUL"]

while True:
    try:
        r = requests.get("https://esoccerbet.org/fifa-8-minutes/")
        soup = BeautifulSoup(r.text, 'html.parser')
        for row in soup.find_all('tr'):
            if 'vs' not in row.text: continue
            try:
                teams = row.find('a') or row.find('span')
                if not teams: continue
                texto = teams.text
                if '(' not in texto: continue
                home = texto.split('vs')[0].strip()
                away = texto.split('vs')[1].strip()
                hp = home.split('(')[-1].replace(')', '').upper()
                ap = away.split('(')[-1].replace(')', '').upper() if '(' in away else ""

                odd = row.find_all('td')[-1].text.strip().replace('@','')
                if not odd.replace('.','').isdigit(): continue
                over35 = float(odd)

                if (hp in OVER_KINGS or ap in OVER_KINGS) and over35 >= 2.00:
                    print("\n" + "█"*80)
                    print(f"GREEN IMPECÁVEL → {home} vs {away}")
                    print(f"Players → {hp} × {ap} | Over 3.5 @ {over35:.2f}")
                    print(f"{datetime.now().strftime('%H:%M:%S')} → METE NA BETANO JÁ!")
                    print("█"*80 + "\n")
            except: continue
        time.sleep(18)
    except Exception as e:
        print("Erro ignorado:", e)
        time.sleep(20)
