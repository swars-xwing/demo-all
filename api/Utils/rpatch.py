import fnmatch
import os
import requests_to_curl
from pprint import pprint


def rpatch(r):
    r.pprint = lambda: pprint(r.json())
    r.ppaths = lambda x=None: printPaths(r.json(), x)
    r.pvals = lambda x=None: printVals(r.json(), x)
    r.getFuzzyPath = lambda x: getFuzzyPath(r.json(), x)
    r.getVal = lambda x: getVal(r.json(), x)
    r.dbg = lambda: retRDbg(r)
    r.good = lambda: goodStatus(r)
    r.assertAll = lambda: assertVals(r.pvals())
    r.dir = lambda: define()
    r.diff = lambda r1: diff(r.pvals(), r1.pvals())
    r.curl = lambda: printCurl(r) 








def printPaths(d, fstr=None):
    ret_dict = flatten_json(d)
    ret_paths = list(ret_dict.keys())
    if fstr is None:
        ret = ret_paths
    else:
        ret = []
        for akey in ret_paths:
            if str_match(fstr, akey):
                ret.append(akey)
    pprint(ret)
    return ret


def printVals(d, fstr=None):
    ret_dict = flatten_json(d)
    ret_paths = list(ret_dict.keys())
    ret = []
    if fstr is None:
        for akey in ret_dict:
            ret.append([akey, getVal(d, akey)])
    else:
        ret = []
        for akey in ret_paths:
            if str_match(fstr, akey):
                ret.append([akey, getVal(d, akey)])
    pprint(ret)
    return ret


def getFuzzyPath(adict, akey):
    ret = None
    if ("*" in akey) and (":" in akey):
        kpath, mval = akey.split(":")
        z = printPaths(adict)
        match_paths = []
        for ap in z:
            if fnmatch.fnmatch(ap, kpath):
                match_paths.append(ap)
        print("++", match_paths)

        ret = None
        for ap in match_paths:
            if getVal(adict, ap).lower() == mval.lower():
                print("mmm", ap)
                if ret is None:
                    ret = '.'.join(ap.split('.')[0:-1])

    elif "*" in akey:
        ret = []
        z = printPaths(adict)
        for ap in z:
            if fnmatch.fnmatch(ap, akey):
                ret.append(ap)
    return ret


def getVal(adict, akey):
    keyz = akey.split(".")
    ret_obj = adict
    for sub_key in keyz:
        try:
            int(sub_key)
            sub_key = int(sub_key)
        except:
            pass

        if not isinstance(sub_key, int):
            if ":" in sub_key:
                for athing in ret_obj:
                    ak, val = sub_key.split(":")
                    if athing[ak].lower() == val.lower():
                        ret_obj = athing
                    break
            else:
                ret_obj = ret_obj[sub_key]
        else:
            ret_obj = ret_obj[sub_key]
    return ret_obj


def retRDbg(r):
    print("status code == {}".format(r.status_code))
    print("call type   == {}".format(r.request))
    print("url == {}".format(r.url))
    print("params == {}".format(r.request.body))
    print("== request headers ==")
    pprint(r.request.headers)


def goodStatus(self):
    assert self.status_code in range(200, 204)
    print(self.status_code)



def printCurl(r):
    pprint(requests_to_curl.parse(r))


def assertVals(dvals):
    val_list = []
    _pth = os.path.dirname(os.path.abspath(__file__))
    afile = _pth + "/assertVals.py"
    for alist in dvals:
        a = alist[0]
        b = alist[1]
        if isinstance(b, str):
            val_list.append("assert(r.getVal('{}') == '{}')".format(a, b))
        elif isinstance(b, type(None)):
            val_list.append("assert(r.getVal('{}') is None)".format(a))
        else:
            val_list.append("assert(r.getVal('{}') == {})".format(a, str(b)))

    with open(afile, 'w') as f:
        for athing in val_list:
            print(athing, file=f)
    print(afile)

    return val_list


def define():
    docstr = """
    dir : this method that prints a doc of what you can do
    pprint  : prints the json representation of the response body
    dbg : returns helpful info on response for debugging isses 
    ppaths (x) : shows all paths for response.json() object in dot notation, can be limited by x 
    pvals(x) : shows all paths/values for response.json() object in dot notation, can be limited by x  
    getVal(apath) : returns a single value given the supplied apth in the json response
    good : asserts r.status_code in range(200, 204)
    assertAll: takes whats in the internal dot.dict of the json and makes assertion staments against 
       everything. The output will go to the terminal shell and ../keystone_qa/Library/assertVals.py
       you can then edit that file further and copy paste what you need (real time saver)
    """
    print(docstr)


def diff(rvals, r1vals):
    zz = []
    for athing in rvals:
        zz.append("{}:{}".format(athing[0], athing[1]))
    r_set = set(zz)

    zz = []
    for athing in r1vals:
        zz.append("{}:{}".format(athing[0], athing[1]))
    r1_set = set(zz)
    return r_set.difference(r1_set)


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def str_match(sstring, akey):
    lfi = 0
    ret = False
    pattern = sstring.split("*")
    for elem in pattern:
        if elem in akey[lfi:]:
            ret = True
            lfi = akey.find(elem) + len(elem)
        else:
            ret = False
            break
    return ret
