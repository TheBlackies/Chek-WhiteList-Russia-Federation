from ping3 import ping
import time

en_hosts = {
  "Google": "google.com",
  "GitHub": "github.com",
  "Pinterest": "pinterest.com",
  "GitLab": "gitlab.com",
  "Docker": "docker.com",
  "Gitea": "about.gitea.com",
  "Oxk": "okx.com",
  "GitBook": "app.gitbook.com",
  "Dropbox": "dropbox.com",
  "Pixlr": "pixlr.com"
}

ru_hosts = {
  "Tproger": "tproger.ru",
  "Teremok": "teremok.ru", # Заменить на другой
  "Mega": "mega.ru",
  "Shoko": "shoko.ru",
  "Zenden": "zenden.ru",
  "Tvoe": "tvoe.ru",
  "Cyberlenika": "cyberleninka.ru",
  "Pikabu": "pikabu.ru", # Заменить на другой
  # "DNS": "dns-shop.ru", Заменить на другой т.к. работает при БС
  # "Mvideo": "mvideo.ru" Заменить на другой т.к. работает при БС
  # Данный список не точен и требует отдельной проверки
}

WhiteList_host = {
  "Max" : "web.max.ru",
  "Yandex" : "ya.ru",
  "Vk" : "vk.ru",
  "Avito" : "avito.ru",
  "Moex" : "moex.com",
  "RuStore" : "rustore.ru",
  "Gismeteo" : "gismeteo.ru",
  "Ozon" : "ozon.ru",
  "Wildberries" : "wildberries.ru",
  "2Gis" : "2gis.ru"
}

while True:
  host_check = input("Какие домены будем пинговать? 1 - EN. 2 - RU. Ваш выбор (бета-версия): ")

  if host_check == "1":
    host_check = en_hosts
    break
  elif host_check == "2":
    host_check = ru_hosts
    break
  else:
    print("Пожалуйста, введите либо 1 - EN, либо 2 - RU")

def check_hosts(host_dict):
  all_ok = True
  for name, address in host_dict.items():
    response = ping(address)
    if response is not None and response is not False:
      print(f'✅ {name:10} — {response:.3f} сек ({address})')
    else:
      print(f"❌ {name:10} — недоступен ({address})")
      all_ok = False
  return all_ok

print("Пингую сайты...\n" + "-" * 40)
all_main_ok = check_hosts(host_check)
print("-" * 40)

if all_main_ok:
  print("✅ Все основные хосты доступны. Вы вне зоне действий БС.")

elif not all_main_ok:
  any_main_available = any(ping(host) not in [None, False] for host in host_check.values())
  
  if any_main_available:
    print("⚠️ Часть основных хостов недоступна. Возможны блокировки.")
  else:
    print("\n❌ Основной список хостов недоступен! Проверяю Белые Списки:")
    print("-" * 40)
    all_white_ok = check_hosts(WhiteList_host)
    print("-" * 40)
    
    if all_white_ok:
      print("✅ Белые Списки работают! Вы находитесь в зоне БС.")
    else:
      any_white_available = any(ping(host) not in [None, False] for host in WhiteList_host.values())
      
      if any_white_available:
        print("⚠️ Часть Белых Списков доступна. Проблемы с сетью или частичные блокировки.")
      else:
        print("⚠️ Интернет не работает. Проверьте интернет соединение.")

print("Скрипт завершен. Закрытие через 10 секунд...")
time.sleep(10)