users = ['Connor', 'Abbey']

def getKey(username):
    print('username')

def getPassword(key):
    print('key')  

def checkPassword(password):
    print('Checking password')

def loginUsers(username, password):
    if username in users:
        key = getKey(username)
        
    else:
        return 'We do not have user {0}.'.format(username)

loginUsers('Connors', 'Life')





