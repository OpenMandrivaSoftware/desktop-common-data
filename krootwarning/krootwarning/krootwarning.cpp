/***************************************************************************
                          krootwarning.cpp  -  description
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

#include "krootwarning.h"
#include <kdialogbase.h>
#include <klocale.h>
#include <qlabel.h>
#include <kdebug.h>
#include <qlayout.h>
#include <qcheckbox.h>
#include <kapp.h>
#include <kconfig.h>
#include <dcopclient.h>
#include <qmessagebox.h>
#include <klocale.h>
#include <kstddirs.h>

Krootwarning::Krootwarning(QWidget *parent, const char *name)
 :KDialogBase( parent, "urldialog", true, i18n("Warning"), User1|User2, User1, true,i18n("Logout"),i18n("Continue") )
{
    initInterface();
}

Krootwarning::~Krootwarning()
{
}

void Krootwarning::initInterface()
{
    QWidget *page = new QWidget( this );
    setMainWidget(page);
    if ( !kapp->dcopClient()->isAttached() )
        kapp->dcopClient()->attach();
    QGridLayout *grid = new QGridLayout( page, 9, 3, KDialog::marginHint(), KDialog::spacingHint() );

    QLabel *label1 = new QLabel( page );

    QString resource_prefix = "krootwarning/pics/";

    label1->setPixmap(QPixmap(locate("data", resource_prefix + "ic-attention-64.png")));


    grid->addMultiCellWidget(label1,0,8,0,0);

    QLabel *info=new QLabel("<qt>" +i18n("You are running a graphical interface as root.")+"<br><br>"+
      i18n("This is a bad idea because as root, you can damage your system, and nothing will stop you.")+"<br><br>"+
      i18n("Click on ")+"<b>"+i18n("'Continue'")+"</b>"+i18n(" if you really know what you are doing.")+"<br>"
			    +i18n("Otherwise, please click on ")+"<b>"+i18n("'Logout' ")+"</b>"+i18n("and read your manual ")+"<br>"+
			    i18n("to know how to add a non-privileged user account ")+"<br>"
      +i18n("to the system.")+"<br></qt>",page);

    grid->addMultiCellWidget(info,0,7,1,1);
    m_showAtTheNewStartUp=new QCheckBox( i18n("Don't show this window again."), page);
    grid->addMultiCellWidget(m_showAtTheNewStartUp,8,8,0,1);
    resize(400,280);
    loadConfig();
}

void Krootwarning::slotUser1()
{
    //logout!!!!!!!!!!!!!!!
    saveConfig();
    logout();
    accept();
}

void Krootwarning::loadConfig()
{
    KConfig* config=kapp->config();
    if( config->hasGroup("Parameter" ) )
    {
        config->setGroup( "Parameter" );
        m_showAtTheNewStartUp->setChecked(config->readBoolEntry("ShowWindowAtTheNextStartUp",false));
    }
}

void Krootwarning::slotUser2()
{
    //ok
    saveConfig();
    accept();
}

void Krootwarning::saveConfig()
{
    KConfig* config=kapp->config();
    config->setGroup( "Parameter" );
    config->writeEntry("ShowWindowAtTheNextStartUp", m_showAtTheNewStartUp->isChecked() );
}

void Krootwarning::logout()
{
    //send a messge to kdesktop logout without confirmation
	kapp->dcopClient()->send( "kdesktop", "", "logoutWithoutConfirmation()", "" );
}

#include "krootwarning.moc"
