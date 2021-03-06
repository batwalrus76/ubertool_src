# Makefile for awstat

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

library = awstatlib.a
Objects = stutil.o profdr.o tscmpr.o tscbat.o \
          a193.o   a193ut.o a193io.o a193pl.o \
          pkplot.o

libdir  = ../../lib
binary  = ../../lib
libMake = $(binary)/$(library)
libInst = $(libdir)/$(library)

# Rules
all: $(binary) $(libMake) install
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
	      cd ./src/awstat ;                                          \
	      echo "*** Library $(libInst) has been updated.";           \
	   fi ;                                                          \
	fi
clean:
	@if [ $(libdir) != $(binary) ] ; then rm -f $(libInst) ; fi
	@rm -f *.o $(libMake)
	@echo "***"
	@echo "*** Removed files generated by make for $(library)."
	@echo "***"

# Define object file dependencies:
a193.f:    pa193.inc
a193pl.o:  pa193.inc
a193ut.o:  pa193.inc
tscmpr.o:  fversn.inc
pkplot.o:  pmxpk.inc

# end of make
