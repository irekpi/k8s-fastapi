from datetime import datetime

dummy_data = 'Some text with date'


def create_file(data):
    filename = f'{datetime.now().time()}-test.txt'
    with open(f'wastebin/{filename}', 'w') as file:
        file.write(data)
    print('Done creating')


if __name__ == '__main__':
    create_file(dummy_data)