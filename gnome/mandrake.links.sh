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
# 		bg*) CAPTION="�������� ������" ;;
# 		ca*) CAPTION="Connexi� a Internet" ;;
# 		da*) CAPTION="Internet forbindelse" ;;
# 		de*) CAPTION="Internetverbindung" ;;
# 		es*) CAPTION="Conexi�n a Internet" ;;
# 		et*) CAPTION="Interneti�hendus" ;;
# 		fr*) CAPTION="Connexion � l'Internet" ;;
# 		gl*) CAPTION="Conexi�n a Internet" ;;
# 		hr*) CAPTION="Veza s InterNetom" ;;
# 		hu*) CAPTION="Internet kapcsolat" ;;
# 		id*) CAPTION="Koneksi Internet" ;;
# 		it*) CAPTION="Connessione a Internet" ;;
# 		is*) CAPTION="L��nets tenging" ;;
#		lv*) CAPTION="Interneta piesl�gums" ;;
# 		nl*) CAPTION="Internet verbinding" ;;
# 		no*) CAPTION="Oppkobling Internett" ;;
# 		ro*) CAPTION="Conectare la Internet" ;;
# 		ru*) CAPTION="Internet-����������" ;;
# 		uk*) CAPTION="�'������� � ����������" ;;
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
		bg*) CAPTION="Mandrake ����������" ;;
		br*) CAPTION="Hizivadurio� Mandrake" ;;
		ca*) CAPTION="Actualitzacions del Mandrake" ;;
		cs*) CAPTION="Aktualizace Mandrake" ;;
		da*) CAPTION="Mandrake Opdateringer" ;;
		de*) CAPTION="Mandrake Updates" ;;
		es*) CAPTION="Actualizaciones de Mandrake" ;;
		et*) CAPTION="Mandrake parandused" ;;
		fr*) CAPTION="Mises � jour de Mandrake" ;;
		ga*) CAPTION="Nuashonra� Mandrake" ;;
		gl*) CAPTION="Actualizaci�ns de Mandrake" ;;
		hr*) CAPTION="Mandrake nadogradnje" ;;
		hu*) CAPTION="Mandrake friss�t�sek" ;;
		id*) CAPTION="Situs Update Mandrake" ;;
		is*) CAPTION="Mandrake uppf�rslur" ;;
		it*) CAPTION="Aggiornamenti Mandrake" ;;
		lt*) CAPTION="Mandrake atnaujinimai" ;;
		lv*) CAPTION="Mandrake atjaunin�jumi" ;;
		nl*) CAPTION="Mandrake updates" ;;
		no*) CAPTION="Mandrake oppdateringer" ;;
		ro*) CAPTION="Actualiz�ri pentru Mandrake" ;;
		uk*) CAPTION="���������� ������� Mandrake" ;;
		wa*) CAPTION="Metaedje a djo� di Mandrake" ;;
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


