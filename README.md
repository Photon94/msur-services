# MSUR Service

Service for communication with AUV "Ivan"

## Build
```bash
make build
```

## Run
```bash
./dist/main
```

## Install Ubuntu dependencies

```bash
sudo apt install virtualenv
virtualenv --python=python3 env
pip install pyinstaller msur-packages
make build
make install
systemctl enable msur-services
systemctl start msur-services
```