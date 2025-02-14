# PC Fonts on the MEGA65

The MEGA65 has a *Tall ChaRacter* (TCR) graphics mode capable of displaying characters with a doubled vertical resolution, 8 x 16. One possible application of this mode is to replace the Commodore PETSCII character set with old-school PC fonts that used the 8 x 16 resolution.

This archive contains fonts from the [Oldschool PC Font Resource](https://int10h.org/oldschool-pc-fonts/), a collection of PC fonts rendered with high accuracy. 43 of these fonts have an 8 x 16 resolution. These fonts have been converted to "TCR files," the in-memory format used by the MEGA65 TCR mode. Their appearance may not match their original context exactly due to differing pixel sizes. See the Resource website for detailed notes on each font.

To browse these fonts on your MEGA65:

1. Copy `PCFONTS.D81` to your SD card.
2. `MOUNT "PCFONTS.D81"`
3. `RUN "*"`

See below for instructions on more ways to use these files.

## The fonts

There are two TCR files for each font:

* 128-char version: The first 128 characters, rearranged in Commodore screen code order, and their reversed versions used by the blinking cursor. This is suitable for typing in the screen terminal, at the expense of missing the upper characters.
* 256-char version: All 256 characters, without reversed versions. This makes all of the upper PC graphics available at all 256 screen codes, at the expense of making the blinking cursor difficult to use (because it blinks between two characters).
    * Filename in the .zip file: `..._all.tcr`
    * Filename in the .d81 image: `...-a.tcr`

I attempted to locate ASCII-style characters at the corresponding screen codes used for PETSCII, such that ASCII text could be displayed without changes. I don't know if PC graphics characters ended up in useful places. [Feedback welcome!](mailto:contact@dansanderson.com) I have also included the Python script I used to produce these from the original `.FON` files, so you can re-order them yourself.

| 8x16 Font | 128-char TCR file | 128-char on D81 |
|           | (256-char: `_all.tcr`) | (256-char: `-a.tcr`) |
|-----------|-------------------|-------------------|
| [ACM VGA](https://int10h.org/oldschool-pc-fonts/fontlist/font?acm_vga_8x16) | `ACM_VGA.tcr` | `acmvga.tcr` |
| [AT&T PC6300](https://int10h.org/oldschool-pc-fonts/fontlist/font?att_pc6300) | `ATT_PC6300.tcr` | `attpc6300.tcr` |
| [ATI](https://int10h.org/oldschool-pc-fonts/fontlist/font?ati_8x16) | `ATI.tcr` | `ati.tcr` |
| [CL EagleII](https://int10h.org/oldschool-pc-fonts/fontlist/font?cl_eagleii_8x16) | `CL_EagleII.tcr` | `cleagleii.tcr` |
| [CL EagleIII](https://int10h.org/oldschool-pc-fonts/fontlist/font?cl_eagleiii_8x16) | `CL_EagleIII.tcr` | `cleagleiii.tcr` |
| [CL Stingray 0](https://int10h.org/oldschool-pc-fonts/fontlist/font?cl_stingray_8x16) | `CL_Stingray_0.tcr` | `clstingry0.tcr` |
| [CL Stingray 1](https://int10h.org/oldschool-pc-fonts/fontlist/font?cl_stingray_8x16) | `CL_Stingray_1.tcr` | `clstingry1.tcr` |
| [Compaq Port3](https://int10h.org/oldschool-pc-fonts/fontlist/font?compaq_port3) | `Compaq_Port3.tcr` | `compaqprt3.tcr` |
| [CompaqThin](https://int10h.org/oldschool-pc-fonts/fontlist/font?compaqthin_8x16) | `CompaqThin.tcr` | `compaqthin.tcr` |
| [Compis](https://int10h.org/oldschool-pc-fonts/fontlist/font?compis) | `Compis.tcr` | `compis.tcr` |
| [DOS/V re. ANK16](https://int10h.org/oldschool-pc-fonts/fontlist/font?dos-v_re_ank16) | `DOS-V_re_ANK16.tcr` | `dosvrank16.tcr` |
| [DOS/V re. JPN16](https://int10h.org/oldschool-pc-fonts/fontlist/font?dos-v_re_jpn16) | `DOS-V_re_JPN16.tcr` | `dosvrjpn16.tcr` |
| [DOS/V re. PRC16](https://int10h.org/oldschool-pc-fonts/fontlist/font?dos-v_re_prc16) | `DOS-V_re_PRC16.tcr` | `dosvrprc16.tcr` |
| [DOS/V TWN16](https://int10h.org/oldschool-pc-fonts/fontlist/font?dos-v_twn16) | `DOS-V_TWN16.tcr` | `dosvtwn16.tcr` |
| [EverexME](https://int10h.org/oldschool-pc-fonts/fontlist/font?everexme_8x16) | `EverexME.tcr` | `everexme.tcr` |
| [FMTowns](https://int10h.org/oldschool-pc-fonts/fontlist/font?fmtowns_re_8x16) | `FMTowns_re.tcr` | `fmtownsre.tcr` |
| [IBM DOS ISO8](https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_dos_iso8) | `IBM_DOS_ISO8.tcr` | `ibmdosiso8.tcr` |
| [IBM Model30r0](https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_model30r0) | `IBM_Model30r0.tcr` | `ibmmod30r0.tcr` |
| [IBM Model3x Alt 1](https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_model3x_alt1) | `IBM_Model3x_alt1.tcr` | `ibmmod3xa1.tcr` |
| [IBM Model3x Alt 2](https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_model3x_alt2) | `IBM_Model3x_alt2.tcr` | `ibmmod3xa2.tcr` |
| [IBM Model3x Alt 3](https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_model3x_alt3) | `IBM_Model3x_alt3.tcr` | `ibmmod3xa3.tcr` |
| [IBM Model3x Alt 4](https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_model3x_alt4) | `IBM_Model3x_alt4.tcr` | `ibmmod3xa4.tcr` |
| [IBM PGC](https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_pgc) | `IBM_PGC.tcr` | `ibmpgc.tcr` |
| [IBM VGA](https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_vga_8x16) | `IBM_VGA.tcr` | `ibmvga.tcr` |
| [IGS VGA](https://int10h.org/oldschool-pc-fonts/fontlist/font?igs_vga_8x16) | `IGS_VGA.tcr` | `igsvga.tcr` |
| [MBytePC230](https://int10h.org/oldschool-pc-fonts/fontlist/font?mbytepc230_8x16) | `MBytePC230.tcr` | `mbytepc230.tcr` |
| [NEC APC3](https://int10h.org/oldschool-pc-fonts/fontlist/font?nec_apc3_8x16) | `NEC_APC3.tcr` | `necapc3.tcr` |
| [Nix8810 M15](https://int10h.org/oldschool-pc-fonts/fontlist/font?nix8810_m15) | `Nix8810_M15.tcr` | `nix8810m15.tcr` |
| [Nix8810 M16](https://int10h.org/oldschool-pc-fonts/fontlist/font?nix8810_m16) | `Nix8810_M16.tcr` | `nix8810m16.tcr` |
| [OlivettiThin](https://int10h.org/oldschool-pc-fonts/fontlist/font?olivettithin_8x16) | `OlivettiThin.tcr` | `olivettthn.tcr` |
| [PhoenixEGA](https://int10h.org/oldschool-pc-fonts/fontlist/font?phoenixega_8x16) | `PhoenixEGA.tcr` | `phoenixega.tcr` |
| [PhoenixVGA](https://int10h.org/oldschool-pc-fonts/fontlist/font?phoenixvga_8x16) | `PhoenixVGA.tcr` | `phoenixvga.tcr` |
| [Robotron A7100](https://int10h.org/oldschool-pc-fonts/fontlist/font?robotron_a7100) | `Robotron_A7100.tcr` | `rbtrna7100.tcr` |
| [Sigma RM](https://int10h.org/oldschool-pc-fonts/fontlist/font?sigma_rm_8x16) | `Sigma_RM.tcr` | `sigmarm.tcr` |
| [SperryPC](https://int10h.org/oldschool-pc-fonts/fontlist/font?sperrypc_8x16) | `SperryPC.tcr` | `sperrypc.tcr` |
| [Tandy2K](https://int10h.org/oldschool-pc-fonts/fontlist/font?tandy2k) | `Tandy2K.tcr` | `tandy2k.tcr` |
| [Tandy2K G](https://int10h.org/oldschool-pc-fonts/fontlist/font?tandy2k_g) | `Tandy2K_G.tcr` | `tandy2kg.tcr` |
| [ToshibaSat](https://int10h.org/oldschool-pc-fonts/fontlist/font?toshibasat_8x16) | `ToshibaSat.tcr` | `toshibasat.tcr` |
| [ToshibaT300](https://int10h.org/oldschool-pc-fonts/fontlist/font?toshibat300_8x16) | `ToshibaT300.tcr` | `toshibt300.tcr` |
| [ToshibaTxL1](https://int10h.org/oldschool-pc-fonts/fontlist/font?toshibatxl1_8x16) | `ToshibaTxL1.tcr` | `toshibtxl1.tcr` |
| [ToshibaTxL2](https://int10h.org/oldschool-pc-fonts/fontlist/font?toshibatxl2_8x16) | `ToshibaTxL2.tcr` | `toshibtxl2.tcr` |
| [Trident](https://int10h.org/oldschool-pc-fonts/fontlist/font?trident_8x16) | `Trident.tcr` | `trident.tcr` |
| [TridentEarly](https://int10h.org/oldschool-pc-fonts/fontlist/font?tridentearly_8x16) | `TridentEarly.tcr` | `tridntearl.tcr` |
| [Verite](https://int10h.org/oldschool-pc-fonts/fontlist/font?verite_8x16) | `Verite.tcr` | `verite.tcr` |

## Using TCR files

The `PCFONTS.D81` disk contains all of the TCR files, as well as a demo program for browsing and displaying the fonts.

You can load a TCR file manually like so:

1. Copy the TCR file directly to the SD card. (This archive includes the loose TCR files for this purpose.)
2. Open the Freezer: hold **Restore** for one second, then release.
3. Press **L**. Browse to the TCR file, press **Return**.
4. Press **F3** to resume. The MEGA65 is now in TCR mode and the selected font is used.

To use a TCR file in a program, copy the TCR file to the D81 disk image for the program. From the program:

1. Load the TCR file from disk into the character generator buffer at FF7E000.
2. Optionally, disable CRT emulation. (TCR mode works with this enabled, but doesn't look as nice.) Clear the PALEMU register D054 bit 5.
3. Enable TCR mode. Set the CHARY16 register D07A bit 4.

In BASIC 65:

```basic
10 BLOAD "MYFONT.TCR",P($FF7E000)
20 CLRBIT $D054,5
30 SETBIT $D07A,4
```

## TCR mode and the TCR data format

In the VIC-IV TCR mode:

* Character set data is read directly from the character generator memory at $FF7E000-$FF7EFFF (4 KB).
* The screen terminal does not switch between "uppercase + graphics" and "lowercase + uppercase" text modes. There is only one case. Specifically, CHARPTR ignores the address bit that normally switches between cases.
* Character set data is interpreted as a single set of 256 characters of 8 x 16 resolution, using interleaving lines from charset positions n and n+256.

For example, screen code 1 is normally a lowercase "a" character. In TCR mode, the topmost line of the character is the topmost line of character 1. The next line of the character is the topmost line of character 257. It continues like so:

```
Byte      Charset address
---------------------------
........  FF7E008
........            FF7E108
........  FF7E009
........            FF7E109
........  FF7E00A
..xxxx..            FF7E10A
.....xx.  FF7E00B
.....xx.            FF7E10B
..xxxxx.  FF7E00C
.xx..xx.            FF7E10C
.xx..xx.  FF7E00D
..xxxxxx            FF7E10D
........  FF7E00E
........            FF7E10E
........  FF7E00F
........            FF7E10F


........  FF7E008
........  FF7E009
........  FF7E00A
.....xx.  FF7E00B
..xxxxx.  FF7E00C
.xx..xx.  FF7E00D
........  FF7E00E
........  FF7E00F

........            FF7E108
........            FF7E109
..xxxx..            FF7E10A
.....xx.            FF7E10B
.xx..xx.            FF7E10C
..xxxxxx            FF7E10D
........            FF7E10E
........            FF7E10F
```

## How these TCR files were made

The Oldschool PC Font Resource distributes PC fonts in several formats. For our purposes, the most useful format is the `.FON` Windows font file, which in this case are all bitmap fonts in their original resolutions.

I used [dewinfont](https://github.com/juanitogan/mkwinfont) by Github user juanitogan, based on work by [Simon Tatham](https://www.chiark.greenend.org.uk/~sgtatham/fonts/). This Python script converts `.FON` files to easy-to-read text files with a `.fb` extension.

My script, `fbtotcr.py`, converts these files to TCR files. It only works on 8x16 fonts with 256 characters. The script makes both the 128-char and 256-char versions. I don't intend to polish this into a useful tool or support it, but you're welcome to mess with it.

## License

This archive was made on February 2025, based on Oldschool PC Font Resource v2.2.

The Oldschool PC Font Resource is [free to use](https://int10h.org/oldschool-pc-fonts/readme/#legal_stuff) under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). The TCR conversions in this archive are released under the same license, per the "ShareAlike" provision of the original license. For the purposes of attribution, the author of the TCR conversions is "dddaaannn," and you can link to the [Filehost](https://files.mega65.org/) page where this archive was published. (I request that VileR, the author of the Oldschool PC Font Resource, be given artistic credit for these reproductions.)

Credit for the original raster binary data charsets goes to their respective designers. US law does not consider typefaces to be copyrightable material. See [VileR's explanation](https://int10h.org/oldschool-pc-fonts/readme/#legal_stuff), dated July 2020.
