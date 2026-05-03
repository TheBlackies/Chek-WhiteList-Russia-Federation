from ping3 import ping
import time

main_hosts = {
	"Google": "google.com",
	"GitHub": "github.com",
	"Pinterest": "pinterest.com",
	# "Backit": "backit.me", изменить хост т.к. работает при БС
	# "Proglib": "proglib.io", изменить хост т.к. работает при БС
	"Gitea": "about.gitea.com",
	"Oxk": "okx.com",
	"GitBook": "app.gitbook.com",
	"Dropbox": "dropbox.com",
	"Pixlr": "pixlr.com"
}

WhiteList_host = {
  "Max" : "max.ru",
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
all_main_ok = check_hosts(main_hosts)
print("-" * 40)

if all_main_ok:
  print("✅ Все основные хосты доступны. Вы вне зоне действий БС.")

elif not all_main_ok:
  any_main_available = any(ping(host) not in [None, False] for host in main_hosts.values())
  
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
