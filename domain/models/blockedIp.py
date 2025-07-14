from dataclasses import dataclass

@dataclass(frozen=True)
class BlockedIp:
  ip: str
  date: str
  eventType: str
  description: str