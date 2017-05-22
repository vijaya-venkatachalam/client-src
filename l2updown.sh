#! /bin/sh
if test $PLUTO_VERB == "up-host"
then 
	ip l2tp add tunnel tunnel_id 5000 peer_tunnel_id 5000 encap udp udp_sport 5000 udp_dport 5000 local 172.20.4.18 remote 78.33.59.117
	ip l2tp add session tunnel_id 5000 session_id 5000 peer_session_id 5000 
	ip link set dev l2tpeth0 up 
	ip addr add 192.168.66.2/31 dev l2tpeth0
fi
if test $PLUTO_VERB == "down-host"
then
	ip l2tp del session tunnel_id 5000 session_id 5000 peer_session_id 5000 
	ip l2tp del tunnel tunnel_id 5000 
fi
exit 0
