
def commands(binary_str):
    secret = []
    if binary_str[4] == '1':
        secret.append('wink')
    if binary_str[3] == '1':
        secret.append('double blink')
    if binary_str[2] == '1':
        secret.append('close your eyes')
    if binary_str[1] == '1':
        secret.append('jump')
    if binary_str[0] == '1':
        secret.reverse()
    return secret
            
