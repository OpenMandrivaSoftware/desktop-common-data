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
CAPTION=""
for i in $LISTLANG
do
	if [ "$CAPTION" != "" ]; then break ; fi
	case "$i" in
		en*) CAPTION="Internet connection" ;;
		bg*) CAPTION="»ÌÚÂÌÂÚ ¬˙ÁÍ‡" ;;
		da*) CAPTION="Internet forbindelse" ;;
		es*) CAPTION="ConexiÛn a Internet" ;;
		et*) CAPTION="Interneti¸hendus" ;;
		fr*) CAPTION="Connexion ‡ l'Internet" ;;
		gl*) CAPTION="ConexiÛn a Internet" ;;
		hr*) CAPTION="Veza s InterNetom" ;;
		hu*) CAPTION="Internet kapcsolat" ;;
		id*) CAPTION="Koneksi Internet" ;;
		it*) CAPTION="Connessione a Internet" ;;
		nl*) CAPTION="Internet verbinding" ;;
		no*) CAPTION="Oppkobling Internett" ;;
		ru*) CAPTION="Internet-”œ≈ƒ…Œ≈Œ…≈" ;;
		uk*) CAPTION="˙'§ƒŒ¡ŒŒ— ⁄ ¶Œ‘≈“Œ≈‘œÕ" ;;
		wa*) CAPTION="Raloyaedje al rantoele daegnrece" ;;
	esac
done
if [ "$CAPTION" = "" ]; then CAPTION="Internet connection" ; fi

/usr/bin/gdesktoplnk \
	--progname="/usr/bin/gnome-ppp" \
	--icon-name="gnome-networktool.png" \
	--icon-caption="$CAPTION" \
	--link-name="MDKppp" \
	--desktop-dir="$HOME/.gnome-desktop"

###################
# Mandrake Update #
###################
CAPTION=""
for i in $LISTLANG
do
	if [ "$CAPTION" != "" ]; then break ; fi
	case "$i" in
		en*) CAPTION="Mandrake Updates" ;;
		bg*) CAPTION="Mandrake Œ·ÌÓ‚ˇ‚‡ÌÂ" ;;
		br*) CAPTION="Hizivadurio˘ Mandrake" ;;
		ca*) CAPTION="Actualitzacions del Mandrake" ;;
		cs*) CAPTION="Aktualizace Mandrake" ;;
		da*) CAPTION="Mandrake Opdateringer" ;;
		de*) CAPTION="Mandrake Updates" ;;
		es*) CAPTION="Actualizaciones de Mandrake" ;;
		et*) CAPTION="Mandrake parandused" ;;
		fr*) CAPTION="Mises ‡ jour de Mandrake" ;;
		ga*) CAPTION="NuashonraÌ Mandrake" ;;
		gl*) CAPTION="ActualizaciÛns de Mandrake" ;;
		hr*) CAPTION="Mandrake nadogradnje" ;;
		hu*) CAPTION="Mandrake frissÌtÈsek" ;;
		id*) CAPTION="Situs Update Mandrake" ;;
		is*) CAPTION="Mandrake uppfÊrslur" ;;
		it*) CAPTION="Aggiornamenti Mandrake" ;;
		lt*) CAPTION="Mandrake atnaujinimai" ;;
		nl*) CAPTION="Mandrake updates" ;;
		no*) CAPTION="Mandrake oppdateringer" ;;
		ro*) CAPTION="Actualiz„ri pentru Mandrake" ;;
		uk*) CAPTION="œŒœ◊Ã≈ŒŒ— ”…”‘≈Õ… Mandrake" ;;
		wa*) CAPTION="Metaedje a djo˚ di Mandrake" ;;
	esac
done
if [ "$CAPTION" = "" ]; then CAPTION="Mandrake Updates" ; fi

/usr/bin/gdesktoplnk \
	--progname="/usr/X11R6/bin/MandrakeUpdate" \
	--icon-name="../icons/mdk-updates.xpm" \
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
	--progname="/usr/bin/kdesu -c '/usr/X11R6/bin/DrakConf'" \
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


