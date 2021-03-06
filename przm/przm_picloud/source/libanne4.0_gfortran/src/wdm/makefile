# Makefile for wdm

include ../make.inc
#
# Usage:  make [libdir=path_to_install_to] [install] [| tee makeout]
#
# Examples:  make
#            make install libdir=/usr/lib
#            make install libdir=$HOME/lib
#
# History:  95/12/05 kmflynn
#           99/07/30 kmflynn

FFVrsn  = $(FFUnix)         # Version FF[Unix, AIX]
SymTbl  = $(BSD)            # symbol table (BSD or SYS_V)

#*******************************************************************
#*****   Some things may need to be changed below this line.   *****
#*******************************************************************

# Compiler flags
#    C - check subranges and array bounds
#    u - default data type for undeclareds is undefined
#    g - generate source level symbolic debug information
# ansi - compile in accordance with rules for ANSI C, flag violations
#    O - optimization
# (NOTES: to generate debug code - set FFLAGS to Dbgf
#            for production code - set FFLAGS to OptM
DbgF   = -u -C -g
OptM   = -u -O

# compile options, use Unix for default
FFUnix =
FFAIX  = -qxlf77=leadzero        # force leading zero on output

# symbol table for library archive may need to be explicitly built;
# System V ar does this automatically (DG and AIX)
# BSD ar does not (Sun)
BSD    = ranlib $@
SYS_V  = @echo
#        note:  some makes have a problem with SYS_V being blank,
#               use an empty echo.

# library archive options
#    r - replace the named files in the archive file
#    v - give a verbose file-by-file description of the making
#    c - suppress the message that is produced by default when
#        the archive file is created
#    q - quickly append the named files to the end of the
#        archive file
ArOpt = rv

# this description file uses the Bourne shell
SHELL = /bin/sh

#*******************************************************************
#***** You should not need to modify anything below this line. *****
#*******************************************************************

library = wdmlib.a
Objects = wdbtch.o wdatrb.o wdatm2.o wdsptm.o wdimpt.o wdexpt.o \
          wdtms2.o wdtms1.o wdtble.o wdtbl2.o wddlg.o  wdatru.o \
          tsbufr.o wdtms3.o wdmid.o
Sadwdm  = cfbuff.inc cdrloc.inc

libdir  = ../../lib
binary  = ../../lib
libMake = $(binary)/$(library)
libInst = $(libdir)/$(library)

# Rules
all: includes $(binary) $(libMake) install
	@echo "***"
	@echo "*** Done making all for $(library), files are now up-to-date."
	@echo "***"

# Library and utility dependencies:
$(libMake):   $(Objects)
	@echo "***"
	@echo "*** making $(libMake)"
	@echo "***"
	ar $(ArOpt) $@ $?
	$(SymTbl)
$(binary):
	@if [ ! -d $(binary) ]   ; then   \
	   mkdir $(binary)  ;             \
	   echo "*** Created $(binary)" ; \
	fi
install:
# Create directory for binary file, if necessary
	@if [ ! -d $(libdir) ]   ; then   \
	   mkdir $(libdir) ;              \
	   echo "*** Created $(libdir)" ; \
	fi
# Link executable to libdir if installing elsewhere
	@if [ ! -s $(libMake) ] ; then                                   \
	   echo "*** library $(libMake) does not exist," ;               \
	   echo "*** use one of the following commands to generate it:"; \
	   echo "***     make" ;  echo "***     make all" ;              \
	else                                                             \
	   if [ $(libdir) != $(binary) ] ; then                          \
	      rm -f $(libInst) ;                                         \
	      cd ../..; ln -s `pwd`/lib/$(library) $(libInst);           \
	      cd ./src/wdm ;                                             \
	      echo "*** Library $(libInst) has been updated.";           \
	   fi ;                                                          \
	fi
clean:
	@if [ $(libdir) != $(binary) ] ; then rm -f $(libInst) ; fi
	@rm -f *.o $(libMake)
	@echo "***"
	@echo "*** Removed files generated by make for $(library)."
	@echo "***"
includes:
	@for inc in $(Sadwdm) ; do                                          \
	   if [ -f $$inc ] ; then                                           \
	     if diff $$inc ../adwdm/$$inc ; then                            \
	        continue ;                                                  \
	     else                                                           \
	        echo "*** NOTICE:--different $$inc appended to ERROR.inc" ; \
	        echo "***" ;                                                \
	        echo "***          different $$inc, `date`" >> ERROR.inc ;  \
	        cat $$inc >> ERROR.inc ;                                    \
	        rm $$inc ;                                                  \
	        cp ../adwdm/$$inc . ;                                       \
	     fi ;                                                           \
	   else                                                             \
	     echo "*** NOTICE:--copying missing $$inc from ../adwdm" ;      \
	     cp ../adwdm/$$inc . ;                                          \
	   fi ;                                                             \
	done

# Define object file dependencies:
tsbufr.o: ctsbuf.inc
wdatrb.o: fversn.inc cfbuff.inc cdrloc.inc
wdbtch.o: cfbuff.inc cdrloc.inc
wddlg.o:  cfbuff.inc
wdexpt.o: ctblab.inc cfbuff.inc
wdmid.o:  cwdmid.inc
wdsptm.o: cfbuff.inc
wdtble.o: cfbuff.inc
wdtms1.o: cwtsds.inc cfbuff.inc
wdtms2.o: cfbuff.inc
wdtms3.o: cwtsds.inc cfbuff.inc

# end of make
