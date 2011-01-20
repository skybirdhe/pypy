# Generated by h2py from f:/emx/include/netinet/in.h

# Included from sys/param.h
PAGE_SIZE = 0x1000
HZ = 100
MAXNAMLEN = 260
MAXPATHLEN = 260
def htonl(X): return _swapl(X)

def ntohl(X): return _swapl(X)

def htons(X): return _swaps(X)

def ntohs(X): return _swaps(X)

IPPROTO_IP = 0
IPPROTO_ICMP = 1
IPPROTO_IGMP = 2
IPPROTO_GGP = 3
IPPROTO_TCP = 6
IPPROTO_EGP = 8
IPPROTO_PUP = 12
IPPROTO_UDP = 17
IPPROTO_IDP = 22
IPPROTO_TP = 29
IPPROTO_EON = 80
IPPROTO_RAW = 255
IPPROTO_MAX = 256
IPPORT_RESERVED = 1024
IPPORT_USERRESERVED = 5000
def IN_CLASSA(i): return (((long)(i) & 0x80000000) == 0)

IN_CLASSA_NET = 0xff000000
IN_CLASSA_NSHIFT = 24
IN_CLASSA_HOST = 0x00ffffff
IN_CLASSA_MAX = 128
def IN_CLASSB(i): return (((long)(i) & 0xc0000000) == 0x80000000)

IN_CLASSB_NET = 0xffff0000
IN_CLASSB_NSHIFT = 16
IN_CLASSB_HOST = 0x0000ffff
IN_CLASSB_MAX = 65536
def IN_CLASSC(i): return (((long)(i) & 0xe0000000) == 0xc0000000)

IN_CLASSC_NET = 0xffffff00
IN_CLASSC_NSHIFT = 8
IN_CLASSC_HOST = 0x000000ff
def IN_CLASSD(i): return (((long)(i) & 0xf0000000) == 0xe0000000)

IN_CLASSD_NET = 0xf0000000
IN_CLASSD_NSHIFT = 28
IN_CLASSD_HOST = 0x0fffffff
def IN_MULTICAST(i): return IN_CLASSD(i)

def IN_EXPERIMENTAL(i): return (((long)(i) & 0xe0000000) == 0xe0000000)

def IN_BADCLASS(i): return (((long)(i) & 0xf0000000) == 0xf0000000)

INADDR_ANY = 0x00000000
INADDR_LOOPBACK = 0x7f000001
INADDR_BROADCAST = 0xffffffff
INADDR_NONE = 0xffffffff
INADDR_UNSPEC_GROUP = 0xe0000000
INADDR_ALLHOSTS_GROUP = 0xe0000001
INADDR_MAX_LOCAL_GROUP = 0xe00000ff
IN_LOOPBACKNET = 127
IP_OPTIONS = 1
IP_MULTICAST_IF = 2
IP_MULTICAST_TTL = 3
IP_MULTICAST_LOOP = 4
IP_ADD_MEMBERSHIP = 5
IP_DROP_MEMBERSHIP = 6
IP_HDRINCL = 2
IP_TOS = 3
IP_TTL = 4
IP_RECVOPTS = 5
IP_RECVRETOPTS = 6
IP_RECVDSTADDR = 7
IP_RETOPTS = 8
IP_DEFAULT_MULTICAST_TTL = 1
IP_DEFAULT_MULTICAST_LOOP = 1
IP_MAX_MEMBERSHIPS = 20
