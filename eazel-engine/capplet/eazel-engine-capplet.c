/* eazel-engine-capplet.c -- control center applet

   Copyright (C) 2001 Eazel, Inc.

   This program is free software; you can redistribute it and/or
   modify it under the terms of the GNU General Public License as
   published by the Free Software Foundation; either version 2 of the
   License, or (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

   $Id: eazel-engine-capplet.c,v 1.3 2001/01/22 20:25:16 jsh Exp $

   Authors: John Harper <jsh@eazel.com>  */

/* AIX requires this to be the first thing in the file.  */
#ifdef HAVE_CONFIG_H
#include <config.h>
#endif
#ifndef __GNUC__
# if HAVE_ALLOCA_H
#  include <alloca.h>
# else
#  ifdef _AIX
 #pragma alloca
#  else
#   ifndef alloca /* predefined by HP cc +Olibcalls */
   char *alloca ();
#   endif
#  endif
# endif
#endif

#include <gtk/gtk.h>
#include <capplet-widget.h>

#define FILENAME ".eazel-engine-color"

static GdkColor original_color;

static GtkWidget *color_picker;

static GtkWidget *capplet;


/* color I/O */

static FILE *
open_color_file (char *mode)
{
    FILE *fh = 0;

    char *home = g_get_home_dir ();
    char buf[PATH_MAX];

    g_snprintf (buf, PATH_MAX, "%s/%s", home, FILENAME);
    fh = fopen (buf, mode);

    return fh;
}

static gboolean
read_color (GdkColor *color)
{
    FILE *fh = open_color_file ("r");
    gboolean ret = FALSE;

    if (fh != 0)
    {
	char buf[256];

	if (fgets (buf, sizeof (buf), fh))
	{
	    int len = strlen (buf);
	    if (len > 0 && buf[len-1] == '\n')
		buf[len-1] = 0;
	    ret = gdk_color_parse (buf, color);
	}
	fclose (fh);
    }

    if (!ret)
    {
	/* Default to the Eazel Teal color */
	color->red = 0x5050;
	color->green = 0x8080;
	color->blue = 0x8383;
    }

    return ret;
}

static gboolean
write_color (GdkColor *color)
{
    FILE *fh = open_color_file ("w");
    if (fh != 0)
    {
	fprintf (fh, "#%02x%02x%02x\n", color->red >> 8,
		 color->green >> 8, color->blue >> 8);
	fclose (fh);
	return TRUE;
    }
    else
	return FALSE;
}

static void
color_changed (GnomeColorPicker *widget, gpointer data)
{
    capplet_widget_state_changed (CAPPLET_WIDGET (capplet), TRUE);
}

static void 
signal_apply_theme (void)
{
    static GdkAtom atom = 0;
    GdkEventClient rcevent;

    if (atom == 0)
	atom = gdk_atom_intern ("_GTK_READ_RCFILES", FALSE);

    rcevent.type = GDK_CLIENT_EVENT;
    rcevent.window = 0;
    rcevent.send_event = TRUE;
    rcevent.message_type = atom;
    rcevent.data_format = 8;
    gdk_event_send_clientmessage_toall((GdkEvent *)&rcevent);

    /* XXX hack hack. GTK will only reread rc files if at
       XXX least one of them has a more recent mtime */
    system ("touch $HOME/.gtkrc");
}

static void
color_picker_set (GdkColor *color)
{
    gnome_color_picker_set_i16 (GNOME_COLOR_PICKER (color_picker),
				color->red, color->green, color->blue, 65535);
}

static void
color_picker_ref (GdkColor *color)
{
    gushort alpha;
    gnome_color_picker_get_i16 (GNOME_COLOR_PICKER (color_picker),
				&color->red, &color->green,
				&color->blue, &alpha);
}


/* capplet button callbacks */

static void
capplet_help (void)
{
}

static void
capplet_apply (void)
{
    GdkColor color;

    color_picker_ref (&color);
    write_color (&color);

    gdk_error_trap_push();
    signal_apply_theme();
    gdk_flush();
    gdk_error_trap_pop();
}

static void
capplet_revert (void)
{
    write_color (&original_color);
    color_picker_set (&original_color);

    gdk_error_trap_push();
    signal_apply_theme();
    gdk_flush();
    gdk_error_trap_pop();
}

static void
capplet_ok (void)
{
    capplet_apply ();
}

static void
capplet_cancel (void)
{
}


/* initialisation */

static void
setup (void)
{
    GtkWidget *vbox, *hbox;

    capplet = capplet_widget_new ();

    gtk_signal_connect (GTK_OBJECT (capplet), "help",
			GTK_SIGNAL_FUNC (capplet_help), NULL);
    gtk_signal_connect (GTK_OBJECT (capplet), "try",
			GTK_SIGNAL_FUNC (capplet_apply), NULL);
    gtk_signal_connect (GTK_OBJECT (capplet), "revert",
			GTK_SIGNAL_FUNC (capplet_revert), NULL);
    gtk_signal_connect (GTK_OBJECT (capplet), "ok",
			GTK_SIGNAL_FUNC (capplet_ok), NULL);
    gtk_signal_connect (GTK_OBJECT (capplet), "cancel",
			GTK_SIGNAL_FUNC (capplet_cancel), NULL);

    color_picker = gnome_color_picker_new ();
    gnome_color_picker_set_use_alpha (GNOME_COLOR_PICKER (color_picker), FALSE);
    read_color (&original_color);
    color_picker_set (&original_color);

    gtk_signal_connect (GTK_OBJECT (color_picker), "color_set",
			GTK_SIGNAL_FUNC (color_changed), NULL);

    vbox = gtk_vbox_new (FALSE, 0);
    hbox = gtk_hbox_new (FALSE, 10);
    gtk_box_pack_start (GTK_BOX (hbox),
			gtk_label_new (_("Accent color for `Crux' theme: ")),
			FALSE, FALSE, 0);
    gtk_box_pack_start (GTK_BOX (hbox), color_picker, FALSE, FALSE, 0);
    gtk_box_pack_start (GTK_BOX (vbox), hbox, FALSE, FALSE, 0);

    gtk_container_add (GTK_CONTAINER (capplet), vbox);
}


/* entry point */

int
main (int argc, char **argv)
{
    GnomeClient *client = NULL;
    GnomeClientFlags flags;
    gchar *session_args[3];
    int token, init_results;

    static struct poptOption options[] = {
	{ 0, 0, 0, 0, 0 }
    };

#if 0
    bindtextdomain (PACKAGE, GNOMELOCALEDIR);
    textdomain (PACKAGE);
#endif

    init_results = gnome_capplet_init("eazel-engine-capplet",
				      "0.0", argc, argv, options, 0, NULL);

    if (init_results < 0)
    {
	g_warning ("an initialization error occurred while "
		   "starting 'eazel-engine-capplet'.\n"
		   "aborting...\n");
	exit (1);
    }

    client = gnome_master_client ();
    flags = gnome_client_get_flags(client);

    if (init_results != 1)
    {
	setup ();
	gtk_widget_show_all (capplet);
	capplet_gtk_main ();
    }
    return 0;
}
