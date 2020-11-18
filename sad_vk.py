import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
key = "3c7dad26e45618a79d6a54d01d2c406b266d32ba412a1b69aefa75efd365f3024234c9544b456aa6c39b8"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message):
                from random import randint
                vk.method('messages.send',
                          {'user_id': user_id,
                           "random_id":randint(1,1000) ,
                           'message': message,}
                          )

# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            msg_send = send_message
            get_msg = event.text.lower()

            if text == 'test':
                send_message(user_id, 'hi niga')

            if text == 'привет':
                send_message(user_id, 'привет')
                if '' in text:
                    msg_send(user_id, 'шо')
                
            print(event.user_id, ':', text)
            
