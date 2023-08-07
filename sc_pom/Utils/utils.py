import base64
import code
import datetime
import hashlib
import json
import random
import string
import sys
import uuid
from json import JSONDecodeError
from pprint import pprint

import requests
from jsondiff import diff

from Utils.constants import common as constants


def base64_encode(input_string):
    string_bytes = bytes_convert(input_string)
    b64_bytes = base64.urlsafe_b64encode(string_bytes)
    b64_string = bytes_convert(b64_bytes)
    return b64_string


def bkpoint(msg=''):
    try:
        raise None
    except TypeError:
        frame = sys.exc_info()[2].tb_frame.f_back

    from inspect import currentframe, getframeinfo
    frameinfo = getframeinfo(currentframe().f_back)

    # Evaluate commands in current namespace
    namespace = frame.f_globals.copy()
    namespace.update(frame.f_locals)
    code.interact(banner=f"{frameinfo.filename} {frameinfo.lineno} : {msg}>>", local=namespace)


def bytes_convert(input_string):  # Converts strings to bytes and bytes to strings
    if type(input_string) == str:
        return input_string.encode('utf-8')
    elif type(input_string) == bytes:
        return input_string.decode('utf-8')
    else:
        raise TypeError(f'bytes_convert expects either string or bytes, got: {type(input_string)}')


def create_param_from_dict(parm_dict):
    parm_str = ""
    for k, v in list(parm_dict.items()):
        if parm_str == "":
            parm_str += "?%s=%s" % (k, v)
        else:
            parm_str += "&%s=%s" % (k, v)
    return parm_str


def dedupe_list(_list):
    return list(dict.fromkeys(_list))


# In your example, dictMatch(d1, d2) should return True even if d2 has other stuff in it,
# plus it applies also to lower levels:
def dict_match(patn, real):
    """does real dict match pattern?"""
    result = True
    try:
        for pkey, pvalue in patn.items():
            if type(pvalue) is dict:
                print("dict", pkey)
                _result = dict_match(pvalue, real[pkey])
                if _result is False:
                    assert (1 == 0)
            else:
                assert real[pkey] == pvalue
                print("+++", pkey)
    except:
        result = False
        print("--- ", pkey)
    return result


def dict_to_class(dictionary):
    class Dict2Class:
        def __init__(self, _dict):
            self.__dict__.update(_dict)

    return json.loads(json.dumps(dictionary), object_hook=Dict2Class)


def json_diff(dict_1, dict_2):
    return diff(dict_1, dict_2)


def gen_rand_subs_id():
    sub_id = ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    return sub_id


def generate_uuid():
    return uuid.uuid4()


def generate_uuid_string():
    return str(generate_uuid())


def get_date_from_str(date_string):
    dt_obj = get_datetime_from_str(date_string)
    return dt_obj.date()


def get_datetime_from_str(date_string):
    return datetime.datetime.strptime(date_string, '%Y-%m-%d')


def get_epoch_time_ms_from_date(date):
    date_string = datetime.datetime.strftime(date, '%Y-%m-%d')
    dt_obj = get_datetime_from_str(date_string)
    return dt_obj.timestamp() * 1000


def md5_hash_convert(input_string):
    return hashlib.md5(input_string.encode('utf-8')).hexdigest()


def milliseconds_to_yyyy_m_d(timestamp):
    return datetime.datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')


def pprint_response(body):
    try:
        if type(body) == requests.models.Response:
            print(body)
            body = body.json()
        if type(body) == dict:
            pprint(body)
        elif type(body) == list:
            if type(body[0]) == dict:
                for i in body:
                    pprint(i)
            else:
                for i in body:
                    print(f'{i}\n')
        else:
            print(body)
    except JSONDecodeError:
        print(body.text)


def pub_key_inx(wgpub_key, inx_str):
    return wgpub_key[0:-2] + inx_str


def random_email():
    return f'{random_string(6)}{constants.test_email_domain}'


def random_ip_address():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


def random_number(length):
    _min = pow(10, length - 1)
    _max = pow(10, length) - 1
    return random.randint(_min, _max)


def random_sfdc_account_id():
    return f'001{random_sfdc_suffix()}'


def random_sfdc_lead_id():
    return f'00Q{random_sfdc_suffix()}'


def random_sfdc_suffix():
    return random_string(15, case='mixed', numbers=True)


def random_string(length, case='lower', numbers=False):
    if case == 'lower':
        chars = string.ascii_lowercase
    elif case == 'upper':
        chars = string.ascii_uppercase
    elif case == 'mixed':
        chars = string.ascii_uppercase + string.ascii_lowercase
    else:
        raise Exception(f'case {case} not recognized')
    if numbers:
        chars = chars + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def random_workato_id():
    return str(random_number(10))


def return_obj_json(obj, remove_nulls=True):
    """ takes all the variables in obj and converts to dict
    :param obj: the object whose local variables will get converted to json
    :param remove_nulls: if true, all None values get removed from response
    """
    resp = vars(obj)
    resp_copy = resp.copy()
    if remove_nulls:
        for i in resp:
            if remove_nulls:
                if resp[i] is None:
                    resp_copy.pop(i)
    return resp_copy


def set_date(date=None, delta=None):
    if date is None:
        date = datetime.datetime.utcnow().date()
    if delta is None:
        return date
    else:
        try:
            return date + datetime.timedelta(days=delta)
        except TypeError:
            if type(date) == str:
                date = datetime.datetime.fromisoformat(date).date()
                return date + datetime.timedelta(days=delta)
            else:
                raise


def today():
    return datetime.datetime.utcnow().date()


def today_with_time():
    return datetime.datetime.utcnow()



def getKeyArg(keyArg,default):
  keyArg = keyArg + "="
  ret_val = default
  for arg in sys.argv[1:]:
    if ( str.find(arg,keyArg,0) != -1 ):
        ret_val = arg[str.find(arg,keyArg,0)+len(keyArg):]
  return ret_val  


