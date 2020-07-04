from random import choice
def generate_dayplopynamepart_english():
    CONSONTANTS =          ['b', 'v', 'g', 'd', 'zh', 'z', 'l', 'm', 'n', 'r',
                            'b', 'v', 'g', 'd', 'zh', 'z', 'l', 'm', 'n', 'r',
                            'b', 'v', 'g', 'd', 'zh', 'z', 'l', 'm', 'n', 'r',
                            'ii', 'k', 'p', 's', 't', 'f', 'x', 'ts', 'ch', 'sh']
    VOWELS =               ['a', 'i', 'o', 'u', 'e']
    LEFTCOMBOS =           ['rb', 'sb', 'fb', 'xb', 'shb',
                            'bv', 'gv', 'dv', 'zhv', 'zv', 'kv', 'mv', 'nv', 'pv', 'rv', 'sv', 'tv', 'fv', 'xv', 'tsv', 'chv', 'shv',
                            'zg', 'mg', 'rg', 'sg', 'fg', 'xg', 'tsg', 'chg',
                            'vd', 'zhd', 'zd', 'md', 'nd', 'rd', 'sd', 'fd', 'xd',
                            'vzh', 'gzh', 'dzh', 'kzh', 'lzh', 'mzh', 'nzh', 'pzh', 'rzh', 'szh', 'tzh', 'fzh', 'xzh', 'chzh',
                            'vz', 'gz', 'dz', 'kz', 'lz', 'mz', 'nz', 'pz', 'rz', 'sz', 'tz', 'fz', 'xz', 'tsz', 'chz',
                            'zk', 'mk', 'nk', 'pk', 'rk', 'sk', 'tk', 'fk', 'xk', 'tsk', 'chk', 'shk',
                            'bl', 'vl', 'gl', 'dl', 'zhl', 'zl', 'kl', 'ml', 'nl', 'pl', 'rl', 'sl', 'tl', 'fl', 'xl', 'tsl', 'chl', 'shl',
                            'vm', 'gm', 'dm', 'zhm', 'zm', 'km', 'lm', 'nm', 'rm', 'sm', 'tm', 'fm', 'xm', 'tsm', 'chm', 'shm',
                            'vn', 'gn', 'dn', 'zhn', 'zn', 'kn', 'ln', 'mn', 'pn', 'rn', 'sn', 'tn', 'fn', 'xn', 'tsn', 'chn', 'shn',
                            'vp', 'kp', 'np', 'rp', 'sp', 'tp', 'fp', 'xp', 'tsp', 'chp', 'shp',
                            'br', 'vr', 'gr', 'dr', 'zhr', 'zr', 'kr', 'mr', 'nr', 'pr', 'sr', 'tr', 'fr', 'xr', 'tsr', 'chr', 'shr',
                            'bs', 'vs', 'ks', 'ls', 'ms', 'ns', 'ps', 'rs', 'ts', 'fs', 'xs', 'shs',
                            'vt', 'kt', 'lt', 'mt', 'nt', 'pt', 'rt', 'st', 'ft', 'xt', 'tst', 'cht', 'sht',
                            'df', 'kf', 'mf', 'nf', 'pf', 'rf', 'sf', 'tf', 'xf', 'tsf', 'chf', 'shf',
                            'bx', 'vx', 'gx', 'dx', 'kx', 'lx', 'mx', 'nx', 'px', 'rx', 'sx', 'tx', 'fx', 'tsx', 'chx', 'shx',
                            'gts', 'lts', 'mts', 'nts', 'pts', 'rts', 'sts', 'tts', 'fts', 'shts',
                            'vch', 'gch', 'mch', 'nch', 'pch', 'rch', 'sch', 'tch', 'fch', 'shch',
                            'bsh', 'vsh', 'gsh', 'ksh', 'lsh', 'msh', 'nsh', 'psh', 'rsh', 'ssh', 'tsh', 'fsh']
    RIGHTCOMBOS =          ['zhb', 'zb', 'iib', 'lb', 'mb', 'nb', 'rb',
                            'dv', 'zv', 'iiv', 'kv', 'lv', 'nv', 'rv',
                            'vg', 'gg', 'zhg', 'zg', 'iig', 'lg', 'mg', 'ng', 'rg', 'sg', 'fg', 'xg', 'shg',
                            'dd', 'zhd', 'zd', 'iid', 'ld', 'md', 'nd', 'rd', 'sd', 'fd', 'xd', 'shd',
                            'vzh', 'gzh', 'dzh', 'zhzh', 'kzh', 'lzh', 'mzh', 'nzh', 'rzh', 'tzh',
                            'vz', 'gz', 'dz', 'zz', 'iiz', 'kz', 'lz', 'mz', 'nz', 'pz', 'rz', 'tz', 'xz',
                            'vk', 'zhk', 'zk', 'iik', 'kk', 'lk', 'mk', 'nk', 'rk', 'sk', 'fk', 'xk', 'tsk', 'chk', 'shk',
                            'zl', 'iil', 'kl', 'll', 'pl', 'sl', 'tl', 'fl', 'tsl', 'chl', 'shl',
                            'zhm', 'zm', 'iim', 'km', 'lm', 'mm', 'rm', 'sm', 'tm', 'fm', 'xm', 'tsm', 'chm', 'shm',
                            'bn', 'vn', 'gn', 'dn', 'zhn', 'zn', 'iin', 'kn', 'ln', 'mn', 'nn', 'rn', 'sn', 'tn', 'fn', 'xn', 'tsn', 'chn', 'shn',
                            'vp', 'iip', 'lp', 'mp', 'np', 'pp', 'rp', 'sp', 'xp', 'shp',
                            'br', 'vr', 'gr', 'dr', 'zhr', 'zr', 'kr', 'mr', 'nr', 'pr', 'rr', 'sr', 'tr', 'fr', 'xr', 'chr', 'shr',
                            'bs', 'vs', 'gs', 'ds', 'iis', 'ks', 'ls', 'ms', 'ns', 'ps', 'rs', 'ss', 'ts', 'fs', 'xs', 'tss', 'chs', 'shs',
                            'vt', 'zht', 'zt', 'iit', 'kt', 'lt', 'mt', 'nt', 'pt', 'rt', 'st', 'tt', 'ft', 'xt', 'tst', 'cht', 'sht',
                            'zf', 'iif', 'kf', 'lf', 'mf', 'nf', 'pf', 'rf', 'sf', 'tf', 'ff', 'shf',
                            'bx', 'vx', 'gx', 'dx', 'zhx', 'zx', 'iix', 'kx', 'lx', 'mx', 'nx', 'px', 'rx', 'sx', 'tx', 'fx', 'xx', 'chx', 'shx',
                            'dts', 'iits', 'kts', 'lts', 'mts', 'nts', 'pts', 'rts', 'tts', 'shts',
                            'dch', 'iich', 'kch', 'lch', 'mch', 'nch', 'pch', 'rch', 'fch', 'shch',
                            'bsh', 'vsh', 'dsh', 'iish', 'ksh', 'lsh', 'msh', 'nsh', 'psh', 'rsh', 'ssh', 'tsh', 'fsh', 'shsh']
    MIDDLECOMBOS =         [x for x in LEFTCOMBOS if x in RIGHTCOMBOS]
    
    possible_names_templates = [
        'CV', 'CV', 'CV', 'CV', 'CV', 'CV', 'CV', 'CV', 'CV', 'CV',
        'VC', 'VC', 'VC', 'VC', 'VC', 'VC', 'VC', 'VC', 'VC', 'VC',
        'CVC', 'CVC', 'CVC', 'CVC', 'CVC', 'CVC', 'CVC', 'CVC', 'CVC', 'CVC',
        'CVR', 'CVM',
        'LVC', 'MVC',
        'LV', 'MV', 'VR', 'VM',
        'LVR', 'MVR', 'LVM', 'MVM'
    ]
    
    # V: Vowel
    # C: Consontant
    # L: Left-to-vowel-combo
    # M: Any-side-to-vowel-combo
    # R: Right-to-vowel-combo
    selected_template = choice(possible_names_templates)
    R = ''
    for letter in selected_template:
        if letter == 'C':
            R += choice(CONSONTANTS)
        elif letter == 'V':
            R += choice(VOWELS)
        elif letter == 'L':
            R += choice(LEFTCOMBOS)
        elif letter == 'M':
            R += choice(MIDDLECOMBOS)
        elif letter == 'R':
            R += choice(RIGHTCOMBOS)
        else:
            R += letter

    return R

def generate_dayplopyname_english():
    R = generate_dayplopynamepart_english().capitalize()
    return R+"-"+R

def main(*args):
    return generate_dayplopyname_english()
