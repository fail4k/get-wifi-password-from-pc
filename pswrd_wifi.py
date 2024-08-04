from WiFi_Access import WiFi

wifi = WiFi.start()

with open("pswrd.txt", "w") as f:
    f.write(str(wifi))