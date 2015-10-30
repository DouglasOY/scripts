#!/bin/bash

#----------------------------------------
# Set Script Name variable
#----------------------------------------
SCRIPT=`basename ${BASH_SOURCE[0]}`

#----------------------------------------
# Set fonts for Help.
#----------------------------------------
NORM=`tput sgr0`
BOLD=`tput bold`
REV=`tput smso`

#----------------------------------------
# Help function
#----------------------------------------
function HELP {
    echo "${REV}Usage:  ${NORM}       ${BOLD}${SCRIPT} [--arga=<ARGA>] --argb --argc=<ARGC> file.ext${NORM}"
    echo ""
    echo "${REV}Options:${NORM}"
    echo "-a, --arga    the value for option arga, default is A"
    echo "-b, --argb    the value for option argb, default is B"
    echo "-c, --argc    the value for option argc, default is C"
    echo "-h, --help    display this help message"
    echo ""
    echo "${REV}Example:${NORM}      ${BOLD}${SCRIPT} -afoo -b -cbar others${NORM}"
    echo "              ${BOLD}${SCRIPT} --arga=foo --argb --argc=bar file.ext${NORM}"
    exit 1
}

#----------------------------------------
# If no arguments, print help and exit.
#----------------------------------------
if [ $# -eq 0 ]; then HELP; fi

#----------------------------------------
# read the options
#----------------------------------------
OPTTEMP=`getopt -o a::bc:h --long arga::,argb,argc:,help -n "${SCRIPT}" -- "$@"`
if [ $? -ne 0 ] ; then echo "Incorrect options provided"; exit 1; fi
eval set -- "${OPTTEMP}"

#----------------------------------------
# “a” and “arga” have optional arguments with default values.
# “b” and “argb” have no arguments, acting as sort of a flag.
# “c” and “argc” have required arguments.
# set an initial value for the flag
#----------------------------------------
ARG_A=default
ARG_B=False
ARG_C=NULL
ARG_O=other

#----------------------------------------
# extract options and their arguments into variables.
#----------------------------------------
while true ; do
    case "$1" in
        -a|--arga)
            case "$2" in
                "") ARG_A='some default value' ; shift 2 ;;
                *) ARG_A=$2 ; shift 2 ;;
            esac ;;
        -b|--argb) ARG_B=True ; shift ;;
        -c|--argc)
            case "$2" in
                "") shift 2 ;;
                *) ARG_C=$2 ; shift 2 ;;
            esac ;;
        -h|--help) HELP ;;
        --) ARG_O=$2; shift ; break ;;
        *) echo "Internal error!" ; exit 1 ;;
    esac
done

#----------------------------------------
# do something with the variables -- in this case the lamest possible one :-)
#----------------------------------------
echo "ARG_A = ${ARG_A}"
echo "ARG_B = ${ARG_B}"
echo "ARG_C = ${ARG_C}"
echo "ARG_O = ${ARG_O}"


