
def commands(binary_str):
    binary_list = list(binary_str)
    secret = []
    for i in range(len(binary_list) -1, -1, -1):
        if i == 4 and binary_list[i] == '1':
            secret.append('wink')
        if i == 3 and binary_list[i] == '1':
            secret.append('double blink')
        if i == 2 and binary_list[i] == '1':
            secret.append('close your eyes')
        if i == 1 and binary_list[i] == '1':
            secret.append('jump')
        if i == 0 and binary_list[i] == '1':
            secret.reverse()
    return secret
            
