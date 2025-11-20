import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

print("BOT IMPECÁVEL v15 - RENDER.COM 24H GRÁTIS - 20/11/2025")
print("Atualização automática + zero erro + greens eternos\n")

OVER_KINGS = ["JAB","CARNAGE","MEXICAN","YAKUZA","PABLO","GANGER_29","DMITRIY","WINSTRIKE","SATO","GROOT","ALBACK","CYPHER","KANE","FIDEL","TORRES"]

def atualizar_kings():
    global OVER_KINGS
    try:
        r = requests.get("https://esoccerbet.org/best-players/")
        soup = BeautifulSoup(r.text, 'html.parser')
        novos = []
        for row in soup.select('table tr')[1:25]:
            cols = row.find_all('td')
            if len(cols) > 2:
                player = cols[1].text.strip().upper()
                if 3 <= len(player) <= 12:
                    novos.append(player)
        if novos:
            OVER_KINGS = novos[:20]
            print(f"KINGS ATUALIZADOS: {OVER_KINGS}\n")
    except:
        pass

ultima_atualizacao = 0

while True:
    try:
        if time.time() - ultima_atualizacao > 10800:  # 3 horas
            atualizar_kings()
            ultima_atualizacao = time.time()

        page = requests.get("https://esoccerbet.org/fifa-8-minutes/", timeout=15)
        soup = BeautifulSoup(page.text, 'html.parser')

        for row in soup.find_all('tr'):
            texto = row.text
            if 'vs' not in texto or '(' not in texto: continue

            try:
                team_cell = row.find('a') or row.find('span', class_='team')
                if not team_cell: continue
                full = team_cell.text
                home = full.split('vs')[0].strip()
                away = full.split('vs')[1].strip()

                hp = home.split('(')[-1].replace(')', '').strip().upper()
                ap = away.split('(')[-1].replace(')', '').strip().upper() if '(' in away else ""

                odd_cell = row.find_all('td')[-1]
                odd = ''.join(filter(str.isdigit, odd_cell.text.replace('.', '1')))  # limpa odd
                if len(odd) < 3: continue
                over35 = float(odd[:1] + '.' + odd[1:])

                if (hp in OVER_KINGS or ap in OVER_KINGS) and over35 >= 2.00:
                    print("\n" + "█" * 90)
                    print(f" GREEN IMPECÁVEL v15 → {home} vs {away}")
                    print(f" PLAYERS → {hp} × {ap} | Over 3.5 @ {over35:.2f}")
                    print(f" {datetime.now().strftime('%H:%M:%S')} → METE NA BETANO JÁ!")
                    print("█" * 90 + "\n")
            except:
                continue

        time.sleep(15)

    except Exception as e:
        print("Erro ignorado:", e)
        time.sleep(20)
