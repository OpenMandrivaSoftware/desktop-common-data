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

# ###################
# # Internet connex #
# ###################
# CAPTION=""
# for i in $LISTLANG
# do
# 	if [ "$CAPTION" != "" ]; then break ; fi
# 	case "$i" in
# 		en*) CAPTION="Internet connection" ;;
# 		bg*) CAPTION="Èíòåðíåò Âðúçêà" ;;
# 		ca*) CAPTION="Connexió a Internet" ;;
# 		da*) CAPTION="Internet forbindelse" ;;
# 		de*) CAPTION="Internetverbindung" ;;
# 		es*) CAPTION="Conexión a Internet" ;;
# 		et*) CAPTION="Internetiühendus" ;;
# 		fr*) CAPTION="Connexion à l'Internet" ;;
# 		gl*) CAPTION="Conexión a Internet" ;;
# 		hr*) CAPTION="Veza s InterNetom" ;;
# 		hu*) CAPTION="Internet kapcsolat" ;;
# 		id*) CAPTION="Koneksi Internet" ;;
# 		it*) CAPTION="Connessione a Internet" ;;
# 		is*) CAPTION="Lýðnets tenging" ;;
#		lv*) CAPTION="Interneta pieslçgums" ;;
# 		nl*) CAPTION="Internet verbinding" ;;
# 		no*) CAPTION="Oppkobling Internett" ;;
# 		ro*) CAPTION="Conectare la Internet" ;;
# 		ru*) CAPTION="Internet-ÓÏÅÄÉÎÅÎÉÅ" ;;
# 		uk*) CAPTION="ú'¤ÄÎÁÎÎÑ Ú ¦ÎÔÅÒÎÅÔÏÍ" ;;
# 		wa*) CAPTION="Raloyaedje al rantoele daegnrece" ;;
# 	esac
# done
# if [ "$CAPTION" = "" ]; then CAPTION="Internet connection" ; fi
# 
# /usr/bin/gdesktoplnk \
# 	--progname="/usr/bin/gnome-ppp" \
# 	--icon-name="gnome-networktool.png" \
# 	--icon-caption="$CAPTION" \
# 	--link-name="MDKppp" \
# 	--desktop-dir="$HOME/.gnome-desktop"

###################
# Mandrake Update #
###################
CAPTION=""
for i in $LISTLANG
do
	if [ "$CAPTION" != "" ]; then break ; fi
	case "$i" in
		en*) CAPTION="Mandrake Updates" ;;
		bg*) CAPTION="Mandrake Îáíîâÿâàíå" ;;
		br*) CAPTION="Hizivadurioù Mandrake" ;;
		ca*) CAPTION="Actualitzacions del Mandrake" ;;
		cs*) CAPTION="Aktualizace Mandrake" ;;
		da*) CAPTION="Mandrake Opdateringer" ;;
		de*) CAPTION="Mandrake Updates" ;;
		es*) CAPTION="Actualizaciones de Mandrake" ;;
		et*) CAPTION="Mandrake parandused" ;;
		fr*) CAPTION="Mises à jour de Mandrake" ;;
		ga*) CAPTION="Nuashonraí Mandrake" ;;
		gl*) CAPTION="Actualizacións de Mandrake" ;;
		hr*) CAPTION="Mandrake nadogradnje" ;;
		hu*) CAPTION="Mandrake frissítések" ;;
		id*) CAPTION="Situs Update Mandrake" ;;
		is*) CAPTION="Mandrake uppfærslur" ;;
		it*) CAPTION="Aggiornamenti Mandrake" ;;
		lt*) CAPTION="Mandrake atnaujinimai" ;;
		lv*) CAPTION="Mandrake atjauninâjumi" ;;
		nl*) CAPTION="Mandrake updates" ;;
		no*) CAPTION="Mandrake oppdateringer" ;;
		ro*) CAPTION="Actualizãri pentru Mandrake" ;;
		uk*) CAPTION="ðÏÎÏ×ÌÅÎÎÑ ÓÉÓÔÅÍÉ Mandrake" ;;
		wa*) CAPTION="Metaedje a djoû di Mandrake" ;;
	esac
done
if [ "$CAPTION" = "" ]; then CAPTION="Mandrake Updates" ; fi

/usr/bin/gdesktoplnk \
	--progname="/usr/X11R6/bin/MandrakeUpdate" \
	--icon-name="../icons/updates-mdk.xpm" \
	--icon-caption="$CAPTION" \
	--link-name="MDKUpdates" \
	--desktop-dir="$HOME/.gnome-desktop"


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
	--icon-name="../icons/DrakConf.xpm" \
	--icon-caption="$CAPTION" \
	--link-name="DrakConf" \
	--desktop-dir="$HOME/.gnome-desktop"


############
# rpmdrake #
############
CAPTION=""
for i in $LISTLANG
do
	if [ "$CAPTION" != "" ]; then break ; fi
	case "$i" in
		en*) CAPTION="RpmDrake" ;;
	esac
done
if [ "$CAPTION" = "" ]; then CAPTION="RpmDrake" ; fi

/usr/bin/gdesktoplnk \
	--progname="/usr/X11R6/bin/rpmdrake" \
	--icon-name="../icons/rpmdrake.xpm" \
	--icon-caption="$CAPTION" \
	--link-name="rpmdrake" \
	--desktop-dir="$HOME/.gnome-desktop"


