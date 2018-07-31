import vk
import time
from keys import *

version = '5.50'

permissions = ['messages', 'groups']

half_an_hour = 1800

def send_message(userID):
	vk_api.messages.send(user_id = userID, message ='check')

def show_users(groupID):
	users = vk_api.groups.getMembers(group_id = groupID, sort = 'id_asc')
	return users

def show_banned(groupID):
	banned_users = vk_api.groups.getBanned(group_id = groupID)
	return banned_users

session = vk.AuthSession(app_id = bot_app_id, user_login = bot_login, user_password = bot_password, scope = permissions)

vk_api = vk.API(session, v = version)

base_users = show_users(test_group_id)
base_count_of_members = base_users['count']


while True:
	time.sleep(half_an_hour)

	black_list = []

	actualy_users = show_users(test_group_id)
	actualy_count_of_members = actu_users['count']

	for i in range(base_count_of_members):
		check = False
		for j in range(actualy_count_of_members):
			#Каждый из base должен быть в actualy
			if base_users[items][i] == actualy_users[items][j]:
				check = True
		if check == False:
			black_list.add(base_users[items][i])

	base_users = show_users(test_group_id)
	base_count_of_members = base_users['count']

	#Проанализируй тех кто в белклисте и забаненых, вычеркни тех, кто в забанненых