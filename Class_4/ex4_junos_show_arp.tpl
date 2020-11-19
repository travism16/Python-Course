Value MAC_ADDR (\S+)
Value IP_ADDR (\S+)
Value NAME (\S+)
Value INTERFACE (\S+)

Start
  ^MAC.*Flags$$ -> IntDetails

IntDetails
  ^${MAC_ADDR}\s+${IP_ADDR}\s+${NAME}\s+${INTERFACE}.*$$ -> Record
