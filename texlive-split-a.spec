%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-a
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source0100:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/12many.tar.xz
Source0101:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/12many.doc.tar.xz
Source0103:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/2up.tar.xz
Source0104:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/2up.doc.tar.xz
Source0105:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/a0poster.tar.xz
Source0106:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/a0poster.doc.tar.xz
Source0109:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/a4wide.tar.xz
Source0110:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/a4wide.doc.tar.xz
Source0111:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/a5comb.tar.xz
Source0112:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/a5comb.doc.tar.xz
Source0113:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aastex.tar.xz
Source0114:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aastex.doc.tar.xz
Source0116:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abbr.tar.xz
Source0117:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abbr.doc.tar.xz
Source0118:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abc.tar.xz
Source0119:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abc.doc.tar.xz
Source0121:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abntex2.tar.xz
Source0122:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abntex2.doc.tar.xz
Source0123:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abraces.tar.xz
Source0124:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abraces.doc.tar.xz
Source0125:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abstract.tar.xz
Source0126:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abstract.doc.tar.xz
Source0128:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abstyles.tar.xz
Source0129:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abstyles.doc.tar.xz
Source0130:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/academicons.tar.xz
Source0131:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/academicons.doc.tar.xz
Source0132:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/accanthis.tar.xz
Source0133:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/accanthis.doc.tar.xz
Source0136:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/achemso.tar.xz
Source0137:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/achemso.doc.tar.xz
Source0139:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/acmconf.tar.xz
Source0140:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/acmconf.doc.tar.xz
Source0142:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/acronym.tar.xz
Source0143:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/acronym.doc.tar.xz
Source0145:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/acroterm.tar.xz
Source0146:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/acroterm.doc.tar.xz
Source0148:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/acro.tar.xz
Source0149:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/acro.doc.tar.xz
Source0150:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/active-conf.tar.xz
Source0151:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/active-conf.doc.tar.xz
Source0153:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/actuarialangle.tar.xz
Source0154:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/actuarialangle.doc.tar.xz
Source0155:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/addlines.tar.xz
Source0156:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/addlines.doc.tar.xz
Source0158:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adfathesis.tar.xz
Source0159:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adfathesis.doc.tar.xz
Source0161:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adforn.tar.xz
Source0162:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adforn.doc.tar.xz
Source0163:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adfsymbols.tar.xz
Source0164:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adfsymbols.doc.tar.xz
Source0168:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adjmulticol.tar.xz
Source0169:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adjmulticol.doc.tar.xz
Source0171:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adjustbox.tar.xz
Source0172:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adjustbox.doc.tar.xz
Source0174:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adobemapping.tar.xz
Source0175:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adrconv.tar.xz
Source0176:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adrconv.doc.tar.xz
Source0178:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/advdate.tar.xz
Source0179:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/advdate.doc.tar.xz
Source0180:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aecc.tar.xz
Source0181:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aecc.doc.tar.xz
Source0182:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aeguill.tar.xz
Source0183:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aeguill.doc.tar.xz
Source0184:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ae.tar.xz
Source0185:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ae.doc.tar.xz
Source0189:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/afparticle.tar.xz
Source0190:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/afparticle.doc.tar.xz
Source0192:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/afthesis.tar.xz
Source0193:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/afthesis.doc.tar.xz
Source0194:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aguplus.tar.xz
Source0195:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aguplus.doc.tar.xz
Source0196:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aiaa.tar.xz
Source0197:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aiaa.doc.tar.xz
Source0199:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aichej.tar.xz
Source0200:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ajl.tar.xz
Source0201:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/akktex.tar.xz
Source0202:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/akktex.doc.tar.xz
Source0203:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/akletter.tar.xz
Source0204:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/akletter.doc.tar.xz
Source0205:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/alegreya.tar.xz
Source0206:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/alegreya.doc.tar.xz
Source0224:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/alertmessage.tar.xz
Source0225:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/alertmessage.doc.tar.xz
Source0227:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/algorithm2e.tar.xz
Source0228:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/algorithm2e.doc.tar.xz
Source0229:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/algorithmicx.tar.xz
Source0230:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/algorithmicx.doc.tar.xz
Source0231:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/algorithms.tar.xz
Source0232:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/algorithms.doc.tar.xz
Source0234:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/alg.tar.xz
Source0235:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/alg.doc.tar.xz
Source0237:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/allrunes.tar.xz
Source0238:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/allrunes.doc.tar.xz
Source0240:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/almfixed.tar.xz
Source0241:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/almfixed.doc.tar.xz
Source0242:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/alnumsec.tar.xz
Source0243:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/alnumsec.doc.tar.xz
Source0245:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/alterqcm.tar.xz
Source0246:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/alterqcm.doc.tar.xz
Source0247:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/altfont.tar.xz
Source0248:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/altfont.doc.tar.xz
Source0250:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ametsoc.tar.xz
Source0251:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ametsoc.doc.tar.xz
Source0252:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amiri.tar.xz
Source0253:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amiri.doc.tar.xz
Source0254:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amsaddr.tar.xz
Source0255:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amsaddr.doc.tar.xz
Source0257:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amscls.tar.xz
Source0258:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amscls.doc.tar.xz
Source0260:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amsfonts.tar.xz
Source0261:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amsfonts.doc.tar.xz
Source0263:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amslatex-primer.doc.tar.xz
Source0264:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amsldoc-it.doc.tar.xz
Source0265:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amsldoc-vn.doc.tar.xz
Source0266:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amsmath-it.doc.tar.xz
Source0267:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amsmath.tar.xz
Source0268:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amsmath.doc.tar.xz
Source0270:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amsrefs.tar.xz
Source0271:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amsrefs.doc.tar.xz
Source0277:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amsthdoc-it.doc.tar.xz
Source0278:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/animate.tar.xz
Source0279:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/animate.doc.tar.xz
Source0281:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/anonchap.tar.xz
Source0282:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/anonchap.doc.tar.xz
Source0283:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/anonymouspro.tar.xz
Source0284:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/anonymouspro.doc.tar.xz
Source0286:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/answers.tar.xz
Source0287:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/answers.doc.tar.xz
Source0289:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/antiqua.tar.xz
Source0290:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/antiqua.doc.tar.xz
Source0291:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/antomega.tar.xz
Source0292:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/antomega.doc.tar.xz
Source0296:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/antt.tar.xz
Source0297:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/antt.doc.tar.xz
Source0298:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/anufinalexam.doc.tar.xz
Source0299:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/anyfontsize.tar.xz
Source0300:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/anyfontsize.doc.tar.xz
Source0301:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/anysize.tar.xz
Source0302:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/anysize.doc.tar.xz
Source0303:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aobs-tikz.tar.xz
Source0304:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aobs-tikz.doc.tar.xz
Source0306:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aomart.tar.xz
Source0307:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aomart.doc.tar.xz
Source0309:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apa6e.tar.xz
Source0310:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apa6e.doc.tar.xz
Source0312:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apa6.tar.xz
Source0313:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apa6.doc.tar.xz
Source0315:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apacite.tar.xz
Source0316:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apacite.doc.tar.xz
Source0318:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apalike2.tar.xz
Source0319:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apa.tar.xz
Source0320:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apa.doc.tar.xz
Source0321:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apnum.tar.xz
Source0322:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apnum.doc.tar.xz
Source0323:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/appendixnumberbeamer.tar.xz
Source0324:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/appendixnumberbeamer.doc.tar.xz
Source0325:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/appendix.tar.xz
Source0326:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/appendix.doc.tar.xz
Source0328:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apprends-latex.doc.tar.xz
Source0329:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apptools.tar.xz
Source0330:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apptools.doc.tar.xz
Source0332:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arabi.tar.xz
Source0333:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arabi.doc.tar.xz
Source0334:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arabtex.tar.xz
Source0335:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arabtex.doc.tar.xz
Source0336:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arabxetex.tar.xz
Source0337:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arabxetex.doc.tar.xz
Source0339:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aramaic-serto.tar.xz
Source0340:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aramaic-serto.doc.tar.xz
Source0344:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/archaic.tar.xz
Source0345:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/archaic.doc.tar.xz
Source0347:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arcs.tar.xz
Source0348:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arcs.doc.tar.xz
Source0350:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arev.tar.xz
Source0351:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arev.doc.tar.xz
Source0353:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/armtex.tar.xz
Source0354:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/armtex.doc.tar.xz
Source0373:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/Asana-Math.tar.xz
Source0374:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/Asana-Math.doc.tar.xz
Source2609:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/MemoirChapStyles.doc.tar.xz
Source2610:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/Type1fonts.doc.tar.xz
Source3391:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ESIEEcv.tar.xz
Source3392:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ESIEEcv.doc.tar.xz
Source3394:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/GS1.tar.xz
Source3395:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/GS1.doc.tar.xz
Source3397:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/HA-prosper.tar.xz
Source3398:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/HA-prosper.doc.tar.xz
Source3400:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/Tabbing.tar.xz
Source3401:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/Tabbing.doc.tar.xz
Source6337:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/IEEEconf.tar.xz
Source6338:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/IEEEconf.doc.tar.xz
Source6340:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/IEEEtran.tar.xz
Source6341:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/IEEEtran.doc.tar.xz
Source6634:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/SIstyle.tar.xz
Source6635:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/SIstyle.doc.tar.xz
Source6637:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/SIunits.tar.xz
Source6638:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/SIunits.doc.tar.xz
Source7216:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/acmart.tar.xz
Source7217:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/acmart.doc.tar.xz
Source7219:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arabi-add.tar.xz
Source7220:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arabi-add.doc.tar.xz
Source7221:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arabluatex.tar.xz
Source7223:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arabluatex.doc.tar.xz
Source7224:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/archaeologie.tar.xz
Source7225:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/archaeologie.doc.tar.xz
Source7580:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adtrees.tar.xz
Source7581:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adtrees.doc.tar.xz
Source7617:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abnt.tar.xz
Source7618:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/abnt.doc.tar.xz
Source7619:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/actuarialsymbol.tar.xz
Source7620:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/actuarialsymbol.doc.tar.xz
Source7621:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/addfont.tar.xz
Source7622:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/addfont.doc.tar.xz
Source7623:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/algolrevived.tar.xz
Source7624:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/algolrevived.doc.tar.xz
Source7625:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/alkalami.tar.xz
Source7626:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/alkalami.doc.tar.xz
Source7627:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apalike-german.tar.xz
Source7628:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apalike-german.doc.tar.xz
Source7629:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arimo.tar.xz
Source7630:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arimo.doc.tar.xz
Source8054:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/algobox.tar.xz
Source8055:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/algobox.doc.tar.xz
Source8056:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adigraph.tar.xz
Source8057:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adigraph.doc.tar.xz
Source8058:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aligned-overset.tar.xz
Source8059:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aligned-overset.doc.tar.xz
Source8060:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amscls-doc.tar.xz
Source8061:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amscls-doc.doc.tar.xz
Source8062:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apxproof.tar.xz
Source8063:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/apxproof.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-12many
Provides:       tex-12many = %{tl_version}
License:        LPPL
Summary:        Generalising mathematical index sets
Version:        svn15878.0.3
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(calc.sty), tex(keyval.sty)
Provides:       tex(12many.sty) = %{tl_version}

%description -n texlive-12many
In the discrete branches of mathematics and the computer
sciences, it will only take some seconds before you're faced
with a set like {1,...,m}. Some people write $1\ldotp\ldotp m$,
others $\{j:1\leq j\leq m\}$, and the journal you're submitting
to might want something else entirely. The 12many package
provides an interface that makes changing from one to another a
one-line change.

%package -n texlive-12many-doc
Summary:        Documentation for 12many
Version:        svn15878.0.3
Provides:       tex-12many-doc
AutoReqProv:    No

%description -n texlive-12many-doc
Documentation for 12many

%package -n texlive-2up
Provides:       tex-2up = %{tl_version}
License:        LPPL
Summary:        2up package
Version:        svn41578
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(2up.sty) = %{tl_version}, tex(2up.tex) = %{tl_version}

%description -n texlive-2up
2up package

%package -n texlive-2up-doc
Summary:        Documentation for 2up
Version:        svn41578
Provides:       tex-2up-doc
AutoReqProv:    No

%description -n texlive-2up-doc
Documentation for 2up

%package -n texlive-a0poster
Provides:       tex-a0poster = %{tl_version}
License:        LPPL
Summary:        Support for designing posters on large paper
Version:        svn15878.1.22b
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(a0poster.cls) = %{tl_version}, tex(a0size.sty) = %{tl_version}

%description -n texlive-a0poster
Provides fonts in sizes of 12pt up to 107pt and also makes sure
that in math formulas the symbols appear in the right size. Can
also create a PostScript header file for dvips which ensures
that the poster will be printed in the right size. Supported
sizes are DIN A0, DIN A1, DIN A2 and DIN A3.

%package -n texlive-a0poster-doc
Summary:        Documentation for a0poster
Version:        svn15878.1.22b
Provides:       tex-a0poster-doc
AutoReqProv:    No

%description -n texlive-a0poster-doc
Documentation for a0poster

%package -n texlive-a4wide
Provides:       tex-a4wide = %{tl_version}
License:        LPPL
Summary:        "Wide" a4 layout
Version:        svn20943.0
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(a4.sty)
Provides:       tex(a4wide.sty) = %{tl_version}

%description -n texlive-a4wide
This package increases the width of the typeset area of an a4
page. This sort of operation is capable of producing
typographically poor results; the operation itself is better
provided by the geometry package. The package uses the a4
package.

%package -n texlive-a4wide-doc
Summary:        Documentation for a4wide
Version:        svn20943.0
Provides:       tex-a4wide-doc
AutoReqProv:    No

%description -n texlive-a4wide-doc
Documentation for a4wide

%package -n texlive-a5comb
Provides:       tex-a5comb = %{tl_version}
License:        Public Domain
Summary:        Support for a5 paper sizes
Version:        svn17020.4
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(a5comb.sty) = %{tl_version}

%description -n texlive-a5comb
Superceded by geometry.

%package -n texlive-a5comb-doc
Summary:        Documentation for a5comb
Version:        svn17020.4
Provides:       tex-a5comb-doc
AutoReqProv:    No

%description -n texlive-a5comb-doc
Documentation for a5comb

%package -n texlive-aastex
Provides:       tex-aastex = %{tl_version}
License:        LPPL
Summary:        Macros for Manuscript Preparation for AAS Journals
Version:        svn47692
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(latexsym.sty), tex(graphicx.sty), tex(amssymb.sty), tex(natbib.sty)
Requires:       tex(verbatim.sty)
Provides:       tex(aastex6.cls) = %{tl_version}

%description -n texlive-aastex
The bundle provides a document class for preparing papers for
American Astronomical Society publications. Authors who wish to
submit papers to AAS journals are strongly urged to use this
class in preference to any of the alternatives available.

%package -n texlive-aastex-doc
Summary:        Documentation for aastex
Version:        svn47692
Provides:       tex-aastex-doc
AutoReqProv:    No

%description -n texlive-aastex-doc
Documentation for aastex

%package -n texlive-abbr
Provides:       tex-abbr = %{tl_version}
License:        Public Domain
Summary:        Simple macros supporting abreviations for Plain and LaTeX
Version:        svn15878.0
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(abbr.tex) = %{tl_version}

%description -n texlive-abbr
The package provides some simple macros to support
abbreviations in Plain TeX or LaTeX. It allows writing (e.g.)
\<TEX> instead of \TeX, hence frees users from having to escape
space after parameterless macros.

%package -n texlive-abbr-doc
Summary:        Documentation for abbr
Version:        svn15878.0
Provides:       tex-abbr-doc
AutoReqProv:    No

%description -n texlive-abbr-doc
Documentation for abbr

%package -n texlive-abc
Provides:       tex-abc = %{tl_version}
License:        LPPL 1.2
Summary:        Support ABC music notation in LaTeX
Version:        svn41157
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(verbatim.sty), tex(keyval.sty), tex(graphicx.sty), tex(ifpdf.sty)
Provides:       tex(abc.sty) = %{tl_version}, tex(mup.sty) = %{tl_version}

%description -n texlive-abc
The abc package lets you include lines of music written in the
ABC Plus language. The package will then employ the \write18
facility to convert your notation to PostScript (using the
established utility abcm2ps) and hence to the format needed for
inclusion in your document.

%package -n texlive-abc-doc
Summary:        Documentation for abc
Version:        svn41157
Provides:       tex-abc-doc
AutoReqProv:    No

%description -n texlive-abc-doc
Documentation for abc

%package -n texlive-abntex2
Provides:       tex-abntex2 = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset technical and scientific Brazilian documents based on ABNT rules
Version:        svn39913
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(textcase.sty), tex(hyperref.sty), tex(bookmark.sty)
Requires:       tex(babel.sty), tex(enumitem.sty), tex(calc.sty), tex(setspace.sty)
Requires:       tex(url.sty), tex(ifpdf.sty), tex(ifxetex.sty), tex(breakurl.sty)
Requires:       tex(relsize.sty)
Provides:       tex(abntex2.cls) = %{tl_version}, tex(abntex2abrev.sty) = %{tl_version}
Provides:       tex(abntex2cite.sty) = %{tl_version}

%description -n texlive-abntex2
The bundle provides support for typesetting technical and
scientific Brazilian documents (like academic thesis, articles,
reports, research project and others) based on the ABNT rules
(Associacao Brasileira de Normas Tecnicas). It replaces the old
abntex.

%package -n texlive-abntex2-doc
Summary:        Documentation for abntex2
Version:        svn39913
Provides:       tex-abntex2-doc
AutoReqProv:    No

%description -n texlive-abntex2-doc
Documentation for abntex2

%package -n texlive-abraces
Provides:       tex-abraces = %{tl_version}
License:        LPPL
Summary:        Asymmetric over-/underbraces in maths
Version:        svn27880.2
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(abraces.sty) = %{tl_version}

%description -n texlive-abraces
The package provides a character key-driven interface to
supplement new constructions of the traditional \overbrace and
\underbrace pairs in an asymmetric or arbitrary way.

%package -n texlive-abraces-doc
Summary:        Documentation for abraces
Version:        svn27880.2
Provides:       tex-abraces-doc
AutoReqProv:    No

%description -n texlive-abraces-doc
Documentation for abraces

%package -n texlive-abstract
Provides:       tex-abstract = %{tl_version}
License:        LPPL
Summary:        Control the typesetting of the abstract environment
Version:        svn15878.1.2a
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(abstract.sty) = %{tl_version}

%description -n texlive-abstract
The abstract package gives you control over the typesetting of
the abstract environment, and in particular provides for a one
column abstract in a two column paper.

%package -n texlive-abstract-doc
Summary:        Documentation for abstract
Version:        svn15878.1.2a
Provides:       tex-abstract-doc
AutoReqProv:    No

%description -n texlive-abstract-doc
Documentation for abstract

%package -n texlive-abstyles
Provides:       tex-abstyles = %{tl_version}
License:        Abstyles
Summary:        Adaptable BibTeX styles
Version:        svn15878.0
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(apreambl.tex) = %{tl_version}

%description -n texlive-abstyles
A family of modifications of the standard BibTeX styles whose
behaviour may be changed by changing the user document, without
change to the styles themselves. The package is largely used
nowadays in its adaptation for working with Babel.

%package -n texlive-abstyles-doc
Summary:        Documentation for abstyles
Version:        svn15878.0
Provides:       tex-abstyles-doc
AutoReqProv:    No

%description -n texlive-abstyles-doc
Documentation for abstyles

%package -n texlive-academicons
Provides:       tex-academicons = %{tl_version}
License:        LPPL 1.3
Summary:        Font containing icons of online academic profiles
Version:        svn48100
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(academicons.ttf) = %{tl_version}, tex(academicons.sty) = %{tl_version}

%description -n texlive-academicons
This package provides access in (La)TeX to 20 high quality
icons of online academic profiles included in the free
"Academicons" font. It requires the fontspec package and either
the Xe(La)TeX or the Lua(La)TeX engine to load the included
academicons.ttf font. The "Academicons" font was designed by
James Walsh and released (see
http://jpswalsh.github.io/academicons/) under the SIL Open Font
License. This package is inspired by and based on the
fontawesome package. academicons.sty provides the generic
\aiicon command to access icons, which takes as a mandatory
argument the name of the desired icon. It also provides
individual direct commands for each specific icon. The full
list of icons and their respective names and direct commands
can be found in the manual.

%package -n texlive-academicons-doc
Summary:        Documentation for academicons
Version:        svn48100
Provides:       tex-academicons-doc
AutoReqProv:    No

%description -n texlive-academicons-doc
Documentation for academicons

%package -n texlive-accanthis
Provides:       tex-accanthis = %{tl_version}
License:        GPLv2+
Summary:        Accanthis fonts, with LaTeX support
Version:        svn32089.0
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(ifxetex.sty)
Requires:       tex(ifluatex.sty), tex(textcomp.sty), tex(xkeyval.sty), tex(fontspec.sty)
Requires:       tex(fontenc.sty), tex(fontaxes.sty)
Provides:       tex(acnt_m4gnvn.enc) = %{tl_version}, tex(acnt_qu6a6x.enc) = %{tl_version}
Provides:       tex(acnt_sjpjw4.enc) = %{tl_version}, tex(acnt_z4e4wk.enc) = %{tl_version}
Provides:       tex(accanthis.map) = %{tl_version}, tex(AccanthisADFStdNo3-Bold.otf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic.otf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic.otf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular.otf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold.pfb) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic.pfb) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic.pfb) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-ItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular.pfb) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-RegularLCDFJ.pfb) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-ot1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-ot1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(AccanthisADFStdNo3-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(LY1AccanthisADFStdNoThree-LF.fd) = %{tl_version}
Provides:       tex(OT1AccanthisADFStdNoThree-LF.fd) = %{tl_version}
Provides:       tex(T1AccanthisADFStdNoThree-LF.fd) = %{tl_version}
Provides:       tex(TS1AccanthisADFStdNoThree-LF.fd) = %{tl_version}
Provides:       tex(accanthis.sty) = %{tl_version}

%description -n texlive-accanthis
Accanthis No. 3 is designed by Hirwin Harendal and is suitable
as an alternative to fonts such as Garamond, Galliard, Horley
old style, Sabon, and Bembo. The support files are suitable for
use with all LaTeX engines.

%package -n texlive-accanthis-doc
Summary:        Documentation for accanthis
Version:        svn32089.0
Provides:       tex-accanthis-doc
AutoReqProv:    No

%description -n texlive-accanthis-doc
Documentation for accanthis

%package -n texlive-achemso
Provides:       tex-achemso = %{tl_version}
License:        LPPL 1.3
Summary:        Support for American Chemical Society journal submissions
Version:        svn48203
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(geometry.sty), tex(caption.sty), tex(float.sty)
Requires:       tex(graphicx.sty), tex(setspace.sty), tex(url.sty), tex(natbib.sty)
Requires:       tex(mciteplus.sty)
Provides:       tex(achemso.cls) = %{tl_version}, tex(achemso.sty) = %{tl_version}
Provides:       tex(achemso-aamick.cfg) = %{tl_version}, tex(achemso-acbcct.cfg) = %{tl_version}
Provides:       tex(achemso-accacs.cfg) = %{tl_version}, tex(achemso-achre4.cfg) = %{tl_version}
Provides:       tex(achemso-acncdm.cfg) = %{tl_version}, tex(achemso-acsccc.cfg) = %{tl_version}
Provides:       tex(achemso-acsodf.cfg) = %{tl_version}, tex(achemso-aelccp.cfg) = %{tl_version}
Provides:       tex(achemso-amclct.cfg) = %{tl_version}, tex(achemso-amlccd.cfg) = %{tl_version}
Provides:       tex(achemso-ancac3.cfg) = %{tl_version}, tex(achemso-ancham.cfg) = %{tl_version}
Provides:       tex(achemso-apchd5.cfg) = %{tl_version}, tex(achemso-asbcd6.cfg) = %{tl_version}
Provides:       tex(achemso-asccii.cfg) = %{tl_version}, tex(achemso-ascecg.cfg) = %{tl_version}
Provides:       tex(achemso-bcches.cfg) = %{tl_version}, tex(achemso-bichaw.cfg) = %{tl_version}
Provides:       tex(achemso-bomaf6.cfg) = %{tl_version}, tex(achemso-cgdefu.cfg) = %{tl_version}
Provides:       tex(achemso-chreay.cfg) = %{tl_version}, tex(achemso-cmatex.cfg) = %{tl_version}
Provides:       tex(achemso-crtoec.cfg) = %{tl_version}, tex(achemso-enfuem.cfg) = %{tl_version}
Provides:       tex(achemso-esthag.cfg) = %{tl_version}, tex(achemso-estlcu.cfg) = %{tl_version}
Provides:       tex(achemso-iecred.cfg) = %{tl_version}, tex(achemso-inoraj.cfg) = %{tl_version}
Provides:       tex(achemso-jacsat.cfg) = %{tl_version}, tex(achemso-jafcau.cfg) = %{tl_version}
Provides:       tex(achemso-jceaax.cfg) = %{tl_version}, tex(achemso-jceda8.cfg) = %{tl_version}
Provides:       tex(achemso-jcisd8.cfg) = %{tl_version}, tex(achemso-jctcce.cfg) = %{tl_version}
Provides:       tex(achemso-jmcmar.cfg) = %{tl_version}, tex(achemso-jnprdf.cfg) = %{tl_version}
Provides:       tex(achemso-joceah.cfg) = %{tl_version}, tex(achemso-jpcafh.cfg) = %{tl_version}
Provides:       tex(achemso-jpcbfk.cfg) = %{tl_version}, tex(achemso-jpccck.cfg) = %{tl_version}
Provides:       tex(achemso-jpclcd.cfg) = %{tl_version}, tex(achemso-jprobs.cfg) = %{tl_version}
Provides:       tex(achemso-langd5.cfg) = %{tl_version}, tex(achemso-mamobx.cfg) = %{tl_version}
Provides:       tex(achemso-mpohbp.cfg) = %{tl_version}, tex(achemso-nalefd.cfg) = %{tl_version}
Provides:       tex(achemso-oprdfk.cfg) = %{tl_version}, tex(achemso-orgnd7.cfg) = %{tl_version}
Provides:       tex(achemso-orlef7.cfg) = %{tl_version}, tex(natmove.sty) = %{tl_version}

%description -n texlive-achemso
The bundle provides the official macros (achemso.cls) and
BibTeX styles (achemso.bst and biochem.bst) for submission to
the journals of the American Chemical Society. The natmove
package, which moves citations relative to punctuation, is
distributed as part of the bundle.

%package -n texlive-achemso-doc
Summary:        Documentation for achemso
Version:        svn48203
Provides:       tex-achemso-doc
AutoReqProv:    No

%description -n texlive-achemso-doc
Documentation for achemso

%package -n texlive-acmconf
Provides:       tex-acmconf = %{tl_version}
License:        LPPL
Summary:        Class for ACM conference proceedings
Version:        svn15878.1.3
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(flushend.sty)
Provides:       tex(acmconf.cls) = %{tl_version}

%description -n texlive-acmconf
This class may be used to typeset articles to be published in
the proceedings of ACM (Association for Computing Machinery)
conferences and workshops. The layout produced by the acmconf
class is based on the ACM's own specification.

%package -n texlive-acmconf-doc
Summary:        Documentation for acmconf
Version:        svn15878.1.3
Provides:       tex-acmconf-doc
AutoReqProv:    No

%description -n texlive-acmconf-doc
Documentation for acmconf

%package -n texlive-acronym
Provides:       tex-acronym = %{tl_version}
License:        LPPL 1.3
Summary:        Expand acronyms at least once
Version:        svn36582.1.41
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(suffix.sty), tex(xstring.sty), tex(relsize.sty)
Provides:       tex(acronym.sty) = %{tl_version}

%description -n texlive-acronym
This package ensures that all acronyms used in the text are
spelled out in full at least once. It also provides an
environment to build a list of acronyms used. The package is
compatible with pdf bookmarks. The package requires the suffix
package, which in turn requires that it runs under e-TeX.

%package -n texlive-acronym-doc
Summary:        Documentation for acronym
Version:        svn36582.1.41
Provides:       tex-acronym-doc
AutoReqProv:    No

%description -n texlive-acronym-doc
Documentation for acronym

%package -n texlive-acroterm
Provides:       tex-acroterm = %{tl_version}
License:        LPPL 1.3
Summary:        Manage and index acronyms and terms
Version:        svn20498.0.1
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(splitidx.sty), tex(xifthen.sty)
Provides:       tex(acroterm.sty) = %{tl_version}

%description -n texlive-acroterm
Yet another package for acronyms: the package offers simple
markup of acronyms and technical terms in the text, giving an
index each of terms and acronyms with their expanded form.

%package -n texlive-acroterm-doc
Summary:        Documentation for acroterm
Version:        svn20498.0.1
Provides:       tex-acroterm-doc
AutoReqProv:    No

%description -n texlive-acroterm-doc
Documentation for acroterm

%package -n texlive-acro
Provides:       tex-acro = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset acronyms
Version:        svn46492
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(l3sort.sty), tex(xparse.sty), tex(l3keys2e.sty)
Requires:       tex(xtemplate.sty), tex(etoolbox.sty), tex(xspace.sty), tex(zref-abspage.sty)
Requires:       tex(accsupp.sty), tex(pdfcomment.sty), tex(translations.sty)
Provides:       tex(acro.sty) = %{tl_version}

%description -n texlive-acro
The package enables the author to create acronyms in a simple
way, and provides means to add them to different 'classes' of
acronyms. Lists can be created of separate acronym classes. The
package option 'single' instructs the package to ignore
acronyms that are used only once in the whole document. As an
experimental feature the package also offers the option 'sort'
which automatically sorts the list created by \printacronyms.

%package -n texlive-acro-doc
Summary:        Documentation for acro
Version:        svn46492
Provides:       tex-acro-doc
AutoReqProv:    No

%description -n texlive-acro-doc
Documentation for acro

%package -n texlive-active-conf
Provides:       tex-active-conf = %{tl_version}
License:        LPPL
Summary:        Class for typesetting ACTIVE conference papers
Version:        svn15878.0.3a
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(helvet.sty), tex(fontenc.sty), tex(textcomp.sty), tex(calc.sty)
Requires:       tex(ifthen.sty), tex(url.sty), tex(geometry.sty), tex(amsmath.sty)
Requires:       tex(amssymb.sty), tex(array.sty), tex(bm.sty), tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Provides:       tex(active-conf.cls) = %{tl_version}

%description -n texlive-active-conf
Active-conf is a class for typesetting papers for the Active
conference on noise and vibration control. It is initially
intended for the 2006 conference in Adelaide, Australia. The
class is based on article with more flexible front-matter, and
can be customised for conferences in future years with a header
file.

%package -n texlive-active-conf-doc
Summary:        Documentation for active-conf
Version:        svn15878.0.3a
Provides:       tex-active-conf-doc
AutoReqProv:    No

%description -n texlive-active-conf-doc
Documentation for active-conf

%package -n texlive-actuarialangle
Provides:       tex-actuarialangle = %{tl_version}
License:        Public Domain
Summary:        Symbol for use in "present value" statements of an annuity
Version:        svn43751
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(actuarialangle.sty) = %{tl_version}

%description -n texlive-actuarialangle
The package defines a single command \actuarialangle to typeset
"angles" in the 'present value of an annuity' symbols common in
actuarial and financial notation.

%package -n texlive-actuarialangle-doc
Summary:        Documentation for actuarialangle
Version:        svn43751
Provides:       tex-actuarialangle-doc
AutoReqProv:    No

%description -n texlive-actuarialangle-doc
Documentation for actuarialangle

%package -n texlive-addlines
Provides:       tex-addlines = %{tl_version}
License:        LPPL
Summary:        A user-friendly wrapper around \enlargethispage
Version:        svn37805.0.2a
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(afterpage.sty), tex(changepage.sty)
Provides:       tex(addlines.sty) = %{tl_version}

%description -n texlive-addlines
This small package provides the command \addlines for adding or
removing space in the textblock of the page it's used on. E.g.,
adding an extra line of text to the page so that a section fits
better on the next page. It will also add space to the facing
page in a two-sided document.

%package -n texlive-addlines-doc
Summary:        Documentation for addlines
Version:        svn37805.0.2a
Provides:       tex-addlines-doc
AutoReqProv:    No

%description -n texlive-addlines-doc
Documentation for addlines

%package -n texlive-adfathesis
Provides:       tex-adfathesis = %{tl_version}
License:        Public Domain
Summary:        Australian Defence Force Academy thesis format
Version:        svn26048.2.42
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(harvard.sty)
Provides:       tex(adfathesis.cls) = %{tl_version}

%description -n texlive-adfathesis
The bundle includes a BibTeX style file.

%package -n texlive-adfathesis-doc
Summary:        Documentation for adfathesis
Version:        svn26048.2.42
Provides:       tex-adfathesis-doc
AutoReqProv:    No

%description -n texlive-adfathesis-doc
Documentation for adfathesis

%package -n texlive-adforn
Provides:       tex-adforn = %{tl_version}
License:        LPPL
Summary:        OrnementsADF font with TeX/LaTeX support
Version:        svn20019.1.001_b_2
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(pifont.sty)
Provides:       tex(OrnementsADF.enc) = %{tl_version}, tex(OrnementsADF.map) = %{tl_version}
Provides:       tex(OrnementsADF.tfm) = %{tl_version}, tex(OrnementsADF.pfb) = %{tl_version}
Provides:       tex(adforn.sty) = %{tl_version}, tex(uornementsadf.fd) = %{tl_version}

%description -n texlive-adforn
The bundle provides the Ornements ADF font in PostScript type 1
format with TeX/LaTeX support files. The font is licensed under
GPL v2 or later with font exception. (See NOTICE, COPYING,
README.) The TeX/LaTeX support is licensed under LPPL. (See
README, manifest.txt.)

%package -n texlive-adforn-doc
Summary:        Documentation for adforn
Version:        svn20019.1.001_b_2
Provides:       tex-adforn-doc
AutoReqProv:    No

%description -n texlive-adforn-doc
Documentation for adforn

%package -n texlive-adfsymbols
Provides:       tex-adfsymbols = %{tl_version}
License:        LPPL
Summary:        SymbolsADF with TeX/LaTeX support
Version:        svn19766.1.001
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(pifont.sty)
Requires:       tex(fp.sty)
Provides:       tex(SymbolsADF.enc) = %{tl_version}, tex(ArrowsADF.map) = %{tl_version}
Provides:       tex(BulletsADF.map) = %{tl_version}, tex(ArrowsADF.tfm) = %{tl_version}
Provides:       tex(BulletsADF.tfm) = %{tl_version}, tex(ArrowsADF.pfb) = %{tl_version}
Provides:       tex(BulletsADF.pfb) = %{tl_version}, tex(adfarrows.sty) = %{tl_version}
Provides:       tex(adfbullets.sty) = %{tl_version}, tex(uarrowsadf.fd) = %{tl_version}
Provides:       tex(ubulletsadf.fd) = %{tl_version}

%description -n texlive-adfsymbols
The package provides Arkandis foundry's ArrowsADF and
BulletsADF fonts in Adobe Type 1 format, together with
TeX/LaTeX support files. The fonts are licensed under GPL v2 or
later with font exception. (See NOTICE, COPYING, README.) The
TeX/LaTeX support is licensed under LPPL. (See README,
manifest.txt.)

%package -n texlive-adfsymbols-doc
Summary:        Documentation for adfsymbols
Version:        svn19766.1.001
Provides:       tex-adfsymbols-doc
AutoReqProv:    No

%description -n texlive-adfsymbols-doc
Documentation for adfsymbols

%package -n texlive-adjmulticol
Provides:       tex-adjmulticol = %{tl_version}
License:        LPPL 1.3
Summary:        Adjusting margins for multicolumn and single column output
Version:        svn28936.1.1
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(multicol.sty)
Provides:       tex(adjmulticol.sty) = %{tl_version}

%description -n texlive-adjmulticol
The package adds, to the multicol package, the option to change
the margins for multicolumn and unicolumn layout. The package
understands the difference between the even and odd margins for
two side printing.

%package -n texlive-adjmulticol-doc
Summary:        Documentation for adjmulticol
Version:        svn28936.1.1
Provides:       tex-adjmulticol-doc
AutoReqProv:    No

%description -n texlive-adjmulticol-doc
Documentation for adjmulticol

%package -n texlive-adjustbox
Provides:       tex-adjustbox = %{tl_version}
License:        LPPL 1.3
Summary:        Graphics package-alike macros for "general" boxes
Version:        svn47405
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(calc.sty), tex(pgf.sty), tex(graphicx.sty)
Requires:       tex(collectbox.sty), tex(ifoddpage.sty), tex(varwidth.sty)
Provides:       tex(adjcalc.sty) = %{tl_version}, tex(adjustbox.sty) = %{tl_version}
Provides:       tex(tc-dvips.def) = %{tl_version}, tex(tc-pdftex.def) = %{tl_version}
Provides:       tex(tc-pgf.def) = %{tl_version}, tex(tc-xetex.def) = %{tl_version}
Provides:       tex(trimclip.sty) = %{tl_version}

%description -n texlive-adjustbox
The package provides several macros to adjust boxed content.
One purpose is to supplement the standard graphics package,
which defines the macros \resizebox, \scalebox and \rotatebox ,
with the macros\trimbox and \clipbox. The main feature is the
general \adjustbox macro which extends the "key=value"
interface of \includegraphics from the graphics package and
applies it to general text content. Additional provided box
macros are \lapbox, \marginbox, \minsizebox, \maxsizebox and
\phantombox. All macros use the collectbox package to read the
content as a box and not as a macro argument. This allows for
all forms of content including special material like verbatim
content. A special feature of collectbox is used to provide
matching environments with the identical names as the macros.

%package -n texlive-adjustbox-doc
Summary:        Documentation for adjustbox
Version:        svn47405
Provides:       tex-adjustbox-doc
AutoReqProv:    No

%description -n texlive-adjustbox-doc
Documentation for adjustbox

%package -n texlive-adobemapping
Provides:       tex-adobemapping = %{tl_version}
License:        BSD
Summary:        Adobe cmap and pdfmapping files
Version:        svn45645
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-adobemapping
The package comprises the collection of CMap and PDF mapping
files now made available for distribution by Adobe systems
incorporated.

%package -n texlive-adrconv
Provides:       tex-adrconv = %{tl_version}
License:        LPPL
Summary:        BibTeX styles to implement an address database
Version:        svn46817
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(adrdir.cfg) = %{tl_version}, tex(adrplaner.cfg) = %{tl_version}
Provides:       tex(adrsmall.cfg) = %{tl_version}

%description -n texlive-adrconv
The bundle provides a collection of BibTeX style files to turn
an address database stored in the .bib format into files
suitable for printing as address books or included into letter
classes like akletter or scrletter2. The data may be sorted
either by name or birthday and output provides files in various
formats for address books or time planners.

%package -n texlive-adrconv-doc
Summary:        Documentation for adrconv
Version:        svn46817
Provides:       tex-adrconv-doc
AutoReqProv:    No

%description -n texlive-adrconv-doc
Documentation for adrconv

%package -n texlive-advdate
Provides:       tex-advdate = %{tl_version}
License:        LPPL 1.3
Summary:        Print a date relative to "today"
Version:        svn20538.0
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(advdate.sty) = %{tl_version}

%description -n texlive-advdate
Provides macros which can add a specified number of days to the
current date (as specified in \today), to save, set and restore
the 'current date' and to print it. Intended use is, for
example, in invoices "payable within 14 days from today", etc.
The package has only been tested with Czech dates.

%package -n texlive-advdate-doc
Summary:        Documentation for advdate
Version:        svn20538.0
Provides:       tex-advdate-doc
AutoReqProv:    No

%description -n texlive-advdate-doc
Documentation for advdate

%package -n texlive-aecc
Provides:       tex-aecc = %{tl_version}
License:        LPPL
Summary:        Almost European Concrete Roman virtual fonts
Version:        svn28574.1.0
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fontenc.sty)
Provides:       tex(aeccr10.tfm) = %{tl_version}, tex(aeccr5.tfm) = %{tl_version}
Provides:       tex(aeccr6.tfm) = %{tl_version}, tex(aeccr7.tfm) = %{tl_version}
Provides:       tex(aeccr8.tfm) = %{tl_version}, tex(aeccr9.tfm) = %{tl_version}
Provides:       tex(aeccsc10.tfm) = %{tl_version}, tex(aeccsl10.tfm) = %{tl_version}
Provides:       tex(aeccsl9.tfm) = %{tl_version}, tex(aeccti10.tfm) = %{tl_version}
Provides:       tex(aeccr10.vf) = %{tl_version}, tex(aeccr5.vf) = %{tl_version}
Provides:       tex(aeccr6.vf) = %{tl_version}, tex(aeccr7.vf) = %{tl_version}
Provides:       tex(aeccr8.vf) = %{tl_version}, tex(aeccr9.vf) = %{tl_version}
Provides:       tex(aeccsc10.vf) = %{tl_version}, tex(aeccsl10.vf) = %{tl_version}
Provides:       tex(aeccsl9.vf) = %{tl_version}, tex(aeccti10.vf) = %{tl_version}
Provides:       tex(aecc.sty) = %{tl_version}, tex(t1aeccr.fd) = %{tl_version}

%description -n texlive-aecc
The package provides a set of virtual fonts (built from the
standard Concrete fonts) providing a set of fonts that almost
cover the T1 encoding. The main characters missing, of those
specified in the T1 specification are eth, thorn, and the Sami
letter eng. Sometimes the PS (pound sterling) character is also
missing. For the typewriter fonts, the situation is worse.

%package -n texlive-aecc-doc
Summary:        Documentation for aecc
Version:        svn28574.1.0
Provides:       tex-aecc-doc
AutoReqProv:    No

%description -n texlive-aecc-doc
Documentation for aecc

%package -n texlive-aeguill
Provides:       tex-aeguill = %{tl_version}
License:        LPPL
Summary:        Add several kinds of guillemets to the ae fonts
Version:        svn15878.0
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ae.sty), tex(latexsym.sty), tex(fontenc.sty)
Provides:       tex(aeguill.sty) = %{tl_version}

%description -n texlive-aeguill
The package enables the user to add guillemets from several
source (Polish cmr, Cyrillic cmr, lasy and ec) to the ae fonts.
This was useful when the ae fonts were used to produce PDF
files, since the additional guillemets exist in fonts available
in Adobe Type 1 format.

%package -n texlive-aeguill-doc
Summary:        Documentation for aeguill
Version:        svn15878.0
Provides:       tex-aeguill-doc
AutoReqProv:    No

%description -n texlive-aeguill-doc
Documentation for aeguill

%package -n texlive-ae
Provides:       tex-ae = %{tl_version}
License:        LPPL
Summary:        Virtual fonts for T1 encoded CMR-fonts
Version:        svn15878.1.4
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fontenc.sty)
Provides:       tex(aeb10.tfm) = %{tl_version}, tex(aebx10.tfm) = %{tl_version}
Provides:       tex(aebx12.tfm) = %{tl_version}, tex(aebx5.tfm) = %{tl_version}
Provides:       tex(aebx6.tfm) = %{tl_version}, tex(aebx7.tfm) = %{tl_version}
Provides:       tex(aebx8.tfm) = %{tl_version}, tex(aebx9.tfm) = %{tl_version}
Provides:       tex(aebxsl10.tfm) = %{tl_version}, tex(aebxti10.tfm) = %{tl_version}
Provides:       tex(aecsc10.tfm) = %{tl_version}, tex(aeitt10.tfm) = %{tl_version}
Provides:       tex(aer10.tfm) = %{tl_version}, tex(aer12.tfm) = %{tl_version}
Provides:       tex(aer17.tfm) = %{tl_version}, tex(aer5.tfm) = %{tl_version}
Provides:       tex(aer6.tfm) = %{tl_version}, tex(aer7.tfm) = %{tl_version}
Provides:       tex(aer8.tfm) = %{tl_version}, tex(aer9.tfm) = %{tl_version}
Provides:       tex(aesl10.tfm) = %{tl_version}, tex(aesl12.tfm) = %{tl_version}
Provides:       tex(aesl8.tfm) = %{tl_version}, tex(aesl9.tfm) = %{tl_version}
Provides:       tex(aesltt10.tfm) = %{tl_version}, tex(aess10.tfm) = %{tl_version}
Provides:       tex(aess12.tfm) = %{tl_version}, tex(aess17.tfm) = %{tl_version}
Provides:       tex(aess8.tfm) = %{tl_version}, tex(aess9.tfm) = %{tl_version}
Provides:       tex(aessbx10.tfm) = %{tl_version}, tex(aessdc10.tfm) = %{tl_version}
Provides:       tex(aessi10.tfm) = %{tl_version}, tex(aessi12.tfm) = %{tl_version}
Provides:       tex(aessi17.tfm) = %{tl_version}, tex(aessi8.tfm) = %{tl_version}
Provides:       tex(aessi9.tfm) = %{tl_version}, tex(aetcsc10.tfm) = %{tl_version}
Provides:       tex(aeti10.tfm) = %{tl_version}, tex(aeti12.tfm) = %{tl_version}
Provides:       tex(aeti7.tfm) = %{tl_version}, tex(aeti8.tfm) = %{tl_version}
Provides:       tex(aeti9.tfm) = %{tl_version}, tex(aett10.tfm) = %{tl_version}
Provides:       tex(aett12.tfm) = %{tl_version}, tex(aett8.tfm) = %{tl_version}
Provides:       tex(aett9.tfm) = %{tl_version}, tex(laess8.tfm) = %{tl_version}
Provides:       tex(laessb8.tfm) = %{tl_version}, tex(laessi8.tfm) = %{tl_version}
Provides:       tex(aeb10.vf) = %{tl_version}, tex(aebx10.vf) = %{tl_version}
Provides:       tex(aebx12.vf) = %{tl_version}, tex(aebx5.vf) = %{tl_version}
Provides:       tex(aebx6.vf) = %{tl_version}, tex(aebx7.vf) = %{tl_version}
Provides:       tex(aebx8.vf) = %{tl_version}, tex(aebx9.vf) = %{tl_version}
Provides:       tex(aebxsl10.vf) = %{tl_version}, tex(aebxti10.vf) = %{tl_version}
Provides:       tex(aecsc10.vf) = %{tl_version}, tex(aeitt10.vf) = %{tl_version}
Provides:       tex(aer10.vf) = %{tl_version}, tex(aer12.vf) = %{tl_version}
Provides:       tex(aer17.vf) = %{tl_version}, tex(aer5.vf) = %{tl_version}
Provides:       tex(aer6.vf) = %{tl_version}, tex(aer7.vf) = %{tl_version}
Provides:       tex(aer8.vf) = %{tl_version}, tex(aer9.vf) = %{tl_version}
Provides:       tex(aesl10.vf) = %{tl_version}, tex(aesl12.vf) = %{tl_version}
Provides:       tex(aesl8.vf) = %{tl_version}, tex(aesl9.vf) = %{tl_version}
Provides:       tex(aesltt10.vf) = %{tl_version}, tex(aess10.vf) = %{tl_version}
Provides:       tex(aess12.vf) = %{tl_version}, tex(aess17.vf) = %{tl_version}
Provides:       tex(aess8.vf) = %{tl_version}, tex(aess9.vf) = %{tl_version}
Provides:       tex(aessbx10.vf) = %{tl_version}, tex(aessdc10.vf) = %{tl_version}
Provides:       tex(aessi10.vf) = %{tl_version}, tex(aessi12.vf) = %{tl_version}
Provides:       tex(aessi17.vf) = %{tl_version}, tex(aessi8.vf) = %{tl_version}
Provides:       tex(aessi9.vf) = %{tl_version}, tex(aetcsc10.vf) = %{tl_version}
Provides:       tex(aeti10.vf) = %{tl_version}, tex(aeti12.vf) = %{tl_version}
Provides:       tex(aeti7.vf) = %{tl_version}, tex(aeti8.vf) = %{tl_version}
Provides:       tex(aeti9.vf) = %{tl_version}, tex(aett10.vf) = %{tl_version}
Provides:       tex(aett12.vf) = %{tl_version}, tex(aett8.vf) = %{tl_version}
Provides:       tex(aett9.vf) = %{tl_version}, tex(laess8.vf) = %{tl_version}
Provides:       tex(laessb8.vf) = %{tl_version}, tex(laessi8.vf) = %{tl_version}
Provides:       tex(ae.sty) = %{tl_version}, tex(aecompl.sty) = %{tl_version}
Provides:       tex(omlaer.fd) = %{tl_version}, tex(omsaer.fd) = %{tl_version}
Provides:       tex(ot1aer.fd) = %{tl_version}, tex(ot1aess.fd) = %{tl_version}
Provides:       tex(ot1aett.fd) = %{tl_version}, tex(ot1laess.fd) = %{tl_version}
Provides:       tex(ot1laett.fd) = %{tl_version}, tex(t1aer.fd) = %{tl_version}
Provides:       tex(t1aess.fd) = %{tl_version}, tex(t1aett.fd) = %{tl_version}
Provides:       tex(t1laess.fd) = %{tl_version}, tex(t1laett.fd) = %{tl_version}

%description -n texlive-ae
A set of virtual fonts which emulates T1 coded fonts using the
standard CM fonts. The package name, AE fonts, supposedly
stands for "Almost European". The main use of the package was
to produce PDF files using Adobe Type 1 versions of the CM
fonts instead of bitmapped EC fonts. Note that direct
substitutes for the bitmapped EC fonts are now available, via
the CM-super, Latin Modern and (in a restricted way) CM-LGC
font sets.

%package -n texlive-ae-doc
Summary:        Documentation for ae
Version:        svn15878.1.4
Provides:       tex-ae-doc
AutoReqProv:    No

%description -n texlive-ae-doc
Documentation for ae

%package -n texlive-afparticle
Provides:       tex-afparticle = %{tl_version}
License:        LPPL 1.3
Summary:        Typesetting articles for Archives of Forensic Psychology
Version:        svn35900.1.3
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(lastpage.sty), tex(fancyhdr.sty), tex(caption.sty)
Requires:       tex(booktabs.sty), tex(graphicx.sty), tex(hyperref.sty), tex(apacite.sty)
Provides:       tex(afparticle.cls) = %{tl_version}

%description -n texlive-afparticle
This package provides a class for typesetting articles for the
open access journal Archives of Forensic Psychology.

%package -n texlive-afparticle-doc
Summary:        Documentation for afparticle
Version:        svn35900.1.3
Provides:       tex-afparticle-doc
AutoReqProv:    No

%description -n texlive-afparticle-doc
Documentation for afparticle

%package -n texlive-afthesis
Provides:       tex-afthesis = %{tl_version}
License:        Public Domain
Summary:        Air Force Institute of Technology thesis class
Version:        svn15878.2.7
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(caption2.sty), tex(ulem.sty)
Provides:       tex(afthes10.sty) = %{tl_version}, tex(afthes11.sty) = %{tl_version}
Provides:       tex(afthes12.sty) = %{tl_version}, tex(afthesis.cls) = %{tl_version}
Provides:       tex(afthesis.sty) = %{tl_version}

%description -n texlive-afthesis
LaTeX thesis/dissertation class for US Air Force Institute Of
Technology.

%package -n texlive-afthesis-doc
Summary:        Documentation for afthesis
Version:        svn15878.2.7
Provides:       tex-afthesis-doc
AutoReqProv:    No

%description -n texlive-afthesis-doc
Documentation for afthesis

%package -n texlive-aguplus
Provides:       tex-aguplus = %{tl_version}
License:        LPPL
Summary:        Styles for American Geophysical Union
Version:        svn17156.1.6b
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(aguplus.cls) = %{tl_version}, tex(aguplus.sty) = %{tl_version}
Provides:       tex(agupp.sty) = %{tl_version}

%description -n texlive-aguplus
This bundle started as an extension to the AGU's own published
styles, providing extra facilities and improved usability. The
AGU now publishes satisfactory LaTeX materials of its own; the
author of aguplus recommends that users switch to using the
official distribution.

%package -n texlive-aguplus-doc
Summary:        Documentation for aguplus
Version:        svn17156.1.6b
Provides:       tex-aguplus-doc
AutoReqProv:    No

%description -n texlive-aguplus-doc
Documentation for aguplus

%package -n texlive-aiaa
Provides:       tex-aiaa = %{tl_version}
License:        LPPL
Summary:        Typeset AIAA conference papers
Version:        svn15878.3.6
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(geometry.sty), tex(graphicx.sty), tex(array.sty), tex(overcite.sty)
Requires:       tex(lastpage.sty), tex(fancyhdr.sty), tex(setspace.sty), tex(ifthen.sty)
Provides:       tex(aiaa-tc.cls) = %{tl_version}

%description -n texlive-aiaa
A bundle of LaTeX/BibTeX files and sample documents to aid
those producing papers and journal articles according to the
guidelines of the American Institute of Aeronautics and
Astronautics (AIAA).

%package -n texlive-aiaa-doc
Summary:        Documentation for aiaa
Version:        svn15878.3.6
Provides:       tex-aiaa-doc
AutoReqProv:    No

%description -n texlive-aiaa-doc
Documentation for aiaa

%package -n texlive-aichej
Provides:       tex-aichej = %{tl_version}
License:        LPPL
Summary:        Bibliography style file for the AIChE Journal
Version:        svn15878.0
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-aichej
The style was generated using custom-bib, and implements the
style of the American Institute of Chemical Engineers Journal
(or AIChE Journal or AIChE J or AIChEJ).

%package -n texlive-ajl
Provides:       tex-ajl = %{tl_version}
License:        LPPL
Summary:        BibTeX style for AJL
Version:        svn34016.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-ajl
Bibliographic style references in style of Australian Journal
of Linguistics.

%package -n texlive-akktex
Provides:       tex-akktex = %{tl_version}
License:        LPPL
Summary:        A collection of packages and classes
Version:        svn26055.0.3.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(amsmath.sty), tex(amssymb.sty), tex(latexsym.sty)
Requires:       tex(inputenc.sty), tex(fontenc.sty), tex(babel.sty), tex(xspace.sty)
Requires:       tex(fancyhdr.sty), tex(amstext.sty), tex(akkmathset.sty), tex(akkmathrel.sty)
Requires:       tex(akkmathfun.sty), tex(akkmathdisc.sty)
Requires:       tex(array.sty), tex(theorem.sty), tex(lscape.sty), tex(longtable.sty)
Requires:       tex(float.sty), tex(enumerate.sty), tex(verbatim.sty), tex(calc.sty)
Provides:       tex(akkconditional.sty) = %{tl_version}, tex(akkcounterlabelpattern.sty) = %{tl_version}
Provides:       tex(akkcs.sty) = %{tl_version}, tex(akkdoc.sty) = %{tl_version}
Provides:       tex(akkgerman.sty) = %{tl_version}, tex(akkgermanabbreviations.sty) = %{tl_version}
Provides:       tex(akklecture.cls) = %{tl_version}, tex(akklongpage.sty) = %{tl_version}
Provides:       tex(akkmath.sty) = %{tl_version}, tex(akkmathbasic.sty) = %{tl_version}
Provides:       tex(akkmathdisc.sty) = %{tl_version}, tex(akkmathfun.sty) = %{tl_version}
Provides:       tex(akkmathnum.sty) = %{tl_version}, tex(akkmathpaper.sty) = %{tl_version}
Provides:       tex(akkmathproof.sty) = %{tl_version}, tex(akkmathrel.sty) = %{tl_version}
Provides:       tex(akkmathset.sty) = %{tl_version}, tex(akkmathtext.sty) = %{tl_version}
Provides:       tex(akknum.sty) = %{tl_version}, tex(akkparskip.sty) = %{tl_version}
Provides:       tex(akkscript.cls) = %{tl_version}, tex(akksection.sty) = %{tl_version}
Provides:       tex(akkstring.sty) = %{tl_version}, tex(akktecdoc.cls) = %{tl_version}
Provides:       tex(akktex.sty) = %{tl_version}, tex(akkwidepage.sty) = %{tl_version}

%description -n texlive-akktex
The bundle provides: new document classes for technical
documents, thesis works, manuscripts and lecture notes; many
mathematical packages providing a large number of macros for
mathematical texts; layout providing a non-empty parskip with
extended length corrections and new section definition
commands; easy label creation for counters; and german language
tools and predefined abbreviations.

%package -n texlive-akktex-doc
Summary:        Documentation for akktex
Version:        svn26055.0.3.2

Provides:       tex-akktex-doc
AutoReqProv:    No

%description -n texlive-akktex-doc
Documentation for akktex

%package -n texlive-akletter
Provides:       tex-akletter = %{tl_version}
License:        LPPL
Summary:        Comprehensive letter support
Version:        svn15878.1.5i

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(akfax.cfg) = %{tl_version}, tex(akletter.cfg) = %{tl_version}
Provides:       tex(akletter.cls) = %{tl_version}, tex(myletter.cls) = %{tl_version}

%description -n texlive-akletter
An advanced letter document class which extends LaTeX's usual
letter class, providing support for building your own
letterhead and marking fold points for window envelopes.
Options supported by the package include: letterpaper for US
letter; a4offset for a modified A4 layout suitable for platic
binders that cover a part of the left margin. The class's
handling of dates has inspired an extended version of date-
handling in the isodate package. The class supersedes an
earlier class called myletter.

%package -n texlive-akletter-doc
Summary:        Documentation for akletter
Version:        svn15878.1.5i

Provides:       tex-akletter-doc
AutoReqProv:    No

%description -n texlive-akletter-doc
Documentation for akletter

%package -n texlive-alegreya
Provides:       tex-alegreya = %{tl_version}
License:        OFL
Summary:        Alegreya fonts with LaTeX support
Version:        svn48339
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(ifxetex.sty)
Requires:       tex(ifluatex.sty), tex(textcomp.sty), tex(xkeyval.sty), tex(fontspec.sty)
Requires:       tex(fontenc.sty), tex(fontaxes.sty), tex(mweights.sty)
Provides:       tex(algr_2thg7t.enc) = %{tl_version}, tex(algr_6gze5d.enc) = %{tl_version}
Provides:       tex(algr_72lo2s.enc) = %{tl_version}, tex(algr_74q4jo.enc) = %{tl_version}
Provides:       tex(algr_7levdp.enc) = %{tl_version}, tex(algr_7nunim.enc) = %{tl_version}
Provides:       tex(algr_7p2ivs.enc) = %{tl_version}, tex(algr_atppps.enc) = %{tl_version}
Provides:       tex(algr_b55zld.enc) = %{tl_version}, tex(algr_bft2rj.enc) = %{tl_version}
Provides:       tex(algr_hghq3b.enc) = %{tl_version}, tex(algr_k3afeh.enc) = %{tl_version}
Provides:       tex(algr_kf7dx2.enc) = %{tl_version}, tex(algr_lm7t5h.enc) = %{tl_version}
Provides:       tex(algr_mcmfge.enc) = %{tl_version}, tex(algr_n534zq.enc) = %{tl_version}
Provides:       tex(algr_nlrspr.enc) = %{tl_version}, tex(algr_prieif.enc) = %{tl_version}
Provides:       tex(algr_qj6qbd.enc) = %{tl_version}, tex(algr_ry4sz3.enc) = %{tl_version}
Provides:       tex(algr_sd6sdy.enc) = %{tl_version}, tex(algr_sutw7e.enc) = %{tl_version}
Provides:       tex(algr_tlfd2e.enc) = %{tl_version}, tex(algr_u55vgl.enc) = %{tl_version}
Provides:       tex(algr_w6adhq.enc) = %{tl_version}, tex(algr_w7rh4a.enc) = %{tl_version}
Provides:       tex(algr_wtbjoa.enc) = %{tl_version}, tex(algr_x6hfhz.enc) = %{tl_version}
Provides:       tex(algr_y5vbsk.enc) = %{tl_version}, tex(algrs_23dk3b.enc) = %{tl_version}
Provides:       tex(algrs_2f3oru.enc) = %{tl_version}, tex(algrs_4zyalv.enc) = %{tl_version}
Provides:       tex(algrs_6tng7i.enc) = %{tl_version}, tex(algrs_777naj.enc) = %{tl_version}
Provides:       tex(algrs_df6qxs.enc) = %{tl_version}, tex(algrs_eeys5m.enc) = %{tl_version}
Provides:       tex(algrs_eoa4mh.enc) = %{tl_version}, tex(algrs_fakese.enc) = %{tl_version}
Provides:       tex(algrs_ffgp2h.enc) = %{tl_version}, tex(algrs_g333yf.enc) = %{tl_version}
Provides:       tex(algrs_i3slmw.enc) = %{tl_version}, tex(algrs_jcxsi2.enc) = %{tl_version}
Provides:       tex(algrs_lfuhub.enc) = %{tl_version}, tex(algrs_lwpqvr.enc) = %{tl_version}
Provides:       tex(algrs_mcmfge.enc) = %{tl_version}, tex(algrs_n6pera.enc) = %{tl_version}
Provides:       tex(algrs_rus6f4.enc) = %{tl_version}, tex(algrs_tcirz5.enc) = %{tl_version}
Provides:       tex(algrs_tlfd2e.enc) = %{tl_version}, tex(algrs_ucdyzh.enc) = %{tl_version}
Provides:       tex(algrs_upluqc.enc) = %{tl_version}, tex(algrs_xdzbhe.enc) = %{tl_version}
Provides:       tex(algrs_xiqcjc.enc) = %{tl_version}, tex(Alegreya.map) = %{tl_version}
Provides:       tex(Alegreya-Black-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-inf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-osf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-sup-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Alegreya-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Black-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Black-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Black-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Black-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Black-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Black-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Black-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BlackItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BlackItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BlackItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BlackItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BlackItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BlackItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BlackItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSC-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Alegreya-Black.ttf) = %{tl_version}, tex(Alegreya-BlackItalic.ttf) = %{tl_version}
Provides:       tex(Alegreya-Bold.ttf) = %{tl_version}, tex(Alegreya-BoldItalic.ttf) = %{tl_version}
Provides:       tex(Alegreya-Italic.ttf) = %{tl_version}
Provides:       tex(Alegreya-Regular.ttf) = %{tl_version}
Provides:       tex(AlegreyaSC-Black.ttf) = %{tl_version}
Provides:       tex(AlegreyaSC-BlackItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSC-Bold.ttf) = %{tl_version}
Provides:       tex(AlegreyaSC-BoldItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSC-Italic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSC-Regular.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-RegularItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin.ttf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-RegularItalic.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin.ttf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic.ttf) = %{tl_version}
Provides:       tex(Alegreya-Black.pfb) = %{tl_version}, tex(Alegreya-BlackItalic.pfb) = %{tl_version}
Provides:       tex(Alegreya-Bold.pfb) = %{tl_version}, tex(Alegreya-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Alegreya-Italic.pfb) = %{tl_version}
Provides:       tex(Alegreya-Regular.pfb) = %{tl_version}
Provides:       tex(AlegreyaSC-Black.pfb) = %{tl_version}
Provides:       tex(AlegreyaSC-BlackItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSC-Bold.pfb) = %{tl_version}
Provides:       tex(AlegreyaSC-BoldItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSC-Italic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSC-Regular.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-Black.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-Light.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin.pfb) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin.pfb) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic.pfb) = %{tl_version}
Provides:       tex(Alegreya-Black-inf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-inf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-osf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-osf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-osf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-sup-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-sup-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-tlf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-tosf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Black-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-BlackItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-inf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(Alegreya-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-Black-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-Black-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-Black-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-BlackItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-BlackItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-BlackItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSC-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Black-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BlackItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ExtraBoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Light-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-LightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Medium-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-MediumItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-Thin-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSans-ThinItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Black-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BlackItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ExtraBoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Light-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-LightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Medium-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-MediumItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-Thin-tosf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-osf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(AlegreyaSansSC-ThinItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Alegreya.sty) = %{tl_version}, tex(AlegreyaSans.sty) = %{tl_version}
Provides:       tex(LY1Alegreya-Inf.fd) = %{tl_version}, tex(LY1Alegreya-LF.fd) = %{tl_version}
Provides:       tex(LY1Alegreya-OsF.fd) = %{tl_version}, tex(LY1Alegreya-Sup.fd) = %{tl_version}
Provides:       tex(LY1Alegreya-TLF.fd) = %{tl_version}, tex(LY1Alegreya-TOsF.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSC-TLF.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSans-Inf.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSans-LF.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSans-OsF.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSans-Sup.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSans-TLF.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSans-TOsF.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSansSC-Inf.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSansSC-LF.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSansSC-OsF.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSansSC-Sup.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSansSC-TLF.fd) = %{tl_version}
Provides:       tex(LY1AlegreyaSansSC-TOsF.fd) = %{tl_version}
Provides:       tex(OT1Alegreya-Inf.fd) = %{tl_version}, tex(OT1Alegreya-LF.fd) = %{tl_version}
Provides:       tex(OT1Alegreya-OsF.fd) = %{tl_version}, tex(OT1Alegreya-Sup.fd) = %{tl_version}
Provides:       tex(OT1Alegreya-TLF.fd) = %{tl_version}, tex(OT1Alegreya-TOsF.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSC-TLF.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSans-Inf.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSans-LF.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSans-OsF.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSans-Sup.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSans-TLF.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSans-TOsF.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSansSC-Inf.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSansSC-LF.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSansSC-OsF.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSansSC-Sup.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSansSC-TLF.fd) = %{tl_version}
Provides:       tex(OT1AlegreyaSansSC-TOsF.fd) = %{tl_version}
Provides:       tex(T1Alegreya-Inf.fd) = %{tl_version}, tex(T1Alegreya-LF.fd) = %{tl_version}
Provides:       tex(T1Alegreya-OsF.fd) = %{tl_version}, tex(T1Alegreya-Sup.fd) = %{tl_version}
Provides:       tex(T1Alegreya-TLF.fd) = %{tl_version}, tex(T1Alegreya-TOsF.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSC-TLF.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSans-Inf.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSans-LF.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSans-OsF.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSans-Sup.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSans-TLF.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSans-TOsF.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSansSC-Inf.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSansSC-LF.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSansSC-OsF.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSansSC-Sup.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSansSC-TLF.fd) = %{tl_version}
Provides:       tex(T1AlegreyaSansSC-TOsF.fd) = %{tl_version}
Provides:       tex(TS1Alegreya-LF.fd) = %{tl_version}, tex(TS1Alegreya-OsF.fd) = %{tl_version}
Provides:       tex(TS1Alegreya-TLF.fd) = %{tl_version}, tex(TS1Alegreya-TOsF.fd) = %{tl_version}
Provides:       tex(TS1AlegreyaSC-TLF.fd) = %{tl_version}
Provides:       tex(TS1AlegreyaSans-LF.fd) = %{tl_version}
Provides:       tex(TS1AlegreyaSans-OsF.fd) = %{tl_version}
Provides:       tex(TS1AlegreyaSans-TLF.fd) = %{tl_version}
Provides:       tex(TS1AlegreyaSans-TOsF.fd) = %{tl_version}
Provides:       tex(TS1AlegreyaSansSC-LF.fd) = %{tl_version}
Provides:       tex(TS1AlegreyaSansSC-OsF.fd) = %{tl_version}
Provides:       tex(TS1AlegreyaSansSC-TLF.fd) = %{tl_version}
Provides:       tex(TS1AlegreyaSansSC-TOsF.fd) = %{tl_version}

%description -n texlive-alegreya
The Alegreya fonts are designed by Juan Pablo del Peral for
Huerta Tipografica. Alegreya is a typeface originally intended
for literature. It conveys a dynamic and varied rhythm which
facilitates the reading of long texts. The italic has just as
much care and attention to detail in the design as the roman.
Bold, black, small caps and five number styles are available.

%package -n texlive-alegreya-doc
Summary:        Documentation for alegreya
Version:        svn48339
Provides:       tex-alegreya-doc
AutoReqProv:    No

%description -n texlive-alegreya-doc
Documentation for alegreya

%package -n texlive-alertmessage
Provides:       tex-alertmessage = %{tl_version}
License:        LPPL 1.3
Summary:        Alert messages for LaTeX
Version:        svn38055.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(picture.sty), tex(xcolor.sty), tex(ifthen.sty), tex(calc.sty)
Requires:       tex(graphicx.sty), tex(tikz.sty)
Provides:       tex(alertmessage.sty) = %{tl_version}

%description -n texlive-alertmessage
Some macros to display alert messages (informations, errors,
warnings and success messages).

%package -n texlive-alertmessage-doc
Summary:        Documentation for alertmessage
Version:        svn38055.1.1

Provides:       tex-alertmessage-doc
AutoReqProv:    No

%description -n texlive-alertmessage-doc
Documentation for alertmessage

%package -n texlive-algorithm2e
Provides:       tex-algorithm2e = %{tl_version}
License:        LPPL
Summary:        Floating algorithm environment with algorithmic keywords
Version:        svn44846
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(xspace.sty), tex(endfloat.sty), tex(relsize.sty)
Requires:       tex(color.sty), tex(tocbibind.sty)
Provides:       tex(algorithm2e.sty) = %{tl_version}

%description -n texlive-algorithm2e
Algorithm2e is an environment for writing algorithms. An
algorithm becomes a floating object (like figure, table, etc.).
The package provides macros that allow you to create different
keywords, and a set of predefined key words is provided; you
can change the typography of the keywords. The package allows
vertical lines delimiting a block of instructions in an
algorithm, and defines different sorts of algorithms such as
Procedure or Function; the name of these functions may be
reused in the text or in other algorithms.

%package -n texlive-algorithm2e-doc
Summary:        Documentation for algorithm2e
Version:        svn44846
Provides:       tex-algorithm2e-doc
AutoReqProv:    No

%description -n texlive-algorithm2e-doc
Documentation for algorithm2e

%package -n texlive-algorithmicx
Provides:       tex-algorithmicx = %{tl_version}
License:        LPPL
Summary:        The algorithmic style you always wanted
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(algc.sty) = %{tl_version}, tex(algcompatible.sty) = %{tl_version}
Provides:       tex(algmatlab.sty) = %{tl_version}, tex(algorithmicx.sty) = %{tl_version}
Provides:       tex(algpascal.sty) = %{tl_version}, tex(algpseudocode.sty) = %{tl_version}

%description -n texlive-algorithmicx
Algorithmicx provides a flexible, yet easy to use, way for
inserting good looking pseudocode or source code in your
papers. It has built in support for Pseudocode, Pascal and C,
and offers powerful means to create definitions for any
programming language. The user can adapt a Pseudocode style to
his native language.

%package -n texlive-algorithmicx-doc
Summary:        Documentation for algorithmicx
Version:        svn15878.0

Provides:       tex-algorithmicx-doc
AutoReqProv:    No

%description -n texlive-algorithmicx-doc
Documentation for algorithmicx

%package -n texlive-algorithms
Provides:       tex-algorithms = %{tl_version}
License:        LGPLv2+
Summary:        A suite of tools for typesetting algorithms in pseudo-code
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(float.sty), tex(ifthen.sty), tex(keyval.sty)
Provides:       tex(algorithm.sty) = %{tl_version}, tex(algorithmic.sty) = %{tl_version}

%description -n texlive-algorithms
Consists of two environments: algorithm and algorithmic. The
algorithm package defines a floating algorithm environment
designed to work with the algorithmic style. Within an
algorithmic environment a number of commands for typesetting
popular algorithmic constructs are available.

%package -n texlive-algorithms-doc
Summary:        Documentation for algorithms
Version:        svn38085.0.1
Provides:       tex-algorithms-doc
AutoReqProv:    No

%description -n texlive-algorithms-doc
Documentation for algorithms

%package -n texlive-alg
Provides:       tex-alg = %{tl_version}
License:        LPPL
Summary:        LaTeX environments for typesetting algorithms
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(float.sty), tex(ifthen.sty)
Provides:       tex(alg.sty) = %{tl_version}

%description -n texlive-alg
Defines two environments for typesetting algorithms in LaTeX2e.
The algtab environment is used to typeset an algorithm with
automatically numbered lines. The algorithm environment can be
used to encapsulate the algtab environment algorithm in a
floating body together with a header, a caption, etc.
\listofalgorithms is defined.

%package -n texlive-alg-doc
Summary:        Documentation for alg
Version:        svn15878.0

Provides:       tex-alg-doc
AutoReqProv:    No

%description -n texlive-alg-doc
Documentation for alg

%package -n texlive-allrunes
Provides:       tex-allrunes = %{tl_version}
License:        LPPL
Summary:        Fonts and LaTeX package for almost all runes
Version:        svn42221
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(ifthen.sty)
Provides:       tex(allrunes.map) = %{tl_version}, tex(fruabm.pfb) = %{tl_version}
Provides:       tex(fruabn.pfb) = %{tl_version}, tex(fruabq.pfb) = %{tl_version}
Provides:       tex(fruabr.pfb) = %{tl_version}, tex(fruabs.pfb) = %{tl_version}
Provides:       tex(fruabt.pfb) = %{tl_version}, tex(fruacm.pfb) = %{tl_version}
Provides:       tex(fruacn.pfb) = %{tl_version}, tex(fruacq.pfb) = %{tl_version}
Provides:       tex(fruacr.pfb) = %{tl_version}, tex(fruacs.pfb) = %{tl_version}
Provides:       tex(fruact.pfb) = %{tl_version}, tex(fruakm.pfb) = %{tl_version}
Provides:       tex(fruakn.pfb) = %{tl_version}, tex(fruakq.pfb) = %{tl_version}
Provides:       tex(fruakr.pfb) = %{tl_version}, tex(fruaks.pfb) = %{tl_version}
Provides:       tex(fruakt.pfb) = %{tl_version}, tex(frualm.pfb) = %{tl_version}
Provides:       tex(frualn.pfb) = %{tl_version}, tex(frualq.pfb) = %{tl_version}
Provides:       tex(frualr.pfb) = %{tl_version}, tex(fruals.pfb) = %{tl_version}
Provides:       tex(frualt.pfb) = %{tl_version}, tex(fruamm.pfb) = %{tl_version}
Provides:       tex(fruamn.pfb) = %{tl_version}, tex(fruamq.pfb) = %{tl_version}
Provides:       tex(fruamr.pfb) = %{tl_version}, tex(fruams.pfb) = %{tl_version}
Provides:       tex(fruamt.pfb) = %{tl_version}, tex(fruanm.pfb) = %{tl_version}
Provides:       tex(fruann.pfb) = %{tl_version}, tex(fruanq.pfb) = %{tl_version}
Provides:       tex(fruanr.pfb) = %{tl_version}, tex(fruans.pfb) = %{tl_version}
Provides:       tex(fruant.pfb) = %{tl_version}, tex(frucbm.pfb) = %{tl_version}
Provides:       tex(frucbn.pfb) = %{tl_version}, tex(frucbq.pfb) = %{tl_version}
Provides:       tex(frucbr.pfb) = %{tl_version}, tex(frucbs.pfb) = %{tl_version}
Provides:       tex(frucbt.pfb) = %{tl_version}, tex(fruccm.pfb) = %{tl_version}
Provides:       tex(fruccn.pfb) = %{tl_version}, tex(fruccq.pfb) = %{tl_version}
Provides:       tex(fruccr.pfb) = %{tl_version}, tex(fruccs.pfb) = %{tl_version}
Provides:       tex(frucct.pfb) = %{tl_version}, tex(fruckm.pfb) = %{tl_version}
Provides:       tex(fruckn.pfb) = %{tl_version}, tex(fruckq.pfb) = %{tl_version}
Provides:       tex(fruckr.pfb) = %{tl_version}, tex(frucks.pfb) = %{tl_version}
Provides:       tex(fruckt.pfb) = %{tl_version}, tex(fruclm.pfb) = %{tl_version}
Provides:       tex(frucln.pfb) = %{tl_version}, tex(fruclq.pfb) = %{tl_version}
Provides:       tex(fruclr.pfb) = %{tl_version}, tex(frucls.pfb) = %{tl_version}
Provides:       tex(fruclt.pfb) = %{tl_version}, tex(frucmm.pfb) = %{tl_version}
Provides:       tex(frucmn.pfb) = %{tl_version}, tex(frucmq.pfb) = %{tl_version}
Provides:       tex(frucmr.pfb) = %{tl_version}, tex(frucms.pfb) = %{tl_version}
Provides:       tex(frucmt.pfb) = %{tl_version}, tex(frucnm.pfb) = %{tl_version}
Provides:       tex(frucnn.pfb) = %{tl_version}, tex(frucnq.pfb) = %{tl_version}
Provides:       tex(frucnr.pfb) = %{tl_version}, tex(frucns.pfb) = %{tl_version}
Provides:       tex(frucnt.pfb) = %{tl_version}, tex(frulbm.pfb) = %{tl_version}
Provides:       tex(frulbn.pfb) = %{tl_version}, tex(frulbq.pfb) = %{tl_version}
Provides:       tex(frulbr.pfb) = %{tl_version}, tex(frulbs.pfb) = %{tl_version}
Provides:       tex(frulbt.pfb) = %{tl_version}, tex(frulcm.pfb) = %{tl_version}
Provides:       tex(frulcn.pfb) = %{tl_version}, tex(frulcq.pfb) = %{tl_version}
Provides:       tex(frulcr.pfb) = %{tl_version}, tex(frulcs.pfb) = %{tl_version}
Provides:       tex(frulct.pfb) = %{tl_version}, tex(frulkm.pfb) = %{tl_version}
Provides:       tex(frulkn.pfb) = %{tl_version}, tex(frulkq.pfb) = %{tl_version}
Provides:       tex(frulkr.pfb) = %{tl_version}, tex(frulks.pfb) = %{tl_version}
Provides:       tex(frulkt.pfb) = %{tl_version}, tex(frullm.pfb) = %{tl_version}
Provides:       tex(frulln.pfb) = %{tl_version}, tex(frullq.pfb) = %{tl_version}
Provides:       tex(frullr.pfb) = %{tl_version}, tex(frulls.pfb) = %{tl_version}
Provides:       tex(frullt.pfb) = %{tl_version}, tex(frulmm.pfb) = %{tl_version}
Provides:       tex(frulmn.pfb) = %{tl_version}, tex(frulmq.pfb) = %{tl_version}
Provides:       tex(frulmr.pfb) = %{tl_version}, tex(frulms.pfb) = %{tl_version}
Provides:       tex(frulmt.pfb) = %{tl_version}, tex(frulnm.pfb) = %{tl_version}
Provides:       tex(frulnn.pfb) = %{tl_version}, tex(frulnq.pfb) = %{tl_version}
Provides:       tex(frulnr.pfb) = %{tl_version}, tex(frulns.pfb) = %{tl_version}
Provides:       tex(frulnt.pfb) = %{tl_version}, tex(frumbm.pfb) = %{tl_version}
Provides:       tex(frumbn.pfb) = %{tl_version}, tex(frumbq.pfb) = %{tl_version}
Provides:       tex(frumbr.pfb) = %{tl_version}, tex(frumbs.pfb) = %{tl_version}
Provides:       tex(frumbt.pfb) = %{tl_version}, tex(frumcm.pfb) = %{tl_version}
Provides:       tex(frumcn.pfb) = %{tl_version}, tex(frumcq.pfb) = %{tl_version}
Provides:       tex(frumcr.pfb) = %{tl_version}, tex(frumcs.pfb) = %{tl_version}
Provides:       tex(frumct.pfb) = %{tl_version}, tex(frumkm.pfb) = %{tl_version}
Provides:       tex(frumkn.pfb) = %{tl_version}, tex(frumkq.pfb) = %{tl_version}
Provides:       tex(frumkr.pfb) = %{tl_version}, tex(frumks.pfb) = %{tl_version}
Provides:       tex(frumkt.pfb) = %{tl_version}, tex(frumlm.pfb) = %{tl_version}
Provides:       tex(frumln.pfb) = %{tl_version}, tex(frumlq.pfb) = %{tl_version}
Provides:       tex(frumlr.pfb) = %{tl_version}, tex(frumls.pfb) = %{tl_version}
Provides:       tex(frumlt.pfb) = %{tl_version}, tex(frummm.pfb) = %{tl_version}
Provides:       tex(frummn.pfb) = %{tl_version}, tex(frummq.pfb) = %{tl_version}
Provides:       tex(frummr.pfb) = %{tl_version}, tex(frumms.pfb) = %{tl_version}
Provides:       tex(frummt.pfb) = %{tl_version}, tex(frumnm.pfb) = %{tl_version}
Provides:       tex(frumnn.pfb) = %{tl_version}, tex(frumnq.pfb) = %{tl_version}
Provides:       tex(frumnr.pfb) = %{tl_version}, tex(frumns.pfb) = %{tl_version}
Provides:       tex(frumnt.pfb) = %{tl_version}, tex(frunbm.pfb) = %{tl_version}
Provides:       tex(frunbn.pfb) = %{tl_version}, tex(frunbq.pfb) = %{tl_version}
Provides:       tex(frunbr.pfb) = %{tl_version}, tex(frunbs.pfb) = %{tl_version}
Provides:       tex(frunbt.pfb) = %{tl_version}, tex(fruncm.pfb) = %{tl_version}
Provides:       tex(fruncn.pfb) = %{tl_version}, tex(fruncq.pfb) = %{tl_version}
Provides:       tex(fruncr.pfb) = %{tl_version}, tex(fruncs.pfb) = %{tl_version}
Provides:       tex(frunct.pfb) = %{tl_version}, tex(frunkm.pfb) = %{tl_version}
Provides:       tex(frunkn.pfb) = %{tl_version}, tex(frunkq.pfb) = %{tl_version}
Provides:       tex(frunkr.pfb) = %{tl_version}, tex(frunks.pfb) = %{tl_version}
Provides:       tex(frunkt.pfb) = %{tl_version}, tex(frunlm.pfb) = %{tl_version}
Provides:       tex(frunln.pfb) = %{tl_version}, tex(frunlq.pfb) = %{tl_version}
Provides:       tex(frunlr.pfb) = %{tl_version}, tex(frunls.pfb) = %{tl_version}
Provides:       tex(frunlt.pfb) = %{tl_version}, tex(frunmm.pfb) = %{tl_version}
Provides:       tex(frunmn.pfb) = %{tl_version}, tex(frunmq.pfb) = %{tl_version}
Provides:       tex(frunmr.pfb) = %{tl_version}, tex(frunms.pfb) = %{tl_version}
Provides:       tex(frunmt.pfb) = %{tl_version}, tex(frunnm.pfb) = %{tl_version}
Provides:       tex(frunnn.pfb) = %{tl_version}, tex(frunnq.pfb) = %{tl_version}
Provides:       tex(frunnr.pfb) = %{tl_version}, tex(frunns.pfb) = %{tl_version}
Provides:       tex(frunnt.pfb) = %{tl_version}, tex(frutbm.pfb) = %{tl_version}
Provides:       tex(frutbn.pfb) = %{tl_version}, tex(frutbq.pfb) = %{tl_version}
Provides:       tex(frutbr.pfb) = %{tl_version}, tex(frutbs.pfb) = %{tl_version}
Provides:       tex(frutbt.pfb) = %{tl_version}, tex(frutcm.pfb) = %{tl_version}
Provides:       tex(frutcn.pfb) = %{tl_version}, tex(frutcq.pfb) = %{tl_version}
Provides:       tex(frutcr.pfb) = %{tl_version}, tex(frutcs.pfb) = %{tl_version}
Provides:       tex(frutct.pfb) = %{tl_version}, tex(frutkm.pfb) = %{tl_version}
Provides:       tex(frutkn.pfb) = %{tl_version}, tex(frutkq.pfb) = %{tl_version}
Provides:       tex(frutkr.pfb) = %{tl_version}, tex(frutks.pfb) = %{tl_version}
Provides:       tex(frutkt.pfb) = %{tl_version}, tex(frutlm.pfb) = %{tl_version}
Provides:       tex(frutln.pfb) = %{tl_version}, tex(frutlq.pfb) = %{tl_version}
Provides:       tex(frutlr.pfb) = %{tl_version}, tex(frutls.pfb) = %{tl_version}
Provides:       tex(frutlt.pfb) = %{tl_version}, tex(frutmm.pfb) = %{tl_version}
Provides:       tex(frutmn.pfb) = %{tl_version}, tex(frutmq.pfb) = %{tl_version}
Provides:       tex(frutmr.pfb) = %{tl_version}, tex(frutms.pfb) = %{tl_version}
Provides:       tex(frutmt.pfb) = %{tl_version}, tex(frutnm.pfb) = %{tl_version}
Provides:       tex(frutnn.pfb) = %{tl_version}, tex(frutnq.pfb) = %{tl_version}
Provides:       tex(frutnr.pfb) = %{tl_version}, tex(frutns.pfb) = %{tl_version}
Provides:       tex(frutnt.pfb) = %{tl_version}, tex(allrunes.sty) = %{tl_version}
Provides:       tex(ara.fd) = %{tl_version}, tex(arc.fd) = %{tl_version}
Provides:       tex(arl.fd) = %{tl_version}, tex(arm.fd) = %{tl_version}
Provides:       tex(arn.fd) = %{tl_version}, tex(art.fd) = %{tl_version}

%description -n texlive-allrunes
This large collection of fonts (in Adobe Type 1 format), with
the LaTeX package gives access to almost all runes ever used in
Europe. The bundle covers not only the main forms but also a
lot of varieties.

%package -n texlive-allrunes-doc
Summary:        Documentation for allrunes
Version:        svn42221
Provides:       tex-allrunes-doc
AutoReqProv:    No

%description -n texlive-allrunes-doc
Documentation for allrunes

%package -n texlive-almfixed
Provides:       tex-almfixed = %{tl_version}
License:        LPPL
Summary:        Arabic-Latin Modern Fixed extends TeX-Gyre Latin Modern Mono 10 Regular to full Arabic Unicode support
Version:        svn35065.0.92

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(almfixed.otf) = %{tl_version}, tex(almfixed.ttf) = %{tl_version}

%description -n texlive-almfixed
Arabic-Latin Modern Fixed is an extension of TeX-Gyre Latin
Modern Mono 10 Regular. Every glyph and opentype feature of the
Latin Modern Mono has been retained, with minor improvements.
On the other hand, we have changed the vertical metrics of the
font. Although the Arabic script is designed to use the same x-
size as Latin Modern Mono, the former script needs greater
ascender and descender space. Every Arabic glyph in each
Unicode-code block is supported (up to Unicode 7.0): Arabic,
Arabic Supplement, Arabic Extended, Arabic Presentation-Forms
A, and Arabic Presentation-Forms B. There are two versions of
the font: otf and ttf. The opentype version is for print
applications (and usually the default for TeX). The TrueType
version is for on-screen applications such as text editors.
Hinting in the ttf version is much better for on-screen, at
least on Microsoft Windows. The unique feature of Arabic-Latin
Modern is its treatment of vowels and diacritics. Each vowel
and diacritic (ALM Fixed contains a total of 68 such glyphs)
may now be edited horizontally within any text editor or
processor. The author believes this is the very first opentype
Arabic font ever to have this capability. Editing complex
Arabic texts will now be much easier to input and to proofread.

%package -n texlive-almfixed-doc
Summary:        Documentation for almfixed
Version:        svn35065.0.92

Provides:       tex-almfixed-doc
AutoReqProv:    No

%description -n texlive-almfixed-doc
Documentation for almfixed

%package -n texlive-alnumsec
Provides:       tex-alnumsec = %{tl_version}
License:        LPPL
Summary:        Alphanumeric section numbering
Version:        svn15878.v0.03

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(alnumsec.sty) = %{tl_version}

%description -n texlive-alnumsec
This package allows you to use alphanumeric section numbering,
for instance "A. Introduction ... III. International Law". Its
output is similar to alphanum, but you can use the standard
LaTeX sectioning commands, so that it is possible to switch
numbering schemes easily. Greek letters, double letters (bb)
and different delimiters around them are supported.

%package -n texlive-alnumsec-doc
Summary:        Documentation for alnumsec
Version:        svn15878.v0.03

Provides:       tex-alnumsec-doc
AutoReqProv:    No

%description -n texlive-alnumsec-doc
Documentation for alnumsec

%package -n texlive-alterqcm
Provides:       tex-alterqcm = %{tl_version}
License:        LPPL
Summary:        Multiple choice questionnaires in two column tables
Version:        svn23385.3.7c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(calc.sty), tex(ifthen.sty), tex(array.sty)
Requires:       tex(multirow.sty), tex(pifont.sty)
Provides:       tex(alterqcm.sty) = %{tl_version}

%description -n texlive-alterqcm
Macros to support the creation of multiple-choice
questionnaires in two-column tables.

%package -n texlive-alterqcm-doc
Summary:        Documentation for alterqcm
Version:        svn23385.3.7c

Provides:       tex-alterqcm-doc
AutoReqProv:    No

%description -n texlive-alterqcm-doc
Documentation for alterqcm

%package -n texlive-altfont
Provides:       tex-altfont = %{tl_version}
License:        GPL+
Summary:        Alternative font handling in LaTeX
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontenc.sty)
Provides:       tex(altfont.cfg) = %{tl_version}, tex(altfont.sty) = %{tl_version}
Provides:       tex(psfont.cfg) = %{tl_version}, tex(psfont.sty) = %{tl_version}

%description -n texlive-altfont
The package provides a replacement for that part of psnfss and
mfnfss that changes the default font. The package is
distributed together with the psfont package, by the same
author.

%package -n texlive-altfont-doc
Summary:        Documentation for altfont
Version:        svn15878.1.1

Provides:       tex-altfont-doc
AutoReqProv:    No

%description -n texlive-altfont-doc
Documentation for altfont

%package -n texlive-ametsoc
Provides:       tex-ametsoc = %{tl_version}
License:        LPPL
Summary:        Official American Meteorological Society LaTeX Template
Version:        svn36030.4.3.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ametsoc.cls) = %{tl_version}

%description -n texlive-ametsoc
This bundle contains all the files necessary to write an
article using LaTeX for the American Meteorological Society
journals. The article and bibliography style files are provided
(with documentation) and a blank template for authors to use
when writing their article. Also available is a separate style
package used to format a two-column, journal page layout draft
for the author's personal use.

%package -n texlive-ametsoc-doc
Summary:        Documentation for ametsoc
Version:        svn36030.4.3.2

Provides:       tex-ametsoc-doc
AutoReqProv:    No

%description -n texlive-ametsoc-doc
Documentation for ametsoc

%package -n texlive-amiri
Provides:       tex-amiri = %{tl_version}
License:        OFL
Summary:        A classical Arabic typeface, Naskh style
Version:        svn46104
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(amiri-bold.ttf) = %{tl_version}, tex(amiri-boldslanted.ttf) = %{tl_version}
Provides:       tex(amiri-quran.ttf) = %{tl_version}, tex(amiri-quran-colored.ttf) = %{tl_version}
Provides:       tex(amiri-regular.ttf) = %{tl_version}, tex(amiri-slanted.ttf) = %{tl_version}

%description -n texlive-amiri
Amiri is a classical Arabic typeface in Naskh style for
typesetting books and other running text. It is a revival of
the beautiful typeface pioneered in the early 20th century by
Bulaq Press in Cairo, also known as Amiria Press, after which
the font is named. The project aims at the revival of the
aesthetics and traditions of Arabic typesetting, and adapting
it to the era of digital typesetting, in a publicly available
form.

%package -n texlive-amiri-doc
Summary:        Documentation for amiri
Version:        svn46104
Provides:       tex-amiri-doc
AutoReqProv:    No

%description -n texlive-amiri-doc
Documentation for amiri

%package -n texlive-amsaddr
Provides:       tex-amsaddr = %{tl_version}
License:        LPPL
Summary:        Alter the position of affiliations in amsart
Version:        svn29630.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(amsaddr.sty) = %{tl_version}

%description -n texlive-amsaddr
The package is to be used with the amsart documentclass. It
lets you move the authors' affiliations either just below the
authors' names on the front page or as footnotes on the first
page. The email addresses are always listed as a footnote on
the front page.

%package -n texlive-amsaddr-doc
Summary:        Documentation for amsaddr
Version:        svn29630.1.1

Provides:       tex-amsaddr-doc
AutoReqProv:    No

%description -n texlive-amsaddr-doc
Documentation for amsaddr

%package -n texlive-amscls
Provides:       tex-amscls = %{tl_version}
License:        LPPL 1.3
Summary:        AMS document classes for LaTeX
Version:        svn46099
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(amstex.sty), tex(amsmath.sty), tex(amsfonts.sty), tex(url.sty)
Requires:       tex(doc.sty)
Provides:       tex(amsart.cls) = %{tl_version}, tex(amsbook.cls) = %{tl_version}
Provides:       tex(amsbooka.sty) = %{tl_version}, tex(amsdtx.cls) = %{tl_version}
Provides:       tex(amsldoc.cls) = %{tl_version}, tex(amsmidx.sty) = %{tl_version}
Provides:       tex(amsproc.cls) = %{tl_version}, tex(amsthm.sty) = %{tl_version}
Provides:       tex(upref.sty) = %{tl_version}

%description -n texlive-amscls
This bundle contains three AMS classes, amsart (for writing
articles for the AMS), amsbook (for books) and amsproc (for
proceedings), together with some supporting material. The
material is made available as part of the AMS-LaTeX
distribution.

%package -n texlive-amsfonts
Provides:       tex-amsfonts = %{tl_version}
License:        OFL
Summary:        TeX fonts from the American Mathematical Society
Version:        svn29208.3.04

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(cm.map) = %{tl_version}, tex(cmextra.map) = %{tl_version}
Provides:       tex(cyrillic.map) = %{tl_version}, tex(euler.map) = %{tl_version}
Provides:       tex(latxfont.map) = %{tl_version}, tex(symbols.map) = %{tl_version}
Provides:       tex(cmbsy5.tfm) = %{tl_version}, tex(cmbsy6.tfm) = %{tl_version}
Provides:       tex(cmbsy7.tfm) = %{tl_version}, tex(cmbsy8.tfm) = %{tl_version}
Provides:       tex(cmbsy9.tfm) = %{tl_version}, tex(cmcsc8.tfm) = %{tl_version}
Provides:       tex(cmcsc9.tfm) = %{tl_version}, tex(cmex7.tfm) = %{tl_version}
Provides:       tex(cmex8.tfm) = %{tl_version}, tex(cmex9.tfm) = %{tl_version}
Provides:       tex(cmmib5.tfm) = %{tl_version}, tex(cmmib6.tfm) = %{tl_version}
Provides:       tex(cmmib7.tfm) = %{tl_version}, tex(cmmib8.tfm) = %{tl_version}
Provides:       tex(cmmib9.tfm) = %{tl_version}, tex(wncyb10.tfm) = %{tl_version}
Provides:       tex(wncyb5.tfm) = %{tl_version}, tex(wncyb6.tfm) = %{tl_version}
Provides:       tex(wncyb7.tfm) = %{tl_version}, tex(wncyb8.tfm) = %{tl_version}
Provides:       tex(wncyb9.tfm) = %{tl_version}, tex(wncyi10.tfm) = %{tl_version}
Provides:       tex(wncyi5.tfm) = %{tl_version}, tex(wncyi6.tfm) = %{tl_version}
Provides:       tex(wncyi7.tfm) = %{tl_version}, tex(wncyi8.tfm) = %{tl_version}
Provides:       tex(wncyi9.tfm) = %{tl_version}, tex(wncyr10.tfm) = %{tl_version}
Provides:       tex(wncyr5.tfm) = %{tl_version}, tex(wncyr6.tfm) = %{tl_version}
Provides:       tex(wncyr7.tfm) = %{tl_version}, tex(wncyr8.tfm) = %{tl_version}
Provides:       tex(wncyr9.tfm) = %{tl_version}, tex(wncysc10.tfm) = %{tl_version}
Provides:       tex(wncyss10.tfm) = %{tl_version}, tex(wncyss8.tfm) = %{tl_version}
Provides:       tex(wncyss9.tfm) = %{tl_version}, tex(dummy.tfm) = %{tl_version}
Provides:       tex(euex10.tfm) = %{tl_version}, tex(euex7.tfm) = %{tl_version}
Provides:       tex(euex8.tfm) = %{tl_version}, tex(euex9.tfm) = %{tl_version}
Provides:       tex(eufb10.tfm) = %{tl_version}, tex(eufb5.tfm) = %{tl_version}
Provides:       tex(eufb6.tfm) = %{tl_version}, tex(eufb7.tfm) = %{tl_version}
Provides:       tex(eufb8.tfm) = %{tl_version}, tex(eufb9.tfm) = %{tl_version}
Provides:       tex(eufm10.tfm) = %{tl_version}, tex(eufm5.tfm) = %{tl_version}
Provides:       tex(eufm6.tfm) = %{tl_version}, tex(eufm7.tfm) = %{tl_version}
Provides:       tex(eufm8.tfm) = %{tl_version}, tex(eufm9.tfm) = %{tl_version}
Provides:       tex(eurb10.tfm) = %{tl_version}, tex(eurb5.tfm) = %{tl_version}
Provides:       tex(eurb6.tfm) = %{tl_version}, tex(eurb7.tfm) = %{tl_version}
Provides:       tex(eurb8.tfm) = %{tl_version}, tex(eurb9.tfm) = %{tl_version}
Provides:       tex(eurm10.tfm) = %{tl_version}, tex(eurm5.tfm) = %{tl_version}
Provides:       tex(eurm6.tfm) = %{tl_version}, tex(eurm7.tfm) = %{tl_version}
Provides:       tex(eurm8.tfm) = %{tl_version}, tex(eurm9.tfm) = %{tl_version}
Provides:       tex(eusb10.tfm) = %{tl_version}, tex(eusb5.tfm) = %{tl_version}
Provides:       tex(eusb6.tfm) = %{tl_version}, tex(eusb7.tfm) = %{tl_version}
Provides:       tex(eusb8.tfm) = %{tl_version}, tex(eusb9.tfm) = %{tl_version}
Provides:       tex(eusm10.tfm) = %{tl_version}, tex(eusm5.tfm) = %{tl_version}
Provides:       tex(eusm6.tfm) = %{tl_version}, tex(eusm7.tfm) = %{tl_version}
Provides:       tex(eusm8.tfm) = %{tl_version}, tex(eusm9.tfm) = %{tl_version}
Provides:       tex(msam10.tfm) = %{tl_version}, tex(msam5.tfm) = %{tl_version}
Provides:       tex(msam6.tfm) = %{tl_version}, tex(msam7.tfm) = %{tl_version}
Provides:       tex(msam8.tfm) = %{tl_version}, tex(msam9.tfm) = %{tl_version}
Provides:       tex(msbm10.tfm) = %{tl_version}, tex(msbm5.tfm) = %{tl_version}
Provides:       tex(msbm6.tfm) = %{tl_version}, tex(msbm7.tfm) = %{tl_version}
Provides:       tex(msbm8.tfm) = %{tl_version}, tex(msbm9.tfm) = %{tl_version}
Provides:       tex(cmb10.pfb) = %{tl_version}, tex(cmbsy10.pfb) = %{tl_version}
Provides:       tex(cmbx10.pfb) = %{tl_version}, tex(cmbx12.pfb) = %{tl_version}
Provides:       tex(cmbx5.pfb) = %{tl_version}, tex(cmbx6.pfb) = %{tl_version}
Provides:       tex(cmbx7.pfb) = %{tl_version}, tex(cmbx8.pfb) = %{tl_version}
Provides:       tex(cmbx9.pfb) = %{tl_version}, tex(cmbxsl10.pfb) = %{tl_version}
Provides:       tex(cmbxti10.pfb) = %{tl_version}, tex(cmcsc10.pfb) = %{tl_version}
Provides:       tex(cmdunh10.pfb) = %{tl_version}, tex(cmex10.pfb) = %{tl_version}
Provides:       tex(cmff10.pfb) = %{tl_version}, tex(cmfi10.pfb) = %{tl_version}
Provides:       tex(cmfib8.pfb) = %{tl_version}, tex(cminch.pfb) = %{tl_version}
Provides:       tex(cmitt10.pfb) = %{tl_version}, tex(cmmi10.pfb) = %{tl_version}
Provides:       tex(cmmi12.pfb) = %{tl_version}, tex(cmmi5.pfb) = %{tl_version}
Provides:       tex(cmmi6.pfb) = %{tl_version}, tex(cmmi7.pfb) = %{tl_version}
Provides:       tex(cmmi8.pfb) = %{tl_version}, tex(cmmi9.pfb) = %{tl_version}
Provides:       tex(cmmib10.pfb) = %{tl_version}, tex(cmr10.pfb) = %{tl_version}
Provides:       tex(cmr12.pfb) = %{tl_version}, tex(cmr17.pfb) = %{tl_version}
Provides:       tex(cmr5.pfb) = %{tl_version}, tex(cmr6.pfb) = %{tl_version}
Provides:       tex(cmr7.pfb) = %{tl_version}, tex(cmr8.pfb) = %{tl_version}
Provides:       tex(cmr9.pfb) = %{tl_version}, tex(cmsl10.pfb) = %{tl_version}
Provides:       tex(cmsl12.pfb) = %{tl_version}, tex(cmsl8.pfb) = %{tl_version}
Provides:       tex(cmsl9.pfb) = %{tl_version}, tex(cmsltt10.pfb) = %{tl_version}
Provides:       tex(cmss10.pfb) = %{tl_version}, tex(cmss12.pfb) = %{tl_version}
Provides:       tex(cmss17.pfb) = %{tl_version}, tex(cmss8.pfb) = %{tl_version}
Provides:       tex(cmss9.pfb) = %{tl_version}, tex(cmssbx10.pfb) = %{tl_version}
Provides:       tex(cmssdc10.pfb) = %{tl_version}, tex(cmssi10.pfb) = %{tl_version}
Provides:       tex(cmssi12.pfb) = %{tl_version}, tex(cmssi17.pfb) = %{tl_version}
Provides:       tex(cmssi8.pfb) = %{tl_version}, tex(cmssi9.pfb) = %{tl_version}
Provides:       tex(cmssq8.pfb) = %{tl_version}, tex(cmssqi8.pfb) = %{tl_version}
Provides:       tex(cmsy10.pfb) = %{tl_version}, tex(cmsy5.pfb) = %{tl_version}
Provides:       tex(cmsy6.pfb) = %{tl_version}, tex(cmsy7.pfb) = %{tl_version}
Provides:       tex(cmsy8.pfb) = %{tl_version}, tex(cmsy9.pfb) = %{tl_version}
Provides:       tex(cmtcsc10.pfb) = %{tl_version}, tex(cmtex10.pfb) = %{tl_version}
Provides:       tex(cmtex8.pfb) = %{tl_version}, tex(cmtex9.pfb) = %{tl_version}
Provides:       tex(cmti10.pfb) = %{tl_version}, tex(cmti12.pfb) = %{tl_version}
Provides:       tex(cmti7.pfb) = %{tl_version}, tex(cmti8.pfb) = %{tl_version}
Provides:       tex(cmti9.pfb) = %{tl_version}, tex(cmtt10.pfb) = %{tl_version}
Provides:       tex(cmtt12.pfb) = %{tl_version}, tex(cmtt8.pfb) = %{tl_version}
Provides:       tex(cmtt9.pfb) = %{tl_version}, tex(cmu10.pfb) = %{tl_version}
Provides:       tex(cmvtt10.pfb) = %{tl_version}, tex(cmbsy5.pfb) = %{tl_version}
Provides:       tex(cmbsy6.pfb) = %{tl_version}, tex(cmbsy7.pfb) = %{tl_version}
Provides:       tex(cmbsy8.pfb) = %{tl_version}, tex(cmbsy9.pfb) = %{tl_version}
Provides:       tex(cmcsc8.pfb) = %{tl_version}, tex(cmcsc9.pfb) = %{tl_version}
Provides:       tex(cmex7.pfb) = %{tl_version}, tex(cmex8.pfb) = %{tl_version}
Provides:       tex(cmex9.pfb) = %{tl_version}, tex(cmmib5.pfb) = %{tl_version}
Provides:       tex(cmmib6.pfb) = %{tl_version}, tex(cmmib7.pfb) = %{tl_version}
Provides:       tex(cmmib8.pfb) = %{tl_version}, tex(cmmib9.pfb) = %{tl_version}
Provides:       tex(wncyb10.pfb) = %{tl_version}, tex(wncyi10.pfb) = %{tl_version}
Provides:       tex(wncyr10.pfb) = %{tl_version}, tex(wncysc10.pfb) = %{tl_version}
Provides:       tex(wncyss10.pfb) = %{tl_version}, tex(euex10.pfb) = %{tl_version}
Provides:       tex(euex7.pfb) = %{tl_version}, tex(euex8.pfb) = %{tl_version}
Provides:       tex(euex9.pfb) = %{tl_version}, tex(eufb10.pfb) = %{tl_version}
Provides:       tex(eufb5.pfb) = %{tl_version}, tex(eufb7.pfb) = %{tl_version}
Provides:       tex(eufm10.pfb) = %{tl_version}, tex(eufm5.pfb) = %{tl_version}
Provides:       tex(eufm7.pfb) = %{tl_version}, tex(eurb10.pfb) = %{tl_version}
Provides:       tex(eurb5.pfb) = %{tl_version}, tex(eurb7.pfb) = %{tl_version}
Provides:       tex(eurm10.pfb) = %{tl_version}, tex(eurm5.pfb) = %{tl_version}
Provides:       tex(eurm7.pfb) = %{tl_version}, tex(eusb10.pfb) = %{tl_version}
Provides:       tex(eusb5.pfb) = %{tl_version}, tex(eusb7.pfb) = %{tl_version}
Provides:       tex(eusm10.pfb) = %{tl_version}, tex(eusm5.pfb) = %{tl_version}
Provides:       tex(eusm7.pfb) = %{tl_version}, tex(lasy10.pfb) = %{tl_version}
Provides:       tex(lasy5.pfb) = %{tl_version}, tex(lasy6.pfb) = %{tl_version}
Provides:       tex(lasy7.pfb) = %{tl_version}, tex(lasy8.pfb) = %{tl_version}
Provides:       tex(lasy9.pfb) = %{tl_version}, tex(lasyb10.pfb) = %{tl_version}
Provides:       tex(lcircle1.pfb) = %{tl_version}, tex(lcirclew.pfb) = %{tl_version}
Provides:       tex(lcmss8.pfb) = %{tl_version}, tex(lcmssb8.pfb) = %{tl_version}
Provides:       tex(lcmssi8.pfb) = %{tl_version}, tex(line10.pfb) = %{tl_version}
Provides:       tex(linew10.pfb) = %{tl_version}, tex(msam10.pfb) = %{tl_version}
Provides:       tex(msam5.pfb) = %{tl_version}, tex(msam6.pfb) = %{tl_version}
Provides:       tex(msam7.pfb) = %{tl_version}, tex(msam8.pfb) = %{tl_version}
Provides:       tex(msam9.pfb) = %{tl_version}, tex(msbm10.pfb) = %{tl_version}
Provides:       tex(msbm5.pfb) = %{tl_version}, tex(msbm6.pfb) = %{tl_version}
Provides:       tex(msbm7.pfb) = %{tl_version}, tex(msbm8.pfb) = %{tl_version}
Provides:       tex(msbm9.pfb) = %{tl_version}, tex(amsfonts.sty) = %{tl_version}
Provides:       tex(amssymb.sty) = %{tl_version}, tex(cmmib57.sty) = %{tl_version}
Provides:       tex(eucal.sty) = %{tl_version}, tex(eufrak.sty) = %{tl_version}
Provides:       tex(euscript.sty) = %{tl_version}, tex(ueuex.fd) = %{tl_version}
Provides:       tex(ueuf.fd) = %{tl_version}, tex(ueur.fd) = %{tl_version}
Provides:       tex(ueus.fd) = %{tl_version}, tex(umsa.fd) = %{tl_version}
Provides:       tex(umsb.fd) = %{tl_version}, tex(amssym.def) = %{tl_version}
Provides:       tex(amssym.tex) = %{tl_version}, tex(cyracc.def) = %{tl_version}

%description -n texlive-amsfonts
An extended set of fonts for use in mathematics, including:
extra mathematical symbols; blackboard bold letters (uppercase
only); fraktur letters; subscript sizes of bold math italic and
bold Greek letters; subscript sizes of large symbols such as
sum and product; added sizes of the Computer Modern small caps
font; cyrillic fonts (from the University of Washington); Euler
mathematical fonts. All fonts are provided as Adobe Type 1
files, and all except the Euler fonts are provided as Metafont
source. The distribution also includes the canonical Type 1
versions of the Computer Modern family of fonts. Plain TeX and
LaTeX macros for using the fonts are provided.

%package -n texlive-amsfonts-doc
Summary:        Documentation for amsfonts
Version:        svn29208.3.04

Provides:       tex-amsfonts-doc
AutoReqProv:    No

%description -n texlive-amsfonts-doc
Documentation for amsfonts

%package -n texlive-amslatex-primer-doc
Summary:        Documentation for amslatex-primer
Version:        svn28980.2.3

Provides:       tex-amslatex-primer-doc
AutoReqProv:    No

%description -n texlive-amslatex-primer-doc
Documentation for amslatex-primer

%package -n texlive-amsldoc-it-doc
Summary:        Documentation for amsldoc-it
Version:        svn15878.0

Provides:       tex-amsldoc-it-doc
AutoReqProv:    No

%description -n texlive-amsldoc-it-doc
Documentation for amsldoc-it

%package -n texlive-amsldoc-vn-doc
Summary:        Documentation for amsldoc-vn
Version:        svn21855.2.0

Provides:       tex-amsldoc-vn-doc
AutoReqProv:    No

%description -n texlive-amsldoc-vn-doc
Documentation for amsldoc-vn

%package -n texlive-amsmath-it-doc
Summary:        Documentation for amsmath-it
Version:        svn22930.0

Provides:       tex-amsmath-it-doc
AutoReqProv:    No

%description -n texlive-amsmath-it-doc
Documentation for amsmath-it

%package -n texlive-amsmath
Provides:       tex-amsmath = %{tl_version}
License:        LPPL
Summary:        AMS mathematical facilities for LaTeX
Version:        svn47349
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(amstext.sty)
Provides:       tex(amsbsy.sty) = %{tl_version}, tex(amscd.sty) = %{tl_version}
Provides:       tex(amsgen.sty) = %{tl_version}, tex(amsmath.sty) = %{tl_version}
Provides:       tex(amsopn.sty) = %{tl_version}, tex(amstex.sty) = %{tl_version}
Provides:       tex(amstext.sty) = %{tl_version}, tex(amsxtra.sty) = %{tl_version}

%description -n texlive-amsmath
The package provides the principal packages in the AMS-LaTeX
distribution. It adapts for use in LaTeX most of the
mathematical features found in AMS-TeX; it is highly
recommendsd as an adjunct to serious mathematical typesetting
in LaTeX. When amsmath is loaded, AMS-LaTeX packages amsbsy
(for bold symbols), amsopn (for operator names) and amstext
(for text embdedded in mathematics) are also loaded. Amsmath is
part of the LaTeX required distribution; however, several
contributed packages add still further to its appeal; examples
are empheq, which provides functions for decorating and
highlighting mathematics, and ntheorem, for specifying theorem
(and similar) definitions.

%package -n texlive-amsmath-doc
Summary:        Documentation for amsmath
Version:        svn47349
Provides:       tex-amsmath-doc
AutoReqProv:    No

%description -n texlive-amsmath-doc
Documentation for amsmath

%package -n texlive-amsrefs
Provides:       tex-amsrefs = %{tl_version}
License:        LPPL 1.3
Summary:        A LaTeX-based replacement for BibTeX
Version:        svn30646.2.14

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(url.sty), tex(ifoption.sty), tex(backref.sty), tex(hyperref.sty)
Requires:       tex(textcmds.sty)
Provides:       tex(amsbst.sty) = %{tl_version}, tex(amsrefs.sty) = %{tl_version}
Provides:       tex(ifoption.sty) = %{tl_version}, tex(mathscinet.sty) = %{tl_version}
Provides:       tex(pcatcode.sty) = %{tl_version}, tex(rkeyval.sty) = %{tl_version}
Provides:       tex(textcmds.sty) = %{tl_version}

%description -n texlive-amsrefs
Amsrefs is a LaTeX package for bibliographies that provides an
archival data format similar to the format of BibTeX database
files, but adapted to make direct processing by LaTeX easier.
The package can be used either in conjunction with BibTeX or as
a replacement for BibTeX.

%package -n texlive-amsrefs-doc
Summary:        Documentation for amsrefs
Version:        svn30646.2.14

Provides:       tex-amsrefs-doc
AutoReqProv:    No

%description -n texlive-amsrefs-doc
Documentation for amsrefs

%package -n texlive-amsthdoc-it-doc
Summary:        Documentation for amsthdoc-it
Version:        svn45662
Provides:       tex-amsthdoc-it-doc
AutoReqProv:    No

%description -n texlive-amsthdoc-it-doc
Documentation for amsthdoc-it

%package -n texlive-animate
Provides:       tex-animate = %{tl_version}
License:        LPPL
Summary:        Create PDF animations from graphics files and inline graphics
Version:        svn48101
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(keyval.sty), tex(ifthen.sty), tex(ifpdf.sty), tex(atbegshi.sty)
Requires:       tex(ifluatex.sty), tex(ifdraft.sty), tex(calc.sty), tex(atenddvi.sty)
Requires:       tex(graphics.sty), tex(pdftexcmds.sty)
Provides:       tex(animate.sty) = %{tl_version}, tex(animfp.sty) = %{tl_version}

%description -n texlive-animate
The package provides an interface to create portable,
JavaScript driven PDF animations from sets of graphics files or
from inline graphics, such as LaTeX picture environment,
PSTricks or pgf/TikZ generated pictures, or just from typeset
text.

%package -n texlive-animate-doc
Summary:        Documentation for animate
Version:        svn48101
Provides:       tex-animate-doc
AutoReqProv:    No

%description -n texlive-animate-doc
Documentation for animate

%package -n texlive-anonchap
Provides:       tex-anonchap = %{tl_version}
License:        LPPL
Summary:        Make chapters be typeset like sections
Version:        svn17049.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(anonchap.sty) = %{tl_version}

%description -n texlive-anonchap
The command \simplechapter sets up the \chapter command not to
number chapters, though they may possibly have a prefix, and a
suffix (the \simplechapterdelim command, which the user may
alter). The \restorechapter command restores the status quo
ante.

%package -n texlive-anonchap-doc
Summary:        Documentation for anonchap
Version:        svn17049.1.1a

Provides:       tex-anonchap-doc
AutoReqProv:    No

%description -n texlive-anonchap-doc
Documentation for anonchap

%package -n texlive-anonymouspro
Provides:       tex-anonymouspro = %{tl_version}
License:        LPPL 1.3
Summary:        Use AnonymousPro fonts with LaTeX
Version:        svn33441.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(kvoptions.sty)
Provides:       tex(AnonymousPro-01.enc) = %{tl_version}
Provides:       tex(AnonymousPro-02.enc) = %{tl_version}
Provides:       tex(AnonymousPro-03.enc) = %{tl_version}
Provides:       tex(AnonymousPro-symbols.enc) = %{tl_version}
Provides:       tex(AnonymousPro.map) = %{tl_version}, tex(AnonymousPro-Bold-01.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Bold-02.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Bold-03.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Bold-Symbols-base.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Bold-Symbols-u.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Bold-base.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Bold-t1.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Bold-ts1.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Bold.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic-01.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic-02.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic-03.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic-Symbols-base.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic-Symbols-u.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic-base.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic-t1.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic-ts1.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-BoldSC-t1.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Italic-01.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Italic-02.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Italic-03.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Italic-Symbols-base.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Italic-Symbols-u.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Italic-base.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Italic-t1.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Italic-ts1.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Italic.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Regular-01.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Regular-02.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Regular-03.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Regular-Symbols-base.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Regular-Symbols-u.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Regular-base.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Regular-t1.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Regular-ts1.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Regular.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-RegularSC-t1.tfm) = %{tl_version}
Provides:       tex(AnonymousPro-Bold.ttf) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic.ttf) = %{tl_version}
Provides:       tex(AnonymousPro-Italic.ttf) = %{tl_version}
Provides:       tex(AnonymousPro-Regular.ttf) = %{tl_version}
Provides:       tex(AnonymousPro-Bold.pfb) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic.pfb) = %{tl_version}
Provides:       tex(AnonymousPro-Italic.pfb) = %{tl_version}
Provides:       tex(AnonymousPro-Regular.pfb) = %{tl_version}
Provides:       tex(AnonymousPro-Bold-Symbols-u.vf) = %{tl_version}
Provides:       tex(AnonymousPro-Bold-t1.vf) = %{tl_version}
Provides:       tex(AnonymousPro-Bold-ts1.vf) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic-Symbols-u.vf) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic-t1.vf) = %{tl_version}
Provides:       tex(AnonymousPro-BoldItalic-ts1.vf) = %{tl_version}
Provides:       tex(AnonymousPro-BoldSC-t1.vf) = %{tl_version}
Provides:       tex(AnonymousPro-Italic-Symbols-u.vf) = %{tl_version}
Provides:       tex(AnonymousPro-Italic-t1.vf) = %{tl_version}
Provides:       tex(AnonymousPro-Italic-ts1.vf) = %{tl_version}
Provides:       tex(AnonymousPro-Regular-Symbols-u.vf) = %{tl_version}
Provides:       tex(AnonymousPro-Regular-t1.vf) = %{tl_version}
Provides:       tex(AnonymousPro-Regular-ts1.vf) = %{tl_version}
Provides:       tex(AnonymousPro-RegularSC-t1.vf) = %{tl_version}
Provides:       tex(AnonymousPro.sty) = %{tl_version}, tex(t1anonymouspro.fd) = %{tl_version}
Provides:       tex(ts1anonymouspro.fd) = %{tl_version}, tex(uanonymouspro.fd) = %{tl_version}

%description -n texlive-anonymouspro
The fonts are a monowidth set, designed for use by coders. They
appear as a set of four TrueType, or Adobe Type 1 font files,
and LaTeX support is also provided.

%package -n texlive-anonymouspro-doc
Summary:        Documentation for anonymouspro
Version:        svn33441.2.1

Provides:       tex-anonymouspro-doc
AutoReqProv:    No

%description -n texlive-anonymouspro-doc
Documentation for anonymouspro

%package -n texlive-answers
Provides:       tex-answers = %{tl_version}
License:        LPPL
Summary:        Setting questions (or exercises) and answers
Version:        svn35032.2.16

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbatim.sty)
Provides:       tex(answers.sty) = %{tl_version}

%description -n texlive-answers
The package allows a lot of flexibility in constructing
question and answer sheets.

%package -n texlive-answers-doc
Summary:        Documentation for answers
Version:        svn35032.2.16

Provides:       tex-answers-doc
AutoReqProv:    No

%description -n texlive-answers-doc
Documentation for answers

%package -n texlive-antiqua
Provides:       tex-antiqua = %{tl_version}
License:        GPL+
Summary:        URW Antiqua condensed font, for use with TeX
Version:        svn24266.001.003

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(uaq.map) = %{tl_version}, tex(uaqr7tc.tfm) = %{tl_version}
Provides:       tex(uaqr8ac.tfm) = %{tl_version}, tex(uaqr8cc.tfm) = %{tl_version}
Provides:       tex(uaqr8rc.tfm) = %{tl_version}, tex(uaqr8tc.tfm) = %{tl_version}
Provides:       tex(uaqrc7tc.tfm) = %{tl_version}, tex(uaqrc8tc.tfm) = %{tl_version}
Provides:       tex(uaqro7tc.tfm) = %{tl_version}, tex(uaqro8cc.tfm) = %{tl_version}
Provides:       tex(uaqro8rc.tfm) = %{tl_version}, tex(uaqro8tc.tfm) = %{tl_version}
Provides:       tex(uaqr8ac.pfb) = %{tl_version}, tex(uaqr7tc.vf) = %{tl_version}
Provides:       tex(uaqr8cc.vf) = %{tl_version}, tex(uaqr8tc.vf) = %{tl_version}
Provides:       tex(uaqrc7tc.vf) = %{tl_version}, tex(uaqrc8tc.vf) = %{tl_version}
Provides:       tex(uaqro7tc.vf) = %{tl_version}, tex(uaqro8cc.vf) = %{tl_version}
Provides:       tex(uaqro8tc.vf) = %{tl_version}, tex(ot1uaq.fd) = %{tl_version}
Provides:       tex(t1uaq.fd) = %{tl_version}, tex(ts1uaq.fd) = %{tl_version}

%description -n texlive-antiqua
The package contains a copy of the Type 1 font "URW Antiqua
2051 Regular Condensed" released under the GPL by URW, with
supporting files for use with (La)TeX.

%package -n texlive-antiqua-doc
Summary:        Documentation for antiqua
Version:        svn24266.001.003

Provides:       tex-antiqua-doc
AutoReqProv:    No

%description -n texlive-antiqua-doc
Documentation for antiqua

%package -n texlive-antomega
Provides:       tex-antomega = %{tl_version}
License:        LPPL
Summary:        Alternative language support for Omega/Lambda
Version:        svn21933.0.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex-omega, tex(keyval.sty), tex(ifthen.sty), tex(calc.sty)
Provides:       tex(antomega.cfg) = %{tl_version}, tex(antomega.sty) = %{tl_version}
Provides:       tex(grhyph16.tex) = %{tl_version}, tex(hyphen.cfg) = %{tl_version}
Provides:       tex(lgc0700.def) = %{tl_version}, tex(lgrenc-antomega.def) = %{tl_version}
Provides:       tex(ograhyph4.tex) = %{tl_version}, tex(ogrmhyph4.tex) = %{tl_version}
Provides:       tex(ogrphyph4.tex) = %{tl_version}, tex(omega-english.ldf) = %{tl_version}
Provides:       tex(omega-french.ldf) = %{tl_version}, tex(omega-german.ldf) = %{tl_version}
Provides:       tex(omega-greek.ldf) = %{tl_version}, tex(omega-latin.ldf) = %{tl_version}
Provides:       tex(omega-latvian.ldf) = %{tl_version}, tex(omega-polish.ldf) = %{tl_version}
Provides:       tex(omega-russian.ldf) = %{tl_version}, tex(omega-spanish.ldf) = %{tl_version}
Provides:       tex(ruhyph16.tex) = %{tl_version}, tex(t1enc-antomega.def) = %{tl_version}
Provides:       tex(t2aenc-antomega.def) = %{tl_version}
Provides:       tex(uni0100.def) = %{tl_version}, tex(uni0370.def) = %{tl_version}
Provides:       tex(uni0400.def) = %{tl_version}, tex(uni1f00.def) = %{tl_version}
Provides:       tex(ut1enc-antomega.def) = %{tl_version}

%description -n texlive-antomega
A language support package for Omega/Lambda. This replaces the
original omega package for use with Lambda, and provides extra
facilities (including Babel-like language switching, which
eases porting of LaTeX documents to Lambda).

%package -n texlive-antomega-doc
Summary:        Documentation for antomega
Version:        svn21933.0.8

Provides:       tex-antomega-doc
AutoReqProv:    No
Requires:       tex-omega-doc

%description -n texlive-antomega-doc
Documentation for antomega


%package -n texlive-antt
Provides:       tex-antt = %{tl_version}
License:        GFSL
Summary:        Antykwa Torunska: a Type 1 family of a Polish traditional type
Version:        svn18651.2.08

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(antt-cs.enc) = %{tl_version}, tex(antt-ec.enc) = %{tl_version}
Provides:       tex(antt-el.enc) = %{tl_version}, tex(antt-ex.enc) = %{tl_version}
Provides:       tex(antt-exp.enc) = %{tl_version}, tex(antt-greek.enc) = %{tl_version}
Provides:       tex(antt-mi.enc) = %{tl_version}, tex(antt-qx.enc) = %{tl_version}
Provides:       tex(antt-rm.enc) = %{tl_version}, tex(antt-sy.enc) = %{tl_version}
Provides:       tex(antt-t2a.enc) = %{tl_version}, tex(antt-t2b.enc) = %{tl_version}
Provides:       tex(antt-t2c.enc) = %{tl_version}, tex(antt-t5.enc) = %{tl_version}
Provides:       tex(antt-texnansi.enc) = %{tl_version}, tex(antt-ts1.enc) = %{tl_version}
Provides:       tex(antt-wncy.enc) = %{tl_version}, tex(anttcap-cs.enc) = %{tl_version}
Provides:       tex(anttcap-ec.enc) = %{tl_version}, tex(anttcap-qx.enc) = %{tl_version}
Provides:       tex(anttcap-t5.enc) = %{tl_version}, tex(anttcap-texnansi.enc) = %{tl_version}
Provides:       tex(antt-cs.map) = %{tl_version}, tex(antt-ec.map) = %{tl_version}
Provides:       tex(antt-el.map) = %{tl_version}, tex(antt-ex.map) = %{tl_version}
Provides:       tex(antt-exp.map) = %{tl_version}, tex(antt-greek.map) = %{tl_version}
Provides:       tex(antt-mi.map) = %{tl_version}, tex(antt-qx.map) = %{tl_version}
Provides:       tex(antt-rm.map) = %{tl_version}, tex(antt-sy.map) = %{tl_version}
Provides:       tex(antt-t2a.map) = %{tl_version}, tex(antt-t2b.map) = %{tl_version}
Provides:       tex(antt-t2c.map) = %{tl_version}, tex(antt-t5.map) = %{tl_version}
Provides:       tex(antt-texnansi.map) = %{tl_version}, tex(antt-ts1.map) = %{tl_version}
Provides:       tex(antt-wncy.map) = %{tl_version}, tex(antt.map) = %{tl_version}
Provides:       tex(AntykwaTorunska-Bold.otf) = %{tl_version}
Provides:       tex(AntykwaTorunska-BoldItalic.otf) = %{tl_version}
Provides:       tex(AntykwaTorunska-Italic.otf) = %{tl_version}
Provides:       tex(AntykwaTorunska-Regular.otf) = %{tl_version}
Provides:       tex(AntykwaTorunskaCond-Bold.otf) = %{tl_version}
Provides:       tex(AntykwaTorunskaCond-BoldItalic.otf) = %{tl_version}
Provides:       tex(AntykwaTorunskaCond-Italic.otf) = %{tl_version}
Provides:       tex(AntykwaTorunskaCond-Regular.otf) = %{tl_version}
Provides:       tex(AntykwaTorunskaCondLight-Italic.otf) = %{tl_version}
Provides:       tex(AntykwaTorunskaCondLight-Regular.otf) = %{tl_version}
Provides:       tex(AntykwaTorunskaCondMed-Italic.otf) = %{tl_version}
Provides:       tex(AntykwaTorunskaCondMed-Regular.otf) = %{tl_version}
Provides:       tex(AntykwaTorunskaLight-Italic.otf) = %{tl_version}
Provides:       tex(AntykwaTorunskaLight-Regular.otf) = %{tl_version}
Provides:       tex(AntykwaTorunskaMed-Italic.otf) = %{tl_version}
Provides:       tex(AntykwaTorunskaMed-Regular.otf) = %{tl_version}
Provides:       tex(cs-anttb.tfm) = %{tl_version}, tex(cs-anttbcap.tfm) = %{tl_version}
Provides:       tex(cs-anttbi.tfm) = %{tl_version}, tex(cs-anttbicap.tfm) = %{tl_version}
Provides:       tex(cs-anttcb.tfm) = %{tl_version}, tex(cs-anttcbcap.tfm) = %{tl_version}
Provides:       tex(cs-anttcbi.tfm) = %{tl_version}, tex(cs-anttcbicap.tfm) = %{tl_version}
Provides:       tex(cs-anttcl.tfm) = %{tl_version}, tex(cs-anttclcap.tfm) = %{tl_version}
Provides:       tex(cs-anttcli.tfm) = %{tl_version}, tex(cs-anttclicap.tfm) = %{tl_version}
Provides:       tex(cs-anttcm.tfm) = %{tl_version}, tex(cs-anttcmcap.tfm) = %{tl_version}
Provides:       tex(cs-anttcmi.tfm) = %{tl_version}, tex(cs-anttcmicap.tfm) = %{tl_version}
Provides:       tex(cs-anttcr.tfm) = %{tl_version}, tex(cs-anttcrcap.tfm) = %{tl_version}
Provides:       tex(cs-anttcri.tfm) = %{tl_version}, tex(cs-anttcricap.tfm) = %{tl_version}
Provides:       tex(cs-anttl.tfm) = %{tl_version}, tex(cs-anttlcap.tfm) = %{tl_version}
Provides:       tex(cs-anttli.tfm) = %{tl_version}, tex(cs-anttlicap.tfm) = %{tl_version}
Provides:       tex(cs-anttm.tfm) = %{tl_version}, tex(cs-anttmcap.tfm) = %{tl_version}
Provides:       tex(cs-anttmi.tfm) = %{tl_version}, tex(cs-anttmicap.tfm) = %{tl_version}
Provides:       tex(cs-anttr.tfm) = %{tl_version}, tex(cs-anttrcap.tfm) = %{tl_version}
Provides:       tex(cs-anttri.tfm) = %{tl_version}, tex(cs-anttricap.tfm) = %{tl_version}
Provides:       tex(ec-anttb.tfm) = %{tl_version}, tex(ec-anttbcap.tfm) = %{tl_version}
Provides:       tex(ec-anttbi.tfm) = %{tl_version}, tex(ec-anttbicap.tfm) = %{tl_version}
Provides:       tex(ec-anttcb.tfm) = %{tl_version}, tex(ec-anttcbcap.tfm) = %{tl_version}
Provides:       tex(ec-anttcbi.tfm) = %{tl_version}, tex(ec-anttcbicap.tfm) = %{tl_version}
Provides:       tex(ec-anttcl.tfm) = %{tl_version}, tex(ec-anttclcap.tfm) = %{tl_version}
Provides:       tex(ec-anttcli.tfm) = %{tl_version}, tex(ec-anttclicap.tfm) = %{tl_version}
Provides:       tex(ec-anttcm.tfm) = %{tl_version}, tex(ec-anttcmcap.tfm) = %{tl_version}
Provides:       tex(ec-anttcmi.tfm) = %{tl_version}, tex(ec-anttcmicap.tfm) = %{tl_version}
Provides:       tex(ec-anttcr.tfm) = %{tl_version}, tex(ec-anttcrcap.tfm) = %{tl_version}
Provides:       tex(ec-anttcri.tfm) = %{tl_version}, tex(ec-anttcricap.tfm) = %{tl_version}
Provides:       tex(ec-anttl.tfm) = %{tl_version}, tex(ec-anttlcap.tfm) = %{tl_version}
Provides:       tex(ec-anttli.tfm) = %{tl_version}, tex(ec-anttlicap.tfm) = %{tl_version}
Provides:       tex(ec-anttm.tfm) = %{tl_version}, tex(ec-anttmcap.tfm) = %{tl_version}
Provides:       tex(ec-anttmi.tfm) = %{tl_version}, tex(ec-anttmicap.tfm) = %{tl_version}
Provides:       tex(ec-anttr.tfm) = %{tl_version}, tex(ec-anttrcap.tfm) = %{tl_version}
Provides:       tex(ec-anttri.tfm) = %{tl_version}, tex(ec-anttricap.tfm) = %{tl_version}
Provides:       tex(el-anttb.tfm) = %{tl_version}, tex(el-anttbi.tfm) = %{tl_version}
Provides:       tex(el-anttcb.tfm) = %{tl_version}, tex(el-anttcbi.tfm) = %{tl_version}
Provides:       tex(el-anttcl.tfm) = %{tl_version}, tex(el-anttcli.tfm) = %{tl_version}
Provides:       tex(el-anttcm.tfm) = %{tl_version}, tex(el-anttcmi.tfm) = %{tl_version}
Provides:       tex(el-anttcr.tfm) = %{tl_version}, tex(el-anttcri.tfm) = %{tl_version}
Provides:       tex(el-anttl.tfm) = %{tl_version}, tex(el-anttli.tfm) = %{tl_version}
Provides:       tex(el-anttm.tfm) = %{tl_version}, tex(el-anttmi.tfm) = %{tl_version}
Provides:       tex(el-anttr.tfm) = %{tl_version}, tex(el-anttri.tfm) = %{tl_version}
Provides:       tex(ex-anttb.tfm) = %{tl_version}, tex(ex-anttcb.tfm) = %{tl_version}
Provides:       tex(ex-anttcl.tfm) = %{tl_version}, tex(ex-anttcm.tfm) = %{tl_version}
Provides:       tex(ex-anttcr.tfm) = %{tl_version}, tex(ex-anttl.tfm) = %{tl_version}
Provides:       tex(ex-anttm.tfm) = %{tl_version}, tex(ex-anttr.tfm) = %{tl_version}
Provides:       tex(exp-anttb.tfm) = %{tl_version}, tex(exp-anttbi.tfm) = %{tl_version}
Provides:       tex(exp-anttcb.tfm) = %{tl_version}, tex(exp-anttcbi.tfm) = %{tl_version}
Provides:       tex(exp-anttcl.tfm) = %{tl_version}, tex(exp-anttcli.tfm) = %{tl_version}
Provides:       tex(exp-anttcm.tfm) = %{tl_version}, tex(exp-anttcmi.tfm) = %{tl_version}
Provides:       tex(exp-anttcr.tfm) = %{tl_version}, tex(exp-anttcri.tfm) = %{tl_version}
Provides:       tex(exp-anttl.tfm) = %{tl_version}, tex(exp-anttli.tfm) = %{tl_version}
Provides:       tex(exp-anttm.tfm) = %{tl_version}, tex(exp-anttmi.tfm) = %{tl_version}
Provides:       tex(exp-anttr.tfm) = %{tl_version}, tex(exp-anttri.tfm) = %{tl_version}
Provides:       tex(greek-anttb.tfm) = %{tl_version}, tex(greek-anttbi.tfm) = %{tl_version}
Provides:       tex(greek-anttcb.tfm) = %{tl_version}, tex(greek-anttcbi.tfm) = %{tl_version}
Provides:       tex(greek-anttcl.tfm) = %{tl_version}, tex(greek-anttcli.tfm) = %{tl_version}
Provides:       tex(greek-anttcm.tfm) = %{tl_version}, tex(greek-anttcmi.tfm) = %{tl_version}
Provides:       tex(greek-anttcr.tfm) = %{tl_version}, tex(greek-anttcri.tfm) = %{tl_version}
Provides:       tex(greek-anttl.tfm) = %{tl_version}, tex(greek-anttli.tfm) = %{tl_version}
Provides:       tex(greek-anttm.tfm) = %{tl_version}, tex(greek-anttmi.tfm) = %{tl_version}
Provides:       tex(greek-anttr.tfm) = %{tl_version}, tex(greek-anttri.tfm) = %{tl_version}
Provides:       tex(mi-anttbi.tfm) = %{tl_version}, tex(mi-anttcbi.tfm) = %{tl_version}
Provides:       tex(mi-anttcli.tfm) = %{tl_version}, tex(mi-anttcmi.tfm) = %{tl_version}
Provides:       tex(mi-anttcri.tfm) = %{tl_version}, tex(mi-anttli.tfm) = %{tl_version}
Provides:       tex(mi-anttmi.tfm) = %{tl_version}, tex(mi-anttri.tfm) = %{tl_version}
Provides:       tex(qx-anttb.tfm) = %{tl_version}, tex(qx-anttbcap.tfm) = %{tl_version}
Provides:       tex(qx-anttbi.tfm) = %{tl_version}, tex(qx-anttbicap.tfm) = %{tl_version}
Provides:       tex(qx-anttcb.tfm) = %{tl_version}, tex(qx-anttcbcap.tfm) = %{tl_version}
Provides:       tex(qx-anttcbi.tfm) = %{tl_version}, tex(qx-anttcbicap.tfm) = %{tl_version}
Provides:       tex(qx-anttcl.tfm) = %{tl_version}, tex(qx-anttclcap.tfm) = %{tl_version}
Provides:       tex(qx-anttcli.tfm) = %{tl_version}, tex(qx-anttclicap.tfm) = %{tl_version}
Provides:       tex(qx-anttcm.tfm) = %{tl_version}, tex(qx-anttcmcap.tfm) = %{tl_version}
Provides:       tex(qx-anttcmi.tfm) = %{tl_version}, tex(qx-anttcmicap.tfm) = %{tl_version}
Provides:       tex(qx-anttcr.tfm) = %{tl_version}, tex(qx-anttcrcap.tfm) = %{tl_version}
Provides:       tex(qx-anttcri.tfm) = %{tl_version}, tex(qx-anttcricap.tfm) = %{tl_version}
Provides:       tex(qx-anttl.tfm) = %{tl_version}, tex(qx-anttlcap.tfm) = %{tl_version}
Provides:       tex(qx-anttli.tfm) = %{tl_version}, tex(qx-anttlicap.tfm) = %{tl_version}
Provides:       tex(qx-anttm.tfm) = %{tl_version}, tex(qx-anttmcap.tfm) = %{tl_version}
Provides:       tex(qx-anttmi.tfm) = %{tl_version}, tex(qx-anttmicap.tfm) = %{tl_version}
Provides:       tex(qx-anttr.tfm) = %{tl_version}, tex(qx-anttrcap.tfm) = %{tl_version}
Provides:       tex(qx-anttri.tfm) = %{tl_version}, tex(qx-anttricap.tfm) = %{tl_version}
Provides:       tex(rm-anttb.tfm) = %{tl_version}, tex(rm-anttbi.tfm) = %{tl_version}
Provides:       tex(rm-anttcb.tfm) = %{tl_version}, tex(rm-anttcbi.tfm) = %{tl_version}
Provides:       tex(rm-anttcl.tfm) = %{tl_version}, tex(rm-anttcli.tfm) = %{tl_version}
Provides:       tex(rm-anttcm.tfm) = %{tl_version}, tex(rm-anttcmi.tfm) = %{tl_version}
Provides:       tex(rm-anttcr.tfm) = %{tl_version}, tex(rm-anttcri.tfm) = %{tl_version}
Provides:       tex(rm-anttl.tfm) = %{tl_version}, tex(rm-anttli.tfm) = %{tl_version}
Provides:       tex(rm-anttm.tfm) = %{tl_version}, tex(rm-anttmi.tfm) = %{tl_version}
Provides:       tex(rm-anttr.tfm) = %{tl_version}, tex(rm-anttri.tfm) = %{tl_version}
Provides:       tex(sy-anttbz.tfm) = %{tl_version}, tex(sy-anttcbz.tfm) = %{tl_version}
Provides:       tex(sy-anttclz.tfm) = %{tl_version}, tex(sy-anttcmz.tfm) = %{tl_version}
Provides:       tex(sy-anttcrz.tfm) = %{tl_version}, tex(sy-anttlz.tfm) = %{tl_version}
Provides:       tex(sy-anttmz.tfm) = %{tl_version}, tex(sy-anttrz.tfm) = %{tl_version}
Provides:       tex(t2a-anttb.tfm) = %{tl_version}, tex(t2a-anttbi.tfm) = %{tl_version}
Provides:       tex(t2a-anttcb.tfm) = %{tl_version}, tex(t2a-anttcbi.tfm) = %{tl_version}
Provides:       tex(t2a-anttcl.tfm) = %{tl_version}, tex(t2a-anttcli.tfm) = %{tl_version}
Provides:       tex(t2a-anttcm.tfm) = %{tl_version}, tex(t2a-anttcmi.tfm) = %{tl_version}
Provides:       tex(t2a-anttcr.tfm) = %{tl_version}, tex(t2a-anttcri.tfm) = %{tl_version}
Provides:       tex(t2a-anttl.tfm) = %{tl_version}, tex(t2a-anttli.tfm) = %{tl_version}
Provides:       tex(t2a-anttm.tfm) = %{tl_version}, tex(t2a-anttmi.tfm) = %{tl_version}
Provides:       tex(t2a-anttr.tfm) = %{tl_version}, tex(t2a-anttri.tfm) = %{tl_version}
Provides:       tex(t2b-anttb.tfm) = %{tl_version}, tex(t2b-anttbi.tfm) = %{tl_version}
Provides:       tex(t2b-anttcb.tfm) = %{tl_version}, tex(t2b-anttcbi.tfm) = %{tl_version}
Provides:       tex(t2b-anttcl.tfm) = %{tl_version}, tex(t2b-anttcli.tfm) = %{tl_version}
Provides:       tex(t2b-anttcm.tfm) = %{tl_version}, tex(t2b-anttcmi.tfm) = %{tl_version}
Provides:       tex(t2b-anttcr.tfm) = %{tl_version}, tex(t2b-anttcri.tfm) = %{tl_version}
Provides:       tex(t2b-anttl.tfm) = %{tl_version}, tex(t2b-anttli.tfm) = %{tl_version}
Provides:       tex(t2b-anttm.tfm) = %{tl_version}, tex(t2b-anttmi.tfm) = %{tl_version}
Provides:       tex(t2b-anttr.tfm) = %{tl_version}, tex(t2b-anttri.tfm) = %{tl_version}
Provides:       tex(t2c-anttb.tfm) = %{tl_version}, tex(t2c-anttbi.tfm) = %{tl_version}
Provides:       tex(t2c-anttcb.tfm) = %{tl_version}, tex(t2c-anttcbi.tfm) = %{tl_version}
Provides:       tex(t2c-anttcl.tfm) = %{tl_version}, tex(t2c-anttcli.tfm) = %{tl_version}
Provides:       tex(t2c-anttcm.tfm) = %{tl_version}, tex(t2c-anttcmi.tfm) = %{tl_version}
Provides:       tex(t2c-anttcr.tfm) = %{tl_version}, tex(t2c-anttcri.tfm) = %{tl_version}
Provides:       tex(t2c-anttl.tfm) = %{tl_version}, tex(t2c-anttli.tfm) = %{tl_version}
Provides:       tex(t2c-anttm.tfm) = %{tl_version}, tex(t2c-anttmi.tfm) = %{tl_version}
Provides:       tex(t2c-anttr.tfm) = %{tl_version}, tex(t2c-anttri.tfm) = %{tl_version}
Provides:       tex(t5-anttb.tfm) = %{tl_version}, tex(t5-anttbcap.tfm) = %{tl_version}
Provides:       tex(t5-anttbi.tfm) = %{tl_version}, tex(t5-anttbicap.tfm) = %{tl_version}
Provides:       tex(t5-anttcb.tfm) = %{tl_version}, tex(t5-anttcbcap.tfm) = %{tl_version}
Provides:       tex(t5-anttcbi.tfm) = %{tl_version}, tex(t5-anttcbicap.tfm) = %{tl_version}
Provides:       tex(t5-anttcl.tfm) = %{tl_version}, tex(t5-anttclcap.tfm) = %{tl_version}
Provides:       tex(t5-anttcli.tfm) = %{tl_version}, tex(t5-anttclicap.tfm) = %{tl_version}
Provides:       tex(t5-anttcm.tfm) = %{tl_version}, tex(t5-anttcmcap.tfm) = %{tl_version}
Provides:       tex(t5-anttcmi.tfm) = %{tl_version}, tex(t5-anttcmicap.tfm) = %{tl_version}
Provides:       tex(t5-anttcr.tfm) = %{tl_version}, tex(t5-anttcrcap.tfm) = %{tl_version}
Provides:       tex(t5-anttcri.tfm) = %{tl_version}, tex(t5-anttcricap.tfm) = %{tl_version}
Provides:       tex(t5-anttl.tfm) = %{tl_version}, tex(t5-anttlcap.tfm) = %{tl_version}
Provides:       tex(t5-anttli.tfm) = %{tl_version}, tex(t5-anttlicap.tfm) = %{tl_version}
Provides:       tex(t5-anttm.tfm) = %{tl_version}, tex(t5-anttmcap.tfm) = %{tl_version}
Provides:       tex(t5-anttmi.tfm) = %{tl_version}, tex(t5-anttmicap.tfm) = %{tl_version}
Provides:       tex(t5-anttr.tfm) = %{tl_version}, tex(t5-anttrcap.tfm) = %{tl_version}
Provides:       tex(t5-anttri.tfm) = %{tl_version}, tex(t5-anttricap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttb.tfm) = %{tl_version}, tex(texnansi-anttbcap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttbi.tfm) = %{tl_version}
Provides:       tex(texnansi-anttbicap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcb.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcbcap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcbi.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcbicap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcl.tfm) = %{tl_version}
Provides:       tex(texnansi-anttclcap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcli.tfm) = %{tl_version}
Provides:       tex(texnansi-anttclicap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcm.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcmcap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcmi.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcmicap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcr.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcrcap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcri.tfm) = %{tl_version}
Provides:       tex(texnansi-anttcricap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttl.tfm) = %{tl_version}, tex(texnansi-anttlcap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttli.tfm) = %{tl_version}
Provides:       tex(texnansi-anttlicap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttm.tfm) = %{tl_version}, tex(texnansi-anttmcap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttmi.tfm) = %{tl_version}
Provides:       tex(texnansi-anttmicap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttr.tfm) = %{tl_version}, tex(texnansi-anttrcap.tfm) = %{tl_version}
Provides:       tex(texnansi-anttri.tfm) = %{tl_version}
Provides:       tex(texnansi-anttricap.tfm) = %{tl_version}
Provides:       tex(ts1-anttb.tfm) = %{tl_version}, tex(ts1-anttbi.tfm) = %{tl_version}
Provides:       tex(ts1-anttcb.tfm) = %{tl_version}, tex(ts1-anttcbi.tfm) = %{tl_version}
Provides:       tex(ts1-anttcl.tfm) = %{tl_version}, tex(ts1-anttcli.tfm) = %{tl_version}
Provides:       tex(ts1-anttcm.tfm) = %{tl_version}, tex(ts1-anttcmi.tfm) = %{tl_version}
Provides:       tex(ts1-anttcr.tfm) = %{tl_version}, tex(ts1-anttcri.tfm) = %{tl_version}
Provides:       tex(ts1-anttl.tfm) = %{tl_version}, tex(ts1-anttli.tfm) = %{tl_version}
Provides:       tex(ts1-anttm.tfm) = %{tl_version}, tex(ts1-anttmi.tfm) = %{tl_version}
Provides:       tex(ts1-anttr.tfm) = %{tl_version}, tex(ts1-anttri.tfm) = %{tl_version}
Provides:       tex(wncy-anttb.tfm) = %{tl_version}, tex(wncy-anttbi.tfm) = %{tl_version}
Provides:       tex(wncy-anttcb.tfm) = %{tl_version}, tex(wncy-anttcbi.tfm) = %{tl_version}
Provides:       tex(wncy-anttcl.tfm) = %{tl_version}, tex(wncy-anttcli.tfm) = %{tl_version}
Provides:       tex(wncy-anttcm.tfm) = %{tl_version}, tex(wncy-anttcmi.tfm) = %{tl_version}
Provides:       tex(wncy-anttcr.tfm) = %{tl_version}, tex(wncy-anttcri.tfm) = %{tl_version}
Provides:       tex(wncy-anttl.tfm) = %{tl_version}, tex(wncy-anttli.tfm) = %{tl_version}
Provides:       tex(wncy-anttm.tfm) = %{tl_version}, tex(wncy-anttmi.tfm) = %{tl_version}
Provides:       tex(wncy-anttr.tfm) = %{tl_version}, tex(wncy-anttri.tfm) = %{tl_version}
Provides:       tex(anttb.pfb) = %{tl_version}, tex(anttbi.pfb) = %{tl_version}
Provides:       tex(anttcb.pfb) = %{tl_version}, tex(anttcbi.pfb) = %{tl_version}
Provides:       tex(anttcl.pfb) = %{tl_version}, tex(anttcli.pfb) = %{tl_version}
Provides:       tex(anttcm.pfb) = %{tl_version}, tex(anttcmi.pfb) = %{tl_version}
Provides:       tex(anttcr.pfb) = %{tl_version}, tex(anttcri.pfb) = %{tl_version}
Provides:       tex(anttl.pfb) = %{tl_version}, tex(anttli.pfb) = %{tl_version}
Provides:       tex(anttm.pfb) = %{tl_version}, tex(anttmi.pfb) = %{tl_version}
Provides:       tex(anttr.pfb) = %{tl_version}, tex(anttri.pfb) = %{tl_version}
Provides:       tex(anttor.sty) = %{tl_version}, tex(antyktor.sty) = %{tl_version}
Provides:       tex(il2antt.fd) = %{tl_version}, tex(il2anttc.fd) = %{tl_version}
Provides:       tex(il2anttl.fd) = %{tl_version}, tex(il2anttlc.fd) = %{tl_version}
Provides:       tex(ly1antt.fd) = %{tl_version}, tex(ly1anttc.fd) = %{tl_version}
Provides:       tex(ly1anttl.fd) = %{tl_version}, tex(ly1anttlc.fd) = %{tl_version}
Provides:       tex(omlantt.fd) = %{tl_version}, tex(omlanttc.fd) = %{tl_version}
Provides:       tex(omlanttl.fd) = %{tl_version}, tex(omlanttlc.fd) = %{tl_version}
Provides:       tex(omsantt.fd) = %{tl_version}, tex(omsanttc.fd) = %{tl_version}
Provides:       tex(omsanttl.fd) = %{tl_version}, tex(omsanttlc.fd) = %{tl_version}
Provides:       tex(omxantt.fd) = %{tl_version}, tex(omxanttc.fd) = %{tl_version}
Provides:       tex(omxanttl.fd) = %{tl_version}, tex(omxanttlc.fd) = %{tl_version}
Provides:       tex(ot1antt.fd) = %{tl_version}, tex(ot1anttc.fd) = %{tl_version}
Provides:       tex(ot1anttcm.fd) = %{tl_version}, tex(ot1anttl.fd) = %{tl_version}
Provides:       tex(ot1anttlc.fd) = %{tl_version}, tex(ot1anttlcm.fd) = %{tl_version}
Provides:       tex(ot1anttlm.fd) = %{tl_version}, tex(ot1anttm.fd) = %{tl_version}
Provides:       tex(ot2antt.fd) = %{tl_version}, tex(ot2anttc.fd) = %{tl_version}
Provides:       tex(ot2anttl.fd) = %{tl_version}, tex(ot2anttlc.fd) = %{tl_version}
Provides:       tex(ot4antt.fd) = %{tl_version}, tex(ot4anttc.fd) = %{tl_version}
Provides:       tex(ot4anttl.fd) = %{tl_version}, tex(ot4anttlc.fd) = %{tl_version}
Provides:       tex(qxantt.fd) = %{tl_version}, tex(qxanttc.fd) = %{tl_version}
Provides:       tex(qxanttl.fd) = %{tl_version}, tex(qxanttlc.fd) = %{tl_version}
Provides:       tex(t1antt.fd) = %{tl_version}, tex(t1anttc.fd) = %{tl_version}
Provides:       tex(t1anttl.fd) = %{tl_version}, tex(t1anttlc.fd) = %{tl_version}
Provides:       tex(t2aantt.fd) = %{tl_version}, tex(t2aanttc.fd) = %{tl_version}
Provides:       tex(t2aanttl.fd) = %{tl_version}, tex(t2aanttlc.fd) = %{tl_version}
Provides:       tex(t2bantt.fd) = %{tl_version}, tex(t2banttc.fd) = %{tl_version}
Provides:       tex(t2banttl.fd) = %{tl_version}, tex(t2banttlc.fd) = %{tl_version}
Provides:       tex(t2cantt.fd) = %{tl_version}, tex(t2canttc.fd) = %{tl_version}
Provides:       tex(t2canttl.fd) = %{tl_version}, tex(t2canttlc.fd) = %{tl_version}
Provides:       tex(t5antt.fd) = %{tl_version}, tex(t5anttc.fd) = %{tl_version}
Provides:       tex(t5anttl.fd) = %{tl_version}, tex(t5anttlc.fd) = %{tl_version}
Provides:       tex(ts1antt.fd) = %{tl_version}, tex(ts1anttc.fd) = %{tl_version}
Provides:       tex(ts1anttl.fd) = %{tl_version}, tex(ts1anttlc.fd) = %{tl_version}
Provides:       tex(antt-math.tex) = %{tl_version}

%description -n texlive-antt
Antykwa Torunska is a serif font designed by the late Polish
typographer Zygfryd Gardzielewski, reconstructed and digitized
as Type 1.

%package -n texlive-antt-doc
Summary:        Documentation for antt
Version:        svn18651.2.08

Provides:       tex-antt-doc
AutoReqProv:    No

%description -n texlive-antt-doc
Documentation for antt

%package -n texlive-anufinalexam-doc
Summary:        Documentation for anufinalexam
Version:        svn26053.0

Provides:       tex-anufinalexam-doc
AutoReqProv:    No

%description -n texlive-anufinalexam-doc
Documentation for anufinalexam

%package -n texlive-anyfontsize
Provides:       tex-anyfontsize = %{tl_version}
License:        LPPL
Summary:        Select any font size in LaTeX
Version:        svn17050.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(anyfontsize.sty) = %{tl_version}

%description -n texlive-anyfontsize
The package allows the to user select any font size (via e.g.
\fontsize{...}{...}\selectfont), even those sizes that are not
listed in the .fd file. If such a size is requested, LaTeX will
search for and select the nearest listed size; anyfontsize will
then scale the font to the size actually requested. Similar
functionality is available for the CM family, for the EC
family, or for either computer modern encoding; the present
package generalises the facility.

%package -n texlive-anyfontsize-doc
Summary:        Documentation for anyfontsize
Version:        svn17050.0

Provides:       tex-anyfontsize-doc
AutoReqProv:    No

%description -n texlive-anyfontsize-doc
Documentation for anyfontsize

%package -n texlive-anysize
Provides:       tex-anysize = %{tl_version}
License:        Public Domain
Summary:        A simple package to set up document margins
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(anysize.sty) = %{tl_version}

%description -n texlive-anysize
This package is considered obsolete; alternatives are the
typearea package from the koma-script bundle, or the geometry
package.

%package -n texlive-anysize-doc
Summary:        Documentation for anysize
Version:        svn15878.0

Provides:       tex-anysize-doc
AutoReqProv:    No

%description -n texlive-anysize-doc
Documentation for anysize

%package -n texlive-aobs-tikz
Provides:       tex-aobs-tikz = %{tl_version}
License:        LPPL 1.3
Summary:        TikZ styles for creating overlaid pictures in beamer
Version:        svn32662.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tikzlibraryoverlay-beamer-styles.code.tex) = %{tl_version}

%description -n texlive-aobs-tikz
The package defines auxiliary TikZ styles useful for overlaying
pictures' elements in Beamer. The TikZ styles are grouped in a
library, overlay-beamer-styles which is automatically called by
the package itself. Users may either load just aobs-tikz or the
library; the latter method necessitates TikZ manual load.

%package -n texlive-aobs-tikz-doc
Summary:        Documentation for aobs-tikz
Version:        svn32662.1.0

Provides:       tex-aobs-tikz-doc
AutoReqProv:    No

%description -n texlive-aobs-tikz-doc
Documentation for aobs-tikz

%package -n texlive-aomart
Provides:       tex-aomart = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset articles for the Annals of Mathematics
Version:        svn46091
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fancyhdr.sty), tex(lastpage.sty), tex(ifpdf.sty), tex(hyperref.sty)
Requires:       tex(yhmath.sty), tex(cmtiup.sty)
Provides:       tex(aomart.cls) = %{tl_version}

%description -n texlive-aomart
The package provides a class for typesetting articles for The
Annals of Mathematics.

%package -n texlive-aomart-doc
Summary:        Documentation for aomart
Version:        svn46091
Provides:       tex-aomart-doc
AutoReqProv:    No

%description -n texlive-aomart-doc
Documentation for aomart

%package -n texlive-apa6e
Provides:       tex-apa6e = %{tl_version}
License:        BSD
Summary:        Format manuscripts to APA 6th edition guidelines
Version:        svn23350.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(times.sty), tex(mathptmx.sty), tex(geometry.sty), tex(ragged2e.sty)
Requires:       tex(fancyhdr.sty), tex(float.sty), tex(caption.sty), tex(ifthen.sty)
Requires:       tex(endnotes.sty), tex(endfloat.sty)
Provides:       tex(apa6e.cls) = %{tl_version}

%description -n texlive-apa6e
This is a minimalist class file for formatting manuscripts in
the style described in the American Psychological Association
(APA) 6th edition guidelines. The apa6 class provides better
coverage of the requirements.

%package -n texlive-apa6e-doc
Summary:        Documentation for apa6e
Version:        svn23350.0.3

Provides:       tex-apa6e-doc
AutoReqProv:    No

%description -n texlive-apa6e-doc
Documentation for apa6e

%package -n texlive-apa6
Provides:       tex-apa6 = %{tl_version}
License:        LPPL 1.3
Summary:        Format documents in APA style (6th edition)
Version:        svn44652
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etoolbox.sty), tex(biblatex.sty), tex(apacite.sty), tex(lmodern.sty)
Requires:       tex(fontenc.sty), tex(draftwatermark.sty)
Requires:       tex(array.sty), tex(longtable.sty), tex(txfonts.sty), tex(pslatex.sty)
Requires:       tex(times.sty), tex(mathptm.sty), tex(geometry.sty), tex(graphicx.sty)
Requires:       tex(booktabs.sty), tex(threeparttable.sty)
Requires:       tex(babel.sty), tex(substr.sty), tex(caption.sty), tex(fancyhdr.sty)
Requires:       tex(bm.sty), tex(endfloat.sty), tex(float.sty), tex(flushend.sty)
Requires:       tex(ftnright.sty)
Provides:       tex(apa6.cls) = %{tl_version}, tex(APAendfloat.cfg) = %{tl_version}

%description -n texlive-apa6
The class formats documents in APA style (6th Edition). It
provides a full set of facilities in three different output
modes (journal-like appearance, double-spaced manuscript, LaTeX-
like document), in contrast to the earlier apa6e, which only
formats double-spaced manuscripts in APA style. The class can
mask author identity for copies for use in masked peer review.
Citations are provided using the apacite bundle; the class
requires that package if citations are to be typeset. The class
is a development of the apa class (which is no longer
maintained).

%package -n texlive-apa6-doc
Summary:        Documentation for apa6
Version:        svn44652
Provides:       tex-apa6-doc
AutoReqProv:    No

%description -n texlive-apa6-doc
Documentation for apa6

%package -n texlive-apacite
Provides:       tex-apacite = %{tl_version}
License:        LPPL
Summary:        Citation style following the rules of the APA
Version:        svn31264.6.03

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(natbib.sty), tex(index.sty), tex(multicol.sty)
Provides:       tex(apacdoc.sty) = %{tl_version}, tex(apacite.sty) = %{tl_version}

%description -n texlive-apacite
Apacite provides a BibTeX style and a LaTeX package which are
designed to match the requirements of the American
Psychological Association's style for citations. The package
follows the 6th edition of the APA manual, and is designed to
work with the apa6 class. A test document is provided. The
package is compatible with chapterbib and (to some extent) with
hyperref (for limits of compatibility, see the documentation).
The package also includes a means of generating an author index
for a document.

%package -n texlive-apacite-doc
Summary:        Documentation for apacite
Version:        svn31264.6.03

Provides:       tex-apacite-doc
AutoReqProv:    No

%description -n texlive-apacite-doc
Documentation for apacite

%package -n texlive-apalike2
Provides:       tex-apalike2 = %{tl_version}
License:        Knuth
Summary:        Bibliography style that approaches APA requirements
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-apalike2
Described as a "local adaptation" of apalike (which is part of
the base bibtex distribution).

%package -n texlive-apa
Provides:       tex-apa = %{tl_version}
License:        LPPL
Summary:        American Psychological Association format
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(longtable.sty), tex(txfonts.sty), tex(pslatex.sty), tex(times.sty)
Requires:       tex(mathptm.sty), tex(babel.sty), tex(apacite.sty), tex(fancyhdr.sty)
Requires:       tex(bm.sty), tex(endnotes.sty), tex(endfloat.sty), tex(flushend.sty)
Requires:       tex(ftnright.sty)
Provides:       tex(apa.cls) = %{tl_version}

%description -n texlive-apa
A LaTeX class to format text according to the American
Psychological Association Publication Manual (5th ed.)
specifications for manuscripts or to the APA journal look found
in journals like the Journal of Experimental Psychology etc. In
addition, it provides regular LaTeX-like output with a few
enhancements and APA-motivated changes. Note that the apa6
(covering the 6th edition of the manual) is now commonly in
use. Apacite, which used to work with this class, has now been
updated for use with apa6.

%package -n texlive-apa-doc
Summary:        Documentation for apa
Version:        svn42428
Provides:       tex-apa-doc
AutoReqProv:    No

%description -n texlive-apa-doc
Documentation for apa

%package -n texlive-apnum
Provides:       tex-apnum = %{tl_version}
License:        Public Domain
Summary:        Arbitrary precision numbers implemented by TeX macros
Version:        svn47510
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(apnum.tex) = %{tl_version}

%description -n texlive-apnum
The basic operations (addition, subtraction, multiplication,
division, power to an integer) are implemented by TeX macros in
this package. Operands may be numbers with arbitrary numbers of
digits; scientific notation is allowed. The expression scanner
is also provided. Exhaustive documentation (including detailed
TeXnical documentation) is included. The macro includes many
optimizations and uses only TeX primitives (from classic TeX)
and \newcount macro.

%package -n texlive-apnum-doc
Summary:        Documentation for apnum
Version:        svn47510

Provides:       tex-apnum-doc
AutoReqProv:    No

%description -n texlive-apnum-doc
Documentation for apnum

%package -n texlive-appendixnumberbeamer
Provides:       tex-appendixnumberbeamer = %{tl_version}
License:        GPLv3+
Summary:        Manage frame numbering in appendixes in beamer
Version:        svn46317
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(appendixnumberbeamer.sty) = %{tl_version}

%description -n texlive-appendixnumberbeamer
The package arranges that an appendix in a beamer presentation
is not counted in the frame count of the presentation;
appendixes are numbered starting from one.

%package -n texlive-appendixnumberbeamer-doc
Summary:        Documentation for appendixnumberbeamer
Version:        svn46317
Provides:       tex-appendixnumberbeamer-doc
AutoReqProv:    No

%description -n texlive-appendixnumberbeamer-doc
Documentation for appendixnumberbeamer

%package -n texlive-appendix
Provides:       tex-appendix = %{tl_version}
License:        LPPL
Summary:        Extra control of appendices
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(appendix.sty) = %{tl_version}

%description -n texlive-appendix
The appendix package provides various ways of formatting the
titles of appendices. Also (sub)appendices environments are
provided that can be used, for example, for per chapter/section
appendices. The word 'Appendix' or similar can be prepended to
the appendix number for article class documents. The word
'Appendices' or similar can be added to the table of contents
before the appendices are listed. The word 'Appendices' or
similar can be typeset as a \part-like heading (page) in the
body. An appendices environment is provided which can be used
instead of the \appendix command.

%package -n texlive-appendix-doc
Summary:        Documentation for appendix
Version:        svn42428
Provides:       tex-appendix-doc
AutoReqProv:    No

%description -n texlive-appendix-doc
Documentation for appendix

%package -n texlive-apprends-latex-doc
Summary:        Documentation for apprends-latex
Version:        svn19306.4.02

Provides:       tex-apprends-latex-doc
AutoReqProv:    No

%description -n texlive-apprends-latex-doc
Documentation for apprends-latex

%package -n texlive-apptools
Provides:       tex-apptools = %{tl_version}
License:        LPPL 1.3
Summary:        Tools for customising appendices
Version:        svn28400.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(apptools.sty) = %{tl_version}

%description -n texlive-apptools
The package provides an \AtAppendix command to add code to a
hook that is executed when \appendix is called by the user.
Additionally, a TeX conditional \ifappendix and a LaTeX-style
conditional \IfAppendix are provided to check if \appendix has
already been called.

%package -n texlive-apptools-doc
Summary:        Documentation for apptools
Version:        svn28400.1.0

Provides:       tex-apptools-doc
AutoReqProv:    No

%description -n texlive-apptools-doc
Documentation for apptools

%package -n texlive-arabi
Provides:       tex-arabi = %{tl_version}
License:        LPPL
Summary:        (La)TeX support for Arabic and Farsi, compliant with Babel
Version:        svn44662
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(amssymb.sty)
Requires:       tex(inputenc.sty), tex(ifthen.sty), tex(pstricks.sty), tex(pst-3d.sty)
Requires:       tex(multido.sty), tex(fp.sty), tex(pst-key.sty), tex(babel.sty)
Requires:       tex(pst-grad.sty), tex(pifont.sty)
Provides:       tex(ararabeyes.enc) = %{tl_version}, tex(ardtpnaskh.enc) = %{tl_version}
Provides:       tex(ardtpthuluth.enc) = %{tl_version}, tex(armonotype.enc) = %{tl_version}
Provides:       tex(aromega.enc) = %{tl_version}, tex(arsimplified.enc) = %{tl_version}
Provides:       tex(arunicode.enc) = %{tl_version}, tex(farsitex.enc) = %{tl_version}
Provides:       tex(farsiwebencoding.enc) = %{tl_version}
Provides:       tex(frmonotype.enc) = %{tl_version}, tex(frsimple.enc) = %{tl_version}
Provides:       tex(frsimplified.enc) = %{tl_version}, tex(frunicode.enc) = %{tl_version}
Provides:       tex(arabi.map) = %{tl_version}, tex(ae_almohanad_xxbold.tfm) = %{tl_version}
Provides:       tex(ae_alyermook.tfm) = %{tl_version}, tex(ae_arab.tfm) = %{tl_version}
Provides:       tex(ae_tholoth.tfm) = %{tl_version}, tex(aealbattar.tfm) = %{tl_version}
Provides:       tex(aealmateen.tfm) = %{tl_version}, tex(aealmohanadb.tfm) = %{tl_version}
Provides:       tex(aealmohanadbolditalic.tfm) = %{tl_version}
Provides:       tex(aealmothnna.tfm) = %{tl_version}, tex(aealyermook.tfm) = %{tl_version}
Provides:       tex(aearab.tfm) = %{tl_version}, tex(aecortoba.tfm) = %{tl_version}
Provides:       tex(aedimnah.tfm) = %{tl_version}, tex(aefurat.tfm) = %{tl_version}
Provides:       tex(aegranada.tfm) = %{tl_version}, tex(aegraph.tfm) = %{tl_version}
Provides:       tex(aehani.tfm) = %{tl_version}, tex(aehor.tfm) = %{tl_version}
Provides:       tex(aekayrawan.tfm) = %{tl_version}, tex(aekhalid.tfm) = %{tl_version}
Provides:       tex(aemashq.tfm) = %{tl_version}, tex(aemetal.tfm) = %{tl_version}
Provides:       tex(aenada.tfm) = %{tl_version}, tex(aenagham.tfm) = %{tl_version}
Provides:       tex(aenice.tfm) = %{tl_version}, tex(aeostorah.tfm) = %{tl_version}
Provides:       tex(aeouhod.tfm) = %{tl_version}, tex(aepetra.tfm) = %{tl_version}
Provides:       tex(aerehan.tfm) = %{tl_version}, tex(aesalem.tfm) = %{tl_version}
Provides:       tex(aeshado.tfm) = %{tl_version}, tex(aesharjah.tfm) = %{tl_version}
Provides:       tex(aesindibad.tfm) = %{tl_version}, tex(aetarablus.tfm) = %{tl_version}
Provides:       tex(aetholoth.tfm) = %{tl_version}, tex(homa.tfm) = %{tl_version}
Provides:       tex(nazli.tfm) = %{tl_version}, tex(nazlib.tfm) = %{tl_version}
Provides:       tex(nazlibout.tfm) = %{tl_version}, tex(nazliout.tfm) = %{tl_version}
Provides:       tex(titr.tfm) = %{tl_version}, tex(titrout.tfm) = %{tl_version}
Provides:       tex(ae_albattar.pfb) = %{tl_version}, tex(ae_almateen.pfb) = %{tl_version}
Provides:       tex(ae_almohanad_bold.pfb) = %{tl_version}
Provides:       tex(ae_almohanad_boldItalitalic.pfb) = %{tl_version}
Provides:       tex(ae_almohanad_thin.pfb) = %{tl_version}
Provides:       tex(ae_almohanad_xxbold.pfb) = %{tl_version}
Provides:       tex(ae_almothnna.pfb) = %{tl_version}, tex(ae_alyermook.pfb) = %{tl_version}
Provides:       tex(ae_arab.pfb) = %{tl_version}, tex(ae_cortoba.pfb) = %{tl_version}
Provides:       tex(ae_dimnah.pfb) = %{tl_version}, tex(ae_furat.pfb) = %{tl_version}
Provides:       tex(ae_granada.pfb) = %{tl_version}, tex(ae_graph.pfb) = %{tl_version}
Provides:       tex(ae_hani.pfb) = %{tl_version}, tex(ae_hor.pfb) = %{tl_version}
Provides:       tex(ae_kayrawan.pfb) = %{tl_version}, tex(ae_khalid.pfb) = %{tl_version}
Provides:       tex(ae_mashq.pfb) = %{tl_version}, tex(ae_metal.pfb) = %{tl_version}
Provides:       tex(ae_nada.pfb) = %{tl_version}, tex(ae_nagham.pfb) = %{tl_version}
Provides:       tex(ae_nice.pfb) = %{tl_version}, tex(ae_ostorah.pfb) = %{tl_version}
Provides:       tex(ae_ouhod.pfb) = %{tl_version}, tex(ae_petra.pfb) = %{tl_version}
Provides:       tex(ae_rehan.pfb) = %{tl_version}, tex(ae_salem.pfb) = %{tl_version}
Provides:       tex(ae_shado.pfb) = %{tl_version}, tex(ae_sharjah.pfb) = %{tl_version}
Provides:       tex(ae_sindibad.pfb) = %{tl_version}, tex(ae_tarablus.pfb) = %{tl_version}
Provides:       tex(ae_tholoth.pfb) = %{tl_version}, tex(homa.pfb) = %{tl_version}
Provides:       tex(nazli.pfb) = %{tl_version}, tex(nazlib.pfb) = %{tl_version}
Provides:       tex(titr.pfb) = %{tl_version}, tex(8859-6.def) = %{tl_version}
Provides:       tex(PPRarabic.sty) = %{tl_version}, tex(arabi4ht.cfg) = %{tl_version}
Provides:       tex(arabic.cfg) = %{tl_version}, tex(arabic.ldf) = %{tl_version}
Provides:       tex(arabicfnt.sty) = %{tl_version}, tex(arabicore.sty) = %{tl_version}
Provides:       tex(arabiftoday.sty) = %{tl_version}, tex(arabnovowel.sty) = %{tl_version}
Provides:       tex(arfonts.sty) = %{tl_version}, tex(ARfonts.sty) = %{tl_version}
Provides:       tex(calendrierfpar.sty) = %{tl_version}, tex(calendrierfpmodified.sty) = %{tl_version}
Provides:       tex(cp1256.def) = %{tl_version}, tex(farsi.ldf) = %{tl_version}
Provides:       tex(farsifnt.sty) = %{tl_version}, tex(fmultico.sty) = %{tl_version}
Provides:       tex(fnum.sty) = %{tl_version}, tex(frfonts.sty) = %{tl_version}
Provides:       tex(FRfonts.sty) = %{tl_version}, tex(haparabica.sty) = %{tl_version}
Provides:       tex(HAPArabica.sty) = %{tl_version}, tex(laeaealbattar.fd) = %{tl_version}
Provides:       tex(laeaealmateen.fd) = %{tl_version}, tex(laeaealmohanadb.fd) = %{tl_version}
Provides:       tex(laeaealmothnna.fd) = %{tl_version}, tex(laeaealyermook.fd) = %{tl_version}
Provides:       tex(laeaearab.fd) = %{tl_version}, tex(laeaecortoba.fd) = %{tl_version}
Provides:       tex(laeaedimnah.fd) = %{tl_version}, tex(laeaefurat.fd) = %{tl_version}
Provides:       tex(laeaegranada.fd) = %{tl_version}, tex(laeaegraph.fd) = %{tl_version}
Provides:       tex(laeaehani.fd) = %{tl_version}, tex(laeaehor.fd) = %{tl_version}
Provides:       tex(laeaekayrawan.fd) = %{tl_version}, tex(laeaekhalid.fd) = %{tl_version}
Provides:       tex(laeaemashq.fd) = %{tl_version}, tex(laeaemetal.fd) = %{tl_version}
Provides:       tex(laeaenada.fd) = %{tl_version}, tex(laeaenagham.fd) = %{tl_version}
Provides:       tex(laeaenice.fd) = %{tl_version}, tex(laeaeostorah.fd) = %{tl_version}
Provides:       tex(laeaeouhod.fd) = %{tl_version}, tex(laeaepetra.fd) = %{tl_version}
Provides:       tex(laeaerehan.fd) = %{tl_version}, tex(laeaesalem.fd) = %{tl_version}
Provides:       tex(laeaeshado.fd) = %{tl_version}, tex(laeaesharjah.fd) = %{tl_version}
Provides:       tex(laeaesindibad.fd) = %{tl_version}, tex(laeaetarablus.fd) = %{tl_version}
Provides:       tex(laeaetholoth.fd) = %{tl_version}, tex(laeandlso.fd) = %{tl_version}
Provides:       tex(laeararial.fd) = %{tl_version}, tex(laearcour.fd) = %{tl_version}
Provides:       tex(laearomega.fd) = %{tl_version}, tex(laearsimpo.fd) = %{tl_version}
Provides:       tex(laeartimes.fd) = %{tl_version}, tex(laeasv.fd) = %{tl_version}
Provides:       tex(laecmr.fd) = %{tl_version}, tex(laecmss.fd) = %{tl_version}
Provides:       tex(laecmtt.fd) = %{tl_version}, tex(laedthuluth.fd) = %{tl_version}
Provides:       tex(laedtpn.fd) = %{tl_version}, tex(laedtpnsp.fd) = %{tl_version}
Provides:       tex(laeenc.def) = %{tl_version}, tex(laekacstbook.fd) = %{tl_version}
Provides:       tex(laemaghribi.fd) = %{tl_version}, tex(laenaskhi.fd) = %{tl_version}
Provides:       tex(laereqaa.fd) = %{tl_version}, tex(laetraditionalarabic.fd) = %{tl_version}
Provides:       tex(lagally.sty) = %{tl_version}, tex(lfecmr.fd) = %{tl_version}
Provides:       tex(lfecmss.fd) = %{tl_version}, tex(lfecmtt.fd) = %{tl_version}
Provides:       tex(lfeelham.fd) = %{tl_version}, tex(lfeenc.def) = %{tl_version}
Provides:       tex(lfefandlso.fd) = %{tl_version}, tex(lfefarsismpl.fd) = %{tl_version}
Provides:       tex(lfefrarial.fd) = %{tl_version}, tex(lfefrtimes.fd) = %{tl_version}
Provides:       tex(lfeftraditionalarabic.fd) = %{tl_version}
Provides:       tex(lfehoma.fd) = %{tl_version}, tex(lfekoodak.fd) = %{tl_version}
Provides:       tex(lfenazli.fd) = %{tl_version}, tex(lfenazliout.fd) = %{tl_version}
Provides:       tex(lferoya.fd) = %{tl_version}, tex(lfesmplarabic.fd) = %{tl_version}
Provides:       tex(lfeterafik.fd) = %{tl_version}, tex(lfetitr.fd) = %{tl_version}
Provides:       tex(lfetitrout.fd) = %{tl_version}, tex(mosq.def) = %{tl_version}
Provides:       tex(poetry.sty) = %{tl_version}, tex(puenc-ar.def) = %{tl_version}
Provides:       tex(transcmr.fd) = %{tl_version}, tex(translit.sty) = %{tl_version}

%description -n texlive-arabi
The package provides an Arabic and Farsi script support for TeX
without the need of any external pre-processor, and in a way
that is compatible with babel. The bi-directional capability
supposes that the user has a TeX engine that knows the four
primitives \beginR, \endR, \beginL and \endL. That is the case
in both the TeX--XeT and e-TeX engines. Arabi will accept input
in several 8-bit encodings, including UTF-8. Arabi can make use
of a wide variety of Arabic and Farsi fonts, and provides one
of its own. PDF files generated using Arabi may be searched,
and text may be copied from them and pasted elsewhere.

%package -n texlive-arabi-doc
Summary:        Documentation for arabi
Version:        svn44662
Provides:       tex-arabi-doc
AutoReqProv:    No

%description -n texlive-arabi-doc
Documentation for arabi

%package -n texlive-arabtex
Provides:       tex-arabtex = %{tl_version}
License:        LPPL
Summary:        Macros and fonts for typesetting Arabic
Version:        svn25711.3.17

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(arabtex.map) = %{tl_version}, tex(hcaption.tfm) = %{tl_version}
Provides:       tex(hclassic.tfm) = %{tl_version}, tex(nash14.tfm) = %{tl_version}
Provides:       tex(nash14bf.tfm) = %{tl_version}, tex(xnsh14.tfm) = %{tl_version}
Provides:       tex(xnsh14bf.tfm) = %{tl_version}, tex(yarborn.tfm) = %{tl_version}
Provides:       tex(hcaption-4.pfb) = %{tl_version}, tex(hclassic-4.pfb) = %{tl_version}
Provides:       tex(xnsh14.pfb) = %{tl_version}, tex(xnsh14bf.pfb) = %{tl_version}
Provides:       tex(Uxnsh.fd) = %{tl_version}, tex(abidir.sty) = %{tl_version}
Provides:       tex(abjad.sty) = %{tl_version}, tex(aboxes.sty) = %{tl_version}
Provides:       tex(acjk.sty) = %{tl_version}, tex(acmd.sty) = %{tl_version}
Provides:       tex(aconfig.sty) = %{tl_version}, tex(aedpatch.sty) = %{tl_version}
Provides:       tex(afonts.sty) = %{tl_version}, tex(afonts0.sty) = %{tl_version}
Provides:       tex(afonts1.sty) = %{tl_version}, tex(afonts2.sty) = %{tl_version}
Provides:       tex(afoot.sty) = %{tl_version}, tex(alatex.sty) = %{tl_version}
Provides:       tex(aligs.sty) = %{tl_version}, tex(alists.sty) = %{tl_version}
Provides:       tex(alocal.sty) = %{tl_version}, tex(altxext.sty) = %{tl_version}
Provides:       tex(amac.sty) = %{tl_version}, tex(aoutput.sty) = %{tl_version}
Provides:       tex(aparse.sty) = %{tl_version}, tex(apatch.sty) = %{tl_version}
Provides:       tex(arababel.sty) = %{tl_version}, tex(arabart.cls) = %{tl_version}
Provides:       tex(arabaux.sty) = %{tl_version}, tex(arabbook.cls) = %{tl_version}
Provides:       tex(arabchrs.sty) = %{tl_version}, tex(arabext.sty) = %{tl_version}
Provides:       tex(arabrep.cls) = %{tl_version}, tex(arabrep1.cls) = %{tl_version}
Provides:       tex(arabskel.sty) = %{tl_version}, tex(arabsymb.sty) = %{tl_version}
Provides:       tex(arabtex-doc.tex) = %{tl_version}, tex(arabtex.sty) = %{tl_version}
Provides:       tex(arabtex.tex) = %{tl_version}, tex(arabtoks.sty) = %{tl_version}
Provides:       tex(arwindoc.tex) = %{tl_version}, tex(ascan.sty) = %{tl_version}
Provides:       tex(asect.sty) = %{tl_version}, tex(asize10.clo) = %{tl_version}
Provides:       tex(asize11.clo) = %{tl_version}, tex(asize12.clo) = %{tl_version}
Provides:       tex(asmo449.sty) = %{tl_version}, tex(asmo449a.sty) = %{tl_version}
Provides:       tex(atabg.sty) = %{tl_version}, tex(atrans.sty) = %{tl_version}
Provides:       tex(awrite.sty) = %{tl_version}, tex(bhs.sty) = %{tl_version}
Provides:       tex(bhslabel.sty) = %{tl_version}, tex(buck.sty) = %{tl_version}
Provides:       tex(captions.def) = %{tl_version}, tex(cp1256.sty) = %{tl_version}
Provides:       tex(etrans.sty) = %{tl_version}, tex(gedalin.sty) = %{tl_version}
Provides:       tex(guha.tex) = %{tl_version}, tex(hebchrs.sty) = %{tl_version}
Provides:       tex(hebsymb.sty) = %{tl_version}, tex(hebtex.sty) = %{tl_version}
Provides:       tex(hebtex.tex) = %{tl_version}, tex(hecmd.sty) = %{tl_version}
Provides:       tex(hefonts.sty) = %{tl_version}, tex(hefonts0.sty) = %{tl_version}
Provides:       tex(hefonts1.sty) = %{tl_version}, tex(hefonts2.sty) = %{tl_version}
Provides:       tex(heparse.sty) = %{tl_version}, tex(hepatch.sty) = %{tl_version}
Provides:       tex(hescan.sty) = %{tl_version}, tex(hetrans.sty) = %{tl_version}
Provides:       tex(hewrite.sty) = %{tl_version}, tex(hmac.sty) = %{tl_version}
Provides:       tex(isiri.sty) = %{tl_version}, tex(iso88596.sty) = %{tl_version}
Provides:       tex(kashmiri.tex) = %{tl_version}, tex(ligtable.tex) = %{tl_version}
Provides:       tex(malay.tex) = %{tl_version}, tex(nashbf.sty) = %{tl_version}
Provides:       tex(omar.tex) = %{tl_version}, tex(raw.sty) = %{tl_version}
Provides:       tex(saw.sty) = %{tl_version}, tex(sindhi.tex) = %{tl_version}
Provides:       tex(sotoku.sty) = %{tl_version}, tex(twoblks.sty) = %{tl_version}
Provides:       tex(uheb.fd) = %{tl_version}, tex(uighur.tex) = %{tl_version}
Provides:       tex(unash.fd) = %{tl_version}, tex(utf8.sty) = %{tl_version}
Provides:       tex(utfcode.sty) = %{tl_version}, tex(verses.sty) = %{tl_version}
Provides:       tex(witbhs.sty) = %{tl_version}, tex(xarbskel.sty) = %{tl_version}
Provides:       tex(xarbsymb.sty) = %{tl_version}, tex(yiddish.sty) = %{tl_version}

%description -n texlive-arabtex
ArabTeX is a package extending the capabilities of TeX/LaTeX to
generate Arabic and Hebrew text. Input may be in ASCII
transliteration or other encodings (including UTF-8); output
may be Arabic, Hebrew, or any of several languages that use the
Arabic script. ArabTeX consists of a TeX macro package and
Arabic and Hebrew fonts (provided both in Metafont format and
Adobe Type 1). The Arabic font is presently only available in
the Naskhi style. ArabTeX will run with Plain TeX and also with
LaTeX.

%package -n texlive-arabtex-doc
Summary:        Documentation for arabtex
Version:        svn25711.3.17

Provides:       tex-arabtex-doc
AutoReqProv:    No

%description -n texlive-arabtex-doc
Documentation for arabtex

%package -n texlive-arabxetex
Provides:       tex-arabxetex = %{tl_version}
License:        LPPL
Summary:        An ArabTeX-like interface for XeLaTeX
Version:        svn38299.1.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(fontspec.sty), tex(bidi.sty)
Provides:       tex(arabicdigits.map) = %{tl_version}, tex(arabtex-farsi-fullvoc.map) = %{tl_version}
Provides:       tex(arabtex-farsi-novoc.map) = %{tl_version}
Provides:       tex(arabtex-farsi-trans-loc.map) = %{tl_version}
Provides:       tex(arabtex-farsi-voc.map) = %{tl_version}
Provides:       tex(arabtex-fullvoc.map) = %{tl_version}
Provides:       tex(arabtex-kashmiri-fullvoc.map) = %{tl_version}
Provides:       tex(arabtex-kashmiri-novoc.map) = %{tl_version}
Provides:       tex(arabtex-kashmiri-voc.map) = %{tl_version}
Provides:       tex(arabtex-kurdish.map) = %{tl_version}
Provides:       tex(arabtex-maghribi-fullvoc.map) = %{tl_version}
Provides:       tex(arabtex-maghribi-novoc.map) = %{tl_version}
Provides:       tex(arabtex-maghribi-voc.map) = %{tl_version}
Provides:       tex(arabtex-malay-fullvoc.map) = %{tl_version}
Provides:       tex(arabtex-malay-novoc.map) = %{tl_version}
Provides:       tex(arabtex-malay-voc.map) = %{tl_version}
Provides:       tex(arabtex-novoc.map) = %{tl_version}, tex(arabtex-pashto-fullvoc.map) = %{tl_version}
Provides:       tex(arabtex-pashto-novoc.map) = %{tl_version}
Provides:       tex(arabtex-pashto-trans-loc.map) = %{tl_version}
Provides:       tex(arabtex-pashto-voc.map) = %{tl_version}
Provides:       tex(arabtex-sindhi-fullvoc.map) = %{tl_version}
Provides:       tex(arabtex-sindhi-novoc.map) = %{tl_version}
Provides:       tex(arabtex-sindhi-trans-loc.map) = %{tl_version}
Provides:       tex(arabtex-sindhi-voc.map) = %{tl_version}
Provides:       tex(arabtex-trans-dmg.map) = %{tl_version}
Provides:       tex(arabtex-trans-loc.map) = %{tl_version}
Provides:       tex(arabtex-turk-fullvoc.map) = %{tl_version}
Provides:       tex(arabtex-turk-novoc.map) = %{tl_version}
Provides:       tex(arabtex-turk-voc.map) = %{tl_version}
Provides:       tex(arabtex-uighur.map) = %{tl_version}, tex(arabtex-urdu-fullvoc.map) = %{tl_version}
Provides:       tex(arabtex-urdu-novoc.map) = %{tl_version}
Provides:       tex(arabtex-urdu-trans-loc.map) = %{tl_version}
Provides:       tex(arabtex-urdu-voc.map) = %{tl_version}
Provides:       tex(arabtex-voc.map) = %{tl_version}, tex(farsidigits.map) = %{tl_version}
Provides:       tex(fixlamalif.map) = %{tl_version}, tex(mirrorpunct.map) = %{tl_version}
Provides:       tex(arabxetex.sty) = %{tl_version}

%description -n texlive-arabxetex
ArabXeTeX provides a convenient ArabTeX-like user-interface for
typesetting languages using the Arabic script in XeLaTeX, with
flexible access to font features. Input in ArabTeX notation can
be set in three different vocalization modes or in roman
transliteration. Direct UTF-8 input is also supported. The
parsing and converting of ArabTeX input to Unicode is done by
means of TECkit mappings. Version 1.0 provides support for
Arabic, Maghribi Arabic, Farsi (Persian), Urdu, Sindhi,
Kashmiri, Ottoman Turkish, Kurdish, Jawi (Malay) and Uighur.
The documentation covers topics such as typesetting the Holy
Quran and typesetting bidirectional critical editions with the
package ednotes.

%package -n texlive-arabxetex-doc
Summary:        Documentation for arabxetex
Version:        svn38299.1.2.1

Provides:       tex-arabxetex-doc
AutoReqProv:    No

%description -n texlive-arabxetex-doc
Documentation for arabxetex

%package -n texlive-aramaic-serto
Provides:       tex-aramaic-serto = %{tl_version}
License:        LPPL 1.3
Summary:        Fonts and LaTeX for Syriac written in Serto
Version:        svn30042.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(syriac.map) = %{tl_version}, tex(assy.tfm) = %{tl_version}
Provides:       tex(assyrb10.tfm) = %{tl_version}, tex(serto10.tfm) = %{tl_version}
Provides:       tex(sertob10.tfm) = %{tl_version}, tex(assy.pfb) = %{tl_version}
Provides:       tex(assyrb10.pfb) = %{tl_version}, tex(serto10.pfb) = %{tl_version}
Provides:       tex(sertob10.pfb) = %{tl_version}, tex(assyr.sty) = %{tl_version}
Provides:       tex(serto.sty) = %{tl_version}, tex(syriac.sty) = %{tl_version}
Provides:       tex(uassyr.fd) = %{tl_version}, tex(userto.fd) = %{tl_version}

%description -n texlive-aramaic-serto
This package enables (La)TeX users to typeset words or phrases
(e-TeX extensions are needed) in Syriac (Aramaic) using the
Serto-alphabet. The package includes a preprocessor written in
Python (>= 1.5.2) in order to deal with right-to-left
typesetting for those who do not want to use elatex and to
choose the correct letter depending on word context
(initial/medial/final form). Detailed documentation and
examples are included.

%package -n texlive-aramaic-serto-doc
Summary:        Documentation for aramaic-serto
Version:        svn30042.1.0

Provides:       tex-aramaic-serto-doc
AutoReqProv:    No

%description -n texlive-aramaic-serto-doc
Documentation for aramaic-serto

%package -n texlive-archaic
Provides:       tex-archaic = %{tl_version}
License:        LPPL
Summary:        A collection of archaic fonts
Version:        svn38005.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(aramaic.map) = %{tl_version}, tex(archaicprw.map) = %{tl_version}
Provides:       tex(cypriot.map) = %{tl_version}, tex(etruscan.map) = %{tl_version}
Provides:       tex(fut10.map) = %{tl_version}, tex(greek4cbc.map) = %{tl_version}
Provides:       tex(greek6cbc.map) = %{tl_version}, tex(hieroglf.map) = %{tl_version}
Provides:       tex(linearb.map) = %{tl_version}, tex(nabatean.map) = %{tl_version}
Provides:       tex(oands.map) = %{tl_version}, tex(oldprsn.map) = %{tl_version}
Provides:       tex(phoenician.map) = %{tl_version}, tex(protosem.map) = %{tl_version}
Provides:       tex(sarabian.map) = %{tl_version}, tex(ugarite.map) = %{tl_version}
Provides:       tex(aram10.tfm) = %{tl_version}, tex(copsn10.tfm) = %{tl_version}
Provides:       tex(cugar10.tfm) = %{tl_version}, tex(cypr10.tfm) = %{tl_version}
Provides:       tex(etr10.tfm) = %{tl_version}, tex(fut10.tfm) = %{tl_version}
Provides:       tex(givbc10.tfm) = %{tl_version}, tex(gvibc10.tfm) = %{tl_version}
Provides:       tex(linb10.tfm) = %{tl_version}, tex(nab10.tfm) = %{tl_version}
Provides:       tex(oandsi10.tfm) = %{tl_version}, tex(oandsu10.tfm) = %{tl_version}
Provides:       tex(phnc10.tfm) = %{tl_version}, tex(pmhg.tfm) = %{tl_version}
Provides:       tex(proto10.tfm) = %{tl_version}, tex(sarab10.tfm) = %{tl_version}
Provides:       tex(vik10.tfm) = %{tl_version}, tex(aram10.pfb) = %{tl_version}
Provides:       tex(copsn10.pfb) = %{tl_version}, tex(cugar10.pfb) = %{tl_version}
Provides:       tex(cypr10.pfb) = %{tl_version}, tex(etr10.pfb) = %{tl_version}
Provides:       tex(fut10.pfb) = %{tl_version}, tex(givbc10.pfb) = %{tl_version}
Provides:       tex(gvibc10.pfb) = %{tl_version}, tex(linb10.pfb) = %{tl_version}
Provides:       tex(nab10.pfb) = %{tl_version}, tex(oandsi10.pfb) = %{tl_version}
Provides:       tex(oandsu10.pfb) = %{tl_version}, tex(phnc10.pfb) = %{tl_version}
Provides:       tex(pmhg.pfb) = %{tl_version}, tex(proto10.pfb) = %{tl_version}
Provides:       tex(sarab10.pfb) = %{tl_version}, tex(aramaic.sty) = %{tl_version}
Provides:       tex(cypriot.sty) = %{tl_version}, tex(etruscan.sty) = %{tl_version}
Provides:       tex(greek4cbc.sty) = %{tl_version}, tex(greek6cbc.sty) = %{tl_version}
Provides:       tex(hieroglf.sty) = %{tl_version}, tex(linearb.sty) = %{tl_version}
Provides:       tex(nabatean.sty) = %{tl_version}, tex(oands.sty) = %{tl_version}
Provides:       tex(oldprsn.sty) = %{tl_version}, tex(ot1aram.fd) = %{tl_version}
Provides:       tex(ot1copsn.fd) = %{tl_version}, tex(ot1cugar.fd) = %{tl_version}
Provides:       tex(ot1cypr.fd) = %{tl_version}, tex(ot1etr.fd) = %{tl_version}
Provides:       tex(ot1fut.fd) = %{tl_version}, tex(ot1givbc.fd) = %{tl_version}
Provides:       tex(ot1gvibc.fd) = %{tl_version}, tex(ot1nab.fd) = %{tl_version}
Provides:       tex(ot1oands.fd) = %{tl_version}, tex(ot1phnc.fd) = %{tl_version}
Provides:       tex(ot1pmhg.fd) = %{tl_version}, tex(ot1proto.fd) = %{tl_version}
Provides:       tex(ot1sarab.fd) = %{tl_version}, tex(ot1vik.fd) = %{tl_version}
Provides:       tex(phoenician.sty) = %{tl_version}, tex(protosem.sty) = %{tl_version}
Provides:       tex(runic.sty) = %{tl_version}, tex(sarabian.sty) = %{tl_version}
Provides:       tex(t1aram.fd) = %{tl_version}, tex(t1copsn.fd) = %{tl_version}
Provides:       tex(t1cugar.fd) = %{tl_version}, tex(t1cypr.fd) = %{tl_version}
Provides:       tex(t1etr.fd) = %{tl_version}, tex(t1fut.fd) = %{tl_version}
Provides:       tex(t1givbc.fd) = %{tl_version}, tex(t1gvibc.fd) = %{tl_version}
Provides:       tex(t1linb.fd) = %{tl_version}, tex(t1nab.fd) = %{tl_version}
Provides:       tex(t1oands.fd) = %{tl_version}, tex(t1phnc.fd) = %{tl_version}
Provides:       tex(t1pmhg.fd) = %{tl_version}, tex(t1proto.fd) = %{tl_version}
Provides:       tex(t1sarab.fd) = %{tl_version}, tex(t1vik.fd) = %{tl_version}
Provides:       tex(ugarite.sty) = %{tl_version}, tex(viking.sty) = %{tl_version}

%description -n texlive-archaic
The collection contains fonts to represent Aramaic, Cypriot,
Etruscan, Greek of the 6th and 4th centuries BCE, Egyptian
hieroglyphics, Linear A, Linear B, Nabatean old Persian, the
Phaistos disc, Phoenician, proto-Semitic, runic, South Arabian
Ugaritic and Viking scripts. The bundle also includes a small
font for use in phonetic transcription of the archaic writings.
The bundle's own directory includes a font installation map
file for the whole collection.

%package -n texlive-archaic-doc
Summary:        Documentation for archaic
Version:        svn38005.0

Provides:       tex-archaic-doc
AutoReqProv:    No

%description -n texlive-archaic-doc
Documentation for archaic

%package -n texlive-arcs
Provides:       tex-arcs = %{tl_version}
License:        LPPL
Summary:        Draw arcs over and under text
Version:        svn15878.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(relsize.sty)
Provides:       tex(arcs.sty) = %{tl_version}

%description -n texlive-arcs
The package provides two commands for placing an arc over
(\overarc) or under (\underarc) a piece of text. (The text may
be up to three letters long.) The commands generate an \hbox,
and may be used both in text and in maths formulae.

%package -n texlive-arcs-doc
Summary:        Documentation for arcs
Version:        svn15878.1

Provides:       tex-arcs-doc
AutoReqProv:    No

%description -n texlive-arcs-doc
Documentation for arcs

%package -n texlive-arev
Provides:       tex-arev = %{tl_version}
License:        LPPL
Summary:        Fonts and LaTeX support files for Arev Sans
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(amssymb.sty), tex(amsfonts.sty), tex(arevmath.sty), tex(beramono.sty)
Requires:       tex(ifthen.sty), tex(fontenc.sty), tex(textcomp.sty)
Provides:       tex(arevoml.enc) = %{tl_version}, tex(arevoms.enc) = %{tl_version}
Provides:       tex(arevot1.enc) = %{tl_version}, tex(arev.map) = %{tl_version}
Provides:       tex(ArevSans-Bold.tfm) = %{tl_version}, tex(ArevSans-BoldOblique.tfm) = %{tl_version}
Provides:       tex(ArevSans-Oblique.tfm) = %{tl_version}
Provides:       tex(ArevSans-Roman.tfm) = %{tl_version}, tex(favb8r.tfm) = %{tl_version}
Provides:       tex(favb8t.tfm) = %{tl_version}, tex(favbi8r.tfm) = %{tl_version}
Provides:       tex(favbi8t.tfm) = %{tl_version}, tex(favmb7t.tfm) = %{tl_version}
Provides:       tex(favmbi7m.tfm) = %{tl_version}, tex(favmr7t.tfm) = %{tl_version}
Provides:       tex(favmr7y.tfm) = %{tl_version}, tex(favmri7m.tfm) = %{tl_version}
Provides:       tex(favr8r.tfm) = %{tl_version}, tex(favr8t.tfm) = %{tl_version}
Provides:       tex(favri8r.tfm) = %{tl_version}, tex(favri8t.tfm) = %{tl_version}
Provides:       tex(zavmb7t.tfm) = %{tl_version}, tex(zavmbi7m.tfm) = %{tl_version}
Provides:       tex(zavmr7t.tfm) = %{tl_version}, tex(zavmr7y.tfm) = %{tl_version}
Provides:       tex(zavmri7m.tfm) = %{tl_version}, tex(ArevSans-Bold.pfb) = %{tl_version}
Provides:       tex(ArevSans-BoldOblique.pfb) = %{tl_version}
Provides:       tex(ArevSans-Oblique.pfb) = %{tl_version}
Provides:       tex(ArevSans-Roman.pfb) = %{tl_version}, tex(favb8t.vf) = %{tl_version}
Provides:       tex(favbi8t.vf) = %{tl_version}, tex(favr8t.vf) = %{tl_version}
Provides:       tex(favri8t.vf) = %{tl_version}, tex(zavmb7t.vf) = %{tl_version}
Provides:       tex(zavmbi7m.vf) = %{tl_version}, tex(zavmr7t.vf) = %{tl_version}
Provides:       tex(zavmr7y.vf) = %{tl_version}, tex(zavmri7m.vf) = %{tl_version}
Provides:       tex(ams-mdbch.sty) = %{tl_version}, tex(arev.sty) = %{tl_version}
Provides:       tex(arevmath.sty) = %{tl_version}, tex(arevsymbols.tex) = %{tl_version}
Provides:       tex(arevtext.sty) = %{tl_version}, tex(omlzavm.fd) = %{tl_version}
Provides:       tex(omszavm.fd) = %{tl_version}, tex(ot1zavm.fd) = %{tl_version}
Provides:       tex(t1fav.fd) = %{tl_version}, tex(uzavm.fd) = %{tl_version}

%description -n texlive-arev
The package arev provides type 1 and virtual fonts, together
with LaTeX packages for using Arev Sans in both text and
mathematics. Arev Sans is a derivative of Bitstream Vera Sans
created by Tavmjong Bah, adding support for Greek and Cyrillic
characters. Bah also added a few variant letters that are more
appropriate for mathematics. The primary purpose for using Arev
Sans in LaTeX is presentations, particularly when using a
computer projector. In such a context, Arev Sans is quite
readable, with large x-height, "open letters", wide spacing,
and thick stems. The style is very similar to the SliTeX font
lcmss, but heavier. Arev is one of a very small number of sans-
font mathematics support packages. Others are cmbright, hvmath
and kerkis.

%package -n texlive-arev-doc
Summary:        Documentation for arev
Version:        svn15878.0

Provides:       tex-arev-doc
AutoReqProv:    No

%description -n texlive-arev-doc
Documentation for arev

%package -n texlive-armtex
Provides:       tex-armtex = %{tl_version}
License:        LPPL
Summary:        A sytem for writing Armenian with TeX and LaTeX
Version:        svn33894.3.0_beta3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(kvoptions.sty)
Provides:       tex(arss.map) = %{tl_version}, tex(artm.map) = %{tl_version}
Provides:       tex(arssb10.tfm) = %{tl_version}, tex(arssbs10.tfm) = %{tl_version}
Provides:       tex(arssr10.tfm) = %{tl_version}, tex(arsssl10.tfm) = %{tl_version}
Provides:       tex(artmb10.tfm) = %{tl_version}, tex(artmbi10.tfm) = %{tl_version}
Provides:       tex(artmbs10.tfm) = %{tl_version}, tex(artmi10.tfm) = %{tl_version}
Provides:       tex(artmr10.tfm) = %{tl_version}, tex(artmsl10.tfm) = %{tl_version}
Provides:       tex(arssb10.pfb) = %{tl_version}, tex(arssbs10.pfb) = %{tl_version}
Provides:       tex(arssr10.pfb) = %{tl_version}, tex(arsssl10.pfb) = %{tl_version}
Provides:       tex(artmb10.pfb) = %{tl_version}, tex(artmbi10.pfb) = %{tl_version}
Provides:       tex(artmbs10.pfb) = %{tl_version}, tex(artmi10.pfb) = %{tl_version}
Provides:       tex(artmr10.pfb) = %{tl_version}, tex(artmsl10.pfb) = %{tl_version}
Provides:       tex(armscii8.def) = %{tl_version}, tex(armtex.sty) = %{tl_version}
Provides:       tex(ot6cmr.fd) = %{tl_version}, tex(ot6cmss.fd) = %{tl_version}
Provides:       tex(ot6enc.def) = %{tl_version}, tex(arm.tex) = %{tl_version}
Provides:       tex(armkb-a8.tex) = %{tl_version}, tex(armkb-u8.tex) = %{tl_version}

%description -n texlive-armtex
ArmTeX is a system for typesetting Armenian text with Plain TeX
or LaTeX(2e). It may be used with input: from a standard Latin
keyboard without any special encoding and/or support for
Armenian letters, any keyboard which uses an encoding that has
Armenian letters in the second half (characters 128-255) of the
extended ASCII table (for example ArmSCII8 Armenian standard),
or encoded in UTF-8. Users should note that the manuals (below)
mostly describe the previous (version 2.0) of the package.
Updating work is still under way.

%package -n texlive-armtex-doc
Summary:        Documentation for armtex
Version:        svn33894.3.0_beta3

Provides:       tex-armtex-doc
AutoReqProv:    No

%description -n texlive-armtex-doc
Documentation for armtex



%package -n texlive-asana-math
Provides:       tex-asana-math = %{tl_version}
License:        OFL
Summary:        A font to typeset maths in Xe(La)TeX and Lua(La)TeX
Version:        svn37556.000.955

Requires:       texlive-base
Provides:       texlive-Asana-Math = %{tl_version}
Obsoletes:      texlive-Asana-Math < %{tl_version}, texlive-Asana-Math-fedora-fonts < %{tl_version}
Requires:       texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(Asana-Math.otf) = %{tl_version}

%description -n texlive-asana-math
The Asana-Math font is an OpenType font that includes almost
all mathematical Unicode symbols and it can be used to typeset
mathematical text with any software that can understand the
MATH OpenType table (e.g., XeTeX 0.997 and Microsoft Word
2007). The font is beta software. Typesetting support for use
with LaTeX is provided by the fontspec and unicode-math
packages.

%package -n texlive-asana-math-doc
Summary:        Documentation for asana-math
Version:        svn37556.000.955

Provides:       tex-asana-math-doc
AutoReqProv:    No

%description -n texlive-asana-math-doc
Documentation for asana-math

%package -n texlive-MemoirChapStyles-doc
Summary:        Documentation for MemoirChapStyles
Version:        svn25918.1.7e

Provides:       tex-MemoirChapStyles-doc
AutoReqProv:    No

%description -n texlive-MemoirChapStyles-doc
Documentation for MemoirChapStyles

%package -n texlive-Type1fonts-doc
Summary:        Documentation for Type1fonts
Version:        svn19603.2.14

Provides:       tex-Type1fonts-doc
AutoReqProv:    No

%description -n texlive-Type1fonts-doc
Documentation for Type1fonts

%package -n texlive-ESIEEcv
Provides:       tex-ESIEEcv = %{tl_version}
License:        LPPL
Summary:        Curriculum vitae for French use
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tabularx.sty)
Provides:       tex(ESIEEcv.sty) = %{tl_version}

%description -n texlive-ESIEEcv
The package allows the user to set up a curriculum vitae as a
French employer will expect.

%package -n texlive-ESIEEcv-doc
Summary:        Documentation for ESIEEcv
Version:        svn15878.0

Provides:       tex-ESIEEcv-doc
AutoReqProv:    No

%description -n texlive-ESIEEcv-doc
Documentation for ESIEEcv

%package -n texlive-GS1
Provides:       tex-GS1 = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset EAN barcodes using TeX rules, only
Version:        svn44822
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty)
Provides:       tex(GS1.sty) = %{tl_version}, tex(rule-D.sty) = %{tl_version}

%description -n texlive-GS1
The (LaTeX 3) package typesets EAN-8 and EAN-13 barcodes, using
the facilities of the rule-D package.

%package -n texlive-GS1-doc
Summary:        Documentation for GS1
Version:        svn44822
Provides:       tex-GS1-doc
AutoReqProv:    No

%description -n texlive-GS1-doc
Documentation for GS1

%package -n texlive-HA-prosper
Provides:       tex-HA-prosper = %{tl_version}
License:        LPPL
Summary:        Patches and improvements for prosper
Version:        svn15878.4.21

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(xcomment.sty), tex(verbatim.sty), tex(pst-grad.sty)
Requires:       tex(pifont.sty), tex(amssymb.sty), tex(palatino.sty), tex(mathpazo.sty)
Requires:       tex(semhelv.sty), tex(multido.sty), tex(pst-slpe.sty)
Provides:       tex(HA-prosper.cfg) = %{tl_version}, tex(HA-prosper.sty) = %{tl_version}
Provides:       tex(HAPAggie.sty) = %{tl_version}, tex(HAPcapsules.sty) = %{tl_version}
Provides:       tex(HAPciment.sty) = %{tl_version}, tex(HAPFyma.sty) = %{tl_version}
Provides:       tex(HAPHA.sty) = %{tl_version}, tex(HAPLakar.sty) = %{tl_version}
Provides:       tex(HAPsimple.sty) = %{tl_version}, tex(HAPTCS.sty) = %{tl_version}
Provides:       tex(HAPTCSTealBlue.sty) = %{tl_version}, tex(HAPTCSgrad.sty) = %{tl_version}
Provides:       tex(HAPTycja.sty) = %{tl_version}

%description -n texlive-HA-prosper
HA-prosper is a patch for prosper that adds new functionality
to prosper based presentations. Among the new features you will
find automatic generation of a table of contents on each slide,
support for notes and portrait slides. The available styles
demonstrate how to expand the functionality of prosper even
further.

%package -n texlive-HA-prosper-doc
Summary:        Documentation for HA-prosper
Version:        svn15878.4.21

Provides:       tex-HA-prosper-doc
AutoReqProv:    No

%description -n texlive-HA-prosper-doc
Documentation for HA-prosper

%package -n texlive-Tabbing
Provides:       tex-Tabbing = %{tl_version}
License:        LPPL
Summary:        Tabbing with accented letters
Version:        svn17022.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(Tabbing.sty) = %{tl_version}

%description -n texlive-Tabbing
By default, some of the tabbing environment's commands clash
with default accent commands; LaTeX provides the odd commands
\a', etc., to deal with the clash. The package offers a variant
of the tabbing environment which does not create this
difficulty, so that users need not learn two sets of accent
commands.

%package -n texlive-Tabbing-doc
Summary:        Documentation for Tabbing
Version:        svn17022.0

Provides:       tex-Tabbing-doc
AutoReqProv:    No

%description -n texlive-Tabbing-doc
Documentation for Tabbing

%package -n texlive-IEEEconf
Provides:       tex-IEEEconf = %{tl_version}
License:        LPPL
Summary:        Macros for IEEE conference proceedings
Version:        svn15878.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(mathptmx.sty), tex(helvet.sty), tex(courier.sty)
Requires:       tex(array.sty), tex(titlesec.sty)
Provides:       tex(IEEEconf.cls) = %{tl_version}

%description -n texlive-IEEEconf
The IEEEconf class implements the formatting dictated by the
IEEE Computer Society Press for conference proceedings.

%package -n texlive-IEEEconf-doc
Summary:        Documentation for IEEEconf
Version:        svn15878.1.4

Provides:       tex-IEEEconf-doc
AutoReqProv:    No

%description -n texlive-IEEEconf-doc
Documentation for IEEEconf

%package -n texlive-IEEEtran
Provides:       tex-IEEEtran = %{tl_version}
License:        LPPL 1.3
Summary:        Document class for IEEE Transactions journals and conferences
Version:        svn38238.1.8b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(newtxmath.sty)
Provides:       tex(IEEEtran.cls) = %{tl_version}, tex(IEEEtrantools.sty) = %{tl_version}
Provides:       tetex-IEEEtran = %{tl_version}
Obsoletes:      tetex-IEEEtran < %{tl_version}

%description -n texlive-IEEEtran
The class and its BibTeX style enable authors to produce
officially-correct output for the Institute of Electrical and
Electronics Engineers (IEEE) transactions, journals and
conferences.

%package -n texlive-IEEEtran-doc
Summary:        Documentation for IEEEtran
Version:        svn38238.1.8b

Provides:       tex-IEEEtran-doc
AutoReqProv:    No

%description -n texlive-IEEEtran-doc
Documentation for IEEEtran

%package -n texlive-SIstyle
Provides:       tex-SIstyle = %{tl_version}
License:        LPPL
Summary:        Package to typeset SI units, numbers and angles
Version:        svn15878.2.3a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amstext.sty)
Provides:       tex(sistyle.sty) = %{tl_version}

%description -n texlive-SIstyle
This package typesets SI units, numbers and angles according to
the ISO requirements. Care is taken with font setup and
requirements, and language customisation is available. Note
that this package is (in principle) superseded by siunitx;
sistyle has maintenance-only support, now.

%package -n texlive-SIstyle-doc
Summary:        Documentation for SIstyle
Version:        svn15878.2.3a

Provides:       tex-SIstyle-doc
AutoReqProv:    No

%description -n texlive-SIstyle-doc
Documentation for SIstyle

%package -n texlive-SIunits
Provides:       tex-SIunits = %{tl_version}
License:        LPPL 1.3
Summary:        International System of Units
Version:        svn15878.1.36

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amstext.sty)
Provides:       tex(SIunits.cfg) = %{tl_version}, tex(SIunits.sty) = %{tl_version}
Provides:       tex(binary.sty) = %{tl_version}

%description -n texlive-SIunits
Typeset physical units following the rules of the International
System of Units (SI). The package requires amstext, for proper
representation of some values. Note that the package is now
superseded by siunitx; siunits has maintenance-only support,
now.

%package -n texlive-SIunits-doc
Summary:        Documentation for SIunits
Version:        svn15878.1.36

Provides:       tex-SIunits-doc
AutoReqProv:    No

%description -n texlive-SIunits-doc
Documentation for SIunits

%package -n texlive-acmart-doc
Provides:       tex-acmart-doc = %{tl_version}
License:        LPPL
Summary:        doc files of acmart
Version:        svn48214
AutoReqProv:    No

%description -n texlive-acmart-doc
Documentation for acmart

%package -n texlive-acmart
Provides:       tex-acmart = %{tl_version}
License:        LPPL
Summary:        Class for typesetting publications of ACM>
Version:        svn48214
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(acmart.cls) = %{tl_version}

%description -n texlive-acmart
This package provides a class for typesetting publications of
Association for Computing Machinery.

%package -n texlive-adtrees
Provides:       tex-adtrees = %{tl_version}
License:        GPL+
Summary:        Macros for drawing adpositional trees
Version:        svn39438
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(adtrees.sty) = %{tl_version}

%description -n texlive-adtrees
The adtrees package provides a package to write adpositional
trees, a formalism devoted to represent natural language
expressions. The package is composed by the files adtree.sty:
containing the LaTeX engine to adpositional trees
adtreedoc.pdf: the human readable documentation for the package
adtreedoc.tex: the source code for the documentation.

%package -n texlive-adtrees-doc
Provides:       tex-adtrees-doc
License:        GPL+
Summary:        doc files of adtrees
Version:        svn39438
AutoReqProv:    No

%description -n texlive-adtrees-doc
Documentation for adtrees

%package -n texlive-arabi-add-doc
Provides:       tex-arabi-add-doc = %{tl_version}
License:        LPPL
Summary:        doc files of arabi-add
Version:        svn37709

AutoReqProv:    No

%description -n texlive-arabi-add-doc
Documentation for arabi-add

%package -n texlive-arabi-add
Provides:       tex-arabi-add = %{tl_version}
License:        LPPL
Summary:        Using hyperref and bookmark packages with arabic and farsi languages
Version:        svn37709

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(arabi-add.sty) = %{tl_version}

%description -n texlive-arabi-add
This package takes advantage of some of the possibilities that
hyperref and bookmark packages offer when you create a table of
contents for Arabic texts created by the arabi package.

%package -n texlive-arabluatex-doc
Provides:       tex-arabluatex-doc = %{tl_version}
License:        GPLv3+
Summary:        doc files of arabluatex
Version:        svn48094
AutoReqProv:    No

%description -n texlive-arabluatex-doc
Documentation for arabluatex

%package -n texlive-arabluatex
Provides:       tex-arabluatex = %{tl_version}
License:        GPLv3+
Summary:        An ArabTeX-like interface for LuaLaTeX
Version:        svn48094
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(arabluatex.sty) = %{tl_version}

%description -n texlive-arabluatex
This package provides for LuaLaTeX an ArabTeX-like interface to
generate Arabic writing from an ascii transliteration. It is
particularly well-suited for complex documents such as
technical documents or critical editions where a lot of left-to-
right commands intertwine with Arabic writing. arabluatex is
able to process any ArabTeX input notation. Its output can be
set in the same modes of vocalization as ArabTeX, or in
different roman transliterations. It further allows many
typographical refinements. It will eventually interact with
some other packages yet to come to produce from .tex source
files, in addition to printed books, TEI xml compliant critical
editions and/or lexicons that can be searched, analyzed and
correlated in various ways.

%package -n texlive-archaeologie-doc
Provides:       tex-archaeologie-doc = %{tl_version}
License:        LPPL
Summary:        doc files of archaeologie
Version:        svn47406
AutoReqProv:    No

%description -n texlive-archaeologie-doc
Documentation for archaeologie

%package -n texlive-archaeologie
Provides:       tex-archaeologie = %{tl_version}
License:        LPPL
Summary:        Citation-style which covers rules of the German Archaeology Institute
Version:        svn47406
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-archaeologie
This citation-style covers the citation and bibliography rules
of the German Archaeology Institute. Various options are
available to change and adjust the outcome according to one's
own preferences.

%package -n texlive-abnt
Summary:        Typesetting academic works according to ABNT rules
Version:        svn48305
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(abnt.sty) = %{tl_version}

%description -n texlive-abnt
The ABNT package provides a clean and practical implementation
of the ABNT rules for academic texts. Its purpose is to be as
simple and user-friendly as possible.

%package -n texlive-actuarialsymbol
Summary:        Actuarial symbols of life contingencies and financial mathematics
Version:        svn44607
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(actuarialsymbol.sty) = %{tl_version}

%description -n texlive-actuarialsymbol
This package provides commands to compose actuarial symbols of
life contingencies and financial mathematics characterized by
subscripts and superscripts on both sides of a principal
symbol. The package also features commands to easily and
consistently position precedence numbers above or below
statuses in symbols for multiple lives contracts. Since the
actuarial notation can get quite involved, the package defines
a number of shortcut macros to ease entry of the most common
elements. Appendix A of the package documentation lists the
commands to typeset a large selection of symbols of life
contingencies. This package requires actuarialangle.

%package -n texlive-addfont
Summary:        easier use of fonts without LaTeX support
Version:        svn41972
License:        GPLv3
Requires:       texlive-base texlive-kpathsea
Provides:       tex(addfont.sty) = %{tl_version}

%description -n texlive-addfont
This package is intended for use by users who know about fonts.
It is a quick-fix for fonts which does not have genuine LaTeX
support. It is not meant as a replacement of the LaTeX font
definition files. It is meant as something more useable for
LaTeX users than the \newfont command. With addfont the loaded
font scales along with the usual LaTeX size selection. Using
this package still requires some knowledge on how to use fonts
with LaTeX.

%package -n texlive-algolrevived
Summary:        A revival of Frutiger's Algol alphabet
Version:        svn44784
License:        OFL and LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(zal_2yvryp.enc) = %{tl_version}, tex(zal_45q3lq.enc) = %{tl_version}
Provides:       tex(zal_6samag.enc) = %{tl_version}, tex(zal_7ov2yu.enc) = %{tl_version}
Provides:       tex(zal_amjsul.enc) = %{tl_version}, tex(zal_cldq6x.enc) = %{tl_version}
Provides:       tex(zal_du2clj.enc) = %{tl_version}, tex(zal_ekxevm.enc) = %{tl_version}
Provides:       tex(zal_exbmso.enc) = %{tl_version}, tex(zal_funcu6.enc) = %{tl_version}
Provides:       tex(zal_gyqugr.enc) = %{tl_version}, tex(zal_hg4hay.enc) = %{tl_version}
Provides:       tex(zal_krbsfx.enc) = %{tl_version}, tex(zal_lxmhqh.enc) = %{tl_version}
Provides:       tex(zal_ly2wza.enc) = %{tl_version}, tex(zal_o7qsmw.enc) = %{tl_version}
Provides:       tex(zal_plrp6e.enc) = %{tl_version}, tex(zal_qttkt5.enc) = %{tl_version}
Provides:       tex(zal_r25n3d.enc) = %{tl_version}, tex(zal_teidbm.enc) = %{tl_version}
Provides:       tex(zal_wkwfu6.enc) = %{tl_version}, tex(zal_wl6hk2.enc) = %{tl_version}
Provides:       tex(zal_xnjnii.enc) = %{tl_version}, tex(zal_ys7y36.enc) = %{tl_version}
Provides:       tex(algolrevived.map) = %{tl_version}, tex(AlgolRevived-Medium.otf) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted.otf) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted.otf) = %{tl_version}
Provides:       tex(AlgolRevived.otf) = %{tl_version}, tex(AlgolRevived-Medium-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-inf-ly1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-inf-ot1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-inf-t1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-sup-ly1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-sup-ot1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-sup-t1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-tlf-t1.tfm) = %{tl_version}
Provides:       tex(AlgolRevived-Medium.pfb) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted.pfb) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted.pfb) = %{tl_version}
Provides:       tex(AlgolRevived.pfb) = %{tl_version}, tex(algolrevived.sty) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-inf-t1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-inf-t1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-sup-t1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-MediumSlanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-inf-ly1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-inf-t1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-sup-ly1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-sup-t1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-tlf-ly1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-Slanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-inf-t1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-sup-t1.vf) = %{tl_version}
Provides:       tex(AlgolRevived-tlf-t1.vf) = %{tl_version}
Provides:       tex(LY1AlgolRevived-Inf.fd) = %{tl_version}
Provides:       tex(LY1AlgolRevived-Sup.fd) = %{tl_version}
Provides:       tex(LY1AlgolRevived-TLF.fd) = %{tl_version}
Provides:       tex(OT1AlgolRevived-Inf.fd) = %{tl_version}
Provides:       tex(OT1AlgolRevived-Sup.fd) = %{tl_version}
Provides:       tex(OT1AlgolRevived-TLF.fd) = %{tl_version}
Provides:       tex(T1AlgolRevived-Inf.fd) = %{tl_version}
Provides:       tex(T1AlgolRevived-Sup.fd) = %{tl_version}
Provides:       tex(T1AlgolRevived-TLF.fd) = %{tl_version}
Provides:       tex(TS1AlgolRevived-TLF.fd) = %{tl_version}

%description -n texlive-algolrevived
The package revives Frutinger's Algol alphabet, designed in
1963 for the code segments in an ALGOL manual. OpenType and
type1, regular and medium weights, upright and slanted. Not
monospaced, but good for listings if you don't need code to be
aligned with specific columns. It also makes a passable but
limited text font.

%package -n texlive-alkalami
Summary:        A font for Arabic-based writing systems in Nigeria and Niger
Version:        svn44497
License:        OFL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(Alkalami-Light.ttf) = %{tl_version}, tex(Alkalami-Regular.ttf) = %{tl_version}

%description -n texlive-alkalami
This font is designed for Arabic-based writing systems in the
Kano region of Nigeria and Niger.

%package -n texlive-apalike-german
Summary:        A copy of apalike.bst with German localization
Version:        svn47002
License:        LPPL
Requires:       texlive-base texlive-kpathsea

%description -n texlive-apalike-german
A copy of apalike.bst with German localization.

%package -n texlive-arimo
Summary:        Arimo sans serif fonts with LaTeX support
Version:        svn42880
License:        ASL 2.0
Requires:       texlive-base texlive-kpathsea
Provides:       tex(arm_7miqnq.enc) = %{tl_version}, tex(arm_c3z4r2.enc) = %{tl_version}
Provides:       tex(arm_f4duzd.enc) = %{tl_version}, tex(arm_l3opzb.enc) = %{tl_version}
Provides:       tex(arimo.map) = %{tl_version}, tex(Arimo-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Arimo-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Arimo-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Arimo-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Arimo-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Arimo-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Arimo-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Arimo-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Arimo-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Arimo-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Arimo-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Arimo-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Arimo-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Arimo-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Arimo-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Arimo-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Arimo-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Arimo-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Arimo-tlf-ly1.tfm) = %{tl_version}, tex(Arimo-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Arimo-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Arimo-tlf-t1.tfm) = %{tl_version}, tex(Arimo-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Arimo-tlf-ts1.tfm) = %{tl_version}, tex(Arimo-Bold.ttf) = %{tl_version}
Provides:       tex(Arimo-BoldItalic.ttf) = %{tl_version}
Provides:       tex(Arimo-Italic.ttf) = %{tl_version}, tex(Arimo-Regular.ttf) = %{tl_version}
Provides:       tex(Arimo-Bold.pfb) = %{tl_version}, tex(Arimo-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Arimo-Italic.pfb) = %{tl_version}, tex(Arimo.pfb) = %{tl_version}
Provides:       tex(arimo.sty) = %{tl_version}, tex(Arimo-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Arimo-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Arimo-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Arimo-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Arimo-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Arimo-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Arimo-tlf-t1.vf) = %{tl_version}, tex(Arimo-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Arimo-TLF.fd) = %{tl_version}, tex(OT1Arimo-TLF.fd) = %{tl_version}
Provides:       tex(T1Arimo-TLF.fd) = %{tl_version}, tex(TS1Arimo-TLF.fd) = %{tl_version}

%description -n texlive-arimo
The Arimo family, designed by Steve Matteson, is an innovative,
refreshing sans serif design which is metrically compatible
with Arial.

%package -n texlive-algobox
Summary:        Typeset Algobox programs
Version:        svn45223
License:        GPLv3+
Requires:       texlive-base texlive-kpathsea, tex(expl3.sty)
Requires:       tex(tikz.sty), tex(environ.sty), tex(xparse.sty), tex(xcolor.sty)
Provides:       tex(algobox.sty) = %{tl_version}

%description -n texlive-algobox
This LaTeX package can typeset Algobox programs almost exactly
as displayed when editing with Algobox itself, using an input
syntax very similar to the actual Algobox program text. It
gives better results than Algobox's own LaTeX export which does
not look like the editor rendition, produces standalone
documents cumbersome to customize, and has arbitrary and
inconsistent differences between the input syntax and the
program text. This package depends upon the following other
LaTeX packages: expl3, TikZ, environ, xparse, and xcolor.

%package -n texlive-adigraph
Summary:        Augmenting directed graphs
Version:        svn47148
License:        MIT
Requires:       texlive-base texlive-kpathsea, texlive-fp
Requires:       tex(fp.sty), tex(xparse.sty), tex(xstring.sty), tex(tikz.sty)
Provides:       tex(adigraph.sty) = %{tl_version}

%description -n texlive-adigraph
This LaTeX package provides the means to easily draw augmenting
oriented graphs, as well as cuts on them, to demonstrate steps
of algorithms for solving max-flow min-cut problems. This
package requires the other LaTeX packages fp, xparse, xstring,
and TikZ (in particular the TikZ calc library).

%package -n texlive-aligned-overset
Summary:        Fix alignment at \overset or \underset
Version:        svn47290
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(aligned-overset.sty) = %{tl_version}

%description -n texlive-aligned-overset
This package allows the base character of \underset or \overset
to be used as the alignment position for the amsmath aligned
math environments.

%package -n texlive-amscls-doc
Summary:        User documentation for AMS document classes
Version:        svn46110
License:        LPPL
Requires:       texlive-base texlive-kpathsea

%description -n texlive-amscls-doc
This collection comprises a set of four manuals, or Author
Handbooks, each documenting the use of a class of publications
based on one of the AMS document classes amsart, amsbook,
amsproc and one "hybrid", as well as a guide to the generation
of the four manuals from a coordinated set of LaTeX source
files. The Handbooks comprise the user documentation for the
pertinent document classes. As the source for the Handbooks
consists of a large number of files, and the intended output is
multiple different documents, the principles underlying this
collection can be used as a model for similar projects. The
manual "Compiling the AMS Author Handbooks" provides
information about the structure of and interaction between the
various components.

%package -n texlive-apxproof
Summary:        Proofs in appendix
Version:        svn48377
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(amsthm.sty)
Requires:       tex(bibunits.sty), tex(environ.sty), tex(etoolbox.sty), tex(fancyvrb.sty)
Requires:       tex(ifthen.sty), tex(kvoptions.sty)
Provides:       tex(apxproof.sty) = %{tl_version}

%description -n texlive-apxproof
The package makes it easier to write articles where proofs and
other material are deferred to the appendix. The appendix
material is written in the LaTeX code along with the main text
which it naturally complements, and it is automatically
deferred. The package can automatically send proofs to the
appendix, can repeat in the appendix the theorem environments
stated in the main text, can section the appendix automatically
based on the sectioning of the main text, and supports a
separate bibliography for the appendix material. It depends on
the following other packages: amsthm, bibunits, environ,
etoolbox, fancyvrb, ifthen, and kvoptions.


%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="arkandis/accanthis public/almfixed public/antt \
public/Asana-Math"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -rf %{buildroot}%{_datadir}/texlive/texmf-dist/omega/otp/antomega/*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tex/plain/amsfonts/*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-12many
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/12many/

%files -n texlive-12many-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/12many/

%files -n texlive-2up
%{_texdir}/texmf-dist/tex/generic/2up/

%files -n texlive-2up-doc
%{_texdir}/texmf-dist/doc/generic/2up/

%files -n texlive-a0poster
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/a0poster/

%files -n texlive-a0poster-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/a0poster/

%files -n texlive-a4wide
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/a4wide/

%files -n texlive-a4wide-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/a4wide/

%files -n texlive-a5comb
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/a5comb/

%files -n texlive-a5comb-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/a5comb/

%files -n texlive-aastex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/aastex/
%{_texdir}/texmf-dist/bibtex/bst/aastex/

%files -n texlive-aastex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/aastex/

%files -n texlive-abbr
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/abbr/

%files -n texlive-abbr-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/generic/abbr/

%files -n texlive-abc
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/abc/

%files -n texlive-abc-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/abc/

%files -n texlive-abntex2
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bib/abntex2/
%{_texdir}/texmf-dist/bibtex/bst/abntex2/
%{_texdir}/texmf-dist/tex/latex/abntex2/

%files -n texlive-abntex2-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/abntex2/

%files -n texlive-abraces
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/abraces/

%files -n texlive-abraces-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/abraces/

%files -n texlive-abstract
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/abstract/

%files -n texlive-abstract-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/abstract/

%files -n texlive-abstyles
%{_texdir}/texmf-dist/bibtex/bib/abstyles/
%{_texdir}/texmf-dist/bibtex/bst/abstyles/
%{_texdir}/texmf-dist/tex/generic/abstyles/

%files -n texlive-abstyles-doc
%{_texdir}/texmf-dist/doc/bibtex/abstyles/

%files -n texlive-academicons
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/truetype/public/academicons/
%{_texdir}/texmf-dist/tex/latex/academicons/

%files -n texlive-academicons-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/academicons/

%files -n texlive-accanthis
%license gpl2.txt
%{_datadir}/fonts/accanthis
%{_texdir}/texmf-dist/fonts/enc/dvips/accanthis/
%{_texdir}/texmf-dist/fonts/map/dvips/accanthis/
%{_texdir}/texmf-dist/fonts/opentype/arkandis/accanthis/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/accanthis/
%{_texdir}/texmf-dist/fonts/type1/arkandis/accanthis/
%{_texdir}/texmf-dist/fonts/vf/arkandis/accanthis/
%{_texdir}/texmf-dist/tex/latex/accanthis/

%files -n texlive-accanthis-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/fonts/accanthis/

%files -n texlive-achemso
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/achemso/
%{_texdir}/texmf-dist/tex/latex/achemso/

%files -n texlive-achemso-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/achemso/

%files -n texlive-acmconf
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/acmconf/

%files -n texlive-acmconf-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/acmconf/

%files -n texlive-acronym
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/acronym/

%files -n texlive-acronym-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/acronym/

%files -n texlive-acroterm
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/acroterm/

%files -n texlive-acroterm-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/acroterm/

%files -n texlive-acro
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/acro/

%files -n texlive-acro-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/acro/

%files -n texlive-active-conf
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/active-conf/

%files -n texlive-active-conf-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/active-conf/

%files -n texlive-actuarialangle
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/actuarialangle/

%files -n texlive-actuarialangle-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/actuarialangle/

%files -n texlive-addlines
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/addlines/

%files -n texlive-addlines-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/addlines/

%files -n texlive-adfathesis
%license pd.txt
%{_texdir}/texmf-dist/bibtex/bst/adfathesis/
%{_texdir}/texmf-dist/tex/latex/adfathesis/

%files -n texlive-adfathesis-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/adfathesis/

%files -n texlive-adforn
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/arkandis/adforn/
%{_texdir}/texmf-dist/fonts/enc/dvips/adforn/
%{_texdir}/texmf-dist/fonts/map/dvips/adforn/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/adforn/
%{_texdir}/texmf-dist/fonts/type1/arkandis/adforn/
%{_texdir}/texmf-dist/tex/latex/adforn/

%files -n texlive-adforn-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/adforn/

%files -n texlive-adfsymbols
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/arkandis/adfsymbols/
%{_texdir}/texmf-dist/fonts/enc/dvips/adfsymbols/
%{_texdir}/texmf-dist/fonts/map/dvips/adfsymbols/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/adfsymbols/
%{_texdir}/texmf-dist/fonts/type1/arkandis/adfsymbols/
%{_texdir}/texmf-dist/tex/latex/adfsymbols/

%files -n texlive-adfsymbols-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/adfsymbols/

%files -n texlive-adjmulticol
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/adjmulticol/

%files -n texlive-adjmulticol-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/adjmulticol/

%files -n texlive-adjustbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/adjustbox/

%files -n texlive-adjustbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/adjustbox/

%files -n texlive-adobemapping
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/

%files -n texlive-adrconv
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/adrconv/
%{_texdir}/texmf-dist/tex/latex/adrconv/

%files -n texlive-adrconv-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/adrconv/

%files -n texlive-advdate
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/advdate/

%files -n texlive-advdate-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/advdate/

%files -n texlive-aecc
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/tfm/public/aecc/
%{_texdir}/texmf-dist/fonts/vf/public/aecc/
%{_texdir}/texmf-dist/tex/latex/aecc/

%files -n texlive-aecc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/aecc/

%files -n texlive-aeguill
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/aeguill/

%files -n texlive-aeguill-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/aeguill/

%files -n texlive-ae
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/tfm/public/ae/
%{_texdir}/texmf-dist/fonts/vf/public/ae/
%{_texdir}/texmf-dist/tex/latex/ae/

%files -n texlive-ae-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/ae/

%files -n texlive-afparticle
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/afparticle/

%files -n texlive-afparticle-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/afparticle/

%files -n texlive-afthesis
%license pd.txt
%{_texdir}/texmf-dist/bibtex/bst/afthesis/
%{_texdir}/texmf-dist/tex/latex/afthesis/

%files -n texlive-afthesis-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/afthesis/

%files -n texlive-aguplus
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/aguplus/
%{_texdir}/texmf-dist/tex/latex/aguplus/

%files -n texlive-aguplus-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/aguplus/

%files -n texlive-aiaa
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/aiaa/
%{_texdir}/texmf-dist/tex/latex/aiaa/

%files -n texlive-aiaa-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/aiaa/

%files -n texlive-aichej
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/aichej/

%files -n texlive-ajl
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/ajl/

%files -n texlive-akktex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/akktex/

%files -n texlive-akktex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/akktex/

%files -n texlive-akletter
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/akletter/

%files -n texlive-akletter-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/akletter/

%files -n texlive-alegreya
%license ofl.txt
%{_texdir}/texmf-dist/tex/latex/alegreya/
%{_texdir}/texmf-dist/fonts/map/dvips/alegreya/
%{_texdir}/texmf-dist/fonts/tfm/huerta/alegreya/
%{_texdir}/texmf-dist/fonts/vf/huerta/alegreya/
%{_texdir}/texmf-dist/fonts/enc/dvips/alegreya/
%{_texdir}/texmf-dist/fonts/type1/huerta/alegreya/
%{_texdir}/texmf-dist/fonts/opentype/huerta/alegreya/

%files -n texlive-alegreya-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/alegreya/

%files -n texlive-alertmessage
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/alertmessage/

%files -n texlive-alertmessage-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/alertmessage/

%files -n texlive-algorithm2e
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/algorithm2e/

%files -n texlive-algorithm2e-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/algorithm2e/

%files -n texlive-algorithmicx
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/algorithmicx/

%files -n texlive-algorithmicx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/algorithmicx/

%files -n texlive-algorithms
%license lgpl2.1.txt
%{_texdir}/texmf-dist/tex/latex/algorithms/

%files -n texlive-algorithms-doc
%license lgpl2.1.txt
%{_texdir}/texmf-dist/doc/latex/algorithms/

%files -n texlive-alg
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/alg/

%files -n texlive-alg-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/alg/

%files -n texlive-allrunes
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/allrunes/
%{_texdir}/texmf-dist/fonts/source/public/allrunes/
%{_texdir}/texmf-dist/fonts/type1/public/allrunes/
%{_texdir}/texmf-dist/tex/latex/allrunes/

%files -n texlive-allrunes-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/allrunes/

%files -n texlive-almfixed
%license gfl.txt
%{_datadir}/fonts/almfixed
%{_texdir}/texmf-dist/fonts/opentype/public/almfixed/
%{_texdir}/texmf-dist/fonts/truetype/public/almfixed/

%files -n texlive-almfixed-doc
%license gfl.txt
%{_texdir}/texmf-dist/doc/fonts/almfixed/

%files -n texlive-alnumsec
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/alnumsec/

%files -n texlive-alnumsec-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/alnumsec/

%files -n texlive-alterqcm
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/alterqcm/

%files -n texlive-alterqcm-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/alterqcm/

%files -n texlive-altfont
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/altfont/

%files -n texlive-altfont-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/altfont/

%files -n texlive-ametsoc
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/ametsoc/
%{_texdir}/texmf-dist/tex/latex/ametsoc/

%files -n texlive-ametsoc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ametsoc/

%files -n texlive-amiri
%license ofl.txt
%{_texdir}/texmf-dist/fonts/truetype/public/amiri/

%files -n texlive-amiri-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/amiri/

%files -n texlive-amsaddr
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/amsaddr/

%files -n texlive-amsaddr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/amsaddr/

%files -n texlive-amscls
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/amscls/
%{_texdir}/texmf-dist/tex/latex/amscls/
%doc %{_texdir}/texmf-dist/doc/latex/amscls/

%files -n texlive-amscls-doc
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/amscls-doc/

%files -n texlive-amsfonts
%license ofl.txt
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/
%{_texdir}/texmf-dist/fonts/map/dvips/amsfonts/
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/
%{_texdir}/texmf-dist/tex/latex/amsfonts/

%files -n texlive-amsfonts-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/amsfonts/

%files -n texlive-amslatex-primer-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/amslatex-primer/

%files -n texlive-amsldoc-it-doc
%{_texdir}/texmf-dist/doc/latex/amsldoc-it/

%files -n texlive-amsldoc-vn-doc
%license lgpl2.1.txt
%{_texdir}/texmf-dist/doc/latex/amsldoc-vn/

%files -n texlive-amsmath-it-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/amsmath-it/

%files -n texlive-amsmath
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/amsmath/

%files -n texlive-amsmath-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/amsmath/

%files -n texlive-amsrefs
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bib/amsrefs/
%{_texdir}/texmf-dist/bibtex/bst/amsrefs/
%{_texdir}/texmf-dist/tex/latex/amsrefs/

%files -n texlive-amsrefs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/amsrefs/

%files -n texlive-amsthdoc-it-doc
%{_texdir}/texmf-dist/doc/latex/amsthdoc-it/

%files -n texlive-animate
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/animate/

%files -n texlive-animate-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/animate/

%files -n texlive-anonchap
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/anonchap/

%files -n texlive-anonchap-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/anonchap/

%files -n texlive-anonymouspro
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/afm/public/anonymouspro/
%{_texdir}/texmf-dist/fonts/enc/dvips/anonymouspro/
%{_texdir}/texmf-dist/fonts/map/dvips/anonymouspro/
%{_texdir}/texmf-dist/fonts/tfm/public/anonymouspro/
%{_texdir}/texmf-dist/fonts/truetype/public/anonymouspro/
%{_texdir}/texmf-dist/fonts/type1/public/anonymouspro/
%{_texdir}/texmf-dist/fonts/vf/public/anonymouspro/
%{_texdir}/texmf-dist/tex/latex/anonymouspro/

%files -n texlive-anonymouspro-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/anonymouspro/

%files -n texlive-answers
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/answers/

%files -n texlive-answers-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/answers/

%files -n texlive-antiqua
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/urw/antiqua/
%{_texdir}/texmf-dist/fonts/map/dvips/antiqua/
%{_texdir}/texmf-dist/fonts/map/vtex/antiqua/
%{_texdir}/texmf-dist/fonts/tfm/urw/antiqua/
%{_texdir}/texmf-dist/fonts/type1/urw/antiqua/
%{_texdir}/texmf-dist/fonts/vf/urw/antiqua/
%{_texdir}/texmf-dist/tex/latex/antiqua/

%files -n texlive-antiqua-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/antiqua/

%files -n texlive-antomega
%license lppl1.txt
%{_texdir}/texmf-dist/omega/ocp/antomega/
%{_texdir}/texmf-dist/tex/lambda/antomega/

%files -n texlive-antomega-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/omega/antomega/

%files -n texlive-antt
%license gfsl.txt
%{_datadir}/fonts/antt
%{_texdir}/texmf-dist/fonts/afm/public/antt/
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/
%{_texdir}/texmf-dist/fonts/map/dvips/antt/
%{_texdir}/texmf-dist/fonts/opentype/public/antt/
%{_texdir}/texmf-dist/fonts/tfm/public/antt/
%{_texdir}/texmf-dist/fonts/type1/public/antt/
%{_texdir}/texmf-dist/tex/latex/antt/
%{_texdir}/texmf-dist/tex/plain/antt/

%files -n texlive-antt-doc
%license gfsl.txt
%{_texdir}/texmf-dist/doc/fonts/antt/
%{_texdir}/texmf-dist/doc/latex/antt/

%files -n texlive-anufinalexam-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/anufinalexam/

%files -n texlive-anyfontsize
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/anyfontsize/

%files -n texlive-anyfontsize-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/anyfontsize/

%files -n texlive-anysize
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/anysize/

%files -n texlive-anysize-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/anysize/

%files -n texlive-aobs-tikz
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/aobs-tikz/

%files -n texlive-aobs-tikz-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/aobs-tikz/

%files -n texlive-aomart
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/aomart/
%{_texdir}/texmf-dist/tex/latex/aomart/

%files -n texlive-aomart-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/aomart/

%files -n texlive-apa6e
%{_texdir}/texmf-dist/tex/latex/apa6e/

%files -n texlive-apa6e-doc
%{_texdir}/texmf-dist/doc/latex/apa6e/

%files -n texlive-apa6
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/apa6/

%files -n texlive-apa6-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/apa6/

%files -n texlive-apacite
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/apacite/
%{_texdir}/texmf-dist/tex/latex/apacite/

%files -n texlive-apacite-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/bibtex/apacite/

%files -n texlive-apalike2
%{_texdir}/texmf-dist/bibtex/bst/apalike2/

%files -n texlive-apa
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/apa/

%files -n texlive-apa-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/apa/

%files -n texlive-apnum
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/apnum/

%files -n texlive-apnum-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/generic/apnum/

%files -n texlive-appendixnumberbeamer
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/appendixnumberbeamer/

%files -n texlive-appendixnumberbeamer-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/appendixnumberbeamer/

%files -n texlive-appendix
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/appendix/

%files -n texlive-appendix-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/appendix/

%files -n texlive-apprends-latex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/apprends-latex/

%files -n texlive-apptools
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/apptools/

%files -n texlive-apptools-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/apptools/

%files -n texlive-arabi
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/arabi/
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/
%{_texdir}/texmf-dist/fonts/map/dvips/arabi/
%{_texdir}/texmf-dist/fonts/tfm/arabi/
%{_texdir}/texmf-dist/fonts/type1/arabi/
%{_texdir}/texmf-dist/tex/latex/arabi/

%files -n texlive-arabi-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/arabi/

%files -n texlive-arabtex
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/arabtex/
%{_texdir}/texmf-dist/fonts/source/public/arabtex/
%{_texdir}/texmf-dist/fonts/tfm/public/arabtex/
%{_texdir}/texmf-dist/fonts/type1/public/arabtex/
%{_texdir}/texmf-dist/tex/latex/arabtex/

%files -n texlive-arabtex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/arabtex/

%files -n texlive-arabxetex
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/
%{_texdir}/texmf-dist/tex/xelatex/arabxetex/

%files -n texlive-arabxetex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/xelatex/arabxetex/

%files -n texlive-aramaic-serto
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/afm/public/aramaic-serto/
%{_texdir}/texmf-dist/fonts/map/dvips/aramaic-serto/
%{_texdir}/texmf-dist/fonts/source/public/aramaic-serto/
%{_texdir}/texmf-dist/fonts/tfm/public/aramaic-serto/
%{_texdir}/texmf-dist/fonts/type1/public/aramaic-serto/
%{_texdir}/texmf-dist/tex/latex/aramaic-serto/

%files -n texlive-aramaic-serto-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/aramaic-serto/

%files -n texlive-archaic
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/archaic/
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/
%{_texdir}/texmf-dist/fonts/source/public/archaic/
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/
%{_texdir}/texmf-dist/fonts/type1/public/archaic/
%{_texdir}/texmf-dist/tex/latex/archaic/

%files -n texlive-archaic-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/archaic/

%files -n texlive-arcs
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/arcs/

%files -n texlive-arcs-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/arcs/

%files -n texlive-arev
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/arev/
%{_texdir}/texmf-dist/fonts/enc/dvips/arev/
%{_texdir}/texmf-dist/fonts/map/dvips/arev/
%{_texdir}/texmf-dist/fonts/tfm/public/arev/
%{_texdir}/texmf-dist/fonts/type1/public/arev/
%{_texdir}/texmf-dist/fonts/vf/public/arev/
%{_texdir}/texmf-dist/tex/latex/arev/

%files -n texlive-arev-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/arev/

%files -n texlive-armtex
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/armenian/
%{_texdir}/texmf-dist/fonts/map/dvips/armenian/
%{_texdir}/texmf-dist/fonts/source/public/armenian/
%{_texdir}/texmf-dist/fonts/tfm/public/armenian/
%{_texdir}/texmf-dist/fonts/type1/public/armenian/
%{_texdir}/texmf-dist/tex/latex/armenian/
%{_texdir}/texmf-dist/tex/plain/armenian/

%files -n texlive-armtex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/armenian/



%files -n texlive-asana-math
%{_datadir}/fonts/Asana-Math
%{_texdir}/texmf-dist/fonts/opentype/public/Asana-Math/
%{_texdir}/texmf-dist/fonts/truetype/public/Asana-Math/

%files -n texlive-asana-math-doc
%{_texdir}/texmf-dist/doc/fonts/Asana-Math/

%files -n texlive-MemoirChapStyles-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/MemoirChapStyles/

%files -n texlive-Type1fonts-doc
%license fdl.txt
%{_texdir}/texmf-dist/doc/fonts/Type1fonts/

%files -n texlive-ESIEEcv
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ESIEEcv/

%files -n texlive-ESIEEcv-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ESIEEcv/

%files -n texlive-GS1
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/GS1/

%files -n texlive-GS1-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/GS1/

%files -n texlive-HA-prosper
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/HA-prosper/

%files -n texlive-HA-prosper-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/HA-prosper/

%files -n texlive-Tabbing
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/Tabbing/

%files -n texlive-Tabbing-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/Tabbing/

%files -n texlive-IEEEconf
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/IEEEconf/

%files -n texlive-IEEEconf-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/IEEEconf/

%files -n texlive-IEEEtran
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bib/IEEEtran/
%{_texdir}/texmf-dist/bibtex/bst/IEEEtran/
%{_texdir}/texmf-dist/tex/latex/IEEEtran/

%files -n texlive-IEEEtran-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/IEEEtran/

%files -n texlive-SIstyle
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/SIstyle/

%files -n texlive-SIstyle-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/SIstyle/

%files -n texlive-SIunits
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/SIunits/

%files -n texlive-SIunits-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/SIunits/

%files -n texlive-acmart-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/acmart/

%files -n texlive-acmart
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/acmart/
%{_texdir}/texmf-dist/bibtex/bst/acmart/

%files -n texlive-adtrees
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/adtrees/

%files -n texlive-adtrees-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/adtrees/

%files -n texlive-arabi-add-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/arabi-add/

%files -n texlive-arabi-add
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/arabi-add/

%files -n texlive-arabluatex-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/lualatex/arabluatex/

%files -n texlive-arabluatex
%license gpl3.txt
%{_texdir}/texmf-dist/tex/lualatex/arabluatex/

%files -n texlive-archaeologie-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/archaeologie/

%files -n texlive-archaeologie
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/archaeologie/
%{_texdir}/texmf-dist/bibtex/bib/archaeologie/

%files -n texlive-abnt
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist//doc/latex/abnt/
%{_texdir}/texmf-dist/tex/latex/abnt/

%files -n texlive-actuarialsymbol
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/actuarialsymbol/
%{_texdir}/texmf-dist/tex/latex/actuarialsymbol/

%files -n texlive-addfont
%license gpl3.txt
%doc %{_texdir}/texmf-dist/doc/latex/addfont/
%{_texdir}/texmf-dist/tex/latex/addfont/

%files -n texlive-algolrevived
%license ofl.txt lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/fonts/algolrevived/
%{_texdir}/texmf-dist/fonts/enc/dvips/algolrevived/
%{_texdir}/texmf-dist/fonts/map/dvips/algolrevived/
%{_texdir}/texmf-dist/fonts/opentype/public/algolrevived/
%{_texdir}/texmf-dist/fonts/tfm/public/algolrevived/
%{_texdir}/texmf-dist/fonts/type1/public/algolrevived/
%{_texdir}/texmf-dist/fonts/vf/public/algolrevived/
%{_texdir}/texmf-dist/tex/latex/algolrevived/

%files -n texlive-alkalami
%license ofl.txt
%doc %{_texdir}/texmf-dist/doc/fonts/alkalami/
%{_texdir}/texmf-dist/fonts/truetype/public/alkalami/

%files -n texlive-apalike-german
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/bibtex/apalike-german/
%{_texdir}/texmf-dist/bibtex/bst/apalike-german/

%files -n texlive-arimo
%license apache2.txt
%doc %{_texdir}/texmf-dist/doc/fonts/arimo/
%{_texdir}/texmf-dist/fonts/enc/dvips/arimo/
%{_texdir}/texmf-dist/fonts/map/dvips/arimo/
%{_texdir}/texmf-dist/fonts/tfm/google/arimo/
%{_texdir}/texmf-dist/fonts/truetype/google/arimo/
%{_texdir}/texmf-dist/fonts/type1/google/arimo/
%{_texdir}/texmf-dist/fonts/vf/google/arimo/
%{_texdir}/texmf-dist/tex/latex/arimo/

%files -n texlive-algobox
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/algobox/
%doc %{_texdir}/texmf-dist/doc/latex/algobox/

%files -n texlive-adigraph
%{_texdir}/texmf-dist/tex/latex/adigraph
%doc %{_texdir}/texmf-dist/doc/latex/adigraph/

%files -n texlive-aligned-overset
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/aligned-overset/
%doc %{_texdir}/texmf-dist/doc/latex/aligned-overset/

%files -n texlive-apxproof
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/apxproof/
%doc %{_texdir}/texmf-dist/doc/latex/apxproof/


%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
