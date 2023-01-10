import random
import string
import time

PORT_FILE = './port_8080'
RESPONSE_FILE = './response'


def generate_url(size=8, chars=string.ascii_uppercase + string.digits):
    return '/persons/' + ''.join(random.sample(chars, size))


def send_request(url):
    with open(PORT_FILE, 'w+') as fp:
        fp.writelines([url])

    with open(RESPONSE_FILE) as fp:
        return fp.readline()


def main():
    prev_response = None
    while 1:
        url = generate_url()
        print(f'sent request {url}')
        while 1:
            response = send_request(url)
            if response != prev_response:
                prev_response = response
                print(f'got response {response}')
                break
        time.sleep(random.randint(2, 5))


if __name__ == '__main__':
    main()
