/***************************************************************************
                          main.cpp  -  description
                             -------------------
    begin                : mar jui 10 13:42:19 CEST 2001
    copyright            : (C) 2001 by Laurent MONTEL
    email                : lmontel@mandrakesoft.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

#include <kcmdlineargs.h>
#include <kaboutdata.h>
#include <klocale.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include "krootwarning.h"

static const char *description =
	I18N_NOOP("Krootwarning");
// INSERT A DESCRIPTION FOR YOUR APPLICATION HERE
	
	
static KCmdLineOptions options[] =
{
  { 0, 0, 0 }
  // INSERT YOUR COMMANDLINE OPTIONS HERE
};

int main(int argc, char *argv[])
{
  if(getuid()!=0)
    exit(1);
  KAboutData aboutData( "krootwarning", I18N_NOOP("Krootwarning"),
    VERSION, description, KAboutData::License_GPL,
    "(c) 2001, Laurent MONTEL", 0, 0, "lmontel@mandrakesoft.com");
  aboutData.addAuthor("Laurent MONTEL",0, "lmontel@mandrakesoft.com");
  KCmdLineArgs::init( argc, argv, &aboutData );
  KCmdLineArgs::addCmdLineOptions( options ); // Add our own options.

  KApplication a;
  Krootwarning *krootwarning = new Krootwarning();
  a.setMainWidget(krootwarning);
  krootwarning->show();  

  return 0;
}
