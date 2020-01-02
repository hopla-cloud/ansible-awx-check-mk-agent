# _ _ _
#(_|_) |
# _ _| |_   _  ___
#| | | | | | |/ _ \
#| | | | |_| | |_| |
#|_|_|_|\__  |\___/
#      (____/
#
# - Writer : Remi Viau
# - Version : 1.0
#
#
#
#on recupere la date du jour et d'hier
from datetime import date, timedelta
yesterday = (date.today() - timedelta(days=1)).strftime('%m.%d.%Y')
today = (date.today()).strftime('%m.%d.%Y')
#on se rend dans le dossier de l'executable
import os
os.system ('cd /usr/lib/Acronis/CommandLineTool')
#on initialise les variables en fonction du contenu des sauvegardes
LastJobFail=os.system ("acrocmd list activities --output=raw | head -n 6 | grep failed")
LastJobWarn=os.system ("acrocmd list activities --output=raw | head -n 6 | grep warn")
LastJobYesterday=os.system ("acrocmd list activities --output=raw | head -n 6 | grep "+yesterday+"")
LastJobToday=os.system ("acrocmd list activities --output=raw | head -n 6 | grep "+today+"")

#si le dernier job n'est pas failed
if LastJobFail==256 and LastJobWarn==256:
	#si le dernier job n'est pas plus vieux de 48h
	if LastJobToday!=256 or LastJobYesterday!=256:
		print("0 _Acronis_Backup - No error in last backup")
	else:
		print("1 _Acronis_Backup - Last backup older than 48h")
else:
	print("2 _Acronis_Backup - Last backup failed")
