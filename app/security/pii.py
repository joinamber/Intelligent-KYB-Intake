SENSITIVE_KEYS={"id_number","tax_id","tin","bank_account","passport_number","date_of_birth"}
def redact(value):
    if value is None:return value
    s=str(value)
    return "*"*(max(len(s)-4,3))+s[-4:] if len(s)>4 else "***"
def redact_mapping(data):
    if isinstance(data,dict): return {k:(redact(v) if k.lower() in SENSITIVE_KEYS else redact_mapping(v)) for k,v in data.items()}
    if isinstance(data,list): return [redact_mapping(x) for x in data]
    return data
