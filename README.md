# COM

# OBJECTIF : 

	Comparer du point de vue du réseau une communication  avec ou sans chiffrement des données.

# RESUME : 

	Pour faire ce test on va établir une connexion entre deux machines considérées client / serveur.
	Le client va donc envoyer un fichier texte (hola.txt) au serveur.
	Les fichiers TCP_client.py et TCP_server.py établissent une connexion pour l'envoie d'un fichier non chiffré.
	Les fichiers TCP_client_chiff.py et TCP_server_chiff.py établissent une connexion pour l'envoie d'un fichier chiffré.
	Dans les deux cas on va intercepter cette communication et observer l'apparence du fichier dans le résau.
	On voit clairement la différence !!

# MISE EN OEUVRE :

	1) On ouvre wireshark en mode super utilisateur depui une machine connectée au réseau puis on lance la capture de paquets avec l' interface graphique.
		sudo wireshark
	2) Dans la machine qui va receptionner le fichier on execute TCP_server.py
		python3 TCP_server.py IP_host
	3) Dans la machine qui envoie le fichier on lance TCP_client.py
		python3 TCP_client.py IP_host NomDuFichier
	4) On arrête la capture wireshark et sur la ligne de filtrage on écrit tcp
	5) On identifie un paquet TCP de notre communication avec l'addresse IP du serveur ou du client, pui on fait click_droit/Suivre/Flux_TCP et on observe le fichier intercepté.
	6) On refait les étapes 2-5 avec les fichiers TCP_client_chiff.py et TCP_server_chiff.py


# OUTILS :

	Reniffleur de réseau :
		Wireshark
	C :
		L'éxécutable aes est le résultat d'un projet en C qu'on peut trouver à quelques modifications près sur https://github.com/zario3/AES_C

	Python :
		Utilisation des librairies sys, socket et subprocess.
		Le code python de communication avec TCP est basé sur https://www.geeksforgeeks.org/file-transfer-using-tcp-socket-in-python/?ref=gcse
