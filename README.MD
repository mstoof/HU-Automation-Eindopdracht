# Automation Eindopdracht
### Geschreven door Maurice Stoof

---

De tool bestaat uit meerdere folders die op verschillende hieronder een beschrijving.
* Agent (Documenten die op de saltstack agent moeten staan, om elke 5 minuten (of afgesproken tijd voor het bedrijf) informatie te sturen)
* Docker binnen deze docker folder staat de installatie voor de RHEL8 agents. 
* Prometheus kan draaien op de master server zodat de alartmanager gerund kan worden om statestieken bij te houden.
* Saltstack binnen deze folder zitten 2 folders. 
  * Pillar deze moet geinstalleerd worden voor de management webserver op de pillar.
  * Salt dit is voor de management server
* Webserver is een Flask web engine om de API requests tussen de salt-agent en salt-master.
* Docker deployments. Er zijn 2 docker deployment files, om de reguliere installatie te kunnen doen voor een Linux server of Windows server.

---

## Webserver 
De flask webserver heeft weinig installatie nodig. 
De tool is gemaakt op python 3.9.14, dus alleen deze versie is gesupport. 
``` 
cd Webserver
pip3 install -r requirements.txt
python3 app.py
```

Voor uitbreiding en verbeteren van de webserver zal de CSS styling en Javascript code uit de 
dashboard.html file gehaald moeten worden. 

Dit kan in de directory static onder benaming 
styles.css en main.js. 

---

## Docker

De Website requirements kunnen geinstalleerd worden doormiddel van een bashfile.
```
cd Docker
bash installation.sh
```
