#ifndef CEMFPLUSPARSER_H
#define CEMFPLUSPARSER_H

#include "../../Common/MetaFileUtils.h"

namespace MetaFile
{
        class CEmfParser;
        class CEmfPlusParser
        {
            public:
                CEmfPlusParser(CEmfParser *pEmfParser);
                void SetStream(BYTE *pBytes, unsigned int unSize);
                void PlayFile();
            private:
                void Read_EMRPLUS_OFFSETCLIP();
                void Read_EMRPLUS_RESETCLIP();
                void Read_EMFPLUS_SETCLIPPATH(unsigned short unShFlags);
                void Read_EMFPLUS_SETCLIPRECT(unsigned short unShFlags);
                void Read_EMFPLUS_SETCLIPREGION(unsigned short unShFlags);

                void Read_EMFPLUS_COMMENT(unsigned int unDataSize);

                void Read_EMFPLUS_ENDOFFILE();
                void Read_EMFPLUS_GETDC();
                void Read_EMRPLUS_HEADER(unsigned short unShFlags);

                void Read_EMFPLUS_CLEAR();
                void Read_EMFPLUS_DRAWARC(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_DRAWARC_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_DRAWBEZIERS(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_DRAWBEZIERS_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_DRAWCLOSEDCURVE(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_DRAWCLOSEDCURVE_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_DRAWCURVE(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_DRAWCURVE_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_DRAWDRIVERSTRING(unsigned short unShFlags);
                void Read_EMFPLUS_DRAWELLIPSE(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_DRAWELLIPSE_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_DRAWIMAGE(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_DRAWIMAGE_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_DRAWIMAGEPOINTS(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_DRAWIMAGEPOINTS_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_DRAWLINES(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_DRAWLINES_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_DRAWPATH(unsigned short unShFlags);
                void Read_EMFPLUS_DRAWPIE(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_DRAWPIE_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_DRAWRECTS(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_DRAWRECTS_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_DRAWSTRING(unsigned short unShFlags);
                void Read_EMFPLUS_FILLCLOSEDCURVE(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_FILLCLOSEDCURVE_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_FILLELLIPSE(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_FILLELLIPSE_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_FILLPATH(unsigned short unShFlags);
                void Read_EMFPLUS_FILLPIE(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_FILLPIE_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_FILLPOLYGON(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_FILLPOLYGON_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_FILLRECTS(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_FILLRECTS_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_FILLREGION(unsigned short unShFlags);

                void Read_EMFPLUS_OBJECT(unsigned short unShFlags);
                void Read_EMFPLUS_SERIALIZABLEOBJECT(unsigned short unShFlags);

                void Read_EMFPLUS_SETANTIALIASMODE(unsigned short unShFlags);
                void Read_EMFPLUS_SETCOMPOSITINGMODE(unsigned short unShFlags);
                void Read_EMFPLUS_SETCOMPOSITINGQUALITY(unsigned short unShFlags);
                void Read_EMFPLUS_SETINTERPOLATIONMODE(unsigned short unShFlags);
                void Read_EMFPLUS_SETPIXELOFFSETMODE(unsigned short unShFlags);
                void Read_EMFPLUS_SETRENDERINGORIGIN();
                void Read_EMFPLUS_SETTEXTCONTRAST(unsigned short unShFlags);
                void Read_EMRPLUS_SETTEXTRENDERINGHINT(unsigned short unShFlags);

                void Read_EMFPLUS_BEGINCONTAINER(unsigned short unShFlags);
                void Read_EMFPLUS_BEGINCONTAINERNOPARAMS();
                void Read_EMFPLUS_ENDCONTAINER();
                void Read_EMFPLUS_RESTORE();
                void Read_EMFPLUS_SAVE();

                void Read_EMFPLUS_SETTSCLIP(unsigned short unShFlags);
                template<typename T>void Read_EMFPLUS_SETTSCLIP_BASE(unsigned short unShFlags);
                void Read_EMFPLUS_SETTSGRAPHICS(unsigned short unShFlags);

                void Read_EMFPLUS_MULTIPLYWORLDTRANSFORM(unsigned short unShFlags);
                void Read_EMFPLUS_RESETWORLDTRANSFORM();
                void Read_EMFPLUS_ROTATEWORLDTRANSFORM(unsigned short unShFlags);
                void Read_EMFPLUS_SCALEWORLDTRANSFORM(unsigned short unShFlags);
                void Read_EMFPLUS_SETPAGETRANSFORM(unsigned short unShFlags);
                void Read_EMFPLUS_SETWORLDTRANSFORM();
                void Read_EMFPLUS_TRANSLATEWORLDTRANSFORM(unsigned short unShFlags);

                virtual short ExpressValue(unsigned short unShFlags, unsigned int unStartIndex, unsigned int unEndIndex) const;

                CEmfParser *m_pEmfParser;
                CDataStream m_oDataStream;
        };
}

#endif // CEMFPLUSPARSER_H