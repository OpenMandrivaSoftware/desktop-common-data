/* Slide Show Screen Saver
 * (C) 1999 Stefan Taferner <taferner@kde.org>
 * Adapted by Laurent MONTEL <lmontel@mandrakesoft.com>
 * for MandrakeSoft.
 */                     


#ifndef MANDRAKE_H
#define MANDRAKE_H

#include <qtimer.h>
#include <qlist.h>
#include <qdialog.h>
#include <qstringlist.h>
#include <qpixmap.h>
#include <qwidget.h>
#include <qpainter.h>
#include <qimage.h>
#include <kscreensaver.h>

class krozatSaver;
class QCheckBox;
class QSlider;
class QComboBox;
class QLabel;


//-----------------------------------------------------------------------------
class krozatSaver: public KScreenSaver
{
  Q_OBJECT
public:
  krozatSaver( WId id );
  virtual ~krozatSaver();

  typedef int (krozatSaver::*EffectMethod)(bool);

  void readConfig();

  void restart();

protected slots:
  void slotTimeout();

protected:
  void blank();

  /** Load list of images from directory */
  virtual void loadDirectory();

  /** Load next image from list. If the file cannot be read
	   it is automatically removed from the file list. 
		mImage contains the image after loading. */
  virtual void loadNextImage();

  /** Show next screen, completely, without transition. */
  virtual void showNextScreen();

  /** Set loaded image to next-screen buffer. */
  virtual void createNextScreen();

  /** Initialize next-screen buffer. */
  virtual void initNextScreen();

  /** Register effect methods in effect list. */
  virtual void registerEffects();

  /** Various effects. If adding one, do not forget to manually
	add the effect to the list in the registerEffects() method. */
  int effectHorizLines(bool doInit);
  int effectVertLines(bool doInit);
  int effectRandom(bool doInit);
  int effectGrowing(bool doInit);
  int effectChessboard(bool doInit);
  int effectIncomingEdges(bool doInit);
  int effectBlobs(bool doInit);
  int effectCircleOut(bool doInit);
  int effectSweep(bool doInit);
  int effectMeltdown(bool doInit);
  int effectSpiralIn(bool doInit);
  int effectMultiCircleOut(bool doInit);

protected:
  /** Init mPainter with next-screen's pixmap and call
      mPainter.begin(&mWidget) */
  void startPainter(Qt::PenStyle penStyle=NoPen);

protected:
  bool mEffectRunning;
  QTimer mTimer;
  int mColorContext;
  QStringList mFileList;
  int mFileIdx;
  QImage mImage;
  QPixmap mNextScreen;
  EffectMethod* mEffectList;
  EffectMethod mEffect;
  int mNumEffects;
  QPainter mPainter;
  QString mImageName;

  // config settings:
  int mDelay;
  QString mDirectory;

  // values for state of various effects:
  int mx, my, mw, mh, mdx, mdy, mix, miy, mi, mj, mSubType;
  int mx0, my0, mx1, my1, mwait;
  double mfx, mfy, mAlpha, mfd;
  int* mIntArray;
};


//-----------------------------------------------------------------------------
class krozatSetup : public QDialog
{
  Q_OBJECT
public:
  krozatSetup(QWidget *parent=NULL, const char *name=NULL);
  void minSize(QWidget* aWidget);

protected slots:
  void slotOkPressed();
  void slotAbout();

};

#endif

