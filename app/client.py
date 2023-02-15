import requests



response = requests.post('http://127.0.0.1:5050/photo/',
                        json={"input_path": "start.txt",
                            "output_path": "finish.txt"
                              }
                        )


print(response.status_code)
# print(response.json())
# print(response.text)

response = requests.get('http://127.0.0.1:5050/photo/1/')

print(response.status_code)
print(response.text)
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


# app         | [2023-02-15 18:55:04,689: ERROR/MainProcess] consumer: Cannot connect to amqp://guest:**@127.0.0.1:5672//: [Errno 111] Connection refused.
# app         | Trying again in 18.00 seconds... (9/100)

