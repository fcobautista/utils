def is_prime(num):
    try:
        num=int(num)
    except ValueError, TypeError:
        return False
    if num <=0: return False
    return 0 not in [num % i for i in range(1 if num < 2 else 2, int(num**.5)+1)]

def get_root_ca(cert_data):
    """Gets all the CA certificates in the root CA chain 

    Arguments:
        `cert_data` -- The dict() containing the root CA information

    Returns:
        A list of PEM formatted certificates
    """
    root_ca_list = []
    while True:
        root_ca_list.append(cert_data['certificateAuthorityCertificate'])
        if 'issuerCertificateAuthority' in cert_data.keys():
            cert_data = cert_data['issuerCertificateAuthority']
        else:
            break

    return root_ca_list
