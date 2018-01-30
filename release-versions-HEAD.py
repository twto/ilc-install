###########################################
#
# iLCSoft versions for installing a current HEAD
# version of the ilcsoft packages.
# The external base tools need to be installed
#
# DESY ilcsoft team
###########################################
import datetime

# --------- ilcsoft release version ------------------------------------------
today = str( datetime.date.today() )
ilcsoft_release='HEAD-'+today

# ----------------------------------------------------------------------------

#-----------------------
# we now always build with c++11 ?
use_cpp11 = True

#===============================================================================
# use a compiler that knows c++11, run
#
# before starting the installation
#================================================================================



# --------- install dir ------------------------------------------------------
# ===========================================================
# Modify this path to where you want to install the software
# ===========================================================
#


#ilcsoft_install_prefix = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6/"
#ilcsoft_install_prefix = "/nfs/dust/ilc/user/voutsina/testarea/ilcsoft_c11/"
ilcsoft_install_prefix = "/ilcsoft/"



ilcPath = ilcsoft_install_prefix


# ======================= PACKAGES WITH NO INSTALL SUPPORT ===================

# these packages need to be pre-installed for your system
# please adjust the path variables accordingly

# ----- mysql --------------------------------------------------------
MySQL_version = "5.7.21"
MySQL_path = "/usr"


#------ boost headers files ------------------------------------------
Boost_path = "/usr"

#------ Eigen headers files ------------------------------------------
Eigen_path =  "/usr"
# ----------------------------------------------------------------------------

##########################################################################################
#
#  end of user configuration section
#  only make changes below if you know what you are doing ...
#
##########################################################################################



# ======================= PACKAGE VERSIONS ===================================

Geant4_version =  "10.02.p02"
CLHEP_version =  "2.3.1.1"

# Geant4_version =  "10.03.p02"
# CLHEP_version =  "2.3.4.3"

ROOT_version = "6.12.04"

GSL_version = "2.1"

QT_version = "4.7.4"

CMake_version = "3.6.3"

CED_version = "HEAD" #""v01-09-02"

# -------------------------------------------

LCIO_version = "HEAD"

GEAR_version = "HEAD"

CondDBMySQL_version = "HEAD"

ILCUTIL_version = "HEAD"

FastJet_version = "3.2.0"
FastJetcontrib_version = "1.024"

MarlinFastJet_version = "HEAD"


# -------------------------------------------

KalTest_version = "HEAD" # "v02-00"

KalDet_version = "HEAD" # "v01-13-02"

aidaTT_version = "HEAD" # "v00-02"

DDKalTest_version = "HEAD" # "v00-02"

MarlinTrk_version = "HEAD" # "v02-00-01"

MarlinTrkProcessors_version = "HEAD" # "v02-01"

Clupatra_version = "HEAD" # "v00-12"

KiTrack_version = "HEAD" # "v01-06"

KiTrackMarlin_version = "HEAD" # "v01-07"

ForwardTracking_version = "HEAD" # "v01-08"

ConformalTracking_version = "HEAD" # "v01-08"

LICH_version = "HEAD" # "v01-08"

# -------------------------------------------

GBL_version = "HEAD" # "V01-16-04"

LCCD_version = "HEAD" # "v01-03"

RAIDA_version = "HEAD" # "v01-06-02"

MarlinUtil_version = "HEAD" # "v01-10"

Marlin_version = "HEAD" # "v01-07"

MarlinDD4hep_version = "HEAD" # "v00-01"

DDMarlinPandora_version = "HEAD" # "v00-01"

Mokka_version = "HEAD" # "mokka-08-05"
MarlinReco_version = "HEAD" # "v01-13"

FCalClusterer_version = "HEAD" # "v00-01"

ILDPerformance_version = "HEAD" # "v00-01"
ClicPerformance_version = "HEAD" # "v00-01"

ILDConfig_version = "HEAD"


LCFIVertex_version = "HEAD" # "v00-07"
LCFIPlus_version = "HEAD" # "v00-05-03"


MarlinKinfit_version = "HEAD" # "v00-01-05"
MarlinKinfitProcessors_version = "HEAD" # "v00-01-05"

PandoraPFANew_version = "HEAD" # "v02-00-00"
MarlinPandora_version = "HEAD" # "v02-00-00"
PandoraAnalysis_version = "HEAD" # "v01-00-01"

CEDViewer_version = "HEAD" # "v01-10"

Overlay_version = "HEAD" # "v00-20"

PathFinder_version = "HEAD" #  "v00-06"

MarlinTPC_version = "HEAD" # "v01-00"

LCTuple_version = "HEAD" # "v01-04"

BBQ_version = "HEAD" #  "v00-01-02"

Druid_version = "HEAD" # "2.2" # "1.8"

Garlic_version = "HEAD" # "v3.0.3"

DD4hep_version = "HEAD" # "v00-14"

DD4hepExamples_version = "HEAD" # "v00-14"

lcgeo_version = "HEAD" # "v00-05"

Physsim_version = "HEAD" # "v00-02"

ConformalTracking_version = "HEAD"

LICH_version = "HEAD"

# xerces-c (needed by geant4 for building gdml support - required by mokka)
XERCESC_ROOT_DIR = ilcPath + "/xercesc/3.2.0"

XercesC_version = "3.2.0"



