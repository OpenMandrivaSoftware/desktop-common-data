#!/bin/bash

if [ -n "$LANGUAGE" ]; then
	LISTLANG="`echo $LANGUAGE | tr ':' ' '`" ;
else
	if [ -n "$LANG" ]; then
		LISTLANG="$LANG"
	else
		LISTLANG=en
	fi
fi

###################
# Internet connex #
###################
#CAPTION=""
#for i in $LISTLANG
#do
#	if [ "$CAPTION" != "" ]; then break ; fi
#	case "$i" in
#		en*) CAPTION="Internet connection" ;;
#		af*) CAPTION="Internetkonneksie" ;;
#		az*) CAPTION="Ýnternet baðlantýsý" ;;
#		be*) CAPTION="Çëó÷ýííå ç ñåòêàé ²íòýðíýò" ;;
#		bg*) CAPTION="Èíòåðíåò Âðúçêà" ;;
#		br*) CAPTION="Kevreañ ouzh ar genrouedad" ;;
#		ca*) CAPTION="Connexió a Internet" ;;
#		cs*) CAPTION="Pøipojení k Internetu" ;;
#		cy*) CAPTION="Cysylltiad Rhyngrwyd" ;;
# 		da*) CAPTION="Internet forbindelse" ;;
#		de*) CAPTION="Internetverbindung" ;;
#		el*) CAPTION="Óýíäåóç Internet" ;;
#		eo*) CAPTION="Interreta konekto" ;;
#		es*) CAPTION="Conexión a Internet" ;;
#		et*) CAPTION="Internetiühendus" ;;
#		fi*) CAPTION="Internet yhteys" ;;
#		fr*) CAPTION="Connexion à l'Internet" ;;
#		ga*) CAPTION="Nasc idirlíon" ;;
#		gl*) CAPTION="Conexión a Internet" ;;
#		hr*) CAPTION="Veza s InterNetom" ;;
#		hu*) CAPTION="Internet kapcsolat" ;;
#		id*) CAPTION="Koneksi Internet" ;;
#		is*) CAPTION="Lýðnets tenging" ;;
#		it*) CAPTION="Connessione a Internet" ;;
#		ko*) CAPTION="ÀÎÅÍ³Ý ¿¬°á" ;;
#		lt*) CAPTION="Prisijungimas prie interneto" ;;
#		lv*) CAPTION="Interneta pieslçgums" ;;
#		nl*) CAPTION="Internetverbinding" ;;
#		no*) CAPTION="Oppkobling Internett" ;;
#		pl*) CAPTION="Po³±czenie z internetem" ;;
#		ro*) CAPTION="Conectare la Internet" ;;
#		ru*) CAPTION="Internet-ÓÏÅÄÉÎÅÎÉÅ" ;;
#		sk*) CAPTION="Pripojenie k internetu" ;;
#		sl*) CAPTION="Povezava v internet" ;;
#		sp*) CAPTION="¸ÝâÕàÝÕâ ÚÞÝÕÚæØøÕ" ;;
#		sr*) CAPTION="Internet konekcije" ;;
#		sv*) CAPTION="Internet uppkoppling" ;;
#		tr*) CAPTION="Ýnternet baðlantýsý" ;;
#		uk*) CAPTION="ú'¤ÄÎÁÎÎÑ Ú ¦ÎÔÅÒÎÅÔÏÍ" ;;
#		wa*) CAPTION="Raloyaedje al rantoele daegnrece" ;;
#		zh_CN*) CAPTION="»¥ÁªÍøÁ¬½Ó" ;;
#	esac
#done
#if [ "$CAPTION" = "" ]; then CAPTION="Internet connection" ; fi
#
#/usr/bin/gdesktoplnk \
#	--progname="/usr/bin/gnome-ppp" \
#	--icon-name="gnome-networktool.png" \
#	--icon-caption="$CAPTION" \
#	--link-name="MDKppp" \
#	--desktop-dir="$HOME/.gnome-desktop"

###################
# Mandrake Update #
###################
#CAPTION=""
#for i in $LISTLANG
#do
#	if [ "$CAPTION" != "" ]; then break ; fi
#	case "$i" in
#		en*) CAPTION="Mandrake Updates" ;;
#		af*) CAPTION="Mandrake Opdaterings" ;;
#		be*) CAPTION="Àäíà¢ëåíí³ Mandrake" ;;
#		bg*) CAPTION="Mandrake Îáíîâÿâàíå" ;;
#		br*) CAPTION="Hizivadurioù Mandrake" ;;
#		ca*) CAPTION="Actualitzacions del Mandrake" ;;
#		cs*) CAPTION="Aktualizace Mandrake" ;;
#		cy*) CAPTION="Diweddariadau Mandrake" ;;
#		da*) CAPTION="Mandrake Opdateringer" ;;
#		de*) CAPTION="Mandrake Updates" ;;
#		el*) CAPTION="Áíáâáèìßóåéò ôïõ Mandrake" ;;
#		eo*) CAPTION="Mandrejkaj Øisdatigoj" ;;
#		es*) CAPTION="Actualizaciones de Mandrake" ;;
#		et*) CAPTION="Mandrake parandused" ;;
#		fi*) CAPTION="Mandrake päivitykset" ;;
#		fr*) CAPTION="Mises à jour de Mandrake" ;;
#		ga*) CAPTION="Nuashonraí Mandrake" ;;
#		gl*) CAPTION="Actualizacións de Mandrake" ;;
#		hr*) CAPTION="Mandrake nadogradnje" ;;
#		hu*) CAPTION="Mandrake frissítések" ;;
#		id*) CAPTION="Situs Update Mandrake" ;;
#		is*) CAPTION="Mandrake uppfærslur" ;;
#		it*) CAPTION="Aggiornamenti Mandrake" ;;
#		ko*) CAPTION="¸Çµå·¹ÀÌÅ© ¾÷µ¥ÀÌÆ®" ;;
#		lt*) CAPTION="Mandrake atnaujinimai" ;;
#		lv*) CAPTION="Mandrake atjauninâjumi" ;;
#		nl*) CAPTION="Mandrake updates" ;;
#		no*) CAPTION="Mandrake oppdateringer" ;;
#		ro*) CAPTION="Actualizãri pentru Mandrake" ;;
#		sk*) CAPTION="Mandrake Updates" ;;
#		sl*) CAPTION="Nadgradnje Mandrake" ;;
#		sp*) CAPTION="Mandrake Update" ;;
#		sr*) CAPTION="Mandrake Update" ;;
#		sv*) CAPTION="Mandrake Uppdateringar" ;;
#		tr*) CAPTION="Mandrake güncellemesi" ;;
#		uk*) CAPTION="ðÏÎÏ×ÌÅÎÎÑ ÓÉÓÔÅÍÉ Mandrake" ;;
#		wa*) CAPTION="Metaedje a djoû di Mandrake" ;;
#		zh_CN*) CAPTION="Mandrake Éý¼¶" ;;
#	esac
#done
#if [ "$CAPTION" = "" ]; then CAPTION="Mandrake Updates" ; fi
#
#/usr/bin/gdesktoplnk \
#	--progname="/usr/X11R6/bin/MandrakeUpdate" \
#	--icon-name="../icons/updates-mdk.xpm" \
#	--icon-caption="$CAPTION" \
#	--link-name="Mandrake Updates" \
#	--desktop-dir="$HOME/.gnome-desktop"


############
# DrakConf #
############
CAPTION=""
for i in $LISTLANG
do
	if [ "$CAPTION" != "" ]; then break ; fi
	case "$i" in
		en*) CAPTION="DrakConf" ;;
	esac
done
if [ "$CAPTION" = "" ]; then CAPTION="DrakConf" ; fi

/usr/bin/gdesktoplnk \
	--progname="/usr/X11R6/bin/DrakConf" \
	--icon-name="../icons/large/DrakConf.xpm" \
	--icon-caption="$CAPTION" \
	--link-name="DrakConf" \
	--desktop-dir="$HOME/.gnome-desktop"


############
# rpmdrake #
############
#CAPTION=""
#for i in $LISTLANG
#do
#	if [ "$CAPTION" != "" ]; then break ; fi
#	case "$i" in
#		en*) CAPTION="RpmDrake" ;;
#		zh_CN*) CAPTION="RpmDrake Èí¼þ°ü¹ÜÀí" ;;
#	esac
#done
#if [ "$CAPTION" = "" ]; then CAPTION="RpmDrake" ; fi
#
#/usr/bin/gdesktoplnk \
#	--progname="/usr/X11R6/bin/rpmdrake" \
#	--icon-name="../icons/rpmdrake.xpm" \
#	--icon-caption="$CAPTION" \
#	--link-name="rpmdrake" \
#	--desktop-dir="$HOME/.gnome-desktop"
#

############
# Netscape #
############
#CAPTION=""
#for i in $LISTLANG
#do
#	if [ "$CAPTION" != "" ]; then break ; fi
#	case "$i" in
#		en*) CAPTION="Netscape" ;;
#		ja*) CAPTION="¥Í¥Ã¥È¥¹¥±¡¼¥×" ;;
#		ko*) CAPTION="³Ý½ºÄÉÀÌÇÁ" ;;
#	esac
#done
#if [ "$CAPTION" = "" ]; then CAPTION="Netscape" ; fi
#
#/usr/bin/gdesktoplnk \
#	--progname="/usr/bin/netscape" \
#	--icon-name="../icons/netscape.xpm" \
#	--icon-caption="$CAPTION" \
#	--link-name="Netscape" \
#	--desktop-dir="$HOME/.gnome-desktop"

cp /usr/share/gnome/apps/Networking/WWW/Netscape-Navigator.desktop $HOME/.gnome-desktop/ -f
