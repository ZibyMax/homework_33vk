import requests


def get_friends(id):
    service_key = '497d9bc6497d9bc6497d9bc626491f5e8e4497d497d9bc6138c218f294555fb7cc65afd'
    parameters = {
        'user_id': id,
        'access_token': service_key,
        'v': '5.74'
    }
    response = requests.get('https://api.vk.com/method/friends.get', parameters)
    return response.json()['response']['items']


def homework():
    print('Ищем общих друзей в ВК')
    first_id = input('ID первого аккаунта:')
    second_id = input('ID второго аккаунта:')

    first_friends = get_friends(first_id)
    second_friends = get_friends(second_id)
    mutual_friends = list(set(first_friends).intersection(second_friends))

    if mutual_friends:
        print('\nОбщие друзья (ссылки на страницы):')
        for friend in mutual_friends:
            print('https://vk.com/id{}'.format(friend))
    else:
        print('\nОбщих друзей нет')


homework()
