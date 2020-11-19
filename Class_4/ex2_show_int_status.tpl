Value PORT_NAME (\S+)
Value PORT_STATUS (\S+)
Value PORT_VLAN (\d+)
Value PORT_DUPLEX (\S+)
Value PORT_SPEED (\S+)
Value PORT_TYPE (\S+)

Start
  ^Port.*Type\s*$$ -> ShowIntStatus

ShowIntStatus
  ^${PORT_NAME}\s+${PORT_STATUS}\s+${PORT_VLAN}\s+${PORT_DUPLEX}\s+${PORT_SPEED}\s+${PORT_TYPE}$$ -> Record
