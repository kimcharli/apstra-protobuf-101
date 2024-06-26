
�
protobuf/aosstream.protoaos.streaming"D
DeviceStateEvent0
state (2.aos.streaming.DeviceStateRstate"�
TrafficEvent5
	node_role (2.aos.streaming.FeatureH RnodeRole5
	port_role (2.aos.streaming.FeatureH RportRole
port (	H Rport
node (	H Rnode
pod (H Rpod)
interval_seconds (RintervalSeconds)
measurement_name (	RmeasurementNameI
aggregation_type (2.aos.streaming.AggregationTypeRaggregationType+
delta_percentage	 (HRdeltaPercentage1
delta_nonnormalized
 (HRdeltaNonnormalizedB
sourceB
delta"�
StreamingEvent

aos_server (	R	aosServerC
streaming_type (2.aos.streaming.StreamingTypeRstreamingType<
protocol (2 .aos.streaming.StreamingProtocolRprotocol6
status (2.aos.streaming.StreamingStatusRstatusO
sequencing_mode (2&.aos.streaming.StreamingSequencingModeRsequencingMode"�
CablePeerEvent"
lcl_device_id (	RlclDeviceId!
lcl_hostname (	RlclHostname

lcl_ifname (	R	lclIfname!
rmt_hostname (	RrmtHostname

rmt_ifname (	R	rmtIfname!
rmt_sysdescr (	RrmtSysdescr"�
BGPNeighborEvent!
lcl_hostname (	RlclHostname

lcl_ipaddr (	R	lclIpaddr
lcl_asn (RlclAsn4
state (2.aos.streaming.BgpSessionStateRstate

rmt_ipaddr (	R	rmtIpaddr
rmt_asn (RrmtAsn
vrf_name (	RvrfNameG
addr_family (2&.aos.streaming.BgpSessionAddressFamilyR
addrFamily"v
LinkStatusEvent
hostname (	Rhostname
ifname (	Rifname/
state (2.aos.streaming.LinkStatusRstate"�
MacEvent

macaddress (	R
macaddress
intfname (	Rintfname
vlan (Rvlan-
state (2.aos.streaming.MacStateRstate"�
ArpEvent
	ipaddress (	R	ipaddress
mac (	Rmac
intfname (	Rintfname-
state (2.aos.streaming.ArpStateRstate
vrfname (	Rvrfname"�
LagEvent
hostname (	Rhostname
lagname (	Rlagname,
interfacesupcount (Rinterfacesupcount"
interfacesup (	Rinterfacesup"�
	MlagEvent
	domain_id (	RdomainIdA
domain_state (2.aos.streaming.MlagDomainStateRdomainState
intfname (	Rintfname;

intf_state (2.aos.streaming.MlagIntfStateR	intfState"@
ExtensibleServiceEvent
key (	Rkey
value (	Rvalue"�

RouteEvent!
dest_network (	RdestNetwork7
status (2.aos.streaming.RouteEntryStatusRstatus
hostname (	Rhostname"�
EvpnType3RouteEvent/
state (2.aos.streaming.RouteStateRstate
	system_id (	RsystemId
vni (Rvni
next_hop (	RnextHop
rd (	Rrd
rt (	Rrt"�
ActiveFloodlistEvent/
state (2.aos.streaming.RouteStateRstate
	system_id (	RsystemId
vni (Rvni
vtep (	Rvtep"�
EvpnType5RouteEvent/
state (2.aos.streaming.RouteStateRstate
	system_id (	RsystemId
af (	Raf
subnet (	Rsubnet
next_hop (	RnextHop
rd (	Rrd
rt (	Rrt"�
Event
id (	RidD
device_state (2.aos.streaming.DeviceStateEventH RdeviceState=
	streaming (2.aos.streaming.StreamingEventH R	streaming>

cable_peer (2.aos.streaming.CablePeerEventH R	cablePeerD
bgp_neighbor (2.aos.streaming.BGPNeighborEventH RbgpNeighborA
link_status (2.aos.streaming.LinkStatusEventH R
linkStatus7
traffic (2.aos.streaming.TrafficEventH Rtraffic6
	mac_state (2.aos.streaming.MacEventH RmacState6
	arp_state	 (2.aos.streaming.ArpEventH RarpState6
	lag_state
 (2.aos.streaming.LagEventH RlagState9

mlag_state (2.aos.streaming.MlagEventH R	mlagStateR
extensible_event (2%.aos.streaming.ExtensibleServiceEventH RextensibleEvent<
route_state (2.aos.streaming.RouteEventH R
routeStateB
data"e
HostnameAlert+
expected_hostname (	RexpectedHostname'
actual_hostname (	RactualHostname"
ConfigDeviationAlert"s
LivenessAlert'
expected_agents (	RexpectedAgents#
actual_agents (	RactualAgents
alive (Ralive"W
ExtensibleAlert
key (	Rkey
expected (	Rexpected
actual (	Ractual"�
DeploymentAlert]
expected_deployment_status (2.aos.streaming.DeploymentStatusRexpectedDeploymentStatusY
actual_deployment_status (2.aos.streaming.DeploymentStatusRactualDeploymentStatus"@
BlueprintRenderingAlert%
failed_systems (	RfailedSystems"�

RouteAlert
ip (	RipQ
expected_dest_status (2.aos.streaming.RouteEntryStatusRexpectedDestStatusM
actual_dest_status (2.aos.streaming.RouteEntryStatusRactualDestStatus"�
LagAlert
hostname (	Rhostname
lagname (	Rlagname.
expected_ifup_count (RexpectedIfupCount*
actual_ifup_count (RactualIfupCount4
expected_interfaces_up (	RexpectedInterfacesUp0
actual_interfaces_up (	RactualInterfacesUp"�
StreamingAlert

aos_server (	R	aosServerC
streaming_type (2.aos.streaming.StreamingTypeRstreamingType<
protocol (2 .aos.streaming.StreamingProtocolRprotocol;
reason (2#.aos.streaming.StreamingAlertReasonRreasonO
sequencing_mode (2&.aos.streaming.StreamingSequencingModeRsequencingMode"�
CablePeerMismatchAlert!
lcl_hostname (	RlclHostname

lcl_ifname (	R	lclIfname!
exp_hostname (	RexpHostname

exp_ifname (	R	expIfname!
rmt_hostname (	RrmtHostname

rmt_ifname (	R	rmtIfname!
rmt_sysdescr (	RrmtSysdescr"�
BGPNeighborMismatchAlert!
lcl_hostname (	RlclHostname

lcl_ipaddr (	R	lclIpaddr
lcl_asn (RlclAsn

rmt_ipaddr (	R	rmtIpaddr
rmt_asn (RrmtAsnE
expected_state (2.aos.streaming.BgpSessionStateRexpectedStateA
actual_state (2.aos.streaming.BgpSessionStateRactualState
rmt_name (	RrmtName
vrf_name	 (	RvrfNameG
addr_family
 (2&.aos.streaming.BgpSessionAddressFamilyR
addrFamily"�
 InterfaceLinkStatusMismatchAlert
hostname (	Rhostname
ifname (	RifnameF
expected_ifstatus (2.aos.streaming.LinkStatusRexpectedIfstatusB
actual_ifstatus (2.aos.streaming.LinkStatusRactualIfstatus"�
CountersAlert5
	node_role (2.aos.streaming.FeatureH RnodeRole5
	port_role (2.aos.streaming.FeatureH RportRole
port (	H Rport
node (	H Rnode
pod (H Rpod)
measurement_name (	RmeasurementName)
interval_seconds (RintervalSecondsI
aggregation_type (2.aos.streaming.AggregationTypeRaggregationTypeB
id"6
KeyValuePair
key (	Rkey
value (	Rvalue"�

ProbeAlert!
expected_int (RexpectedInt

actual_int (R	actualInt%
expected_float (RexpectedFloat!
actual_float (RactualFloat6
expected_discrete_state (	RexpectedDiscreteState2
actual_discrete_state (	RactualDiscreteState
probe_id (	RprobeId

stage_name	 (	R	stageNameC
key_value_pairs
 (2.aos.streaming.KeyValuePairRkeyValuePairs
item_id (	RitemId#
expected_text (	RexpectedText
actual_text (	R
actualText
probe_label (	R
probeLabel(
expected_int_max (RexpectedIntMax,
expected_float_max (RexpectedFloatMax"[
ConfigMismatchAlert!
blueprint_id (	RblueprintId!
collector_id (	RcollectorId"�
HeadroomAlert
node_a (	RnodeA
node_b (	RnodeB)
interval_seconds (RintervalSeconds@
headroom_type (2.aos.streaming.HeadroomTypeRheadroomType"�
MacAlert

macaddress (	R
macaddress
intfname (	Rintfname
vlan (Rvlan
	movecount (R	movecount0
actual_move_interval (RactualMoveInterval2
expected_max_interval (RexpectedMaxInterval"V
ArpAlert
	ipaddress (	R	ipaddress
mac (	Rmac
intfname (	Rintfname"�
	MlagAlert
hostname (	Rhostname
	domain_id (	RdomainId
mlag_id (RmlagIdR
expected_domain_state (2.aos.streaming.MlagDomainStateRexpectedDomainStateN
actual_domain_state (2.aos.streaming.MlagDomainStateRactualDomainState
ifname (	RifnameL
expected_intf_state (2.aos.streaming.MlagIntfStateRexpectedIntfStateH
actual_intf_state (2.aos.streaming.MlagIntfStateRactualIntfState
	peer_link	 (	RpeerLink(
peer_link_status
 (	RpeerLinkStatus9
expected_peer_link_status (	RexpectedPeerLinkStatus"&
	TestAlert
test_int (RtestInt"�
InterfaceCounters,
tx_unicast_packets (RtxUnicastPackets0
tx_broadcast_packets (RtxBroadcastPackets0
tx_multicast_packets (RtxMulticastPackets
tx_bytes (RtxBytes,
rx_unicast_packets (RrxUnicastPackets0
rx_broadcast_packets (RrxBroadcastPackets0
rx_multicast_packets (RrxMulticastPackets
rx_bytes (RrxBytes(
tx_error_packets	 (RtxErrorPackets,
tx_discard_packets
 (RtxDiscardPackets(
rx_error_packets (RrxErrorPackets,
rx_discard_packets (RrxDiscardPackets)
alignment_errors (RalignmentErrors

fcs_errors (R	fcsErrors#
symbol_errors (RsymbolErrors
runts (Rrunts
giants (Rgiants&
delta_seconds (:5RdeltaSeconds6
delta_microseconds (:5000000RdeltaMicroseconds"�

SystemInfo
cpu_user (RcpuUser

cpu_system (R	cpuSystem
cpu_idle (RcpuIdle
memory_used (R
memoryUsed!
memory_total (RmemoryTotal"�
ProcessInfo!
process_name (	RprocessName
cpu_user (RcpuUser

cpu_system (R	cpuSystem
memory_used (R
memoryUsed"D
FileInfo
	file_name (	RfileName
	file_size (RfileSize"�
SysResourceCounters:
system_info (2.aos.streaming.SystemInfoR
systemInfo=
process_info (2.aos.streaming.ProcessInfoRprocessInfo4
	file_info (2.aos.streaming.FileInfoRfileInfo"�
Tag
name (	Rname!
int64_value (H R
int64Value!
float_value (H R
floatValue#
string_value (	H RstringValueB
value"�
Field
name (	Rname!
int64_value (H R
int64Value!
float_value (H R
floatValue#
string_value (	H RstringValueB
value"9
ProbeProperty
name (	Rname
value (	Rvalue"�
InterfaceCountersUtilization%
tx_utilization (RtxUtilization%
rx_utilization (RrxUtilization$
tx_unicast_pps (RtxUnicastPps(
tx_broadcast_pps (RtxBroadcastPps(
tx_multicast_pps (RtxMulticastPps
tx_bps (RtxBps 
tx_error_pps (R
txErrorPps$
tx_discard_pps (RtxDiscardPps$
rx_unicast_pps	 (RrxUnicastPps(
rx_broadcast_pps
 (RrxBroadcastPps(
rx_multicast_pps (RrxMulticastPps
rx_bps (RrxBps 
rx_error_pps (R
rxErrorPps$
rx_discard_pps (RrxDiscardPps=
alignment_errors_per_second (RalignmentErrorsPerSecond1
fcs_errors_per_second (RfcsErrorsPerSecond7
symbol_errors_per_second (RsymbolErrorsPerSecond(
runts_per_second (RruntsPerSecond*
giants_per_second (RgiantsPerSecond"�
SystemInterfaceUtilization(
aggregate_tx_bps (RaggregateTxBps(
aggregate_rx_bps (RaggregateRxBps3
max_ifc_tx_utilization (RmaxIfcTxUtilization3
max_ifc_rx_utilization (RmaxIfcRxUtilization8
aggregate_tx_utilization (RaggregateTxUtilization8
aggregate_rx_utilization (RaggregateRxUtilization"�
ProbeMessage8
property (2.aos.streaming.ProbePropertyRproperty!
int64_value (H R
int64Value!
float_value (H R
floatValue#
string_value (	H RstringValueY
evpn_type3_route_state	 (2".aos.streaming.EvpnType3RouteEventH RevpnType3RouteStateY
evpn_type5_route_state
 (2".aos.streaming.EvpnType5RouteEventH RevpnType5RouteStates
interface_counters_utilization (2+.aos.streaming.InterfaceCountersUtilizationH RinterfaceCountersUtilizationm
system_interface_utilization (2).aos.streaming.SystemInterfaceUtilizationH RsystemInterfaceUtilizationP
active_floodlist (2#.aos.streaming.ActiveFloodlistEventH RactiveFloodlist
probe_id (	RprobeId

stage_name (	R	stageName!
blueprint_id (	RblueprintId
item_id (	RitemId
probe_label (	R
probeLabelB
value"m
GenericPerfmonMessage&
tags (2.aos.streaming.TagRtags,
fields (2.aos.streaming.FieldRfields"a
	ProbeData&
tags (2.aos.streaming.TagRtags,
fields (2.aos.streaming.FieldRfields"�
PerfMonQ
interface_counters (2 .aos.streaming.InterfaceCountersH RinterfaceCounters^
system_resource_counters (2".aos.streaming.SysResourceCountersH RsystemResourceCounters@
generic (2$.aos.streaming.GenericPerfmonMessageH RgenericB
probe_message (2.aos.streaming.ProbeMessageH RprobeMessage

time_delta (R	timeDeltaB
data"�
Alert8
severity (2.aos.streaming.AlertSeverityRseverity

first_seen (R	firstSeen
id (	Rid
raised (Rraised[
config_deviation_alert (2#.aos.streaming.ConfigDeviationAlertH RconfigDeviationAlertH
streaming_alert (2.aos.streaming.StreamingAlertH RstreamingAlertb
cable_peer_mismatch_alert (2%.aos.streaming.CablePeerMismatchAlertH RcablePeerMismatchAlerth
bgp_neighbor_mismatch_alert (2'.aos.streaming.BGPNeighborMismatchAlertH RbgpNeighborMismatchAlert�
$interface_link_status_mismatch_alert	 (2/.aos.streaming.InterfaceLinkStatusMismatchAlertH R interfaceLinkStatusMismatchAlertE
hostname_alert
 (2.aos.streaming.HostnameAlertH RhostnameAlert<
route_alert (2.aos.streaming.RouteAlertH R
routeAlertE
liveness_alert (2.aos.streaming.LivenessAlertH RlivenessAlertK
deployment_alert (2.aos.streaming.DeploymentAlertH RdeploymentAlertd
blueprint_rendering_alert (2&.aos.streaming.BlueprintRenderingAlertH RblueprintRenderingAlertE
counters_alert (2.aos.streaming.CountersAlertH RcountersAlert6
	mac_alert (2.aos.streaming.MacAlertH RmacAlert6
	arp_alert (2.aos.streaming.ArpAlertH RarpAlertE
headroom_alert (2.aos.streaming.HeadroomAlertH RheadroomAlert6
	lag_alert (2.aos.streaming.LagAlertH RlagAlert9

mlag_alert (2.aos.streaming.MlagAlertH R	mlagAlert<
probe_alert (2.aos.streaming.ProbeAlertH R
probeAlertX
config_mismatch_alert (2".aos.streaming.ConfigMismatchAlertH RconfigMismatchAlertK
extensible_alert (2.aos.streaming.ExtensibleAlertH RextensibleAlert:

test_alert� (2.aos.streaming.TestAlertH R	testAlertB
data"�

AosMessage
	timestamp (R	timestamp
origin_name (	R
originName'
origin_hostname (	RoriginHostname
origin_role (	R
originRole'
blueprint_label (	RblueprintLabel,
alert (2.aos.streaming.AlertH Ralert,
event (2.aos.streaming.EventH Revent3
perf_mon (2.aos.streaming.PerfMonH RperfMonB
data"K
AosSequencedMessage
seq_num (RseqNum
	aos_proto (RaosProto*�
DeviceState
DEVICE_STATE_IS_ACTIVE
DEVICE_STATE_IS_READY
DEVICE_STATE_IS_NOCOMMS
DEVICE_STATE_IS_MAINT
DEVICE_STATE_IS_REBOOTING
DEVICE_STATE_OOS_STOCKED 
DEVICE_STATE_OOS_QUARANTINED
DEVICE_STATE_OOS_READY
DEVICE_STATE_OOS_NOCOMMS	
DEVICE_STATE_OOS_DECOMM

DEVICE_STATE_OOS_MAINT
DEVICE_STATE_OOS_REBOOTING
DEVICE_STATE_ERROR*�
Feature
FEATURE_UNKNOWN 
FEATURE_LO0
FEATURE_FABRIC
FEATURE_LEAF_SERVER
FEATURE_L3EDGE
FEATURE_L2EDGE
FEATURE_SPINE_LEAF
FEATURE_FABRIC_SPINE
FEATURE_EXTERNAL_ROUTER
FEATURE_TO_EXTERNAL_ROUTER	
FEATURE_LEAF_L3_SERVER

FEATURE_LEAF_L2_SERVER
FEATURE_LEAF
FEATURE_SPINE
FEATURE_L3_SERVER
FEATURE_L2_SERVER
FEATURE_SERVER
FEATURE_PEER
FEATURE_LEAF_PEER_LINK
FEATURE_LEAF_PAIR
FEATURE_LEAF_PAIR_L2_SERVER
FEATURE_UNUSED*a
StreamingType
STREAMING_TYPE_PERFMON 
STREAMING_TYPE_EVENTS
STREAMING_TYPE_ALERTS*=
StreamingProtocol(
$STREAMING_PROTOCOL_PROTOBUF_OVER_TCP *E
StreamingStatus
STREAMING_STATUS_UP 
STREAMING_STATUS_DOWN*M
StreamingSequencingMode
STREAMING_UNSEQUENCED 
STREAMING_SEQUENCED*7
BgpSessionAddressFamily
IPV4 
IPV6
EVPN*L

LinkStatus
LINK_UP 
	LINK_DOWN
LINK_UNKNOWN
LINK_MISSING*5
MacState
MAC_ADD 

MAC_DELETE
MAC_MOVE*'
ArpState
ARP_ADD 

ARP_DELETE*l
MlagDomainState
MLAG_UNKNOWN 
MLAG_MISSING
MLAG_DISABLED
MLAG_INACTIVE
MLAG_ACTIVE*�
MlagIntfState
MLAG_INTF_UNKNOWN 
MLAG_INTF_MISSING
MLAG_INTF_DISABLED
MLAG_INTF_CONFIGURED
MLAG_INTF_INACTIVE
MLAG_INTF_ACTIVE_PARTIAL
MLAG_INTF_ACTIVE_FULL*-

RouteState
	ROUTE_ADD 
ROUTE_DELETE*T
AlertSeverity
	ALERT_LOW 
ALERT_MEDIUM

ALERT_HIGH
ALERT_CRITICAL*�
RouteEntryStatus
ROUTE_ENTRY_STATUS_UNKNOWN 
ROUTE_ENTRY_STATUS_UP
ROUTE_ENTRY_STATUS_PARTIAL
ROUTE_ENTRY_STATUS_MISSING*a
NextHopStatus
NEXT_HOP_STATUS_UNKNOWN 
NEXT_HOP_STATUS_UP
NEXT_HOP_STATUS_MISSING*c
	RouteType
ROUTE_TYPE_UNKNOWN 
ROUTE_TYPE_DIRECT
ROUTE_TYPE_BGP
ROUTE_TYPE_STAT*s
DeploymentStatus 
DEPLOYMENT_STATUS_INPROGRESS 
DEPLOYMENT_STATUS_SUCCEEDED
DEPLOYMENT_STATUS_FAILED*�
StreamingAlertReason,
(STREAMING_ALERT_REASON_FAILED_CONNECTION "
STREAMING_ALERT_REASON_TIMEOUT&
"STREAMING_ALERT_REASON_DNS_FAILURE(
$STREAMING_ALERT_REASON_WRITE_TIMEOUT*m
BgpSessionState
BGP_SESSION_UP 
BGP_SESSION_DOWN
BGP_SESSION_MISSING
BGP_SESSION_UNKNOWN*�
AggregationType
AGGREGATION_TYPE_MAX
AGGREGATION_TYPE_MIN
AGGREGATION_TYPE_SUM
AGGREGATION_TYPE_AVG
AGGREGATION_TYPE_STD*<
HeadroomType
HEADROOM_TYPE_MAX
HEADROOM_TYPE_MIN