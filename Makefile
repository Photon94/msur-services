
build:
	pyinstaller msur-services.py --onefile

install:
	sudo cp dist/msur-services /usr/bin/ && sudo cp msur-services.service /lib/systemd/system/
