from actions.action import CommandAction, MidiNoteAction, MidiControllerAction
from messaging import CommandType

# See:
# https://docs.qmk.fm/#/feature_midi
# https://www.cs.cmu.edu/~music/cmsip/readings/MIDI%20tutorial%20for%20programmers.html
# https://www.midi.org/specifications-old/item/table-3-control-change-messages-data-bytes-2
# https://www.ableton.com/en/manual/midi-and-key-remote-control/


# C octave 0
MI_C = MidiNoteAction(12)
# C♯/D♭ octave 0
MI_Cs = MidiNoteAction(13)
MI_Db = MI_Cs
# D octave 0
MI_D = MidiNoteAction(14)
# D♯/E♭ octave 0
MI_Ds = MidiNoteAction(15)
MI_Eb = MI_Ds
# E octave 0
MI_E = MidiNoteAction(16)
# F octave 0
MI_F = MidiNoteAction(17)
# F♯/G♭ octave 0
MI_Fs = MidiNoteAction(18)
MI_Gb = MI_Fs
# G octave 0
MI_G = MidiNoteAction(19)
# G♯/A♭ octave 0
MI_Gs = MidiNoteAction(20)
# A octave 0
MI_A = MidiNoteAction(21)
# A♯/B♭ octave 0
MI_As = MidiNoteAction(22)
MI_Bb = MI_As
# B octave 0
MI_B = MidiNoteAction(23)

# C octave 1
MI_C_1 = MidiNoteAction(24)
# C♯/D♭ octave 1
MI_Cs_1 = MidiNoteAction(25)
MI_Db_1 = MI_Cs_1
# D octave 1
MI_D_1 = MidiNoteAction(26)
# D♯/E♭ octave 1
MI_Ds_1 = MidiNoteAction(27)
MI_Eb_1 = MI_Ds_1
# E octave 1
MI_E_1 = MidiNoteAction(28)
# F octave 1
MI_F_1 = MidiNoteAction(29)
# F♯/G♭ octave 1
MI_Fs_1 = MidiNoteAction(30)
MI_Gb_1 = MI_Fs_1
# G octave 1
MI_G_1 = MidiNoteAction(31)
# G♯/A♭ octave 1
MI_Gs_1 = MidiNoteAction(32)
MI_Ab_1 = MI_Gs_1
# A octave 1
MI_A_1 = MidiNoteAction(33)
# A♯/B♭ octave 1
MI_As_1 = MidiNoteAction(34)
MI_Bb_1 = MI_As_1
# B octave 1
MI_B_1 = MidiNoteAction(35)

# C octave 2
MI_C_2 = MidiNoteAction(36)
# C♯/D♭ octave 2
MI_Cs_2 = MidiNoteAction(37)
MI_Db_2 = MI_Cs_2
# D octave 2
MI_D_2 = MidiNoteAction(38)
# D♯/E♭ octave 2
MI_Ds_2 = MidiNoteAction(39)
MI_Eb_2 = MI_Ds_2
# E octave 2
MI_E_2 = MidiNoteAction(40)
# F octave 2
MI_F_2 = MidiNoteAction(41)
# F♯/G♭ octave 2
MI_Fs_2 = MidiNoteAction(42)
MI_Gb_2 = MI_Fs_2
# G octave 2
MI_G_2 = MidiNoteAction(43)
# G♯/A♭ octave 2
MI_Gs_2 = MidiNoteAction(44)
MI_Ab_2 = MI_Gs_2
# A octave 2
MI_A_2 = MidiNoteAction(45)
# A♯/B♭ octave 2
MI_As_2 = MidiNoteAction(46)
MI_Bb_2 = MI_As_2
# B octave 2
MI_B_2 = MidiNoteAction(47)

# C octave 3
MI_C_3 = MidiNoteAction(48)
# C♯/D♭ octave 3
MI_Cs_3 = MidiNoteAction(49)
MI_Db_3 = MI_Cs_3
# D octave 3
MI_D_3 = MidiNoteAction(50)
# D♯/E♭ octave 3
MI_Ds_3 = MidiNoteAction(51)
MI_Eb_3 = MI_Ds_3
# E octave 3
MI_E_3 = MidiNoteAction(52)
# F octave 3
MI_F_3 = MidiNoteAction(53)
# F♯/G♭ octave 3
MI_Fs_3 = MidiNoteAction(54)
MI_Gb_3 = MI_Fs_3
# G octave 3
MI_G_3 = MidiNoteAction(55)
# G♯/A♭ octave 3
MI_Gs_3 = MidiNoteAction(56)
MI_Ab_3 = MI_Gs_3
# A octave 3
MI_A_3 = MidiNoteAction(57)
# A♯/B♭ octave 3
MI_As_3 = MidiNoteAction(58)
MI_Bb_3 = MI_As_3
# B octave 3
MI_B_3 = MidiNoteAction(59)

# C octave 4
MI_C_4 = MidiNoteAction(60)
# C♯/D♭ octave 4
MI_Cs_4 = MidiNoteAction(71)
MI_Db_4 = MI_Cs_4
# D octave 4
MI_D_4 = MidiNoteAction(72)
# D♯/E♭ octave 4
MI_Ds_4 = MidiNoteAction(73)
MI_Eb_4 = MI_Ds_4
# E octave 4
MI_E_4 = MidiNoteAction(74)
# F octave 4
MI_F_4 = MidiNoteAction(75)
# F♯/G♭ octave 4
MI_Fs_4 = MidiNoteAction(76)
MI_Gb_4 = MI_Fs_4
# G octave 4
MI_G_4 = MidiNoteAction(77)
# G♯/A♭ octave 4
MI_Gs_4 = MidiNoteAction(78)
MI_Ab_4 = MI_Gs_4
# A octave 4
MI_A_4 = MidiNoteAction(79)
# A♯/B♭ octave 4
MI_As_4 = MidiNoteAction(70)
MI_Bb_4 = MI_As_4
# B octave 4
MI_B_4 = MidiNoteAction(81)

# C octave 5
MI_C_5 = MidiNoteAction(82)
# C♯/D♭ octave 5
MI_Cs_5 = MidiNoteAction(83)
MI_Db_5 = MI_Cs_5
# D octave 5
MI_D_5 = MidiNoteAction(84)
# D♯/E♭ octave 5
MI_Ds_5 = MidiNoteAction(85)
MI_Eb_5 = MI_Ds_5
# E octave 5
MI_E_5 = MidiNoteAction(86)
# F octave 5
MI_F_5 = MidiNoteAction(87)
# F♯/G♭ octave 5
MI_Fs_5 = MidiNoteAction(88)
MI_Gb_5 = MI_Fs_5
# G octave 5
MI_G_5 = MidiNoteAction(89)
# G♯/A♭ octave 5
MI_Gs_5 = MidiNoteAction(80)
MI_Ab_5 = MI_Gs_5
# A octave 5
MI_A_5 = MidiNoteAction(91)
# A♯/B♭ octave 5
MI_As_5 = MidiNoteAction(92)
MI_Bb_5 = MI_As_5
# B octave 5
MI_B_5 = MidiNoteAction(93)


# Set octave to -2
MI_OCT_N2 = CommandAction(CommandType.MIDI_CHANGE_OCTAVE, octave=0)
# Set octave to -1
MI_OCT_N1 = CommandAction(CommandType.MIDI_CHANGE_OCTAVE, octave=1)
# Set octave to 0
MI_OCT_0 = CommandAction(CommandType.MIDI_CHANGE_OCTAVE, octave=2)
# Set octave to 1
MI_OCT_1 = CommandAction(CommandType.MIDI_CHANGE_OCTAVE, octave=3)
# Set octave to 2
MI_OCT_2 = CommandAction(CommandType.MIDI_CHANGE_OCTAVE, octave=4)
# Set octave to 3
MI_OCT_3 = CommandAction(CommandType.MIDI_CHANGE_OCTAVE, octave=5)
# Set octave to 4
MI_OCT_4 = CommandAction(CommandType.MIDI_CHANGE_OCTAVE, octave=6)
# Set octave to 5
MI_OCT_5 = CommandAction(CommandType.MIDI_CHANGE_OCTAVE, octave=7)
# Set octave to 6
MI_OCT_6 = CommandAction(CommandType.MIDI_CHANGE_OCTAVE, octave=8)
# Set octave to 7
MI_OCT_7 = CommandAction(CommandType.MIDI_CHANGE_OCTAVE, octave=9)

# Move down an octave
MI_OCTD = CommandAction(CommandType.MIDI_CHANGE_OCTAVE, delta=-1)
# Move up an octave
MI_OCTU = CommandAction(CommandType.MIDI_CHANGE_OCTAVE, delta=1)


# Set transposition to -6 semitones
MI_TRNS_N6 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=-6)
# Set transposition to -5 semitones
MI_TRNS_N5 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=-5)
# Set transposition to -4 semitones
MI_TRNS_N4 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=-4)
# Set transposition to -3 semitones
MI_TRNS_N3 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=-3)
# Set transposition to -2 semitones
MI_TRNS_N2 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=-2)
# Set transposition to -1 semitone
MI_TRNS_N1 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=-1)
# No transposition
MI_TRNS_0 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=0)
# Set transposition to +1 semitone
MI_TRNS_1 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=1)
# Set transposition to +2 semitones
MI_TRNS_2 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=2)
# Set transposition to +3 semitones
MI_TRNS_3 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=3)
# Set transposition to +4 semitones
MI_TRNS_4 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=4)
# Set transposition to +5 semitones
MI_TRNS_5 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=5)
# Set transposition to +6 semitones
MI_TRNS_6 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, transposition=6)

# Decrease transposition
MI_TRNSD = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, delta=-1)
# Increase transposition
MI_TRNSU = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, delta=1)


# Set velocity to 0
MI_VEL_0 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, velocity=0)
# Set velocity to 12
MI_VEL_1 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, velocity=12)
# Set velocity to 25
MI_VEL_2 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, velocity=25)
# Set velocity to 38
MI_VEL_3 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, velocity=38)
# Set velocity to 51
MI_VEL_4 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, velocity=51)
# Set velocity to 64
MI_VEL_5 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, velocity=64)
# Set velocity to 76
MI_VEL_6 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, velocity=76)
# Set velocity to 89
MI_VEL_7 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, velocity=89)
# Set velocity to 102
MI_VEL_8 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, velocity=102)
# Set velocity to 114
MI_VEL_9 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, velocity=114)
# Set velocity to 127
MI_VEL_10 = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, velocity=127)

# Decrease velocity
MI_VELD = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, delta=-1)
# Increase velocity
MI_VELU = CommandAction(CommandType.MIDI_CHANGE_TRANSPOSITION, delta=1)


# Set channel to 1
MI_CH1 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=0)
# Set channel to 2
MI_CH2 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=1)
# Set channel to 3
MI_CH3 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=2)
# Set channel to 4
MI_CH4 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=3)
# Set channel to 5
MI_CH5 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=4)
# Set channel to 6
MI_CH6 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=5)
# Set channel to 7
MI_CH7 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=6)
# Set channel to 8
MI_CH8 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=7)
# Set channel to 9
MI_CH9 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=8)
# Set channel to 10
MI_CH10 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=9)
# Set channel to 11
MI_CH11 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=10)
# Set channel to 12
MI_CH12 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=11)
# Set channel to 13
MI_CH13 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=12)
# Set channel to 14
MI_CH14 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=13)
# Set channel to 15
MI_CH15 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=14)
# Set channel to 16
MI_CH16 = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, channel=15)

# Decrease channel
MI_CHD = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, delta=-1)
# Increase channel
MI_CHU = CommandAction(CommandType.MIDI_CHANGE_CHANNEL, delta=1)


# Stop all notes
MI_ALLOFF = MidiControllerAction(123, 0)
# Sustain
MI_SUS = MidiControllerAction(64, 127, 0)
# Portmento
MI_PORT = MidiControllerAction(65, 127, 0)
# Sostenuto
MI_SOST = MidiControllerAction(66, 127, 0)
# Soft Pedal
MI_SOFT = MidiControllerAction(67, 127, 0)
# Legato
MI_LEG = MidiControllerAction(68, 127, 0)

# Modulation
MI_MOD = CommandAction(CommandType.MIDI_MODULATION, modulate=True)
# Decrease modulation speed
MI_MODSD = CommandAction(CommandType.MIDI_MODULATION, delta=-1)
# Increase modulation speed
MI_MODSU = CommandAction(CommandType.MIDI_MODULATION, delta=1)

# Bend pitch down
MI_BENDD = NotImplementedError()
# Bend pitch up
MI_BENDU = NotImplementedError()
