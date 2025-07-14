import re

class IPAddressValidator:
    ipv4_pattern = re.compile(
        r'^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
        r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
        r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
        r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    )

    ipv6_pattern = re.compile(
        r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    )

    @classmethod
    def is_valid(cls, ip: str) -> bool:
        return bool(cls.ipv4_pattern.fullmatch(ip) or cls.ipv6_pattern.fullmatch(ip))
