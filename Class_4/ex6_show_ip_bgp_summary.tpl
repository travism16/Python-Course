Value Filldown ROUTER_ID (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
Value Filldown LOCAL_AS (\d+)
Value NEIGHBOR (\S+)
Value REMOTE_AS (\d+)
Value UP_DOWN (\w+)
Value STATE_PFX_RCD (\w+)

Start
  ^BGP router identifier ${ROUTER_ID}.*number ${LOCAL_AS}
  ^Neighbor.*PfxRcd -> BgpNeighbors

BgpNeighbors
  ^${NEIGHBOR}\s+\d+\s+${REMOTE_AS}\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+${UP_DOWN}\s+${STATE_PFX_RCD} -> Record

EOF
