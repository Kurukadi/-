import vk
import time
from keys import *

#vk=vk_api.VkApi(login='', password='')
session = vk.AuthSession(app_id = bot_app_id, user_login = bot_login, user_password = bot_password, scope = 'messages')
vk_api = vk.API(session, v = '5.50')

vk_api.messages.send(user_id=check_user_id, message ='check')