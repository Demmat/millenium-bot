Dans ce Dossier se trouve des scripts python simplifi�s pour voter sur millenuim 
( ie pas d'utilisation de sqlite ni de class config et autres fonctionnalit�s )



=============== Script de Vote pour un seul compte ===================

	Pour l'installer sur un server web poss�dant cgi-python (on peut aussi le mettre sur Google app engine), 
	
		Il faut tout d'abord configurer le script pour cela :
		
			ouvrez 'vote.py' du dossier 'cgi-bin' (avec notepad par ex sous Windows)
			Compl�tez USER (ligne 12) en rempla�ant '___________________________' par 'LeNomdeVotreCompte'
			Compl�tez PASSW (ligne 13) en rempla�ant '___________________________' par 'LeMotdePasse'
			
		La configuration est alors termin�e.
	
		Puis il suffit de copier 'vote.py' dans le dossier 'cgi-bin' de votre site (dossier www, public_html, ect...) par FTP par ex.
		Ensuite, un chmod 755 et c'est tout bon.
	
	Vous pouvez alors appeler le script en tapant http://votresite.cc/cgi-bin/vote.py   .

======================================================================




=============== Script de Vote Multicomptes ===================
	
	Il faut tout d'abord configurer le script pour cela :
			
				ouvrez 'multivote.py' du dossier 'cgi-bin' (avec notepad par ex sous Windows)
				Compl�tez ou ajouter des lignes contenant vos identifiants au format : ('nomcompte','motdepass'),
				
			La configuration est alors termin�e.
		
			Puis il suffit de copier 'vote.py' et 'multivote.py' dans le dossier 'cgi-bin' de votre site (dossier www, public_html, ect...) par FTP par ex.
			Ensuite, un chmod 755 sur les DEUX fichiers et c'est Tout bon.
		
	Vous pouvez alors appeler le script en tapant http://votresite.cc/cgi-bin/multivote.py
	
	
	Note : 	Attention, si votre host est trop lent ou que vous avez mis trop de comptes,
			le script peut s'arr�ter. (car il y a un temps maximal d'ex�cution des scripts sur les hosts) 
			Mais vous pouvez ais�ment cr�e des sous dossiers dans cgi-bin et mettre les scripts en double
			(en partitionnant vos comptes entre les scripts ) puis mettre en place plusieurs crons.
			
===============================================================



Bonus :

Sur la pluspars des hosts cPanel, on peut effectuer des crons .

Il suffit donc de cr�� un cron se lan�ant toutes les 2h avec la cmd suivante :
wget -O - http://votresite.cc/cgi-bin/vote.py

Cela permet de lancer le script toutes les 2h automatiquement.


