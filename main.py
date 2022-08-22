import msur_packages.driver.protocol as p
import os
from msur_packages.driver.service import Service
import anyio
import signal

# адрес и порт аппарата
AUV_PORT = int(os.getenv('MSUR_AUV_PORT', '2030'))
AUV_ADDRESS = os.getenv('MSUR_AUV_ADDRESS', '127.0.0.1')
LOCAL_PORT = int(os.getenv('MSUR_LOCAL_PORT', '2065'))
LOCAL_ADDRESS = os.getenv('MSUR_LOCAL_ADDRESS', '127.0.0.1')


auv = p.Service(AUV_ADDRESS, AUV_PORT, LOCAL_PORT, LOCAL_ADDRESS)
service = Service(auv)


async def signal_handler(scope):
    with anyio.open_signal_receiver(signal.SIGINT, signal.SIGTERM) as signals:
        async for signum in signals:
            if signum == signal.SIGINT:
                print('Ctrl+C pressed!')
            else:
                print('Terminated!')
            await scope.cancel()
            return


async def main():
    async with anyio.create_task_group() as tg:
        tg.start_soon(signal_handler, tg.cancel_scope)
        tg.start_soon(auv.run_sender)
        tg.start_soon(auv.run_listener)
        tg.start_soon(service.run)


if __name__ == '__main__':
    anyio.run(main)
