def start_scan():
  input_scan = input(str("\nfile yang berisi Url/domain yang ingin di cek :"))
  print("")
  
  try:
    with open(input_scan , "r") as file:
      isi_url = file.read().splitlines()
  except:
    print("File Nya Tidak Ditemukan")
    exit()
    
  mid = len(isi_url) // 2
  hasil_mid1 = isi_url[:mid]
  hasil_mid2 = isi_url[mid:]
  
  def bagi_string(s):
    mid_th = len(s) // 2
    return s[:mid_th], s[mid_th:]
    # Bagi hasil_mid1 dan hasil_mid2
  hasil_mid3, hasil_mid4 = bagi_string(hasil_mid1)
  hasil_mid5, hasil_mid6 = bagi_string(hasil_mid2)
  # Bagi hasil_mid3 dan hasil_mid4
  scan_th1, scan_th2 = bagi_string(hasil_mid3)
  scan_th3, scan_th4 = bagi_string(hasil_mid4)
  # Bagi hasil_mid5 dan hasil_mid6
  scan_th5, scan_th6 = bagi_string(hasil_mid5)
  scan_th7, scan_th8 = bagi_string(hasil_mid6)
  # Print hasil
  #print(scan_th1)
  #print(scan_th2)
  #print(scan_th3)
  #print(scan_th4)
  #print(scan_th5)
  #print(scan_th6)
  #print(scan_th7)
  #print(scan_th8)
  def scan_th1_func():
    found = False
    for isi in scan_th1:
      domain_url1 = f"{isi}/wp-login.php"
      try:
        req1 = requests.get(domain_url1)
        if req1.status_code == 200:
          found = True
      except:
        pass
      if found:
        print(GREEN +f"Found : [ {domain_url1} ] [ SAVED scan_wp_{input_scan}]")
        with open(f"scan_wp_{input_scan}" , "a") as file:
          file.write(f"\n{domain_url1}")
      else:
        print(RED +f"Not Found : [ {isi} ]")
        
        
  def scan_th2_func():
    found = False
      
    for isi in scan_th2:
      domain_url1 = f"{isi}/wp-login.php"
      try:
        req1 = requests.get(domain_url1)
        if req1.status_code == 200:
          found = True
      except:
        print("error")
      if found:
        print(GREEN +f"Found : [ {domain_url1} ] [ SAVED scan_wp_{input_scan}]")
        with open(f"scan_wp_{input_scan}" , "a") as file:
          file.write(f"\n{domain_url1}")
    else:
      print(RED +f"Not Found : [ {isi} ]")
  
  def scan_th3_func():
    found = False
      
    for isi in scan_th3:
      domain_url1 = f"{isi}/wp-login.php"
      try:
        req1 = requests.get(domain_url1)
        if req1.status_code == 200:
          found = True
      except Exception as e:
        print(RED +f"Not Found : [ {isi} ]")
      if found:
        print(GREEN +f"Found : [ {domain_url1} ] [ SAVED scan_wp_{input_scan}]")
        with open(f"scan_wp_{input_scan}" , "a") as file:
          file.write(f"\n{domain_url1}")
    else:
      print(RED +f"Not Found : [ {isi} ]")
  
  def scan_th4_func():
    found = False
      
    for isi in scan_th4:
      domain_url1 = f"{isi}/wp-login.php"
      try:
        req1 = requests.get(domain_url1)
        if req1.status_code == 200:
          found = True
      except:
        print("error")
      if found:
        print(GREEN +f"Found : [ {domain_url1} ] [ SAVED scan_wp_{input_scan}]")
        with open(f"scan_wp_{input_scan}" , "a") as file:
          file.write(f"\n{domain_url1}")
    else:
      print(RED +f"Not Found : [ {isi} ]")
  
  def scan_th5_func():
    found = False
      
    for isi in scan_th5:
      domain_url1 = f"{isi}/wp-login.php"
      try:
        req1 = requests.get(domain_url1)
        if req1.status_code == 200:
          found = True
      except:
        print("error")
      if found:
        print(GREEN +f"Found : [ {domain_url1} ] [ SAVED scan_wp_{input_scan}]")
        with open(f"scan_wp_{input_scan}" , "a") as file:
          file.write(f"\n{domain_url1}")
    else:
      print(RED +f"Not Found : [ {isi} ]")
    
  def scan_th6_func():
    found = False
      
    for isi in scan_th6:
      domain_url1 = f"{isi}/wp-login.php"
      try:
        req1 = requests.get(domain_url1)
        if req1.status_code == 200:
          found = True
      except:
        print("error")
      if found:
        print(GREEN +f"Found : [ {domain_url1} ] [ SAVED scan_wp_{input_scan}]")
        with open(f"scan_wp_{input_scan}" , "a") as file:
          file.write(f"\n{domain_url1}")
    else:
      print(RED +f"Not Found : [ {isi} ]")
      
  def scan_th7_func():
    found = False
      
    for isi in scan_th7:
      domain_url1 = f"{isi}/wp-login.php"
      try:
        req1 = requests.get(domain_url1)
        if req1.status_code == 200:
          found = True
      except:
        print("error")
      if found:
        print(GREEN +f"Found : [ {domain_url1} ] [ SAVED scan_wp_{input_scan}]")
        with open(f"scan_wp_{input_scan}" , "a") as file:
          file.write(f"\n{domain_url1}")
    else:
      print(RED +f"Not Found : [ {isi} ]")
      
  def scan_th8_func():
    found = False
      
    for isi in scan_th8:
      domain_url1 = f"{isi}/wp-login.php"
      try:
        req1 = requests.get(domain_url1)
        if req1.status_code == 200:
          found = True
      except:
        print("error")
      if found:
        print(GREEN +f"Found : [ {domain_url1} ] [ SAVED scan_wp_{input_scan}]")
        with open(f"scan_wp_{input_scan}" , "a") as file:
          file.write(f"\n{domain_url1}")
    else:
      print(RED +f"Not Found : [ {isi} ]")
      
      
  th1_scan_on = threading.Thread(target=scan_th1_func)
  th2_scan_on = threading.Thread(target=scan_th2_func)
  th3_scan_on = threading.Thread(target=scan_th3_func)
  th4_scan_on = threading.Thread(target=scan_th4_func)
  th5_scan_on = threading.Thread(target=scan_th5_func)
  th6_scan_on = threading.Thread(target=scan_th6_func)
  th7_scan_on = threading.Thread(target=scan_th7_func)
  th8_scan_on = threading.Thread(target=scan_th8_func)
  
  th1_scan_on.start()
  th2_scan_on.start()
  th3_scan_on.start()
  th4_scan_on.start()
  th5_scan_on.start()
  th6_scan_on.start()
  th7_scan_on.start()
  th8_scan_on.start()
  
  th1_scan_on.join()
  th2_scan_on.join()
  th3_scan_on.join()
  th4_scan_on.join()
  th5_scan_on.join()
  th6_scan_on.join()
  th7_scan_on.join()
  th8_scan_on.join()
  
  print("\nSucces Scan")
  input_terminal()
  
start_scan()