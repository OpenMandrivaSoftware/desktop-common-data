/* eazel-theme-main.c -- entry point

   Copyright (C) 1998 Randy Gordon, Integrand Systems
   Copyright (C) 2000 Eazel, Inc.

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

   $Id: eazel-theme-main.c,v 1.15 2001/03/23 22:53:04 jsh Exp $

   Authors: The Rasterman <raster@redhat.com>
            Owen Taylor <otaylor@redhat.com>
	    Randy Gordon <randy@integrand.com>
	    John Harper <jsh@eazel.com>   */

/* adapted from gtk-engines/notif/notif_theme_main.c
   and gtk-engines/metal/metal_theme_main.c */

#include "eazel-theme.h"
#include <gdk/gdkrgb.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <memory.h>
#include <gmodule.h>

#ifndef G_TOKEN_COLON
# define G_TOKEN_COLON ((guint) ':')
#endif
#ifndef G_TOKEN_LESS_THAN
# define G_TOKEN_LESS_THAN ((guint) '<')
#endif
#ifndef G_TOKEN_GREATER_THAN
# define G_TOKEN_GREATER_THAN ((guint) '>')
#endif

#define WINDOW_FOCUS_DATA_KEY "eazel-engine-focus-data"
static GQuark window_focus_data_key;

/* saved values */
static int range_slider_width, range_min_slider_size, range_stepper_size,
    range_stepper_slider_spacing, scale_slider_length,
    check_size, check_spacing;

static void install_focus_hooks (GdkWindow *window);
static void uninstall_all_focus_hooks (void);


/* utilities */

static char *
read_line_from_file (char *filename)
{
    gboolean free_filename = FALSE;
    FILE *fh;
    char *ret = 0;

    if (!g_path_is_absolute (filename))
    {
	char *home = g_get_home_dir ();
	char buf[PATH_MAX];
	g_snprintf (buf, PATH_MAX, "%s/%s", home, filename);
	filename = g_strdup (buf);
	free_filename = TRUE;
    }

    fh = fopen (filename, "r");
    if (fh != 0)
    {
	char buf[256];
	if (fgets (buf, sizeof (buf), fh) != 0)
	{
	    int len = strlen (buf);
	    if (len > 0)
		buf[len-1] = 0;
	    ret = g_strdup (buf);
	}
	fclose (fh);
    }

    if (free_filename)
	g_free (filename);

    return ret;
}


/* internals */

struct symbol_struct {
    gchar *name;
    guint token;
};

static struct symbol_struct theme_symbols[] = { THEME_SYMBOLS };

static guint n_theme_symbols = (sizeof(theme_symbols) / sizeof(theme_symbols[0])) - 1;

static struct symbol_struct stock_symbols[] = { STOCK_SYMBOLS };

static guint n_stock_symbols = (sizeof(stock_symbols) / sizeof(stock_symbols[0])) - 1;

static eazel_theme_data *default_theme_data;
static eazel_engine_stock_table *default_stock_data;

static eazel_theme_data original_theme_data = DEFAULT_THEME_DATA;

static int
stock_index (const char *symbol)
{
    int i;
    for (i = 0; i < n_stock_symbols; i++)
    {
	if (strcmp (symbol, stock_symbols[i].name) == 0)
	    return i;
    }
    g_error ("Unknown stock symbol: `%s'\n", symbol);
    exit (1);
}

static void
theme_data_ref (eazel_theme_data *theme_data)
{
    theme_data->refcount++;
}

static void
theme_data_unref (eazel_theme_data *theme_data)
{
    theme_data->refcount--;
    if (theme_data->refcount == 0)
    {
	int i;
	for (i = 0; i < 5; i++)
	{
	    if (theme_data->gradients[i] != NULL)
		eazel_engine_gradient_unref (theme_data->gradients[i]);
	}
	eazel_engine_stock_table_unref (theme_data->stock);
	g_free (theme_data);
    }
}

static guint
parse_int_assign (GScanner *scanner, guint *value)
{
    guint token;

    (void) g_scanner_get_next_token (scanner);

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_EQUAL_SIGN)
	return G_TOKEN_EQUAL_SIGN;

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_INT)
	return G_TOKEN_INT;

    *value = scanner->value.v_int;
    return G_TOKEN_NONE;
}

static guint
parse_int_array_assign (GScanner *scanner, guint *value, int size)
{
    guint token;
    int i;

    (void) g_scanner_get_next_token (scanner);

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_EQUAL_SIGN)
	return G_TOKEN_EQUAL_SIGN;

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_LEFT_CURLY)
	return G_TOKEN_LEFT_CURLY;

    for (i = 0; i < size; i++)
    {
	if (i != 0)
	{
	    token = g_scanner_get_next_token (scanner);
	    if (token != G_TOKEN_COMMA)
		return G_TOKEN_COMMA;
	}

	token = g_scanner_get_next_token (scanner);
	if (token != G_TOKEN_INT)
	    return G_TOKEN_INT;

	value[i] = scanner->value.v_int;
    }

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_RIGHT_CURLY)
	return G_TOKEN_RIGHT_CURLY;

    return G_TOKEN_NONE;
}

static guint
parse_boolean_assign (GScanner *scanner, gboolean *value)
{
    guint token;

    (void) g_scanner_get_next_token (scanner);

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_EQUAL_SIGN)
	return G_TOKEN_EQUAL_SIGN;

    token = g_scanner_get_next_token (scanner);
    if (token == TOKEN_YES)
    {
	*value = TRUE;
	return G_TOKEN_NONE;
    }
    else
    {
	*value = FALSE;
	return G_TOKEN_NONE;
    }
}

static guint
parse_string_assign (GScanner *scanner, char **value)
{
    guint token;

    (void) g_scanner_get_next_token (scanner);

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_EQUAL_SIGN)
	return G_TOKEN_EQUAL_SIGN;

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_STRING)
	return G_TOKEN_STRING;

    *value = g_strdup (scanner->value.v_string);
    return G_TOKEN_NONE;
}

static guint
parse_color (eazel_theme_data *theme_data, GScanner *scanner, GdkColor *color)
{
    guint token;

    token = g_scanner_peek_next_token (scanner);
    if (theme_data != 0 && token == G_TOKEN_LESS_THAN)
    {
	(void) g_scanner_get_next_token (scanner);

	token = g_scanner_get_next_token (scanner);

	if (token == G_TOKEN_INT)
	{
	    int index = scanner->value.v_int;

	    if (index < 0 || index >= EAZEL_ENGINE_PALETTE_SIZE)
	    {
		g_error ("Palette only has %d entries\n",
			 EAZEL_ENGINE_PALETTE_SIZE);
	    }
		    
	    index = CLAMP (index, 0, EAZEL_ENGINE_PALETTE_SIZE - 1);

	    /* XXX just taking the first color of the gradient.. */
	    if (theme_data->palette[index] != 0)
		*color = theme_data->palette[index]->from;
	    else
		g_error ("No color in palette with index %d", index);

	    token = g_scanner_peek_next_token (scanner);
	    if (token == G_TOKEN_COMMA)
	    {
		float tem;

		(void) g_scanner_get_next_token (scanner);

		token = g_scanner_get_next_token (scanner);
		if (token != G_TOKEN_FLOAT)
		    return G_TOKEN_FLOAT;

		tem = color->red;
		tem *= scanner->value.v_float;
		color->red = tem;

		tem = color->green;
		tem *= scanner->value.v_float;
		color->green = tem;

		tem = color->blue;
		tem *= scanner->value.v_float;
		color->blue = tem;
	    }
	}
	else if (token == G_TOKEN_STRING)
	{
	    char *string;
	    gboolean ret = FALSE;

	    string = read_line_from_file (scanner->value.v_string);
	    if (string != 0)
		ret = gdk_color_parse (string, color);

	    if (!ret)
	    {
		/* Default to the Eazel Teal color */
		color->red = 0x5050;
		color->green = 0x8080;
		color->blue = 0x8383;
	    }

	    g_free (string);
	}
	else
	    return G_TOKEN_INT;

	token = g_scanner_get_next_token (scanner);
	if (token != G_TOKEN_GREATER_THAN)
	    return G_TOKEN_GREATER_THAN;

	return G_TOKEN_NONE;
    }
    else
	return gtk_rc_parse_color (scanner, color);
}

static guint
parse_n_colors (eazel_theme_data *theme_data,
		GScanner *scanner, GdkColor *value, int n)
{
    guint token;
    int i;
    for (i = 0; i < n; i++)
    {
	if (i != 0)
	{
	    token = g_scanner_get_next_token (scanner);
	    if (token != G_TOKEN_COMMA)
		return G_TOKEN_COMMA;
	}

	token = parse_color (theme_data, scanner, value + i);
	if (token != G_TOKEN_NONE)
	    return token;
    }
    return G_TOKEN_NONE;
}

static guint
parse_n_color_assign (eazel_theme_data *theme_data,
		      GScanner *scanner, GdkColor *value, int n)
{
    guint token;

    (void) g_scanner_get_next_token (scanner);

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_EQUAL_SIGN)
	return G_TOKEN_EQUAL_SIGN;

    return parse_n_colors (theme_data, scanner, value, n);
}

static guint
parse_color_assign (eazel_theme_data *theme_data,
		    GScanner *scanner, GdkColor *color)
{
    return parse_n_color_assign (theme_data, scanner, color, 1);
}

static guint
parse_standard_color_assign (eazel_theme_data *theme_data, GScanner *scanner,
			     GtkRcStyle *rc_style, GdkColor *colors, int flag)
{
    GtkStateType state;
    guint token;

    (void) g_scanner_get_next_token (scanner);

    token = gtk_rc_parse_state (scanner, &state);
    if (token != G_TOKEN_NONE)
	return token;

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_EQUAL_SIGN)
	return G_TOKEN_EQUAL_SIGN;

    token = parse_color (theme_data, scanner, colors + state);
    if (token != G_TOKEN_NONE)
	return token;

    rc_style->color_flags[state] |= flag;
    return G_TOKEN_NONE;
}

static guint
parse_gradient (eazel_theme_data *theme_data, GScanner *scanner,
		eazel_engine_gradient **gradient)
{
    eazel_engine_gradient_direction direction;
    GdkColor from;
    GSList *colors = NULL;

    guint token;

    token = g_scanner_get_next_token (scanner);

    if (token == G_TOKEN_LESS_THAN)
    {
	int index;

	/* a palette reference */

	token = g_scanner_get_next_token (scanner);
	if (token != G_TOKEN_INT)
	    return G_TOKEN_INT;

	index = scanner->value.v_int;
	if (index < 0 || index >= EAZEL_ENGINE_PALETTE_SIZE)
	{
	    g_error ("Palette only has %d entries\n",
		     EAZEL_ENGINE_PALETTE_SIZE);
	}
		    
	if (theme_data->palette[index] != 0)
	    *gradient = eazel_engine_gradient_ref (theme_data->palette[index]);
	else
	    g_error ("No color in palette with index %d", index);

	token = g_scanner_get_next_token (scanner);
	if (token != G_TOKEN_GREATER_THAN)
	    return G_TOKEN_GREATER_THAN;

	return G_TOKEN_NONE;
    }
    else if (token != G_TOKEN_LEFT_CURLY)
	return G_TOKEN_LEFT_CURLY;

    token = g_scanner_peek_next_token (scanner);
    if (token == TOKEN_HORIZONTAL)
    {
	direction = GRADIENT_HORIZONTAL;
	(void) g_scanner_get_next_token (scanner);

	token = g_scanner_get_next_token (scanner);
	if (token != G_TOKEN_COLON)
	    return G_TOKEN_COLON;
    }
    else if (token == TOKEN_VERTICAL)
    {
	direction = GRADIENT_VERTICAL;
	(void) g_scanner_get_next_token (scanner);

	token = g_scanner_get_next_token (scanner);
	if (token != G_TOKEN_COLON)
	    return G_TOKEN_COLON;
    }
    else if (token == G_TOKEN_RIGHT_CURLY)
	direction = GRADIENT_NONE;
    else
	direction = GRADIENT_VERTICAL;

    if (direction != GRADIENT_NONE)
    {
	token = parse_color (theme_data, scanner, &from);
	if (token != G_TOKEN_NONE)
	    return token;

	while (1)
	{
	    float weight = 1.0;
	    GdkColor color;
	    eazel_engine_gradient_component *component;

	    token = g_scanner_peek_next_token (scanner);
	    if (token == G_TOKEN_COMMA)
		(void) g_scanner_get_next_token (scanner);
	    else if (token == G_TOKEN_LEFT_BRACE)
	    {
		(void) g_scanner_get_next_token (scanner);

		token = g_scanner_get_next_token (scanner);
		if (token == G_TOKEN_FLOAT)
		    weight = scanner->value.v_float;
		else if (token == G_TOKEN_INT)
		    weight = scanner->value.v_int;
		else
		    return G_TOKEN_FLOAT;

		token = g_scanner_get_next_token (scanner);
		if (token != G_TOKEN_RIGHT_BRACE)
		    return G_TOKEN_RIGHT_BRACE;
	    }
	    else
		break;

	    token = parse_color (theme_data, scanner, &color);
	    if (token != G_TOKEN_NONE)
		return token;

	    component = g_new (eazel_engine_gradient_component, 1);
	    component->color = color;
	    component->weight = weight;
	    colors = g_slist_prepend (colors, component);
	}

	colors = g_slist_reverse (colors);
    }

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_RIGHT_CURLY)
	return G_TOKEN_RIGHT_CURLY;

    if (*gradient != NULL)
	eazel_engine_gradient_unref (*gradient);
    *gradient = eazel_engine_gradient_new (direction, &from, colors);

    return G_TOKEN_NONE;
}

static guint
parse_gradient_assign (eazel_theme_data *theme_data, GScanner *scanner,
		       eazel_engine_gradient **gradients)
{
    guint token, state;

    (void) g_scanner_get_next_token (scanner);

    token = gtk_rc_parse_state (scanner, &state);
    if (token != G_TOKEN_NONE)
	return token;

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_EQUAL_SIGN)
	return G_TOKEN_EQUAL_SIGN;

    token = parse_gradient (theme_data, scanner, gradients + state);
    if (token != G_TOKEN_NONE)
	return token;

    return G_TOKEN_NONE;
}

static guint
parse_1_gradient_assign (eazel_theme_data *theme_data, GScanner *scanner,
			 eazel_engine_gradient **gradient)
{
    guint token;

    (void) g_scanner_get_next_token (scanner);

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_EQUAL_SIGN)
	return G_TOKEN_EQUAL_SIGN;

    token = parse_gradient (theme_data, scanner, gradient);
    if (token != G_TOKEN_NONE)
	return token;

    return G_TOKEN_NONE;
}

static guint
parse_stock_stmt (GScanner *scanner, eazel_theme_data *theme_data,
		  eazel_engine_stock_table **table_ptr)
{
    eazel_engine_stock_table *table = g_new0 (eazel_engine_stock_table, 1);
    guint token;

    table->ref_count = 1;

    (void) g_scanner_get_next_token (scanner);

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_LEFT_CURLY)
	return G_TOKEN_LEFT_CURLY;

    token = g_scanner_peek_next_token (scanner);
    while (token != G_TOKEN_RIGHT_CURLY)
    {
	switch (token)
	{
	    guint stock;
	    eazel_engine_image *image;

	case G_TOKEN_STRING:
	    (void) g_scanner_get_next_token (scanner);

	    stock = stock_index (scanner->value.v_string);
	    image = &table->images[stock];

	    token = g_scanner_get_next_token (scanner);
	    if (token != G_TOKEN_LEFT_CURLY)
		return G_TOKEN_LEFT_CURLY;

	    token = g_scanner_peek_next_token (scanner);
	    while (token != G_TOKEN_RIGHT_CURLY)
	    {
		switch (token)
		{
		case TOKEN_IMAGE:
		    token = parse_string_assign (scanner, &image->filename);
		    break;

		case TOKEN_BORDER:
		    token = parse_int_array_assign (scanner, image->border, 4);
		    break;

		case TOKEN_RECOLOR:
		    token = parse_1_gradient_assign (theme_data, scanner,
						     &image->recolor);
		    break;

		default:
		    g_scanner_get_next_token (scanner);
		    token = G_TOKEN_RIGHT_CURLY;
		    break;
		}

		if (token != G_TOKEN_NONE)
		    goto out;

		token = g_scanner_peek_next_token (scanner);
	    }

	    token = g_scanner_get_next_token (scanner);
	    if (token == G_TOKEN_RIGHT_CURLY)
		token = G_TOKEN_NONE;
	    else
		token = G_TOKEN_RIGHT_CURLY;
	    break;

	default:
	    g_scanner_get_next_token (scanner);
	    token = G_TOKEN_RIGHT_CURLY;
	    break;
	}
    
    out:
	if (token != G_TOKEN_NONE)
	{
	    g_free (table);
	    return token;
	}

    	token = g_scanner_peek_next_token (scanner);
    }

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_RIGHT_CURLY)
	return G_TOKEN_RIGHT_CURLY;

    *table_ptr = table;
    return G_TOKEN_NONE;
}

static guint
parse_palette_assign (GScanner *scanner, eazel_theme_data *theme_data)
{
    int index;
    guint token;

    (void) g_scanner_get_next_token (scanner);

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_LEFT_BRACE)
	return G_TOKEN_LEFT_BRACE;

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_INT)
	return G_TOKEN_INT;

    index = scanner->value.v_int;
    if (index < 0 || index >= EAZEL_ENGINE_PALETTE_SIZE)
    {
	g_error ("Only %d colors are allowed in the palette",
		 EAZEL_ENGINE_PALETTE_SIZE);
    }

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_RIGHT_BRACE)
	return G_TOKEN_RIGHT_BRACE;

    token = g_scanner_get_next_token (scanner);
    if (token != G_TOKEN_EQUAL_SIGN)
	return G_TOKEN_EQUAL_SIGN;

    token = parse_gradient (theme_data, scanner, &theme_data->palette[index]);
    if (token != G_TOKEN_NONE)
	return token;

    return G_TOKEN_NONE;
}

/* external theme functions called */

static guint
theme_parse_rc_style (GScanner *scanner, GtkRcStyle *rc_style)
{
    static GQuark scope_id = 0;
    guint old_scope;
    guint token;
    eazel_theme_data *theme_data;
    gint i;
    gboolean had_stock_table = FALSE;

    /* Set up a new scope in this scanner. */

    if (!scope_id)
	scope_id = g_quark_from_string ("theme_engine");

    /* If we bail out due to errors, we *don't* reset the scope, so the
       error messaging code can make sense of our tokens. */
    old_scope = g_scanner_set_scope (scanner, scope_id);

    /* Now check if we already added our symbols to this scope
      (in some previous call to theme_parse_rc_style for the
      same scanner. */

    if (!g_scanner_lookup_symbol (scanner, theme_symbols[0].name))
    {
	g_scanner_freeze_symbol_table(scanner);
	for (i = 0; i < n_theme_symbols; i++)
	{
	    g_scanner_scope_add_symbol (scanner, scope_id,
					theme_symbols[i].name,
					GINT_TO_POINTER(theme_symbols[i].token));
	}
	g_scanner_thaw_symbol_table (scanner);
    }

    /* We're ready to go, now parse the top level */

    theme_data = g_new (eazel_theme_data, 1);
    if (default_theme_data != 0)
	memcpy (theme_data, default_theme_data, sizeof (eazel_theme_data));
    else
	memcpy (theme_data, &original_theme_data, sizeof (eazel_theme_data));

    /* ref all gradients */
    for (i = 0; i < 5; i++)
    {
	if (theme_data->gradients[i] != NULL)
	    theme_data->gradients[i] = (eazel_engine_gradient_ref
					(theme_data->gradients[i]));
    }
    for (i = 0; i < EAZEL_ENGINE_PALETTE_SIZE; i++)
    {
	if (theme_data->palette[i] != NULL)
	    theme_data->palette[i] = (eazel_engine_gradient_ref
				      (theme_data->palette[i]));
    }

    theme_data->refcount = 1;

    if (default_stock_data != 0)
	theme_data->stock = eazel_engine_stock_table_ref (default_stock_data);
    else
	theme_data->stock = 0;

    token = g_scanner_peek_next_token(scanner);
    while (token != G_TOKEN_RIGHT_CURLY)
    {
	switch (token)
	{
	    gboolean tem;
	    eazel_engine_stock_table *stock_tem;

	case TOKEN_THICKNESS:
	    token = parse_int_assign (scanner, &theme_data->thickness);
	    break;

	case TOKEN_FOCUS_THICKNESS:
	    token = parse_int_assign (scanner, &theme_data->focus_thickness);
	    break;

	case TOKEN_DEFAULT_THICKNESS:
	    token = parse_int_assign (scanner, &theme_data->default_thickness);
	    break;

	case TOKEN_FOCUS_COLOR:
	    token = parse_color_assign (theme_data, scanner,
					&theme_data->focus_color);
	    break;

	case TOKEN_INSENSITIVE_COLORS:
	    token = parse_n_color_assign (theme_data, scanner,
					  theme_data->insensitive_colors, 2);
	    break;

	case TOKEN_GRADIENT:
	    token = parse_gradient_assign (theme_data, scanner,
					   theme_data->gradients);
	    break;

	case TOKEN_SHADOW:
	    token = parse_boolean_assign (scanner, &tem);
	    if (token == G_TOKEN_NONE)
		theme_data->no_shadow = !tem;
	    break;

	case TOKEN_INVERSE_SHADOW:
	    token = parse_boolean_assign (scanner, &tem);
	    if (token == G_TOKEN_NONE)
		theme_data->inverse_shadow = tem;
	    break;

	case TOKEN_OUTLINE_SHADOW:
	    token = parse_boolean_assign (scanner, &tem);
	    if (token == G_TOKEN_NONE)
		theme_data->outline_shadow = !tem;
	    break;

	case TOKEN_PALETTE:
	    token = parse_palette_assign (scanner, theme_data);
	    break;

	case TOKEN_STOCK:
	    token = parse_stock_stmt (scanner, theme_data, &stock_tem);
	    if (token == G_TOKEN_NONE)
	    {
		if (theme_data->stock != 0)
		    eazel_engine_stock_table_unref (theme_data->stock);

		theme_data->stock = stock_tem;
		had_stock_table = TRUE;
	    }
	    break;

	case TOKEN_FG:
	    token = parse_standard_color_assign (theme_data, scanner, rc_style,
						 rc_style->fg, GTK_RC_FG);
	    break;

	case TOKEN_BG:
	    token = parse_standard_color_assign (theme_data, scanner, rc_style,
						 rc_style->bg, GTK_RC_BG);
	    break;

	case TOKEN_BASE:
	    token = parse_standard_color_assign (theme_data, scanner, rc_style,
						 rc_style->base, GTK_RC_BASE);
	    break;

	case TOKEN_TEXT:
	    token = parse_standard_color_assign (theme_data, scanner, rc_style,
						 rc_style->text, GTK_RC_TEXT);
	    break;

	default:
	    g_scanner_get_next_token (scanner);
	    token = G_TOKEN_RIGHT_CURLY;
	    break;
	}

	if (token != G_TOKEN_NONE)
	{
	    g_free (theme_data);
	    return token;
	}

	token = g_scanner_peek_next_token (scanner);
    }

    g_scanner_get_next_token(scanner);

    if (theme_data->stock == 0)
	g_error ("First `engine' section must include a `stock' section.");

    if (had_stock_table)
    {
	/* Defining a stock table makes it the default for any
	   engine sections in the future that don't have one.. */

	if (default_stock_data != 0)
	    eazel_engine_stock_table_unref (default_stock_data);

	default_stock_data = eazel_engine_stock_table_ref (theme_data->stock);

	/* Engine data section with stock table (usually the first in
	   in the file) sets some other default values. A hack, but
	   a very useful one! */

	if (default_theme_data != 0)
	    theme_data_unref (default_theme_data);

	theme_data_ref (theme_data);
	default_theme_data = theme_data;
    }

    rc_style->engine_data = theme_data;
    g_scanner_set_scope (scanner, old_scope);

    return G_TOKEN_NONE;
}

static void
theme_merge_rc_style (GtkRcStyle *dest, GtkRcStyle *src)
{
    eazel_theme_data *src_data = src->engine_data;

    if (!dest->engine_data)
    {
	if (src_data)
	{
	    theme_data_ref (src_data);
	    dest->engine_data = src_data;
	}
    }
}

static void
theme_rc_style_to_style (GtkStyle *style, GtkRcStyle *rc_style)
{
    eazel_theme_data *data = rc_style->engine_data;

    switch (data->thickness)
    {
    case 0:
	style->klass = &eazel_class_0;
	break;
    case 1:
	style->klass = &eazel_class_1;
	break;
    case 3:
	style->klass = &eazel_class_3;
	break;
    default:
	g_warning ("eazel theme: Invalid thickness %d in RC file\n",
		   data->thickness);
	/* FALL THROUGH */
    case 2:
	style->klass = &eazel_class_2;
	break;
    }
    style->engine_data = data;
    theme_data_ref (data);
}

static void
theme_duplicate_style (GtkStyle *dest, GtkStyle *src)
{
    dest->klass = src->klass;
    dest->engine_data = src->engine_data;
    theme_data_ref (dest->engine_data);
}

static void
theme_realize_style (GtkStyle *style)
{
}

static void
theme_unrealize_style (GtkStyle *style)
{
}

static void
theme_destroy_rc_style (GtkRcStyle *rc_style)
{
    theme_data_unref (rc_style->engine_data);
    rc_style->engine_data = NULL;
}

static void
theme_destroy_style (GtkStyle *style)
{
    theme_data_unref (style->engine_data);
    style->engine_data = NULL;
}

static void
theme_set_background(GtkStyle *style, GdkWindow *window,
		     GtkStateType state_type)
{
    GdkPixmap *pixmap;
    gint parent_relative;
    eazel_theme_data *theme_data;

    g_return_if_fail (style != NULL);
    g_return_if_fail (window != NULL);

    theme_data = STYLE_THEME_DATA (style);
    g_assert (theme_data != NULL);

    if (style->bg_pixmap[state_type])
    {
	if (style->bg_pixmap[state_type] == (GdkPixmap *) GDK_PARENT_RELATIVE)
	{
	    pixmap = NULL;
	    parent_relative = TRUE;
	}
	else
	{
	    pixmap = style->bg_pixmap[state_type];
	    parent_relative = FALSE;
	}

	gdk_window_set_back_pixmap (window, pixmap, parent_relative);
    }
    else
	gdk_window_set_background (window, &style->bg[state_type]);

    install_focus_hooks (window);
}

void
theme_init (GtkThemeEngine * engine)
{
    GtkRangeClass *rangeclass;
    GtkScaleClass *scaleclass;
    GtkCheckButtonClass *checkclass;

    window_focus_data_key = g_quark_from_static_string (WINDOW_FOCUS_DATA_KEY);

    engine->parse_rc_style = theme_parse_rc_style;
    engine->merge_rc_style = theme_merge_rc_style;
    engine->rc_style_to_style = theme_rc_style_to_style;
    engine->duplicate_style = theme_duplicate_style;
    engine->realize_style = theme_realize_style;
    engine->unrealize_style = theme_unrealize_style;
    engine->destroy_rc_style = theme_destroy_rc_style;
    engine->destroy_style = theme_destroy_style;
    engine->set_background = theme_set_background;

    /* make scrollbar the correct width */
    rangeclass = (GtkRangeClass *) gtk_type_class (gtk_range_get_type ());
    range_slider_width = rangeclass->slider_width;
    range_min_slider_size = rangeclass->min_slider_size;
    range_stepper_size = rangeclass->stepper_size;
    range_stepper_slider_spacing = rangeclass->stepper_slider_spacing;
    rangeclass->slider_width = RANGE_WIDTH - 4;
    rangeclass->min_slider_size = MIN_THUMB_HEIGHT;
    rangeclass->stepper_size = RANGE_WIDTH - 4;
    rangeclass->stepper_slider_spacing = 0;

    /* Make scale slider smaller */
    scaleclass = (GtkScaleClass *)gtk_type_class(gtk_scale_get_type());
    scale_slider_length = scaleclass->slider_length;
    scaleclass->slider_length = SCALE_HEIGHT;

    /* Make check/radio buttons bigger */
    checkclass = (GtkCheckButtonClass *)gtk_type_class(gtk_check_button_get_type());
    check_size = checkclass->indicator_size;
    check_spacing = checkclass->indicator_spacing;
    checkclass->indicator_size = CHECK_SIZE;
    checkclass->indicator_spacing = CHECK_SPACING;

    eazel_engine_install_hacks ();

    gdk_rgb_init ();

    /* Initialize default theme data */
    original_theme_data.gradients[0] = eazel_engine_make_two_point_gradient (GRADIENT_VERTICAL, 0xeeeeee, 0xaaaaaa);
    original_theme_data.gradients[1] = eazel_engine_make_two_point_gradient (GRADIENT_VERTICAL, 0xcccccc, 0x888888);
    original_theme_data.gradients[2] = eazel_engine_make_two_point_gradient (GRADIENT_VERTICAL, 0xffffff, 0xbbbbbb);
    original_theme_data.gradients[3] = eazel_engine_make_two_point_gradient (GRADIENT_VERTICAL, 0xcccccc, 0x888888);
}

void
theme_exit (void)
{
    GtkRangeClass *rangeclass;
    GtkScaleClass *scaleclass;
    GtkCheckButtonClass *checkclass;

    rangeclass = (GtkRangeClass *)gtk_type_class(gtk_range_get_type());
    scaleclass = (GtkScaleClass *)gtk_type_class(gtk_scale_get_type());
    checkclass = (GtkCheckButtonClass *)gtk_type_class(gtk_check_button_get_type());

    rangeclass->slider_width = range_slider_width;
    rangeclass->min_slider_size = range_min_slider_size;
    rangeclass->stepper_size = range_stepper_size;
    rangeclass->stepper_slider_spacing = range_stepper_slider_spacing;

    scaleclass->slider_length = scale_slider_length;

    checkclass->indicator_size = check_size;
    checkclass->indicator_spacing = check_spacing;

    eazel_engine_remove_hacks ();
    uninstall_all_focus_hooks ();
}


/* Focus change hooks */

typedef struct focus_change_data_struct focus_change_data;
struct focus_change_data_struct {
    GtkWidget *widget;

    gboolean is_focused;
    gboolean connected;

    guint focus_in_signal_id;
    guint focus_out_signal_id;
    guint destroyed_signal_id;
};

static GSList *focus_data_list = NULL;

static focus_change_data *
get_focus_data (GtkWidget *widget, gboolean add)
{
    GtkWidget *toplevel = gtk_widget_get_toplevel (widget);
    focus_change_data *data = gtk_object_get_data_by_id (GTK_OBJECT (toplevel),
							 window_focus_data_key);
    if (data == 0 && add)
    {
	data = g_new0 (focus_change_data, 1);
	data->widget = widget;
	gtk_object_set_data_by_id_full (GTK_OBJECT (toplevel),
					window_focus_data_key,
					data, g_free);
	focus_data_list = g_slist_prepend (focus_data_list, data);
    }

    return data;
}

static void
focus_change_helper (GtkWidget *widget, gpointer data)
{
    if (GTK_IS_CONTAINER (widget))
    {
	gtk_container_forall (GTK_CONTAINER (widget),
			      focus_change_helper, NULL);
    }
    else if (GTK_IS_RANGE (widget))
    {
	gtk_widget_queue_draw (widget);
    }
    else if (GTK_IS_PROGRESS (widget))
    {
	/* This is horrible. But the GtkProgress widget stores the
	   progress bar in a pixmap, then blits it on expose. But
	   it will refresh the pixmap when asked to resize.. */
	if (GTK_WIDGET_DRAWABLE (widget))
	    gtk_widget_queue_resize (widget);
    }
}

static void
window_focus_in_callback (GtkWidget *window, GdkEventFocus *event,
			  focus_change_data *data)
{
    data->is_focused = TRUE;
    gtk_container_forall (GTK_CONTAINER (window),
			  focus_change_helper, NULL);
}

static void
window_focus_out_callback (GtkWidget *window, GdkEventFocus *event,
			   focus_change_data *data)
{
    data->is_focused = FALSE;
    gtk_container_forall (GTK_CONTAINER (window),
			  focus_change_helper, NULL);
}

static void
window_destroyed_callback (GtkWidget *window, focus_change_data *data)
{
    focus_data_list = g_slist_remove (focus_data_list, data);
}

gboolean
eazel_engine_widget_in_focused_window_p (GtkWidget *widget)
{
    focus_change_data *data = get_focus_data (widget, FALSE);
    return (data != 0) ? data->is_focused : FALSE;
}

static void
install_focus_hooks (GdkWindow *window)
{
    /* Evilness */
    GtkWidget *widget;
    gdk_window_get_user_data (window, (gpointer *) &widget);
    if (widget != NULL && GTK_IS_WINDOW (widget))
    {
	focus_change_data *data = get_focus_data (widget, TRUE);
	if (!data->connected)
	{
	    /* Connect to this window so we get focus-in/out events */
	    data->focus_in_signal_id
		= gtk_signal_connect (GTK_OBJECT (widget), "focus_in_event",
				      window_focus_in_callback, data);
	    data->focus_out_signal_id
		= gtk_signal_connect (GTK_OBJECT (widget), "focus_out_event",
				      window_focus_out_callback, data);
	    data->destroyed_signal_id
		= gtk_signal_connect (GTK_OBJECT (widget), "destroy",
				      window_destroyed_callback, data);

	    data->connected = TRUE;
	}
    }
}

static void
uninstall_all_focus_hooks (void)
{
    GSList *ptr;
    for (ptr = focus_data_list; ptr != 0; ptr = ptr->next)
    {
	focus_change_data *data = ptr->data;
	if (data->connected)
	{
	    gtk_signal_disconnect (GTK_OBJECT (data->widget),
				   data->focus_in_signal_id);
	    gtk_signal_disconnect (GTK_OBJECT (data->widget),
			       data->focus_out_signal_id);
	    gtk_signal_disconnect (GTK_OBJECT (data->widget),
				   data->destroyed_signal_id);
	}
	gtk_object_remove_data_by_id (GTK_OBJECT (data->widget),
				      window_focus_data_key);
    }
    g_slist_free (focus_data_list);
    focus_data_list = NULL;
}


/* The following function will be called by GTK+ when the module
 * is loaded and checks to see if we are compatible with the
 * version of GTK+ that loads us.
 */

G_MODULE_EXPORT const gchar *g_module_check_init (GModule *module);

const gchar *
g_module_check_init (GModule *module)
{
  return gtk_check_version (GTK_MAJOR_VERSION,
			    GTK_MINOR_VERSION,
			    GTK_MICRO_VERSION - GTK_INTERFACE_AGE);
}
