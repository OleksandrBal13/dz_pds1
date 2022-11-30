import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is on')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    decoded_data = data.decode('utf-8')
    numbers = decoded_data.split()
    numbers = [float(i) for i in numbers]
    print(f'Number 1 is {numbers[0]}', f'and Number 2 is {numbers[1]}')

    async def add():
        await asyncio.sleep(0)
        result = numbers[0] + numbers[1]
        return result

    async def subt():
        await asyncio.sleep(0)
        result = numbers[0] - numbers[1]
        return result

    async def mult():
        await asyncio.sleep(0)
        result = numbers[0] * numbers[1]
        return result

    async def div():
        await asyncio.sleep(0)
        result = numbers[0] / numbers[1]
        return result


    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(add()), ioloop.create_task(subt()), ioloop.create_task(mult()), ioloop.create_task(div())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)

    message = ['Addition: ' + str(tasks[0].result()), 'Subtraction: ' + str(tasks[1].result()),
               'Multiplication: ' + str(tasks[2].result()), 'Division: ' + str(tasks[3].result())]
    message = '\n'.join(message)
    conn.send(bytes(message, encoding='UTF-8'))
    conn.close()