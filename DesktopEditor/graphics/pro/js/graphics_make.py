import sys
sys.path.append("../../../../../build_tools/scripts")
import base
import os

if not base.is_file("raster.o"):
  print("Please use raster_make.py previously")
  exit(0)

base.configure_common_apps()

if base.is_dir("./temp"):
    base.delete_dir("./temp")
base.create_dir("./temp")

# fetch emsdk
command_prefix = "" if ("windows" == base.host_platform()) else "./"
if not base.is_dir("emsdk"):
    base.cmd("git", ["clone", "https://github.com/emscripten-core/emsdk.git"])
    os.chdir("emsdk")
    base.cmd(command_prefix + "emsdk", ["install", "latest"])
    base.cmd(command_prefix + "emsdk", ["activate", "latest"])
    os.chdir("../")

if not base.is_dir("xml"):
   base.copy_dir("../../../xml", "./xml")
   base.replaceInFile("./xml/libxml2/libxml.h", "xmlNop(void)", "xmlNop(void* context, char* buffer, int len)")
   base.replaceInFile("./xml/libxml2/xmlIO.c", "xmlNop(void)", "xmlNop(void* context, char* buffer, int len)")
   base.replaceInFile("./xml/src/xmllight_private.h", "#include \"../../common/", "#include \"../../../../../common/")
   base.replaceInFile("./xml/include/xmlutils.h", "#include \"../../common/", "#include \"../../../../../common/")

# compile
compiler_flags = ["-O3",
                  "-fno-rtti",
                  "-s WASM=1",
                  "-s ALLOW_MEMORY_GROWTH=1",
                  "-s FILESYSTEM=0",
                  "-s ENVIRONMENT='web'",
                  "-s LLD_REPORT_UNDEFINED"]

exported_functions = ["_malloc",
                      "_free",
                      "_XPS_Load",
                      "_DJVU_Load",
                      "_XPS_Close",
                      "_XPS_GetInfo",
                      "_XPS_GetPixmap",
                      "_XPS_GetGlyphs",
                      "_XPS_GetStructure",
                      "_XPS_Delete"]

libGraphics_src_path = "../../"
input_graphics_sources = ["GraphicsRenderer.cpp", "pro/pro_Graphics.cpp", "pro/pro_Fonts.cpp", "pro/pro_Image.cpp", "Graphics.cpp", "Brush.cpp", "GraphicsPath.cpp", "Image.cpp", "Matrix.cpp", "Clip.cpp", "TemporaryCS.cpp"]

libFontEngine_src_path = "../../../fontengine/"
input_fontengine_sources = ["GlyphString.cpp", "FontManager.cpp", "FontFile.cpp", "FontPath.cpp", "ApplicationFonts.cpp"]

libAgg_src_path = "../../../agg-2.4/src/"
input_agg_sources = ["agg_arc.cpp", "agg_vcgen_stroke.cpp", "agg_vcgen_dash.cpp", "agg_trans_affine.cpp", "agg_curves.cpp"]

libFreetype_src_path = "../../../freetype-2.10.4/src/"
input_freetype_sources = ["base/ftinit.c", "base/ftlcdfil.c", "base/ftobjs.c", "base/ftglyph.c", "base/ftoutln.c", "base/ftutil.c", "base/ftgloadr.c", "base/ftfntfmt.c", "base/ftcalc.c", "base/ftbitmap.c", "base/ftstream.c", "base/fthash.c", "base/ftdebug.c", "base/fttrigon.c", "base/ftadvanc.c", "base/ftpsprop.c", "base/ftrfork.c", "bdf/bdfdrivr.c", "bdf/bdflib.c", "smooth/ftsmooth.c", "smooth/ftgrays.c", "../builds/unix/ftsystem.c", "autofit/afmodule.c", "autofit/afhints.c", "autofit/afloader.c", "autofit/afglobal.c", "autofit/afshaper.c", "autofit/afranges.c", "autofit/afdummy.c", "autofit/aflatin.c", "autofit/afcjk.c", "autofit/afindic.c", "autofit/afangles.c", "autofit/afblue.c", "autofit/afwarp.c", "truetype/ttdriver.c", "truetype/ttgload.c", "truetype/ttpload.c", "truetype/ttobjs.c", "truetype/ttgxvar.c", "truetype/ttinterp.c", "type1/t1driver.c", "type1/t1afm.c", "type1/t1load.c", "type1/t1gload.c", "type1/t1objs.c", "type1/t1parse.c", "cff/cffdrivr.c", "cff/cffgload.c", "cff/cffload.c", "cff/cffcmap.c", "cff/cffparse.c", "cff/cffobjs.c", "cid/cidriver.c", "cid/cidobjs.c", "cid/cidgload.c", "cid/cidload.c", "cid/cidparse.c", "pfr/pfrdrivr.c", "pfr/pfrobjs.c", "pfr/pfrload.c", "pfr/pfrgload.c", "pfr/pfrcmap.c", "pfr/pfrsbit.c", "type42/t42drivr.c", "type42/t42objs.c", "type42/t42parse.c", "winfonts/winfnt.c", "pcf/pcfdrivr.c", "pcf/pcfread.c", "pcf/pcfutil.c", "psaux/psauxmod.c", "psaux/psobjs.c", "psaux/t1decode.c", "psaux/psft.c", "psaux/afmparse.c", "psaux/t1cmap.c", "psaux/cffdecode.c", "psaux/psconv.c", "psaux/psfont.c", "psaux/psblues.c", "psaux/psintrp.c", "psaux/pserror.c", "psaux/psstack.c", "psaux/pshints.c", "psaux/psarrst.c", "psaux/psread.c", "psnames/psmodule.c", "pshinter/pshmod.c", "pshinter/pshrec.c", "pshinter/pshglob.c", "pshinter/pshalgo.c", "raster/ftrend1.c", "raster/ftraster.c", "sfnt/sfdriver.c", "sfnt/ttpost.c", "sfnt/sfobjs.c", "sfnt/ttload.c", "sfnt/ttbdf.c", "sfnt/ttmtx.c", "sfnt/ttkern.c", "sfnt/sfwoff.c", "sfnt/ttcmap.c", "sfnt/ttsbit.c", "sfnt/sfwoff2.c", "sfnt/ttcolr.c", "sfnt/woff2tags.c", "sfnt/ttcpal.c", "gzip/ftgzip.c", "lzw/ftlzw.c"]

libCommon_src_path = "../../../common/"
input_common_sources = ["File.cpp", "Directory.cpp", "ByteBuilder.cpp", "Base64.cpp", "StringExt.cpp"]

libUnicodeConverter_src_path = "../../../../UnicodeConverter/"
input_unicodeconverter_sources = ["UnicodeConverter.cpp"]

libIcu_src_path = "../../../../Common/3dParty/icu/icu/source/common/"
input_icu_sources = ["ucnv.c", "ustr_wcs.cpp", "ucnv_err.c", "ucnv_bld.cpp", "ustrtrns.cpp", "ucnv_cb.c", "udata.cpp", "ucnv_io.cpp", "uhash.c", "udatamem.c", "cmemory.c", "ustring.cpp", "umutex.cpp", "putil.cpp", "ustr_cnv.cpp", "ucnvmbcs.cpp", "ucnvlat1.c", "ucnv_u16.c", "ucnv_u8.c", "ucnv_u32.c", "ucnv_u7.c", "ucln_cmn.cpp", "ucnv2022.cpp", "ucnv_lmb.c", "ucnvhz.c", "ucnvscsu.c", "ucnvisci.c", "ucnvbocu.cpp", "ucnv_ct.c", "ucnv_cnv.c", "stringpiece.cpp", "charstr.cpp", "umapfile.c", "ucmndata.c", "ucnv_ext.cpp", "uobject.cpp", "umath.c"]

libXps_src_path = "../../../../XpsFile/XpsLib/"
input_xps_sources = ["Document.cpp", "Page.cpp", "StaticResources.cpp", "Utils.cpp", "WString.cpp", "ContextState.cpp"]

libDjVu_src_path = "../../../../DjVuFile/libdjvu/"
input_djvu_sources = ["Arrays.cpp", "BSByteStream.cpp", "BSEncodeByteStream.cpp", "ByteStream.cpp", "DataPool.cpp", "debug.cpp", "DjVmDir.cpp", "DjVmDir0.cpp", "DjVmDoc.cpp", "DjVmNav.cpp", "DjVuAnno.cpp", "DjVuDocEditor.cpp", "DjVuDocument.cpp", "DjVuDumpHelper.cpp", "DjVuErrorList.cpp", "DjVuFile.cpp", "DjVuFileCache.cpp", "DjVuGlobal.cpp", "DjVuGlobalMemory.cpp", "DjVuImage.cpp", "DjVuInfo.cpp", "DjVuMessageLite.cpp", "DjVuNavDir.cpp", "DjVuPalette.cpp", "DjVuPort.cpp", "DjVuText.cpp", "DjVuToPS.cpp", "GBitmap.cpp", "GContainer.cpp", "GException.cpp", "GIFFManager.cpp", "GMapAreas.cpp", "GPixmap.cpp", "GRect.cpp", "GScaler.cpp", "GSmartPointer.cpp", "GString.cpp", "GThreads.cpp", "GUnicode.cpp", "IFFByteStream.cpp", "IW44EncodeCodec.cpp", "IW44Image.cpp", "JB2EncodeCodec.cpp", "JB2Image.cpp", "JPEGDecoder.cpp", "MMRDecoder.cpp", "MMX.cpp", "UnicodeByteStream.cpp", "XMLParser.cpp", "XMLTags.cpp", "ZPCodec.cpp"]

libWasmDjVu_src_path = "../../../../DjVuFile/wasm/libdjvu/"
input_wasmdjvu_sources = ["atomic.cpp", "DjVuMessage.cpp", "GOS.cpp", "GURL.cpp"]

libOfficeUtils_src_path = "../../../../OfficeUtils/src/"
input_officeutils_sources = ["OfficeUtils.cpp", "ZipBuffer.cpp", "ZipUtilsCP.cpp"]

libMinizip_src_path = "../../../../OfficeUtils/src/zlib-1.2.11/contrib/minizip/"
input_minizip_sources = ["ioapi.c", "miniunz.c", "minizip.c", "mztools.c", "unzip.c", "zip.c", "ioapibuf.c"]

libZlib_src_path = "../../../../OfficeUtils/src/zlib-1.2.11/"
input_zlib_sources = ["adler32.c", "crc32.c", "deflate.c", "infback.c", "inffast.c", "inflate.c", "inftrees.c", "trees.c", "zutil.c", "compress.c"]

input_xml_sources = ["xml/src/xmllight.cpp", "xml/src/xmldom.cpp", "xml/build/qt/libxml2_all.c", "xml/build/qt/libxml2_all2.c"]

libPdf_src_path = "../../../../PdfWriter/"
input_pdf_sources = ["PdfRenderer.cpp"]

# sources
sources = []
for item in input_graphics_sources:
    sources.append(libGraphics_src_path + item)
for item in input_fontengine_sources:
    sources.append(libFontEngine_src_path + item)
for item in input_agg_sources:
    sources.append(libAgg_src_path + item)
# freetype
for item in input_common_sources:
    sources.append(libCommon_src_path + item)
for item in input_unicodeconverter_sources:
    sources.append(libUnicodeConverter_src_path + item)
# icu
sources.append("../../../../XpsFile/XpsFile.cpp")
# xps
for item in input_djvu_sources:
    sources.append(libDjVu_src_path + item)
for item in input_wasmdjvu_sources:
    sources.append(libWasmDjVu_src_path + item)
sources.append("../../../../DjVuFile/DjVu.cpp ../../../../DjVuFile/DjVuFileImplementation.cpp")
for item in input_officeutils_sources:
    sources.append(libOfficeUtils_src_path + item)
# minizip
# zlib
for item in input_xml_sources:
    sources.append(item)
for item in input_pdf_sources:
    sources.append(libPdf_src_path + item)
sources.append("raster.o")
sources.append("wasm/src/wasmgraphics.cpp")

compiler_flags.append("-I../../../agg-2.4/include -I../../../cximage/jasper/include -I../../../cximage/jpeg -I../../../cximage/png -I../../../freetype-2.10.4/include -I../../../freetype-2.10.4/include/freetype -I../../../../OfficeUtils/src/zlib-1.2.11 -I../../../../Common/3dParty/icu/icu/source/common -I../../../xml/libxml2/include -I../../../xml/build/qt -I../../../../OfficeUtils/src/zlib-1.2.11/contrib/minizip -I../../../../OfficeUtils/src/zlib-1.2.11")
compiler_flags.append("-D__linux__ -D_LINUX -DUNIX -DFT2_BUILD_LIBRARY -DHAVE_FCNTL_H -DFT_CONFIG_OPTION_SYSTEM_ZLIB -DBUILDING_WASM_MODULE -DU_COMMON_IMPLEMENTATION")
compiler_flags.append("-DWASM_MODE -Derrno=0 -DTHREADMODEL=0 -DDEBUGLVL=0 -DHAVE_MBSTATE_T -DHAVE_STDINCLUDES -DHAS_WCHAR")
compiler_flags.append("-DHAVE_VA_COPY -DLIBXML_READER_ENABLED -DLIBXML_PUSH_ENABLED -DLIBXML_HTML_ENABLED -DLIBXML_XPATH_ENABLED -DLIBXML_OUTPUT_ENABLED -DLIBXML_C14N_ENABLED -DLIBXML_SAX1_ENABLED -DLIBXML_TREE_ENABLED -DLIBXML_XPTR_ENABLED -DIN_LIBXML -DLIBXML_STATIC -DBUILD_ZLIB_AS_SOURCES")

# arguments
arguments = ""
for item in compiler_flags:
    arguments += (item + " ")

# command
windows_bat = []
if base.host_platform() == "windows":
    windows_bat.append("call emsdk/emsdk_env.bat") 

    libs = ""
    for item in input_freetype_sources:
        windows_bat.append("call emcc -o temp/" + os.path.basename(item) + ".o -c " + arguments + libFreetype_src_path + item)
        libs += ("temp/" + os.path.basename(item) + ".o ")
    
    for item in input_icu_sources:
        windows_bat.append("call emcc -o temp/" + item + ".o -c " + arguments + libIcu_src_path + item)
        libs += ("temp/" + item + ".o ")
    
    for item in input_xps_sources:
        windows_bat.append("call emcc -o temp/" + item + ".o -c " + arguments + libXps_src_path + item)
        libs += ("temp/" + item + ".o ")
    
    for item in input_minizip_sources:
        windows_bat.append("call emcc -o temp/" + item + ".o -c " + arguments + libMinizip_src_path + item)
        libs += ("temp/" + item + ".o ")
    
    for item in input_zlib_sources:
        windows_bat.append("call emcc -o temp/" + item + ".o -c " + arguments + libZlib_src_path + item)
        libs += ("temp/" + item + ".o ")

    arguments += "-s EXPORTED_FUNCTIONS=\"["
    for item in exported_functions:
        arguments += ("'" + item + "',")
    arguments = arguments[:-1]
    arguments += "]\" "

    for item in sources:
        arguments += (item + " ")

    windows_bat.append("call emcc -o xps_djvu.js " + arguments + libs)
else:
    windows_bat.append("#!/bin/bash")
    windows_bat.append("source ./emsdk/emsdk_env.sh")

    libs = ""
    for item in input_freetype_sources:
        windows_bat.append("emcc -o temp/" + os.path.basename(item) + ".o -c " + arguments + libFreetype_src_path + item)
        libs += ("temp/" + os.path.basename(item) + ".o ")
    
    for item in input_icu_sources:
        windows_bat.append("emcc -o temp/" + item + ".o -c " + arguments + libIcu_src_path + item)
        libs += ("temp/" + item + ".o ")
    
    for item in input_xps_sources:
        windows_bat.append("emcc -o temp/" + item + ".o -c " + arguments + libXps_src_path + item)
        libs += ("temp/" + item + ".o ")
    
    for item in input_minizip_sources:
        windows_bat.append("emcc -o temp/" + item + ".o -c " + arguments + libMinizip_src_path + item)
        libs += ("temp/" + item + ".o ")
    
    for item in input_zlib_sources:
        windows_bat.append("emcc -o temp/" + item + ".o -c " + arguments + libZlib_src_path + item)
        libs += ("temp/" + item + ".o ")
    
    arguments += "-s EXPORTED_FUNCTIONS=\"["
    for item in exported_functions:
        arguments += ("'" + item + "',")
    arguments = arguments[:-1]
    arguments += "]\" "

    for item in sources:
        arguments += (item + " ")
    
    windows_bat.append("emcc -o xps_djvu.js " + arguments + libs)
base.run_as_bat(windows_bat)

# finalize
base.replaceInFile("./xps_djvu.js", "function getBinaryPromise(){", "function getBinaryPromise2(){")
graphics_js_content = base.readFile("./xps_djvu.js")
engine_base_js_content = base.readFile("./wasm/js/xps_djvu_base.js")
string_utf8_content    = base.readFile("./../../../../Common/js/string_utf8.js")
engine_js_content = engine_base_js_content.replace("//module", graphics_js_content)
engine_js_content = engine_js_content.replace("//string_utf8", string_utf8_content)

# write new version
base.writeFile("./deploy/xps_djvu.js", engine_js_content)
base.copy_file("./xps_djvu.wasm", "./deploy/xps_djvu.wasm")

base.delete_file("xps_djvu.js")
base.delete_file("xps_djvu.wasm")
base.delete_dir("./temp")
base.delete_dir("./xml")
#base.delete_file("raster.o")