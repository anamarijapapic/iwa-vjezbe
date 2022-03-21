import socket, time

def connect_to_server(ip, port, retry = 10):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except Exception as e:
        print(e)
        if retry > 0:
            time.sleep(1)
            retry -=1
            connect_to_server(ip, port, retry)       

    return s

def get_source(s, ip, page):

    CRLF = '\r\n'
    get = 'GET /' + page + ' HTTP/1.1' + CRLF
    get += 'Host: '
    get += ip
    get += CRLF
    get += CRLF

    print(get)
    s.send(get.encode('utf-8'))
    response = s.recv(10000000).decode('latin-1')
    # print(response)
    return response

def get_all_links(response):
    beg = 0
    while True:
        beg_str = response.find('href="', beg)   
        if beg_str == -1:
            return links
        end_str = response.find('"', beg_str + 6)      
        link = response[beg_str + 6:end_str]

        if len(links) >= 50:
            break

        if link[-4:] == 'html' and any(substring in link for substring in substring_list) and link not in links:
            links.append(link)

        beg = end_str + 1

def crawl(links):
    for link in links:
        s = connect_to_server(ip, port)

        # managing different pages URLs so the status is 200 OK
        if '/' in link and substring_list[2] not in link:
            curr_link = link
        elif substring_list[0] in link or substring_list[2] in link:
            curr_link = substring_list[0] + '/' + link
        else:
            curr_link = substring_list[1] + '/' + link
        
        # print('URL: ' + ip + '/' + curr_link)
        response = get_source(s, ip, curr_link)
        get_all_links(response)


ip = 'www.optimazadar.hr'
port = 80
page = '1280/djelatnost1280.html'

links = [ page ]
substring_list = [ '1024', '1280', 'index' ]

s = connect_to_server(ip, port)
# print(s)
crawl(links)
s.close()

print(links)