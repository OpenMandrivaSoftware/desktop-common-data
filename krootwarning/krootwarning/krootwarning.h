/***************************************************************************
                          krootwarning.h  -  description
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

#ifndef KROOTWARNING_H
#define KROOTWARNING_H

#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <kapp.h>
#include <kdialogbase.h>
class QCheckBox;

/** Krootwarning is the base class of the porject */
class Krootwarning : public KDialogBase
{
  Q_OBJECT 
  public:
    /** construtor */
    Krootwarning(QWidget* parent=0, const char *name=0);
    /** destructor */
    ~Krootwarning();
 protected:
    void initInterface();
    void saveConfig();
    void loadConfig();
    void logout();
 private:
    QCheckBox *m_showAtTheNewStartUp;
 protected slots:
     virtual void slotUser1();
 virtual void slotUser2();
};

#endif
