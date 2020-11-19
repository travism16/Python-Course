Value INT_NAME (\S+)
Value LINE_STATUS (\S+)
Value ADMIN_STATE (up|down)
Value MAC (\S+)
Value MTU (\d+)
Value DUPLEX (full-duplex|half-duplex)
Value SPEED (\d+)

Start
  ^${INT_NAME} is ${LINE_STATUS}$$
  ^admin state is ${ADMIN_STATE}.*$$
  ^\s+Hardware:\s+\S+\s+address:\s+${MAC}.*$$
  ^\s+MTU\s${MTU}.*$$
  ^\s+${DUPLEX}, ${SPEED}.*$$ -> Record
