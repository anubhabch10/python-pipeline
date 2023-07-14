import requests, os
dir_path = os.path.join(os.getcwd(), 'pdfs') #note to self
if not os.path.exists(dir_path):
    os.mkdir(dir_path)
#https://aclanthology.org/Dj-k00i/--- where j ranges from 15-17 and for each j, k is different and for eachk, i is different..
#https://aclanthology.org/D17-300i/

#2008:
for i in range (0,146):
    n = 1000 + i
    url = f'https://aclanthology.org/C08-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
        with open (os.path.join(dir_path,f'2008(1) paper-{i}.pdf'),'wb') as pdf:
            print (f'downloading file {i}')
            for packet in response.iter_content(chunk_size=1024):
                pdf.write(packet)
print('success!!')

for i in range (0,36):
     n = 2000 + i
     url = f'https://aclanthology.org/C08-{n}.pdf'
     response = requests.get(url)
     if response.status_code == 200:
         with open (os.path.join(dir_path,f'2008(2) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

for i in range (0,13):
    n = 3000 + i
    url = f'https://aclanthology.org/C08-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
         with open (os.path.join(dir_path,f'2008(3) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

for i in range (0,3):
    n = 4000 + i
    url = f'https://aclanthology.org/C08-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
         with open (os.path.join(dir_path,f'2008(4) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

for i in range (0,2):
    n = 5000 + i
    url = f'https://aclanthology.org/C08-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
         with open (os.path.join(dir_path,f'2008(5) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

#2006:
for i in range (0,148):
    n = 1000 + i
    url = f'https://aclanthology.org/P06-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
         with open (os.path.join(dir_path,f'2006(1) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

for i in range (0,126):
    n = 2000 + i
    url = f'https://aclanthology.org/P06-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
         with open (os.path.join(dir_path,f'2006(2) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

for i in range (0,16):
    n = 3000 + i
    url = f'https://aclanthology.org/P06-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
         with open (os.path.join(dir_path,f'2006(3) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

for i in range (0,26):
    n = 4000 + i 
    url = f'https://aclanthology.org/P06-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
         with open (os.path.join(dir_path,f'2006(4) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

#2004:
for i in range (0,205):
    n = 1000 + i 
    url = f'https://aclanthology.org/C04-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
         with open (os.path.join(dir_path,f'2004(1) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

#2002:
for i in range (0,171):
    n = 1000 + i
    url = f'https://aclanthology.org/C02-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
         with open (os.path.join(dir_path,f'2002(1) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

for i in range (0,29):
    n = 2000 + i
    url = f'https://aclanthology.org/C02-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
         with open (os.path.join(dir_path,f'2002(2) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

#2000:
for i in range (0,86):
    n = 1000 + i
    url = f'https://aclanthology.org/C00-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
         with open (os.path.join(dir_path,f'2000(1) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

for i in range (0,91):
    n = 2000 + i 
    url = f'https://aclanthology.org/C00-{n}.pdf'
    response = requests.get(url)
    if response.status_code == 200:
         with open (os.path.join(dir_path,f'2000(2) paper-{i}.pdf'),'wb') as pdf:
             print (f'downloading file {i}')
             for packet in response.iter_content(chunk_size=1024):
                 pdf.write(packet)
print('success!!')

print('Finished downloading research papers')