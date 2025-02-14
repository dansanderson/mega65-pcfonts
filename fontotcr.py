#!/usr/bin/env python3
#
# Generate MEGA65 TCR files from the Oldschool PC Fonts Resource.
#
# Based on dewinfont, originally by Simon Tatham, modified by juanitogan.
# https://github.com/juanitogan/mkwinfont/blob/master/python/dewinfont.py

# dewinfont is copyright 2001 Simon Tatham. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys

FON_FILES = [
    'Bm437_ACM_VGA_8x16.FON',
    'Bm437_ATI_8x16.FON',
    'Bm437_ATT_PC6300.FON',
    'Bm437_CL_EagleIII_8x16.FON',
    'Bm437_CL_EagleII_8x16.FON',
    'Bm437_CL_Stingray_8x16.FON',
    'Bm437_Compaq_Port3.FON',
    'Bm437_CompaqThin_8x16.FON',
    'Bm437_Compis.FON',
    'Bm437_DOS-V_TWN16.FON',
    'Bm437_DOS-V_re_ANK16.FON',
    'Bm437_DOS-V_re_JPN16.FON',
    'Bm437_DOS-V_re_PRC16.FON',
    'Bm437_EverexME_8x16.FON',
    'Bm437_FMTowns_re_8x16.FON',
    'Bm437_IBM_DOS_ISO8.FON',
    'Bm437_IBM_Model30r0.FON',
    'Bm437_IBM_Model3x_Alt1.FON',
    'Bm437_IBM_Model3x_Alt2.FON',
    'Bm437_IBM_Model3x_Alt3.FON',
    'Bm437_IBM_Model3x_Alt4.FON',
    'Bm437_IBM_PGC.FON',
    'Bm437_IBM_VGA_8x16.FON',
    'Bm437_IGS_VGA_8x16.FON',
    'Bm437_MBytePC230_8x16.FON',
    'Bm437_NEC_APC3_8x16.FON',
    'Bm437_Nix8810_M15.FON',
    'Bm437_Nix8810_M16.FON',
    'Bm437_OlivettiThin_8x16.FON',
    'Bm437_PhoenixEGA_8x16.FON',
    'Bm437_PhoenixVGA_8x16.FON',
    'Bm437_Robotron_A7100.FON',
    'Bm437_Sigma_RM_8x16.FON',
    'Bm437_SperryPC_8x16.FON',
    'Bm437_Tandy2K.FON',
    'Bm437_Tandy2K_G.FON',
    'Bm437_ToshibaSat_8x16.FON',
    'Bm437_ToshibaT300_8x16.FON',
    'Bm437_ToshibaTxL1_8x16.FON',
    'Bm437_ToshibaTxL2_8x16.FON',
    'Bm437_TridentEarly_8x16.FON',
    'Bm437_Trident_8x16.FON',
    'Bm437_Verite_8x16.FON',
]


class FbError(Exception):
    pass


cnum_to_scrcode_dict = dict((n, n) for n in range(256))
for n in range(1, 32):  # 1-31 -> 95-124
    cnum_to_scrcode_dict[n] = n+94
cnum_to_scrcode_dict[64] = 0    # @
cnum_to_scrcode_dict[91] = 27   # [
cnum_to_scrcode_dict[92] = 28   # / (pnd)
cnum_to_scrcode_dict[93] = 29   # ]
cnum_to_scrcode_dict[94] = 30   # ^ (uparr)
cnum_to_scrcode_dict[95] = 31   # _ (leftarr)
cnum_to_scrcode_dict[96] = 64   # ` (horiz bar)
for n in range(97, 123):  # a-z  -> 1-26
    cnum_to_scrcode_dict[n] = n-96
cnum_to_scrcode_dict[123] = 91  # {
cnum_to_scrcode_dict[124] = 92  # |
cnum_to_scrcode_dict[125] = 93  # }
cnum_to_scrcode_dict[126] = 94  # ~


def isfon(data):
    "Determine if a file is a .FON or a .FNT format font."
    if data[0:2] == b"MZ":
        return 1  # FON
    else:
        return 0  # FNT


class font:
    pass


class char:
    pass


def frombyte(s):
    return s[0]


def fromword(s):
    return frombyte(s[0:1]) + 256 * frombyte(s[1:2])


def fromdword(s):
    return fromword(s[0:2]) | (fromword(s[2:4]) << 16)


def asciz(s):
    i = s.find(b"\0")
    if i != -1:
        s = s[:i]
    return s


def dofnt(fnt):
    "Create an internal font description from a .FNT-shaped string."
    f = font()
    f.chars = [None] * 256
    version = fromword(fnt[0:])
    ftype = fromword(fnt[0x42:])
    if ftype & 1:
        raise FbError('This font is a vector font')
    off_facename = fromdword(fnt[0x69:])
    if off_facename < 0 or off_facename > len(fnt):
        raise FbError('Face name not contained within font data')
    f.facename = str(asciz(fnt[off_facename:]), encoding="windows-1252")
    f.copyright = str(asciz(fnt[6:66] + b"\0"), encoding="windows-1252")
    f.pointsize = fromword(fnt[0x44:])
    f.ascent = fromword(fnt[0x4A:])
    f.inleading = fromword(fnt[0x4C:])
    f.exleading = fromword(fnt[0x4E:])
    f.height = fromword(fnt[0x58:])
    f.italic = frombyte(fnt[0x50:]) != 0
    f.underline = frombyte(fnt[0x51:]) != 0
    f.strikeout = frombyte(fnt[0x52:]) != 0
    f.weight = fromword(fnt[0x53:])
    f.charset = frombyte(fnt[0x55:])
    # Read the char table.
    if version == 0x200:
        ctstart = 0x76
        ctsize = 4
    else:
        ctstart = 0x94
        ctsize = 6
    for i in range(256):
        f.chars[i] = char()
        f.chars[i].width = 0
        f.chars[i].data = [0] * f.height
    firstchar = frombyte(fnt[0x5F:])
    lastchar = frombyte(fnt[0x60:])
    for i in range(firstchar, lastchar + 1):
        entry = ctstart + ctsize * (i-firstchar)
        w = fromword(fnt[entry:])
        f.chars[i].width = w
        if ctsize == 4:
            off = fromword(fnt[entry+2:])
        else:
            off = fromdword(fnt[entry+2:])
        widthbytes = (w + 7) // 8
        for j in range(f.height):
            for k in range(widthbytes):
                bytepos = off + k * f.height + j
                f.chars[i].data[j] = f.chars[i].data[j] << 8
                f.chars[i].data[j] |= frombyte(fnt[bytepos:])
            f.chars[i].data[j] = f.chars[i].data[j] >> (8*widthbytes - w)
    return f


def nefon(fon, neoff):
    "Finish splitting up a NE-format FON file."
    ret = []
    # Find the resource table.
    rtable = fromword(fon[neoff + 0x24:])
    rtable = rtable + neoff
    # Read the shift count out of the resource table.
    shift = fromword(fon[rtable:])
    # Now loop over the rest of the resource table.
    p = rtable+2
    while 1:
        rtype = fromword(fon[p:])
        if rtype == 0:
            break  # end of resource table
        count = fromword(fon[p+2:])
        p = p + 8  # type, count, 4 bytes reserved
        for i in range(count):
            start = fromword(fon[p:]) << shift
            size = fromword(fon[p+2:]) << shift
            if start < 0 or size < 0 or start+size > len(fon):
                sys.stderr.write("Resource overruns file boundaries\n")
                return None
            if rtype == 0x8008:  # this is an actual font
                font = dofnt(fon[start:start+size])
                if font is None:
                    raise FbError(f'Failed to read font resource at {start}')
                ret = ret + [font]
            p = p + 12  # start, size, flags, name/id, 4 bytes reserved
    return ret


def pefon(fon, peoff):
    "Finish splitting up a PE-format FON file."
    dirtables = []
    dataentries = []

    def gotoffset(off, dirtables=dirtables, dataentries=dataentries):
        if off & 0x80000000:
            off = off & ~0x80000000
            dirtables.append(off)
        else:
            dataentries.append(off)

    def dodirtable(rsrc, off, rtype, gotoffset=gotoffset):
        number = fromword(rsrc[off+12:]) + fromword(rsrc[off+14:])
        for i in range(number):
            entry = off + 16 + 8*i
            thetype = fromdword(rsrc[entry:])
            theoff = fromdword(rsrc[entry+4:])
            if rtype == -1 or rtype == thetype:
                gotoffset(theoff)

    # We could try finding the Resource Table entry in the Optional
    # Header, but it talks about RVAs instead of file offsets, so
    # it's probably easiest just to go straight to the section table.
    # So let's find the size of the Optional Header, which we can
    # then skip over to find the section table.
    secentries = fromword(fon[peoff+0x06:])
    sectable = peoff + 0x18 + fromword(fon[peoff+0x14:])
    for i in range(secentries):
        secentry = sectable + i * 0x28
        secname = asciz(fon[secentry:secentry+8])
        secrva = fromdword(fon[secentry+0x0C:])
        secsize = fromdword(fon[secentry+0x10:])
        secptr = fromdword(fon[secentry+0x14:])
        if secname == b".rsrc":
            break
    if secname != b".rsrc":
        raise FbError('Unable to locate resource section')
    # Now we've found the resource section, let's throw away the rest.
    rsrc = fon[secptr:secptr+secsize]

    # Now the fun begins. To start with, we must find the initial
    # Resource Directory Table and look up type 0x08 (font) in it.
    # If it yields another Resource Directory Table, we stick the
    # address of that on a list. If it gives a Data Entry, we put
    # that in another list.
    dodirtable(rsrc, 0, 0x08)
    # Now process Resource Directory Tables until no more remain
    # in the list. For each of these tables, we accept _all_ entries
    # in it, and if they point to subtables we stick the subtables in
    # the list, and if they point to Data Entries we put those in
    # the other list.
    while len(dirtables) > 0:
        table = dirtables[0]
        del dirtables[0]
        dodirtable(rsrc, table, -1)  # accept all entries
    # Now we should be left with Resource Data Entries. Each of these
    # describes a font.
    ret = []
    for off in dataentries:
        rva = fromdword(rsrc[off:])
        start = rva - secrva
        size = fromdword(rsrc[off+4:])
        font = dofnt(rsrc[start:start+size])
        if font is None:
            raise FbError(f'Failed to read font resource at {start}')
        ret = ret + [font]
    return ret


def dofon(fon):
    "Split a .FON up into .FNTs and pass each to dofnt."
    # Check the MZ header.
    if fon[0:2] != b"MZ":
        raise FbError('MZ signature not found')
    # Find the NE header.
    neoff = fromdword(fon[0x3C:])
    if fon[neoff:neoff+2] == b"NE":
        return nefon(fon, neoff)
    elif fon[neoff:neoff+4] == b"PE\0\0":
        return pefon(fon, neoff)
    else:
        raise FbError('NE or PE signature not found')


def get_fonts_from_fon_data(fon_data):
    if isfon(fon_data):
        fonts = dofon(fon_data)
    else:
        fonts = [dofnt(fon_data)]
    return fonts


def convert_font_to_tcr(f):
    if f.height != 16:
        raise FbError(
            f'Only 8 x 16 fonts are supported. '
            f'(Found: height={f.height})')

    result_bytes = [0] * 4096
    for cnum in range(256):
        if f.chars[cnum].width != 8:
            raise FbError(
                f'Only 8 x 16 fonts are supported. '
                f'(Found: char {cnum} width={f.chars[cnum].width})')
        for row in range(f.height):
            b = f.chars[cnum].data[row]
            scr = cnum_to_scrcode_dict[cnum]
            addr = (scr + (row % 2) * 256) * 8 + (row // 2)
            result_bytes[addr] = b
    return result_bytes


def bs(b):
    s = bin(b)[2:].replace('0', ' ').replace('1', '#')
    return (' ' * (8-len(s))) + s


def dump_tcr(tcr):
    for scrcode in range(256):
        print(f'screen code {scrcode}')
        for i in range(scrcode*8, scrcode*8+8):
            print(bs(tcr[i]))
            print(bs(tcr[i+2048]))


def main(args):
    if len(args) != 1:
        print('Usage: python3 fontotcr.py <path to OSFR FON directory>')
        return 1

    for infname in FON_FILES:
        infpath = os.path.join(args[0], infname)
        outfname_prefix = (
            infname
            .replace('Bm437_', '')
            .replace('_8x16', '')
            .replace('.FON', ''))

        with open(infpath, 'rb') as infh:
            try:
                fon_data = infh.read()
                fonts = get_fonts_from_fon_data(fon_data)

                for i, f in enumerate(fonts):
                    tcr_data = convert_font_to_tcr(f)
                    tcr_blink_data = (
                        tcr_data[0:(128*8)] +
                        [x ^ 0xff for x in tcr_data[0:(128*8)]] +
                        tcr_data[(256*8):(384*8)] +
                        [x ^ 0xff for x in tcr_data[(256*8):(384*8)]])

                    if len(fonts) > 1:
                        fontnum = '_' + str(i)
                    else:
                        fontnum = ''

                    outfname = outfname_prefix + fontnum + '_all.tcr'
                    blinkoutfname = outfname_prefix + fontnum + '.tcr'

                    print(f'{infname} -> {outfname}, {blinkoutfname}')
                    # dump_tcr(tcr_data)

                    with open(outfname, 'wb') as outfh:
                        outfh.write(bytes(tcr_data))
                    with open(blinkoutfname, 'wb') as outfh:
                        outfh.write(bytes(tcr_blink_data))
            except Exception as e:
                print(f'{infname}: {str(e)}')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
