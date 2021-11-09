# read and interpret the rdb format from usgs
import csv

def readDict(txt, params={}):
    # txt - the text to decode
    # params - dictionary parameters, if any
    res = []
    txt = [x for x in txt.split("\n") if x and x[0]!="#"]
    headers = txt[0].split("\t")
    for i in range(1, len(txt)):
        rec = txt[i].split("\t")
        tmp = {}
        for j in range(min(len(rec), len(headers))):
            val = rec[j] # raw value
            hdr = headers[j]
            # ignore fields with header like #####_PARAM_cd
            if len(hdr.split("_")) == 3 and hdr.split("_")[0].isnumeric():
                continue
            # map fields with header like #####_PARAM
            if len(hdr.split("_")) == 2 and hdr.split("_")[0].isnumeric():
                hdr = hdr.split("_")[1]
                hdr = params.get(hdr, hdr)
                # coerce our params to float if we can
                try:
                    val = float(val)
                except (ValueError):
                    print("FLOAT ERR", val)
                    pass # leave it as a string
            tmp[hdr] = val
        res.append(tmp)
    return res

__all__ = "readDict"
