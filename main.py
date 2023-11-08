import threading
import datetime
import uuid
import time

from backend.Spectrum import Spectrum
from backend.Banners import *

Spectrum = Spectrum()

def titleC():
    symbols = ['|', '\\', '-', '/']
    while True:
        for symbol in symbols:
            current_time = datetime.datetime.now().strftime('%H:%M:%S %p')
            Spectrum.title(f'[{symbol}] License Creator | @Sacrifice.zip | {current_time}')
            time.sleep(.75)

def main():
    threading.Thread(target=titleC).start()
    
    Spectrum.clear()
    Spectrum.print(banner, color='pink')
    _companyN = Spectrum.input("Company Name: ", color='pink')
    _productN = Spectrum.input("Product Name: ", color='pink')
    _shareable = Spectrum.input("May the Licensed User Share? (Y/N): ", color='pink').lower()
    
    if _shareable == 'n':
        _licensedU = Spectrum.input("Recipient of This Application: ", color='pink')
        _productID = uuid.uuid4()
        with open('License.txt', 'w+') as l:
            l.write(f'''Date: {datetime.datetime.now().strftime('%d/%m/%y')}
Company Name: {_companyN}
Company Product: {_productN}
Restrictions:
{_productN} may not be shared, edited, decompiled, or subjected to reverse engineering. Users are strictly prohibited from using the tool for unlawful purposes, including hacking, spreading malware, or attempting unauthorized access to third-party systems.\n
Agreement of Terms of Service: 
By executing this software in any way, you are agreeing to the Terms of Service. If you choose not to open the Terms but engage with this software in any manner, you expressly consent to abide by the Terms of Service. Even if you decide not to explicitly review the Terms of Service but proceed to open the file, your actions still constitute a binding agreement to the Terms of Service.

License Details:
Company: {_companyN}
Product: {_productN}
Licensed Recipient: {_licensedU}
Recipient Product ID: {_productID}

(Made by License Creator made by Sacrifice.zip)''')
        Spectrum.logging(mode='Success', color='green', text='Wrote License!', fg='green')
        time.sleep(2)
        main()
            
    elif _shareable == 'y':
        _licensedU = Spectrum.input("Recipient of This Application: ", color='pink')
        _productID = uuid.uuid4()
        with open('License.txt', 'w+') as l:
            l.write(f'''Date: {datetime.datetime.now().strftime('%d/%m/%y')}
Company Name: {_companyN}
Company Product: {_productN}
Restrictions:
{_productN} may be shared for legitimate purposes and may be edited or modified for personal use. However, decompiling or reverse engineering is not allowed. Users are prohibited from using the tool for unlawful activities, including hacking, spreading malware, or attempting unauthorized access to third-party systems.
Agreement of Terms of Service: 
By executing this software in any way, you are agreeing to the Terms of Service. If you choose not to open the Terms but engage with this software in any manner, you expressly consent to abide by the Terms of Service. Even if you decide not to explicitly review the Terms of Service but proceed to open the file, your actions still constitute a binding agreement to the Terms of Service.

License Details:
Company: {_companyN}
Product: {_productN}
Licensed Recipient: {_licensedU}
Recipient Product ID: {_productID}

(Made by License Creator made by Sacrifice.zip)''')        
        Spectrum.logging(mode='Success', color='green', text='Wrote License!', fg='green')
        time.sleep(2)
        main()  
    else:
        Spectrum.logging(mode='Failed', color='red', text='Invalid Choice!', fg='red')
        time.sleep(2)
        main()
main()
