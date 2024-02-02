import requests

url = 'https://todoimproved.onrender.com/api/tasks/add/'
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2ODU3ODc5LCJpYXQiOjE3MDY4NTcxNzcsImp0aSI6IjBmZDMzMzA3NDkxNTQ3NTY4MGRlNTkwN2Q2YmJiZjQ3IiwidXNlcl9pZCI6NSwidXNlcm5hbWUiOiJ5dWxpYW5jZXNhciJ9.mffRyEZEBN0QhcDr3zIVtq_b8XwBkzy11haSFP_yZr8"
headers = {'Authorization': f'Bearer {access_token}'}
task_data = {
    'user_id': 5,
    'title': 'Новая задача',
    'description': 'Описание новой задачи',
    'progress': False,
}

response = requests.post(url, headers=headers, json=task_data)

print('Статус код:', response.status_code)
print('Ответ сервера:', response.text)
