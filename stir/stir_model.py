import numpy as np
import logging
import sys

import math

def cs(vp,mw):
    try:
        vp = float(vp)
        mw = float(mw)
    except IndexError:
        raise IndexError\
        ('The vapor pressure and/or molecular weight must be '\
        'supplied on the command line.')
    except ValueError:
        raise ValueError\
        ('The vapor pressure must be a real number, not "%mm Hg"' %vp)
    except ValueError:
        raise ValueError\
        ('The molecular weight must be a real number, not "%g/mol"' %mw)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The volume must be greater than zero.')
    if vp < 0:
        raise ValueError\
        ('vp=%g is a non-physical value.' % vp)
    if mw < 0:
        raise ValueError\
        ('mw=%g is a non-physical value.' % mw)
    return (vp * mw * 1000000.0)/(760.0 * 24.45)



# Avian inhalation rate

def ir_avian(aw_avian):
    try:
        aw_avian = float(aw_avian)
    except IndexError:
        raise IndexError\
        ('The body weight of the assessed bird '\
        'must be supplied on the command line.')
    except ValueError:
        raise ValueError\
        ('The body weight must be a real number, not "%kg"' %aw_avian)
    if aw_avian < 0:
        raise ValueError\
        ('aw_avian=%g is a non-physical value.' % aw_avian)
    return 284 * (aw_avian**0.77) * 60.0 * 3


# Maximum avian vapor inhalation dose

def vid_avian(cs,ir_avian,aw_avian):
    try:
        cs = float(cs)
        ir_avian = float(ir_avian)
        aw_avian = float(aw_avian)
    except IndexError:
        raise IndexError\
        ('The vapor air concentration, inhalation rate,'\
        ' and/or body weight of assessed bird must be supplied'\
        ' on the command line.')
    except ValueError:
        raise ValueError\
        ('The vapor air concentration must be a real number, not "%mg/m3"' %cs)
    except ValueError:
        raise ValueError\
        ('The inhalation rate must be a real number, not "%cm3/hr"' %ir_avian)
    except ValueError:
        raise ValueError\
        ('The body weight of the assessed bird must be a real number'\
        ' not "%kg"' %aw_avian)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The body weight of the assessed bird must be greater than zero.')
    if cs < 0:
        raise ValueError\
        ('cs=%g is a non-physical value.' % cs)
    if ir_avian < 0:
        raise ValueError\
        ('ir_avian=%g is a non-physical value.' % ir_avian)
    if aw_avian < 0:
        raise ValueError\
        ('aw_avian=%g is a non-physical value.' % aw_avian)
    return (cs * ir_avian * 1)/(1000000.0 * aw_avian) # 1 (hr) is duration of exposure


# Mammalian inhalation rate

def ir_mammal(aw_mammal):
    try:
        aw_mammal = float(aw_mammal)
    except IndexError:
        raise IndexError\
        ('The body weight of the assessed mammal '\
        'must be supplied on the command line.')
    except ValueError:
        raise ValueError\
        ('The body weight of the assessed mammal must be a real'\
        ' number, not "%kg"' %aw_mammal)
    if aw_mammal < 0:
        raise ValueError\
        ('aw_mammal=%g is a non-physical value.' % aw_mammal)
    return 379.0 * (aw_mammal**0.80) * 60.0 * 3.0


# Maximum mammalian vapor inhalation dose

def vid_mammal(cs,ir_mammal,aw_mammal):
    try:
        cs = float(cs)
        ir_mammal = float(ir_mammal)
        aw_mammal = float(aw_mammal)
    except IndexError:
        raise IndexError\
        ('The vapor air concentration, inhalation rate,'\
        ' and/or body weight of assessed mammal must be supplied'\
        ' on the command line.')
    except ValueError:
        raise ValueError\
        ('The vapor air concentration must be a real number, not "%mg/m3"' %cs)
    except ValueError:
        raise ValueError\
        ('The inhalation rate must be a real number, not "%cm3/hr"' %ir_mammal)
    except ValueError:
        raise ValueError\
        ('The body weight of the assessed mammal must be a real number'\
        ' not "%kg"' %aw_mammal)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The body weight of the assessed mammal must be greater than zero.')
    if cs < 0:
        raise ValueError\
        ('cs=%g is a non-physical value.' % cs)
    if ir_mammal < 0:
        raise ValueError\
        ('ir_mammal=%g is a non-physical value.' % ir_mammal)
    if aw_mammal < 0:
        raise ValueError\
        ('aw_mammal=%g is a non-physical value.' % aw_mammal)
    return (cs * ir_mammal * 1)/(1000000.0 * aw_mammal) # 1 hr = duration of exposure


# Air column concentration after spray

def c_air(ar2,h):
    try:
        ar2 = float(ar2)
        h = float(h)
    except IndexError:
        raise IndexError\
        ('The pesticide application rate and/or height of direct spray column'\
        ' must be supplied on the command line.')
    except ValueError:
        raise ValueError\
        ('The pesticide application rate must be a real number, '\
        ' not "%mg/cm2"' % ar2)
    except ValueError:
        raise ValueError\
        ('The height of the direct spray column must be a real number, '\
        'not "%m"' % h)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The height of the direct spray column must be non-zero.')
    if ar2 < 0:
        raise ValueError\
        ('ar2=%g is a non-physical value.' %ar2)
    if h < 0:
        raise ValueError\
        ('h=%g is a non-physical value.' %h)
    return ar2/(h * 100.0)


# Avian spray droplet inhalation dose

def sid_avian(c_air,ir_avian,ddsi,f_inhaled,aw_avian):
    try:
        c_air = float(c_air)
        ir_avian = float(ir_avian)
        ddsi = float(ddsi)
        f_inhaled = float(f_inhaled)
        aw_avian = float(aw_avian)
    except IndexError:
        raise IndexError\
        ('The droplet concentration of pesticide, inhalation rate, '\
        'duration of exposure, fraction of inhaled spray, and/or body '
        'weight of assessed bird must be supplied on the command line.')
    except ValueError:
        raise ValueError\
        ('The droplet concentration of pesticide must be a real number, '\
        'not "%mg/cm3"' %c_air)
    except ValueError:
        raise ValueError\
        ('The inhalation rate must be a real number, not "%cm3/hr"' %ir_avian)
    except ValueError:
        raise ValueError\
        ('The duration of exposure must be a real number, not "%hr"' %ddsi)
    except ValueError:
        raise ValueError\
        ('The fraction of inhaled spray must be a real number' % f_inhaled)
    except ValueError:
        raise ValueError\
        ('The body weight of the assessed bird must be a real number'\
        ' not "%kg"' %aw_avian)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The body weight of the assessed bird must non-zero.')
    if c_air < 0:
        raise ValueError\
        ('c_air=%g is a non-physical value.' % c_air)
    if ir_avian < 0:
        raise ValueError\
        ('ir_avian=%g is a non-physical value.' % ir_avian)
    if ddsi < 0:
        raise ValueError\
        ('ddsi=%g is a non-physical value.' % ddsi)
    if f_inhaled < 0:
        raise ValueError\
        ('f_inhaled=g% is a non-physical value.' % f_inhaled)
    if aw_avian < 0:
        raise ValueError\
        ('aw_avian=%g is a non-physical value.' % aw_avian)
    return (c_air * ir_avian * ddsi * f_inhaled)/(60.0 * aw_avian)


# Mammalian spray droplet inhalation dose

def sid_mammal(c_air,ir_mammal,ddsi,f_inhaled,aw_mammal):
    try:
        c_air = float(c_air)
        ir_mammal = float(ir_mammal)
        ddsi = float(ddsi)
        f_inhaled = float(f_inhaled)
        aw_mammal = float(aw_mammal)
    except IndexError:
        raise IndexError\
        ('The droplet concentration of pesticide, inhalation rate, '\
        'duration of exposure, fraction of inhaled spray, and/or body '
        'weight of assessed mammal must be supplied on the command line.')
    except ValueError:
        raise ValueError\
        ('The droplet concentration of pesticide must be a real number, '\
        'not "%mg/cm3"' %c_air)
    except ValueError:
        raise ValueError\
        ('The inhalation rate must be a real number, not "%cm3/hr"' %ir_mammal)
    except ValueError:
        raise ValueError\
        ('The duration of exposure must be a real number, not "%hr"' %ddsi)
    except ValueError:
        raise ValueError\
        ('The fraction of inhaled spray must be a real number' % f_inhaled)
    except ValueError:
        raise ValueError\
        ('The body weight of the assessed mammal must be a real number'\
        ' not "%kg"' %aw_mammal)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The body weight of the assessed mammal must non-zero.')
    if c_air < 0:
        raise ValueError\
        ('c_air=%g is a non-physical value.' % c_air)
    if ir_mammal < 0:
        raise ValueError\
        ('ir_mammal=%g is a non-physical value.' % ir_mammal)
    if ddsi < 0:
        raise ValueError\
        ('ddsi=%g is a non-physical value.' % ddsi)
    if f_inhaled < 0:
        raise ValueError\
        ('f_inhaled=g% is a non-physical value.' % f_inhaled)
    if aw_mammal < 0:
        raise ValueError\
        ('aw_mammal=%g is a non-physical value.' % aw_mammal)
    return (c_air * ir_mammal * ddsi * f_inhaled)/(60.0 * aw_mammal)

# Conversion Factor

def cf(ir_mammal, aw_mammal):
    try:
        ir_mammal = float(ir_mammal)
        aw_mammal = float(aw_mammal)
    except IndexError:
        raise IndexError\
        ('The mammalian inhalation rate, and/or body '
        'weight of assessed mammal must be supplied on the command line.')
    except ValueError:
        raise ValueError\
        ('The mammalian inhalation rate must be a real number, '\
        'not "%cm3/hr"' % ir_mammal)
    except ValueError:
        raise ValueError\
        ('The body weight of the assessed mammal must be a real number'\
        ' not "%kg"' %aw_mammal)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The body weight of the assessed mammal must non-zero.')
    if ir_mammal < 0:
        raise ValueError\
        ('ir_mammal=%g is a non-physical value.' % ir_mammal)
    if aw_mammal < 0:
        raise ValueError\
        ('aw_mammal=%g is a non-physical value.' % aw_mammal)
    return ((ir_mammal * 0.001)/aw_mammal)



# Conversion of mammalian LC50 to LD50

def ld50 (lc50,cf,dur):
    try:
        lc50 = float(lc50)
        cf = float(cf)
        dur = float(dur)
    except IndexError:
        raise IndexError\
        ('The lethal concentration, conversion factor, and/or duration'\
        ' of inhalation study must be supplied on the command line.')
    except ValueError:
        raise ValueError\
        ('The lethal concentration must be a real number, '\
        'not "%mg/L"' %lc50)
    except ValueError:
        raise ValueError\
        ('The conversion factor must be a real number, not "%hr"' %cf)
    except ValueError:
        raise ValueError\
        ('The duration of inhalation study must be a real number' % dur)
    if lc50 < 0:
        raise ValueError\
        ('lc50=%g is a non-physical value.' % lc50)
    if cf < 0:
        raise ValueError\
        ('cf=%g is a non-physical value.' % cf)
    if dur < 0:
        raise ValueError\
        ('dur=g% is a non-physical value.' % dur)
    return lc50 * 1 * cf * dur * 1 # Absorption is assumed to be 100% = 1 -- Activity Factor = 1 (reflects the rat at rest in the experimental conditions)


# Adjusted mammalian inhalation LD50

def ld50adj_mammal(ld50,tw_mammal,aw_mammal):
    try:
        ld50 = float(ld50)
        tw_mammal = float(tw_mammal)
        aw_mammal = float(aw_mammal)
    except IndexError:
        raise IndexError\
        ('The lethal dose, body weight of the tested mammal, and/or body '\
        'weight of assessed mammal must be supplied on the command line.')
    except ValueError:
        raise ValueError\
        ('The lethal dose must be a real number, not "%mg/kg"' %ld50)
    except ValueError:
        raise ValueError\
        ('The body weight of the tested animal must be a real number, not'\
        ' "%cm3/hr"' %tw_mammal)
    except ValueError:
        raise ValueError\
        ('The body weight of the assessed mammal must be a real number'\
        ' not "%kg"' %aw_mammal)
    if ld50 < 0:
        raise ValueError\
        ('ld50=%g is a non-physical value.' % ld50)
    if tw_mammal < 0:
        raise ValueError\
        ('tw_mammal=%g is a non-physical value.' % tw_mammal)
    if aw_mammal < 0:
        raise ValueError\
        ('aw_mammal=%g is a non-physical value.' % aw_mammal)
    return ld50 * (tw_mammal/aw_mammal)**0.25


# Estimated avian inhalation LD50

def ld50est(ld50ao,ld50ri,ld50ro):
    try:
        ld50ao = float(ld50ao)
        ld50ri = float(ld50ri)
        ld50ro = float(ld50ro)
    except IndexError:
        raise IndexError\
        ('The avian oral LD50, rat inhalation LD50, and/or rat oral LD50 '\
        'must be supplied on the command line.')
    except ValueError:
        raise ValueError\
        ('The avian oral LD50 of pesticide must be a real number, '\
        'not "%mg/kg"' %ld50ao)
    except ValueError:
        raise ValueError\
        ('The rat inhalation LD50 must be a real number, not "%mg/kg"' % ld50ri)
    except ValueError:
        raise ValueError\
        ('The rat oral LD50 must be a real number, not "%mg/kg"' %ld50ro)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The rat oral LD50 must non-zero.')
    if ld50ao < 0:
        raise ValueError\
        ('ld50ao=%g is a non-physical value.' % ld50ao)
    if ld50ri < 0:
        raise ValueError\
        ('ld50ri=%g is a non-physical value.' % ld50ri)
    if ld50ro < 0:
        raise ValueError\
        ('ld50ro%g is a non-physical value.' % ld50ro)
    return (ld50ao * ld50ri)/(3.5 * ld50ro)


# Adjusted avian inhalation LD50

def ld50adj_avian(ld50est,aw_avian,tw_avian,mineau):
    try:
        ld50est = float(ld50est)
        aw_avian = float(aw_avian)
        tw_avian = float(tw_avian)
        mineau = float(mineau)
    except IndexError:
        raise IndexError\
        ('The estimated avian inhalation LD50, body weight of the assessed'\
        ' bird, body weight of the tested bird,  and/or Mineau scaling factor '
        ' for birds must be supplied on the command line.')
    except ValueError:
        raise ValueError\
        ('The estimated avian inhalation LD50 must be a real number, '\
        'not "%mg/kg"' % ld50est)
    except ValueError:
        raise ValueError\
        ('The body weight of the assessed bird must be a real number,'\
        ' not "%kg"' % aw_avian)
    except ValueError:
        raise ValueError\
        ('The body weight of the tested bird must be a real number, '\
        'not "%kg"' % tw_avian)
    except ValueError:
        raise ValueError\
        ('The Mineau scaling factor for bords must be a real number' % mineau)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The body weight of the tested bird must non-zero.')
    if ld50est < 0:
        raise ValueError\
        ('ld50est=%g is a non-physical value.' % ld50est)
    if aw_avian < 0:
        raise ValueError\
        ('aw_avian=%g is a non-physical value.' % aw_avian)
    if tw_avian < 0:
        raise ValueError\
        ('tw_avian=%g is a non-physical value.' % tw_avian)
    if mineau < 0:
        raise ValueError\
        ('mineau=g% is a non-physical value.' % mineau)
    return ld50est * (aw_avian/tw_avian)**(mineau - 1)

# ----------------------------------------------
# Ratio of avian vapor dose to adjusted inhalation LD50

def ratio_vd_avian(vid_avian,ld50adj_avian):
    try:
        vid_avian = float(vid_avian)
        ld50adj_avian = float(ld50adj_avian)
    except IndexError:
        raise IndexError\
        ('The avian vapor inhalation dose and/or adjusted avian inhalation LD50'\
        ' must be supplied on the command line. ')
    except ValueError:
        raise ValueError\
        ('The avian vapor inhalation dose must be a real number,'\
        ' not "%mg/kg"' %vid_avian)
    except ValueError:
        raise ValueError\
        ('The adjusted avian inhalation LD50 must be a real number, '\
        'not"%mg/kg"' %ld50adj_avian)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The adjusted avian inhalation LD50 must be non-zero.')
    if vid_avian < 0:
        raise ValueError\
        ('vid_avian=%g is a non-physical value.' %vid_avian)
    if ld50adj_avian < 0:
        raise ValueError\
        ('ld50adj_avian=%g is a non-physical value' %ld50adj_avian)
    return vid_avian/ld50adj_avian

# Level of Concern for avian vapor phase risk

def LOC_vd_avian(ratio_vd_avian):
    if ratio_vd_avian < 0.1:
        return ('Exposure not Likely Significant')
    else:
        return ('Proceed to Refinements')


# Ratio of avian droplet inhalation dose to adjusted inhalation LD50

def ratio_sid_avian(sid_avian,ld50adj_avian):
    try:
        sid_avian = float(sid_avian)
        ld50adj_avian = float(ld50adj_avian)
    except IndexError:
        raise IndexError\
        ('The avian spray droplet inhalation dose and/or adjusted avian inhalation LD50'\
        ' must be supplied on the command line. ')
    except ValueError:
        raise ValueError\
        ('The avian spray droplet inhalation dose must be a real number,'\
        ' not "%mg/kg"' %sid_avian)
    except ValueError:
        raise ValueError\
        ('The adjusted avian inhalation LD50 must be a real number, '\
        'not"%mg/kg"' %ld50adj_avian)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The adjusted avian inhalation LD50 must be non-zero.')
    if sid_avian < 0:
        raise ValueError\
        ('sid_avian=%g is a non-physical value.' %sid_avian)
    if ld50adj_avian < 0:
        raise ValueError\
        ('ld50adj_avian=%g is a non-physical value' %ld50adj_avian)
    return sid_avian/ld50adj_avian

# Level of Concern for avian droplet inhalation risk

def LOC_sid_avian(ratio_sid_avian):
    if ratio_sid_avian < 0.1:
        return ('Exposure not Likely Significant')
    else:
        return ('Proceed to Refinements')

# Ratio of mammalian vapor dose to adjusted inhalation LD50

def ratio_vd_mammal(vid_mammal,ld50adj_mammal):
    try:
        vid_mammal = float(vid_mammal)
        ld50adj_mammal = float(ld50adj_mammal)
    except IndexError:
        raise IndexError\
        ('The mammalian vapor inhalation dose and/or adjusted mammalian'\
        ' inhalation LD50 must be supplied on the command line. ')
    except ValueError:
        raise ValueError\
        ('The mammalian vapor inhalation dose must be a real number,'\
        ' not "%mg/kg"' %vid_mammal)
    except ValueError:
        raise ValueError\
        ('The adjusted mammalian inhalation LD50 must be a real number, '\
        'not"%mg/kg"' %ld50adj_mammal)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The adjusted mammalian inhalation LD50 must be non-zero.')
    if vid_mammal < 0:
        raise ValueError\
        ('vid_mammal=%g is a non-physical value.' %vid_mammal)
    if ld50adj_mammal < 0:
        raise ValueError\
        ('ld50adj_mammal=%g is a non-physical value' %ld50adj_mammal)
    return vid_mammal/ld50adj_mammal

# Level of Concern for mammalian vapor phase risk

def LOC_vd_mammal(ratio_vd_mammal):
    if ratio_vd_mammal < 0.1:
        return ('Exposure not Likely Significant')
    else:
        return ('Proceed to Refinements')


# Ratio of mammalian droplet inhalation dose to adjusted inhalation LD50

def ratio_sid_mammal(sid_mammal,ld50adj_mammal):
    try:
        sid_mammal = float(sid_mammal)
        ld50adj_mammal = float(ld50adj_mammal)
    except IndexError:
        raise IndexError\
        ('The mammalian spray droplet inhalation dose and/or adjusted mammalian'\
        ' inhalation LD50 must be supplied on the command line. ')
    except ValueError:
        raise ValueError\
        ('The mammalian spray droplet inhalation dose must be a real number,'\
        ' not "%mg/kg"' %sid_mammal)
    except ValueError:
        raise ValueError\
        ('The adjusted mammalian inhalation LD50 must be a real number, '\
        'not"%mg/kg"' %ld50adj_mammal)
    except ZeroDivisionError:
        raise ZeroDivisionError\
        ('The adjusted mammalian inhalation LD50 must be non-zero.')
    if sid_mammal < 0:
        raise ValueError\
        ('sid_mammal=%g is a non-physical value.' %sid_mammal)
    if ld50adj_mammal < 0:
        raise ValueError\
        ('ld50adj_mammal=%g is a non-physical value' %ld50adj_mammal)
    return sid_mammal/ld50adj_mammal

# Level of Concern for mammaliam droplet inhalation risk

def LOC_sid_mammal(ratio_sid_mammal):
    if ratio_sid_mammal < 0.1:
        return ('Exposure not Likely Significant')
    else:
        return ('Proceed to Refinements')