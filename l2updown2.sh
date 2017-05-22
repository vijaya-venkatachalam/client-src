#! /bin/sh
if test $PLUTO_VERB == "up-host"
then 
	ip l2tp add tunnel tunnel_id 5001 peer_tunnel_id 5001 encap udp udp_sport 5001 udp_dport 5001 local 172.20.4.18 remote 78.33.59.116
	ip l2tp add session tunnel_id 5001 session_id 5001 peer_session_id 5001 
	ip link set dev l2tpeth0 up 
	ip addr add 192.168.67.2/31 dev l2tpeth0
fi
if test $PLUTO_VERB == "down-host"
then
	ip l2tp del session tunnel_id 5001 session_id 5001 peer_session_id 5001 
	ip l2tp del tunnel tunnel_id 5001
fi
exit 0
