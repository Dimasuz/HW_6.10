import requests



response = requests.post('http://127.0.0.1:5000/photo/',
                        json={'input_path': 'start.txt',
                            'output_path': 'finish.txt'
                              }
                        )


print(response.status_code)
print(response.json())
# print(response.text)

# response = requests.get('http://127.0.0.1:5000/photo/1/')
#
# print(response.status_code)
# print(response.text)
#
# response = requests.post('http://127.0.0.1:5000/adv/',
#                         json={'title': 'title_1',
#                               'descr': 'descr_1',
#                               'user_id': 2,
#                               'password': '321',
#                               }
#                         )


# print(response.status_code)
# print(response.json())
# print(response.text)
