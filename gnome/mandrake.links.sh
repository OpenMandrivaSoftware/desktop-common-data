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
#		bg*) CAPTION="�������� ������" ;;
#		br*) CAPTION="Kevrea� ouzh ar genrouedad" ;;
#		ca*) CAPTION="Connexi� a Internet" ;;
#		cs*) CAPTION="P�ipojen� k Internetu" ;;
#		cy*) CAPTION="Cysylltiad Rhyngrwyd" ;;
# 		da*) CAPTION="Internet forbindelse" ;;
#		de*) CAPTION="Internetverbindung" ;;
#		el*) CAPTION="������� Internet" ;;
#		eo*) CAPTION="Interreta konekto" ;;
#		es*) CAPTION="Conexi�n a Internet" ;;
#		et*) CAPTION="Interneti�hendus" ;;
#		fi*) CAPTION="Internet yhteys" ;;
#		fr*) CAPTION="Connexion � l'Internet" ;;
#		ga*) CAPTION="Nasc idirl�on" ;;
#		gl*) CAPTION="Conexi�n a Internet" ;;
#		hr*) CAPTION="Veza s InterNetom" ;;
#		hu*) CAPTION="Internet kapcsolat" ;;
#		id*) CAPTION="Koneksi Internet" ;;
#		it*) CAPTION="Connessione a Internet" ;;
#		is*) CAPTION="L��nets tenging" ;;
#		lt*) CAPTION="Prisijungimas prie interneto" ;;
#		lv*) CAPTION="Interneta piesl�gums" ;;
#		nl*) CAPTION="Internetverbinding" ;;
#		no*) CAPTION="Oppkobling Internett" ;;
#		ro*) CAPTION="Conectare la Internet" ;;
#		ru*) CAPTION="Internet-����������" ;;
#		sk*) CAPTION="Pripojenie k internetu" ;;
#		sl*) CAPTION="Povezava v internet" ;;
#		sv*) CAPTION="Internet uppkoppling" ;;
#		tr*) CAPTION="�nternet ba�lant�s�" ;;
#		uk*) CAPTION="�'������� � ����������" ;;
#		wa*) CAPTION="Raloyaedje al rantoele daegnrece" ;;
#		zh_CN*) CAPTION="����������" ;;
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
#		bg*) CAPTION="Mandrake ����������" ;;
#		br*) CAPTION="Hizivadurio� Mandrake" ;;
#		ca*) CAPTION="Actualitzacions del Mandrake" ;;
#		cs*) CAPTION="Aktualizace Mandrake" ;;
#		cy*) CAPTION="Diweddariadau Mandrake" ;;
#		da*) CAPTION="Mandrake Opdateringer" ;;
#		de*) CAPTION="Mandrake Updates" ;;
#		el*) CAPTION="������������ ��� Mandrake" ;;
#		eo*) CAPTION="Mandrejkaj �isdatigoj" ;;
#		es*) CAPTION="Actualizaciones de Mandrake" ;;
#		et*) CAPTION="Mandrake parandused" ;;
#		fi*) CAPTION="Mandrake p�ivitykset" ;;
#		fr*) CAPTION="Mises � jour de Mandrake" ;;
#		ga*) CAPTION="Nuashonra� Mandrake" ;;
#		gl*) CAPTION="Actualizaci�ns de Mandrake" ;;
#		hr*) CAPTION="Mandrake nadogradnje" ;;
#		hu*) CAPTION="Mandrake friss�t�sek" ;;
#		id*) CAPTION="Situs Update Mandrake" ;;
#		is*) CAPTION="Mandrake uppf�rslur" ;;
#		it*) CAPTION="Aggiornamenti Mandrake" ;;
#		lt*) CAPTION="Mandrake atnaujinimai" ;;
#		lv*) CAPTION="Mandrake atjaunin�jumi" ;;
#		nl*) CAPTION="Mandrake updates" ;;
#		no*) CAPTION="Mandrake oppdateringer" ;;
#		ro*) CAPTION="Actualiz�ri pentru Mandrake" ;;
#		sk*) CAPTION="Mandrake Updates" ;;
#		sl*) CAPTION="Nadgradnje Mandrake" ;;
#		sv*) CAPTION="Mandrake Uppdateringar" ;;
#		tr*) CAPTION="Mandrake g�ncellemesi" ;;
#		uk*) CAPTION="���������� ������� Mandrake" ;;
#		wa*) CAPTION="Metaedje a djo� di Mandrake" ;;
#		zh_CN*) CAPTION="Mandrake ����" ;;
#	esac
#done
#if [ "$CAPTION" = "" ]; then CAPTION="Mandrake Updates" ; fi
#
#/usr/bin/gdesktoplnk \
#	--progname="/usr/X11R6/bin/MandrakeUpdate" \
#	--icon-name="../icons/updates-mdk.xpm" \
#	--icon-caption="$CAPTION" \
#	--link-name="MDKUpdates" \
#	--desktop-dir="$HOME/.gnome-desktop"
#

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
#		zh_CN*) CAPTION="RpmDrake ���������" ;;
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
"		en*) CAPTION="Netscape" ;;
"		ja*) CAPTION="�ͥåȥ�������" ;;
#		ko*) CAPTION="�ݽ�������" ;;
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
