from ping3 import ping
import time

hosts = {
	"Google": "google.com",
	"GitHub": "github.com",
	"Pinterest": "pinterest.com",
	"Backit": "backit.me",
	"Proglib": "proglib.io",
	"Gitea": "about.gitea.com",
	"Oxk": "okx.com",
	"GitBook": "app.gitbook.com",
	"Dropbox": "dropbox.com",
	"Pixlr": "pixlr.com"

}



print("Пингую сайты...\n" + "-" * 40)
for name, address in hosts.items():
	response = ping(address)
	if response is not None:
		print(f'✅ {name:10} — {response:.3f} сек ({address})')
	else:
		print(f"❌ {name:10} — недоступен ({address})'")

print("-" * 40)
print("Скрипт завершен. Закрытие через 10 секунд...")
time.sleep(10)